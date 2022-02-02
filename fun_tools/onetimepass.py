import math, random

n=13

def generateOTP():
  string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  OTP = ""
  length = len(string)
  print("OTP Generation")

  global n
  
  for i in range(n):
        OTP += string[math.floor(random.random() * length)]

  return OTP

if __name__ == "__main__":
  print("OTP of length {num}:".format(num=n), generateOTP())