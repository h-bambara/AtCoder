import sys

numList = list(map(int, input().split()))

numList.sort()
for i in range len(numList):
    if(i == 0){
        if(numList[i] != 5) {
            print("NO")
            sys.exit()
        }
    }else if(i == 1){
        if(numList[i] != 5) {
            print("NO")
            sys.exit()
        }
    }else if(i == 2){
        if(numList[i] != 7) {
            print("NO")
            sys.exit()
        }
    }
print("YES")