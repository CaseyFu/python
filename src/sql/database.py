import mysql.connector
import pickle
import os
db = mysql.connector.connect(
    host="localhost",
    user="xfk",
    passwd="38524",
)
database = "pythonDB1"  # 要操作的数据库, 谨防被覆盖
dbObj = db.cursor()  # 获取游标


def useDatabase(database):
    """use database"""
    try:
        dbObj.execute("use "+database)
    except Exception:
        print("数据库未初始化")


def existDatabase(database):
    """数据库存在返回1, 不存在返回0"""
    try:
        dbObj.execute("use "+database)
    except Exception:
        return 0
    return 1


def createTable():
    """创建student, major, grade, curriculum表"""
    dbObj.execute(
        "create table major (id int PRIMARY KEY auto_increment,major_id varchar(30) not null,major_name varchar(30) not null)")  # 生成专业表
    print("生成major表成功√")
    dbObj.execute(
        "create table student (id int PRIMARY KEY auto_increment, stu_id varchar(30) not null, stu_name varchar(7) not null, stu_gender tinyint not null, birthday varchar(20) not null, major_id varchar(30) not null, scholarship NUMERIC, party TINYINT, photograph BLOB, note varchar(255))")  # 生成学生表
    print("生成student表成功√")
    dbObj.execute(
        "create table curriculum (id int PRIMARY KEY auto_increment, cur_id varchar(30) not null, cur_name varchar(30) not null, cur_period smallint not null, cur_credit smallint not null, advance_cur varchar(30))")  # 生成课程表
    print("生成curriculum表成功√")
    dbObj.execute(
        "create table grade (id int PRIMARY KEY auto_increment, stu_id varchar(30) not null, cur_id varchar(30) not null, score smallint not null)")  # 生成成绩表
    print("生成grade表成功√")


def readData():
    """从pkl文件中读取数据到数据库"""
    with open(os.path.dirname(__file__)+"\\student.pkl", "rb") as f:
        sql = "insert into student (id, stu_id, stu_name, stu_gender, birthday, major_id, scholarship, party, photograph, note) value(null, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        for stu in pickle.load(f):
            value = (stu[1], stu[2], stu[3], stu[4],
                     stu[5], stu[6], stu[7], stu[8], stu[9])
            dbObj.execute(sql, value)
    with open(os.path.dirname(__file__)+"\\major.pkl", "rb") as f:
        sql = "insert into major (id, major_id, major_name) value(null, %s, %s)"
        for major in pickle.load(f):
            value = (major[1], major[2])
            dbObj.execute(sql, value)
    with open(os.path.dirname(__file__)+"\\curriculum.pkl", "rb") as f:
        sql = "insert into curriculum (id, cur_id, cur_name, cur_period, cur_credit, advance_cur) value(null, %s, %s, %s, %s, %s)"
        for cur in pickle.load(f):
            value = (cur[1], cur[2], cur[3], cur[4], cur[5])
            dbObj.execute(sql, value)
    with open(os.path.dirname(__file__)+"\\grade.pkl", "rb") as f:
        sql = "insert into grade (id, stu_id, cur_id, score) value(null, %s, %s, %s)"
        for grade in pickle.load(f):
            value = (grade[1], grade[2], grade[3])
            dbObj.execute(sql, value)


def init():
    """初始化数据库, 表结构"""
    if(existDatabase(database)):
        dbObj.execute("drop database "+database)
    dbObj.execute("create database "+database)
    useDatabase(database)
    createTable()
    readData()
    print("初始化", database, "数据库成功√")
    db.commit()


def saveData():
    """将表数据保存到pkl文件中"""
    useDatabase(database)
    dbObj.execute("select * from student")
    with open(os.path.dirname(__file__)+"\\student.pkl", "wb") as f:
        pickle.dump(dbObj.fetchall(), f)
        print("保存student表数据-->student.pkl")
    dbObj.execute("select * from major")
    with open(os.path.dirname(__file__)+"\\major.pkl", "wb") as f:
        pickle.dump(dbObj.fetchall(), f)
        print("保存major表数据-->major.pkl")
    dbObj.execute("select * from curriculum")
    with open(os.path.dirname(__file__)+"\\curriculum.pkl", "wb") as f:
        pickle.dump(dbObj.fetchall(), f)
        print("保存curriculum表数据-->curriculum.pkl")
    dbObj.execute("select * from grade")
    with open(os.path.dirname(__file__)+"\\grade.pkl", "wb") as f:
        pickle.dump(dbObj.fetchall(), f)
        print("保存grade表数据-->grade.pkl")


def dropDatabase(dbName):
    """删除数据库"""
    dbObj.execute("drop database "+dbName)
    db.commit()
    print("数据库"+dbName+"删除成功")


def select():
    useDatabase(database)
    dbObj.execute("show tables")
    for i in dbObj.fetchall():
        print(i)
    tableName = input("输入表名")
    sql = "select * from "+tableName
    try:
        dbObj.execute(sql)
    except Exception:
        print("表", tableName, "不存在")
        return
    s = []
    for i in dbObj.description:
        s.append(i[0])
    print(s)
    for i in dbObj.fetchall():
        print(i)


