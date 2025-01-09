import csv
import pandas as pd 
from datetime import datetime
def sum_to_single_digit(number):
    while number > 9:
        total = 0
        while number > 0:
            total += number % 10
            number //= 10
        number = total
    return number
chaldean_alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'U': 6,
                         'O': 7, 'F': 8, 'I': 1, 'G': 3, 'H': 5, 'Z': 7,
                         'Y': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'X': 5,
                         'O': 7, 'P': 8, 'Q': 1, 'R': 2, 'S': 3, 'T': 4,
                         'V': 6, 'W': 6, 'J': 1}


def sum_to_digit(number):
    sum=0
    for num in str(number):
        sum=sum+int(num)
    return sum
def sum_to_single_digit(number):
    while number > 9:
        total = 0
        while number > 0:
            total += number % 10
            number //= 10
        number = total
    return number

dict_data={}
df = pd.read_csv("./data-2.csv") 

golden2=0
count_b=0
count_56=0
doable_count=0
def planes():
        aa=0
        golden2+=check_mb(day,month,year)
        golden1=golden(mb_string(day,month,year))
        silver1=silver(mb_string(day,month,year))
        will1=will(mb_string(day,month,year))
        thought1=thought(mb_string(day,month,year))
        action1=action(mb_string(day,month,year))
        practical1=practical(mb_string(day,month,year))
        emotional1=emotional(mb_string(day,month,year))
        mental1=mental(mb_string(day,month,year))
        if "golden" not in dict_data:
            dict_data["golden"]=golden1
        else:
            dict_data["golden"]+=golden1
        if "silver" not in dict_data:
            dict_data["silver"]=silver1
        else:
            dict_data["silver"]+=silver1
        if "will" not in dict_data:
            dict_data["will"]=will1
        else:
            dict_data["will"]+=will1
        if "thought" not in dict_data:
            dict_data["thought"]=thought1
        else:
            dict_data["thought"]+=thought1
        if "action" not in dict_data:
            dict_data["action"]=action1
        else:
            dict_data["action"]+=action1
        if "practical" not in dict_data:
            dict_data["practical"]=practical1
        else:
            dict_data["practical"]+=practical1
        if "emotional" not in dict_data:
            dict_data["emotional"]=emotional1
        else:
            dict_data["emotional"]+=emotional1
        if "mental" not in dict_data:
            dict_data["mental"]=mental1
        else:
            dict_data["mental"]+=mental1
for index, row in df.iterrows():

                # if not pd.isna(row[0]) :
                if not pd.isna(row[14]):
                            doable_count=doable_count+1           
                            try:
                                date_object = datetime.strptime(row[14], "%m/%d/%Y %H:%M")           
                                day = date_object.day
                                month = date_object.month
                                year = date_object.year
                                mulank=sum_to_single_digit(day)
                                bhagyank=sum_to_single_digit(int(str(day)+str(month)+str(year)))
                                final_str=str(day)+str(month)+str(year)+str(mulank)+str(bhagyank)
                                c_temp=0
                                for num in range(1 , 10):
                                    if str(num) in final_str:
                                        c_temp=c_temp+1
                                if str(c_temp) in dict_data.keys():
                                    dict_data[str(c_temp)]=dict_data[str(c_temp)]+1
                                else:
                                    dict_data[str(c_temp)]=1
                            except Exception as e:
                                print("Error message:", e)
                                             

sorted_mbc= dict(sorted(dict_data.items(), key=lambda item: -item[1]))
print(sorted_mbc)                
