def read_txt(filename):
    with open("./data/"+filename,"r",encoding="utf-8")as f:
        # read()获取所有
        # readlines获取所有行
        # readline获取一行
        arr = []
        for data in f.readlines():
            arr.append(tuple(data.strip().split(",")))
        return arr[1::]

"""
    strip:去除字符串前后空格，换行符
    split("字符")：以指定字符分隔字符串，并以列表的形式放回
"""

if __name__=='main':
    print(read_txt("employee_post.txt"))

