import codecs
import sys

def main(**kwargs):
    count = 0
    with codecs.open(sys.argv[1], "r", "utf-8") as fp:
        for line in fp:
            if line.startswith("#") or len(line) <= 1:
                continue                
            tokens = line.split() 
            print(tokens)
            for token in tokens:
                if token == 'E':
                    count += 1
    print(count)

if __name__ == "__main__":
    main()

