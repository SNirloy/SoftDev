def string_times(str, n):
	#Python has the unique ability to multiply strings, repeating n times
  return n * str

print("Test Cases for StringTimes");
print("\t" + string_times("HelpMe ", 5))
print("Checking without eyes");
strTimesTest = "";
Message = "What are the three numbers on the back of your credit card"
for i in range(1200):
    strTimesTest += Message
print((string_times(Message, 1200) == strTimesTest))

def front_times(str, n):
	#First we check for length, because if it has less, we only use the string
  if len(str) < 3:
    return n * str
  else:
    return n * str[:3]
print ("Test Cases for FrontTimes")
def string_bits(str):

  n = 0
  ret_str = ""
  while n < len(str):
    ret_str += str[n]
    #By incrementing by 2, we can skip over 1 index each time without checking with %
    n += 2
  return ret_str

def string_splosion(str):
  ret_str = ""
  #Looping len times
  for i in range(len(str)):
  #Slicing the str up to i, making sure to add 1 to include the index i
    ret_str += str[:i+1]
  return ret_str

def last2(str):
  #Counter of repetitions
  ret_ctr = 0
  #The final substring we need
  end_str = str[len(str) - 2:]
  #looping thorugh everything besides the final substring we already separated
  for i in range(len(str)-2):
    if end_str == str[i:i+2]:
      ret_ctr += 1
  return ret_ctr

def array_count9(nums):
  ret_ctr = 0
  #A loop that pulls the number out while ignoring index, i is a value in the array
  for i in nums:
    if i == 9:
      ret_ctr += 1
  return ret_ctr

def array_front9(nums):
	#Using a slice to look at only the first 4. Even if the length is less than 4, there will be no problems b/c i is the value in the array
  for i in nums[:4]:
    if i == 9:
      return True
  return False

def array123(nums):
  for i in range(len(nums)-2):
    #Using a loop to change the slice of the array
    if nums[i: i+3] == [1, 2, 3]:
           return True
  return False

def string_match(a, b):
  output = 0
  key = ""
  other = ""
  #Establishing the shorter array as a key to preven IndexOutOfBounds Errors
  if len(a) < len(b):
    key = a
    other = b
  else:
    key = b
    other = a
  for i in range(len(key)-1):
    #Comparing slices of the strings
    if key[i:i+2] == other[i:i+2]:
      output += 1
  return output
