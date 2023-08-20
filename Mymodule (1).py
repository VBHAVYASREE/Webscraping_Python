# greetings
def greeting(name):
    print(f"Hello {name} have a good day.")

# add list of value
def add(num):
    s=0
    for i in num:
        s+=i
    return s

# multiply list number
def multiply(num):
    m=0
    for i in num:
        m+=i
    return m

# check list of prime numbers
def list_prime(num):
    prime_numbers=[]
    for i in num:
        if i >= 1:
            for k in range(2,i):
                if i%k==0:
                    break
            else:
                prime_numbers.append(i)
    return prime_numbers
                
# check prime number
def prime(n):
    flag=False
    if n <= 1:
        flag=False
    elif n==2:
        flag=True
    else:
        for i in range(2,n):
            if n%i==0:
                flag=False
                break
            else:
                flag=True
    return flag

# check leap year
def leap(year):
    l=False
    if year%4==0:
        if year%100==0:
            if year%400==0:
                l=True
            else:
                l=False
        else:
            l=True
    else:
        l=False
    return l

# check armstrong  number
def armstrong(num):
    x=len(str(num))
    z=0
    for i in str(num):
        n=int(i)**x
        z+=n
    if num==z:
        return True
    else:
        return False
    
# check palindrome or not
def palindrome(num):
    x=str(num)
    z=x[::-1]
    if str(num)==z:
        return True
    else:
        return False

# find ascii value
def ascii(s):
    return ord(s)

# convert celsius to fahernheit
def celsius(num):
    f = (num * 1.8) + 32
    return f

# convert fahrenheit to celsius
def fahrenheit(num):
    c = (num-32)/1.8
    return c

# find outliers
def outlier(data):
    import numpy as np
    data=sorted(data)
    q1,q3=np.percentile(data,[25,75])
    IQR=q3-q1
    lower_fence=q1-(1.5*IQR)
    upper_fence=q3+(1.5*IQR)
    outliers=[]
    for i in data:
        if lower_fence > i or upper_fence < i:
            outliers.append(i)
    return outliers

# check higest top 3 value into the list
def highest_three(num):
    num.sort()
    x=num[-3:]
    z=x[::-1]
    return z

# select table from database
def selectTable(**kwargs):
    import mysql.connector as ms
    mydb=ms.connect(host='localhost',user='root',password='Neeraj@123',database=kwargs['database'])
    mycur=mydb.cursor()
    sql=f"select * from {kwargs['table']}"
    mycur.execute(sql)
    x=mycur.fetchall()
    return x

# timer functions countdown 
def countdown(time_sec):
    import time
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        tim=f"{mins:02}:{secs:02}"
        print(tim,end='\r')
        time.sleep(1)
        time_sec -= 1
    print("Time's Up")
    
# sum of odd and even numbers
def even_odd_sum(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=i
        else:
            odd+=i
    print(f"Sum of even numbers are {even}.\nSum of odd numbers are {odd}.")

def file_to_database(file, **kwargs):
    import pandas as pd
    import mysql.connector as ms
    df=pd.read_csv(file,encoding='unicode_escape')
    n=df.shape
    mydb=ms.connect(host='localhost',user='root',password='Neeraj@123',database=kwargs['database'])
    for i in range(n[0]):
        x=df.loc[i]
        mycur=mydb.cursor()
        c=kwargs['table']
        sql=f'insert into {c} values ({x[0]},"{x[1]}",{x[2]})'
        mycur.execute(sql)
        mydb.commit()
    return 'Submitted'

# formating DataFrame
def formating_DataFrame(df, **kwargs):
    '''DataFram*: any,
    Table Heading: 'str'
    '''
    columns = [i for i in df.columns]
    str_length = []
    for i in columns:
        check_len = [len(str(k)) for k in df[i]]
        check_len.insert(0, len(str(i)))
        str_length.append(max(check_len))
      
    # print Table heading and Columns Name
    txt=''
    for index,col in enumerate(columns):
        sc = ''
        for s in range(str_length[index]-len(col)):
            sc+= ' '
        txt += f"| {col}{sc} "
    txt = txt+'|'
    heading = str(kwargs['title'])
    for line in range(round((len(txt))/2)-round(len(heading)/2)):
        print(' ',end='')
    print(heading)
    print('+',end='')
    for line in range(len(txt)-2):
        print('-',end='')
    print('+')
    print(txt)
    print('+',end='')
    for line in range(len(txt)-2):
        print('-',end='')
    print('+')
    
    # print data values
    dataset_shpe = df.shape
    for i in range(dataset_shpe[0]):
        row_data = df.iloc[i]
        txt_1=''
        for index,data in enumerate(row_data):
            sc = ''
            for s in range(str_length[index]-len(str(data))):
                c=' '
                sc+=c
            txt_1 += f"| {data}{sc} "
        txt_1 = txt_1+'| '
        print(txt_1)
    print('+',end='')
    for line in range(len(txt)-2):
        print('-',end='')
    print('+')

# design String line
def design_text(text):
    x = f"| {text} |"
    print('+',end='')
    for i in range(len(x)-2):
        print('-',end='')
    print('+')
    print(x)
    print('+',end='')
    for i in range(len(x)-2):
        print('-',end='')
    print('+')
    