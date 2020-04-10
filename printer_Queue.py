test_case_number=int(input())
n_and_m_list=[]
m_list=[]
importance=[]
test_case_list=[]

def organize(num_list,m):
    printed=0
    while num_list[m]<=max(num_list):
        while num_list[0]!=max(num_list):
            if m==0:
                num_list.append(num_list[0])
                num_list.remove(num_list[0])
                m=len(num_list)-1
            else:
                num_list.append(num_list[0])
                num_list.remove(num_list[0])
                m=m-1
        if m!=0:
            num_list.remove(num_list[0])
            m=m-1
            printed=printed+1
        elif m==0:
            printed=printed+1
            break
    return printed


for s in range(0,test_case_number):
    n_and_m_list.append(input())
    importance.append(input())
for k in n_and_m_list:
    m=k.split(" ")[1]
    m_list.append(int(m))
for k in importance:
    num_list=k.split(" ")
    test_case_list.append(num_list)
for k in range(0,len(m_list)):
    print(organize(test_case_list[k],m_list[k]))








