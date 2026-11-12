import argparse,csv,json,sys
def transform(rows):
    return "\n".join(json.dumps(r,ensure_ascii=False) for r in rows)

def main():
    parser=argparse.ArgumentParser(description='CSV to JSON records converter')
    parser.add_argument("file",nargs="?",help="input path; defaults to stdin")
    args=parser.parse_args()
    source=open(args.file,encoding="utf-8",newline="").read() if args.file else sys.stdin.read()
    reader=csv.DictReader(source.splitlines())
    result=transform(list(reader))
    print(result if isinstance(result,str) else json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__": main()
