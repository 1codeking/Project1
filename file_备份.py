# def copyFile():
#     old_file = input('请输入备份文件名：')
#     file_list = old_file.split('.')
#     new_file = file_list[0]+'_备份.'+file_list[1]
#     robj = open(old_file,'r')
#     content = robj.read()
#     wobj = open(new_file,'wb')
#     wobj.write(content.encode('utf-8'))
#     robj.close()
#     wobj.close()

#脚本优化
def copyFile():
    old_file = input('请输入备份文件名：')
    file_list = old_file.split('.')
    new_file = file_list[0]+'_备份.'+file_list[1]
    try:
        with open(old_file,'r') as robj,open(new_file,'w') as wobj:
            while True:
                content = robj.read(1024)
                wobj.write(content)
                if len(content) < 1024:
                    break
    except Exception as msg:
        print(msg)











# copyFile()