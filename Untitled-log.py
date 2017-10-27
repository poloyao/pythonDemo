import sys
import os

def main():
    rowid = 1
    while True:
        
        logStr = str(input('请输入第' + str(rowid) + '条：'))
        if logStr != "exit":
            print(logStr)

        else:
            print('error')
            break
        rowid += 1


if __name__ == '__main__':
    main()
