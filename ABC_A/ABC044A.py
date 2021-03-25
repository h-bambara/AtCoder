NKXY = [int(input()) for i in range(4)]

if(NKXY[0] > NKXY[1]):
    print(NKXY[1] * NKXY[2] + (NKYX[0] - NKXY[1]) * NKXY[3])
else:
    print(NKXY[0] * NKXY[2])
