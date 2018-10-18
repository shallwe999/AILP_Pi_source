
def memo_read():
    file_1 = open("./memo.txt", 'r')
    str = file_1.read()
    file_1.close()
    return str

def memo_clean():
    file_1 = open("./memo.txt", 'w+')
    file_1.close()
    
def memo_write(str):
    file_1 = open("./memo.txt", 'a+')
    file_1.write(str)
    file_1.close()


