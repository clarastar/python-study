# age = 20
#
# if age < 21:
#     print("no beer for you")



# name = 'Clara'
# if name is 'Tony':
#     print("Hey there Tony")
# elif name is "Clara":
#     print("This is Clara")
# elif name is "Derik":
#     print("How about you Derik")
# else:
#     print("please signup the website!")



# foods = ['bacon', 'tuna', 'ham', 'beef']
# for f in foods[:2]:
#     print(f)
#     print(len(f))


# for x in range(5, 20, 2):
#     print(x)

# cherry = 80
# while cherry < 90:
#     print(cherry)
#     cherry += 1


# magicNumber = 0
# for n in range(101):
#     if n is magicNumber:
#         print(n, "is the magicNumber")
#         break
#     else:
#         print(n)


# numbersToken = [3, 5, 6, 7, 0]
# print("here are the numbers")
#
# for n in range(2, 30):
#     if n in numbersToken:
#         continue
#     print(n)


# functions
# def summer():
#     print("function is cool")
# summer()

#
# def bitcoin_to_usd(btc):
#     amount = btc * 100
#     print(amount)
#
# bitcoin_to_usd(2)


# def allowed_dating_age(my_age):
#     girls_age = my_age / 2 + 7
#     return girls_age
#
# claras_limit = allowed_dating_age(30)
# tonys_limit = allowed_dating_age(50)
# print("clara", claras_limit)
# print("tony", tonys_limit)



# def get_gender(sex='Unknown'):
#     if sex is 'm':
#         sex = 'Male'
#     elif sex is 'f':
#         sex = 'Female'
#     print(sex)
#
#
# get_gender('m')
# get_gender('f')
# get_gender()


# def corn():
#     a = 8789
#     print(a)
#
# def fudge():
#     print(a)
#
# corn()
# fudge()


# def dumb_sentence(name='Bucky', action='eat', item='tuna'):
#     print(name, action, item)
#
#
# dumb_sentence()
# dumb_sentence('Sally', 'farts', 'gently')
# dumb_sentence(item='awesome')


# def add_numbers(*args):
#     total = 0
#     for a in args:
#         total += a
#     print(total)
#
#
# add_numbers(3)
# add_numbers(3, 4, 4, 4)


# def health_calculator(age, apples_ate, cigs_smoked):
#     answer = (100 - age) + (apples_ate * 3.5) - cigs_smoked * 2
#     print(answer)
#
#
# buckys_data = [27, 20, 0]
# health_calculator(buckys_data[0], buckys_data[1], buckys_data[2])
# health_calculator(*buckys_data)


# groceries = {'cereal', 'milk', 'starcrunch', 'beer', 'duck_tape', 'lotion', 'beer'}
# print(groceries)
# if 'milk' in groceries:
#     print('you already have milk')
# else:
#     print('you need milk')


# classmates = {"Tony": "cool but smells", "Emma": "is awesome", "Lucy": "study hard"}
# print(classmates)
# print(classmates['Emma'])
#
# for k, v in classmates.items():
#     print(k + v)


# import tuna
# import random
#
# tuna.fish()
#
# x = random.randrange(1, 1000)
# print(x)



# import random
# import urllib.request
#
#
# def download_web_image(url):
#     name = random.randrange(1, 1000)
#     full_name = str(name) + '.jpg'
#     urllib.request.urlretrieve(url, full_name)

# download_web_image('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1497777483203&di=3af25aa94b14220ac100be1d5259fc96&imgtype=0&src=http%3A%2F%2Fimage14-c.poco.cn%2Fmypoco%2Fmyphoto%2F20130320%2F01%2F173350639201303200055373079844208499_007.jpg')


# fw = open('sample.txt', 'w')
# fw.write('writing some stuff in my text file\n')
# fw.write('I like bacon\n')
# fw.close()
#
# fr = open('sample.txt', 'r')
# text = fr.read()
# print(text)
# fr.close()


from urllib import request

goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1495089768&period2=1497768168&interval=1d&events=history&crumb=WHg8kEZlFjC'


def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, "w")

    for line in lines:
        fx.write(line + "\\n")
    fx.close()


download_stock_data(goog_url)
