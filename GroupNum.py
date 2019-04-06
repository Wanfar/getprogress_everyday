#计算作业分工
snum_ori = 19117201
snum_ori = input('请输入班级第一个同学的学号:')
snum_ori = int(snum_ori)
for i in range(30):
    snum = snum_ori + i
    groupNum = snum % 9
    print('学号为{}，所在小组{}'.format(snum, groupNum))
    print('题号是：')
    x = groupNum
    for i in range(29):
        print('{}  '.format(x), end='')
        if (x+9) <= 256:
            x = x + 9
    print('\n')

# #不是按顺序的学号
# snum = input('请输入学号:')
# snum = int(snum)
# print('学号为{}，所在小组{}'.format(snum, snum % 9))
