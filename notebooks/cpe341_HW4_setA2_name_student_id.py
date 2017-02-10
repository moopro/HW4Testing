
# coding: utf-8

# # CPE-341, Quiz 2/2015 - Question Set A2
# 
# - Iteration Design Pattern : List, Dictionary
# - Using Class Die in a List

# In[1]:

get_ipython().magic('reload_ext load_style')
get_ipython().magic('load_style talk.css')


# In[20]:

## รหัสประจำตัวนักศึกษา :
## ชื่อนักศึกษา
##
## คลิก Run cell นี้เพียงครั้งเดียว
##
##
import datetime
datetime.datetime.now().isoformat()


# ## Question 1 ( @2 pt x 2 = 4 pts )
# 
# ### Q1.a 
# จงเขียนคำสั่ง เพื่อพิมพ์ค่าตัวเลขด้วย index ที่กำหนดให้ใน list `mynums` ต่อไปนี้ 

# In[3]:

## ไม่แก้ไขข้อมูลใน cell นี้

mynums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]


# In[4]:

## ANSWER Q1.a
##
##
index = 6 




# ### Q1.b 
# จงเขียนคำสั่ง เพื่อพิมพ์ตัวเลขที่มีค่าน้อยกว่า 1 จาก list `mynums` ในข้อ (1.a)

# In[5]:

## ANSWER Q1.b
##




# In[ ]:




# ## Question 2 ( @3 pts x 4 = 12 pts )
# 
# ### Q2.a 
# จงสร้าง **list** เพื่อเก็บข้อมูลตัวเลขคี่ -13 ถึง 13  โดยใข้ `range`

# In[6]:

## ANSWER Q2.a
##



# ### Q2.b 
# จงสร้าง **list** เพื่อเก็บตัวเลขสุ่มในช่วง 1-12 จำนวน 20 ตัวเลข โดยใข้ฟังก์ชั่น `randint` จากไลบรารี `random`

# In[7]:

## ANSWER Q2.b
##
from random import randint 




# In[ ]:




# ### Q2.c 
# จงหาผลรวมของ **list** ต่อไปนี้แล้วเก็บไว้ที่ตัวแปรชื่อ myTotal โดยใข้ฟังก์ชั่น `sum`
# 
# ```
# myTest = [-38, 72, -33, 18, 96, -83, 57, 41]
# ```

# In[8]:

## ANSWER Q1.c
##




# In[ ]:




# ### Q2.d 
# จงเขียน `def` ชื่อ `average` สำหรับหาค่าเฉี่ยของตัวเลขใน **list** `numbers` ที่เป็น argument  
# 
# เช่น เมื่อเรียกใช้ `average()` จะได้ผลลัพธ์ดังงนี้
# 
# **Hint:**__  ใช้ฟังก์ชัน `sum` และ `len` เพื่อหาค่าเฉลี่ย

# In[9]:

# ตีวอย่างการหาค่า float (ตัวเลขมีทศนิยม)
i = 5
print( float(i) )


# In[10]:

## ANSWER Q2.d
##

def average(numbers):
    pass



# In[11]:

## Test average()
mynums = [i for i in range(51,101,5) ]

print(mynums)
average(mynums)


# In[ ]:




# ## Question 3 ( @6 pts x 2 = 12 pts )
# 
# ### Q3.a 
# กำหนดให้ **dict** `NZ_COINS` เก็บค่าเงินของเหรียญนิวซีแลนด์ 5 ชนิด (ใช้ใน Q3.b)
# 
# จงหาจำนวนเหรียญทั้งหมดใน list `mypiggy` ซึ่งเป็นกระปุกเงินเก็บเหรียญ

# In[12]:

## ไม่แก้ไขข้อมูลใน cell นี้

## เหรียญเงินนิวซีแลนด์ เช่น '20c' หมายถึง 20 cents, '2$' หมายถึง 2 Dollars 
NZ_COINS = { "10c": 0.10, "20c": 0.20, "50c": 0.50, "1$": 1, "2$": 2 } 

## mypiggy keeps the number of NZ coins 
mypiggy  = { "20c": 11, "2$": 4, "10c": 5, "1$": 12 }


# In[13]:

## ANSWER Q3.a
## หาจำนวนเหรียญทั้งหมดใน list mypiggy 
##





# In[ ]:




# ### Q3.b
# จงหามูลค่าของเงินทั้งหมดใน list `mypiggy` (หน่วย: ดอลลาร์ นิวซีแลนด์)

# In[14]:

## ANSWER Q3.b
## 




# In[ ]:




# ## Question 4 ( @6 pts x 2 = 12 pts )
# 
# ### Q4.a 
# จาก class `Die` ที่กำหนดให้ จงสร้างลูกเต๋าเก็บไว้ใน list ชื่อ `my2dice` สองลูก แล้วหาค่าผลรวมของหน้าลูกเต๋าสองลูกนั้น

# In[15]:

## ไม่แก้ไขข้อมูลใน cell นี้
from random import randint

class Die(object):
    def __init__(self):
        """ สร้างลูกเต๋า 1 ลุก 6 หน้า ที่มีค่าเริ่มต้นค่าสุ่ม 1..6 """
        self.__face = randint(1,6)
    @property
    def face(self):
        """ return เลขหน้าลูกเต๋า 1..6 """
        return self.__face
    
    def roll(self):
        """ ทอดลุกเต๋า เลขหน้าลูกเต๋าจะเปลี่ยนด้วยค่า random 1..6 """
        self.__face = randint(1,6)
        
    def __str__(self):
        """ return ข้อความ str, พร้อมกับเลขหน้าลูกเต๋า """
        return ( "Die face: {}".format(self.__face) )
        


# In[16]:

help(Die)


# In[17]:

## ANSWER Q4.a
##
##






# In[ ]:




# ### Q4.b 
# จงปรับปรุุง def `printDiceStat` เพื่อหาสถิติ (เปอร์เซ็นต์) ของการทอดลูกเต๋า จำนวน 1,000 ครั้ง โดยพิมพ์สถิติของหน้าลุกเต๋าทุกหน้า `1..6`  โดยจะพิมพ์สถิติตามตัวอย่างต่อไปนี้
# 
# ```
# Number of rolls: 1000
# 
# ---------- Dice Stats -----------
# face <= 3 count: 497,  49.70 %
# face  > 3 count: 503,  50.30 % 
# ```
# 

# In[18]:

def printDiceStat( numberRolls ):
    """ numberRolls : the number of rolls """
    
    die = Die()

    # เก็บจำนวนครั้งที่ได้หน้าูลูกเต๋า <= 3 ที่ index = 0, จำนวนครั้งที่หน้าูลูกเต๋า > 3 ที่ index = 1 
    counts = [0, 0] 
    
    
    
    
    
    
            
    print("Number of rolls: {}".format(numberRolls)) 
    
    print("\n---------- Dice Stats -----------")    
    percentage = 100. * counts[0] / numberRolls
    print("face {} count: {:>3}, {:6.2f} %".format( "<= 3", counts[0], percentage )) 
    
    
    
    

#--- Test the def printDiceStat ---
rolls = 1000
printDiceStat( rolls )


# In[ ]:




# In[ ]:




# In[21]:

import datetime
datetime.datetime.now().isoformat()
##
## รหัสประจำตัวนักศึกษา :
##
## แล้วคลิก Run cell ครั้งเดียว เมื่อส่งงาน


# ## end of IPynb
