'''
字符串标识符。修改例 6-1的 idcheck.py 脚本，使之可以检测长度为1的标识符，
并且可以识别 Python 关键字。对后一个要求，你可以使用 keyword 模块(特别是 keyword.kelist)来辅助。
'''
import string
import keyword
alphas = string.ascii_letters + '_'
nums = string.digits
print('Welcome to the Identifier Checker v2.0')
print('Testees must be atleast 1 chars long.')
myInput = input('Identifier to test?')

if keyword.iskeyword(myInput):
    print('keyword error')
else:
    if len(myInput) > 1:
        if myInput[0] not in alphas:
            print('''invalid:first symbol must be alphabetic''')
        else:
            for otherChar in myInput[1:]:
                if otherChar not in alphas + nums:
                    print("invalid:remaining symbols must be alphanumeric")
                    break
            else:

                print("okay as an identifier")
    elif len(myInput) == 1:
        if myInput[0] not in alphas:
            print('''invalid:first symbol must be alphabetic''')
        else:
            print("okay as an identifier")


