#https://enlqn1010.tistory.com/39
#16진수 숫자 입력하면 10진수로 바꾸기
import sys
num = input()
hex_num = '0x' + num
print(int(hex_num, 16))