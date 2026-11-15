#!/usr/bin/env python3
"""Convert an RSS or Atom feed into a compact Markdown digest."""
import argparse,pathlib,sys,unittest,urllib.request
import xml.etree.ElementTree as ET
def local_name(tag): return tag.rsplit("}",1)[-1].lower()
def child_text(node,names):
    for child in node:
        if local_name(child.tag) in names and child.text: return child.text.strip()
    return ""
def parse_feed(xml_text):
    root=ET.fromstring(xml_text); entries=[]
    for node in root.iter():
        if local_name(node.tag) not in {"item","entry"}: continue
        item={"title":child_text(node,{"title"}) or "(untitled)","link":"","date":child_text(node,{"pubdate","published","updated"}),"summary":child_text(node,{"description","summary","content"})}
        for child in node:
            if local_name(child.tag)=="link":
                item["link"]=child.attrib.get("href") or (child.text or "").strip()
                if item["link"]: break
        entries.append(item)
    return entries
def load_source(source,timeout=12):
    if source.startswith(("http://","https://")):
        req=urllib.request.Request(source,headers={"User-Agent":"feed-folio/1.0"})
        with urllib.request.urlopen(req,timeout=timeout) as response: data=response.read(2_000_001)
        if len(data)>2_000_000: raise ValueError("feed exceeds 2 MB limit")
        return data.decode("utf-8-sig")
    return pathlib.Path(source).read_text(encoding="utf-8-sig")
def render(entries,limit=20):
    lines=["# Reading digest",""]
    for item in entries[:limit]:
        lines.append(f"- **[{item['title']}]({item['link']})**" if item["link"] else f"- **{item['title']}**")
        if item["date"]: lines.append(f"  - {item['date']}")
        if item["summary"]: lines.append(f"  - {item['summary'][:240].replace(chr(10),' ')}")
    return "\n".join(lines)+"\n"
class Tests(unittest.TestCase):
    def test_rss(self): self.assertEqual(parse_feed("<rss><channel><item><title>One</title><link>https://e.test/1</link></item></channel></rss>")[0]["title"],"One")
    def test_atom(self): self.assertEqual(parse_feed('<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>Two</title><link href="https://e.test/2"/></entry></feed>')[0]["link"],"https://e.test/2")
def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("source"); ap.add_argument("--limit",type=int,default=20); ap.add_argument("-o","--output"); a=ap.parse_args()
    try: result=render(parse_feed(load_source(a.source)),max(0,a.limit))
    except (OSError,ValueError,ET.ParseError,UnicodeError) as exc: ap.error(str(exc))
    if a.output: pathlib.Path(a.output).write_text(result,encoding="utf-8")
    else: print(result,end="")
if __name__=="__main__":
    if "--self-test" in sys.argv: unittest.main(argv=[sys.argv[0]])
    else: main()
