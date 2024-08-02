import sys
sys.stdin = open('input (4).txt','r')

T=int(input())
new_list = []
for tc in range(1,T+1):
    N_list=list(input())

    N_list = N_list[::-1]

    # for i in range(len(N_list)):
    #     if N_list[i]=='q':
    #         N_list[i]='p'
    #     elif N_list[i]=='p':
    #         N_list[i]='q'
    #     elif N_list[i]=='b':
    #         N_list[i]='d'
    #     elif N_list[i]=='d':
    #         N_list[i]='b'
    # N_list=''.join(N_list)

    new_list = []
    #
    for N in N_list:
        if N == 'q':
            N ='p'
        elif N =='p':
            N ='q'
        elif N =='b':
            N ='d'
        elif N =='d':
            N = 'b'

        new_list.append(N)
    N_list=''.join(new_list)

    print(f'#{tc} {N_list}')



