# list1 = [10]
# list1[0] = 9000
# # list1[1] = 600

# print(list1)

import json

f1 = open("record.txt","r")
g = f1.read()
record = json.loads(g)
f1.close()

# record = {'1001' : {'pName' : '5 star', 'qn' : 220, 'price' : 10},
#           '1002' : {'pName' : 'Parle G', 'qn' : 160, 'price' : 5},
#           '1003' : {'pName' : 'Oats', 'qn' : 400, 'price' : 30},
#           '1004' : {'pName' : 'kellogs', 'qn' : 304, 'price' : 60},
#           }

# print(record['1003']['price'])

print("--------------------Menu---------------------")
for i in record.keys():
    print(i ,"------>", record[i]['pName'],'||',record[i]['qn'], '||', record[i]['price'])


user_need = input("Enter Product Id: ")
quantity = int(input("ENter Product Quantity: "))
total_bill = 0
if quantity <= record[user_need]['qn']:
    total_bill = quantity * record[user_need]['price']
    record[user_need]['qn'] -= quantity
    print("Total Bill Amount is",total_bill)
    print("Inventory Updated!!!")
else:
    print(f"We have Only {record[user_need]['qn']} quantities.")
    temp = input("If u need then press Y or y: ")

    if temp.lower() == 'y':
        total_bill = record[user_need]['qn'] * record[user_need]['price']
        record[user_need]['qn'] = 0
        print("Total Bill Amount is",total_bill)
        print("Inventory Updated!!!")
    else:
        print("Thank You!!!")

print("Updated Record: ")
for i in record.keys():
    print(i ,"------>", record[i]['pName'],'||',record[i]['qn'], '||', record[i]['price'])



fp = open("record.txt","w")
js = json.dumps(record)
fp.write(js)
fp.close()