s = int(input())

s_list = list(str(s))
print(s_list)

for i in range(0, len(s_list)-1):
    if int(s_list[i]) + 1 == int(s_list[i+1]) and int(s_list[i+1])+1 == int(s_list[i+2]):
        print(int(s_list[i]))
        break
    elif int(s_list[i]+s_list[i+1])+1 == int(s_list[i+2]+s_list[i+3]):
        print(int(s_list[i]+s_list[i+1]))
        break
    elif int(s_list[i]+s_list[i+1]+s_list[i+2])+1 == int(s_list[i+3]+s_list[i+3]+s_list[i+5]):
        print(int(s_list[i]+s_list[i+1]+s_list[i+2]))
        break