def selectOneStu(stu_id):
    """查询一名学生的信息, 和成绩"""
    useDatabase(database)
    sql = "select * from student where stu_id=%s"
    value = (stu_id,)
    dbObj.execute(sql, value)
    stu = dbObj.fetchone()
    print("学号:"+stu[1], "姓名:"+stu[2], "性别:" +
          "男"if(stu[3] == 1)else"女", "生日:"+stu[4],
          "专业代码:"+stu[5], "奖学金:￥"+str(stu[6]), "党员"if(stu[7] == 1)else"非党员", "备注:", "无"if(stu[9] == None)else stu[9])
    print("课程信息:")
    sql = "select c.cur_id, c.cur_name, g.score from grade g left join curriculum c on g.cur_id = c.cur_id where g.stu_id=%s"
    value = (stu_id, )
    dbObj.execute(sql, value)
    t = dbObj.fetchall()
    if(len(t)):
        for i in t:
            print("课程号:", i[0], i[1], ":", i[2], "分")
    else:
        print("无课程信息")


def existStu(stu_id):
    """student表中学号是否存在, 存在返回1, 不存在返回0"""
    useDatabase(database)
    sql = "select count(*) from student where stu_id=%s"
    value = (stu_id,)
    dbObj.execute(sql, value)
    if(dbObj.fetchone()[0] == 0):
        return 0
    return 1


def createStu():
    """增加一条学生记录"""
    useDatabase(database)
    stu_id = 0
    while(1):
        stu_id = input("输入学号:")
        if(existStu(stu_id) == 0):
            break
        print("学号存在, 请从新输入")
    stu_name = input("输入姓名:")
    stu_gender = 1 if(input("输入性别:") == "男") else 0
    birthday = input("输入出生日期:")
    major_id = input("输入专业代号:")
    scholarship = float(input("输入奖学金:"))
    party = 1 if(input("是否是党员:") == "是") else 0
    note = input("输入备注:")
    sql = "insert into student (id, stu_id, stu_name, stu_gender, birthday, major_id, scholarship, party, photograph, note) value(null, %s, %s, %s, %s, %s, %s, %s, null, %s)"
    value = (stu_id, stu_name, stu_gender, birthday,
             major_id, scholarship, party, note)
    dbObj.execute(sql, value)
    db.commit()
    print("成功增加学号为:", stu_id, "的学生记录")


def updateGrade():
    """更新成绩, 输入学号, 输入课程号, 输入分数"""
    useDatabase(database)
    stu_id = input("输入学号:")
    if(existStu(stu_id) == 0):
        print("学号不存在")
        return
    selectOneStu(stu_id)
    cur_id = input("输入课程代码:")
    score = int(input("输入分数:"))
    sql = "update grade set score=%s where stu_id=%s and cur_id=%s"
    value = (score, stu_id, cur_id)
    dbObj.execute(sql, value)
    print("修改", dbObj.rowcount, "条记录")
    db.commit()


def deleteStu():
    """删除学生记录, 先删除所有成绩记录"""
    useDatabase(database)
    stu_id = input("输入学号:")
    if(existStu(stu_id) == 0):
        print("学号不存在")
        return
    selectOneStu(stu_id)
    sql = "delete from grade where stu_id=%s"
    value = (stu_id,)
    dbObj.execute(sql, value)
    print("删除", dbObj.rowcount, "条grade数据")
    sql = "delete from student where stu_id=%s"
    dbObj.execute(sql, value)
    print("删除", dbObj.rowcount, "条student数据")
    db.commit()


def selectExcellentStuInCur():
    """在某课程中搜索某课程成绩为优秀的学生, 返回学号, 姓名, 专业, 分数, 90<=优秀<=100"""
    useDatabase(database)
    sql = "select * from curriculum"
    print("课程代码,  课程名,  课程学期,  课程学分")
    dbObj.execute(sql)
    for i in dbObj.fetchall():
        print(i[1], i[2], str(i[3])+"学期", i[4], "学分")
    cur_id = input("输入课程代码:")
    sql = "select s.stu_id, s.stu_name, m.major_name, g.score from student s left join grade g on s.stu_id=g.stu_id left join major m on s.major_id=m.major_id where g.cur_id=%s and g.score>=%s and g.score<=%s"
    value = (cur_id, 90, 100)  # [90, 100]之间
    dbObj.execute(sql, value)
    print("学号", "姓名", "专业", "分数")
    for i in dbObj.fetchall():
        print(i[0], i[1], i[2], i[3], "分")


def line():
    print("============================================")


init()
print("控制台-学生管理数据库系统")
print("课程号 KC-001开始")
print("专业号 001开始")
line()
i = 1
while(i != 0):
    print("1. 在学生表中新增一条记录")
    print("2. 更新成绩")
    print("3. 删除学生记录")
    print("4. 查询某课程中优秀学生名单")
    print("5. 保存数据(student表数据-->student.pkl, ...)")
    print("6. 删除数据库")
    print("7. 查询表")
    print("8. 根据学号查找学生信息")
    print("0. 退出")
    line()
    i = input("输入选项")
    if(i == '1'):
        createStu()
    elif(i == '2'):
        updateGrade()
    elif(i == '3'):
        deleteStu()
    elif(i == '4'):
        selectExcellentStuInCur()
    elif(i == '5'):
        saveData()
    elif(i == '6'):
        dropDatabase(input("输入要删除的数据库名字"))
    elif(i == '7'):
        select()
    elif(i == '8'):
        stu_id = input("输入学号:")
        if(existStu(stu_id) == 1):
            selectOneStu(stu_id)
        else:
            print("学号不存在")
    elif(i == '0'):
        print("===================再会=====================")
        db.close()
        break
    else:
        print("请重新输入")
    line()
os.system("pause")
