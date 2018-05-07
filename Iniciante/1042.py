A, B, C = map(int, input().split(' '))

if (A < B and A < C):
    if(B < C):
        print("{}\n{}\n{}\n".format(A,B,C));
    else:
         print("{}\n{}\n{}\n".format(A,C,B));
if(B < A and B < C):
        if(A < C):
            print("{}\n{}\n{}\n".format(B,A,C));
        else:
             print("{}\n{}\n{}\n".format(B,C,A));
if(C < B and C < A):
    if(B < A):
        print("{}\n{}\n{}\n".format(C,B,A));
    else:
        print("{}\n{}\n{}\n".format(C,A,B));
print("{}\n{}\n{}".format(A,B,C));
