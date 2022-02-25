# Python program for implementation of MergeSort
from collections import defaultdict

if __name__ == '__main__':
    C,P = map(int,input().split())

    dic_skills = defaultdict(list)
    dic_work = defaultdict(list)

    for c in range(C):
        name,skills =  map(str,input().split())

        for s in range(int(skills)):
            skill,lvl = map(str,input().split())
            if dic_skills[skill] == 0:
                dic_skills = [(name,lvl)]
            else:
                lvl = int(lvl)
                dic_skills[skill] += [[name,lvl]]
    
    for key,val in dic_skills.items():
        sorter = lambda x: (-(x[1]), (x[0]))
        dic_skills[key] = sorted(val, key=sorter)
    
    for p in range(P):
        arr = [i for i in input().split()] 
        proj = arr[0]
        d = int(arr[1])
        s = int(arr[2])
        b = int(arr[3])
        r = int(arr[4]) 

        dic_work[proj] += [d,s,b,r,[]]

        for skills in range(r):
            skill,lvl =  map(str,input().split())
            dic_work[proj][4] += [[skill,lvl]]
    
    dic_work = dict(sorted(dic_work.items(), key=lambda i: i[1], reverse=True))
    # print(dic_skills)
    for i,j in dic_work.items():
        print(i,j)

    atlast = []
    final = []
    for key,val in dic_work.items():
        dic_skills2 = dic_skills
        ans = []
        flag = False
        work = val[4]
        for data in work:
            
            skill = data[0]
            lvl = int(data[1])
            
            if dic_skills[skill][0][0] in ans:
                flag = False
                break
            if dic_skills[skill][0][1] < lvl:
                flag = False
                break

            flag = True

            if dic_skills[skill][0][1] == lvl:
                dic_skills2[skill][0][1] += 1
            ans.append(dic_skills[skill][0][0])
        if flag:
            dic_skills = dic_skills2
            final.append([key,ans])

    # print(len(final))
    # for i in range(len(final)):
    #     print(final[i][0])
    #     print(*final[i][1])
    # print(dic_skills)
    # print(dic_work)
                




    

    




