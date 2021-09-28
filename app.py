from helpers import upload_prep, upload
import datetime




nums = []

while True:

    x = input("Enter value: ")

    if x == 'done':
        break

    else:

        try:
            nums.append(float(x))
        except:
            print('Not an integer or done')

tt = input('Today? (T or F) \n' ).lower()

if tt == 't':
    x = datetime.datetime.now().strftime('%y%m%d')
else:
    x = input('Enter date (YYMMDD): \n')
    
 
x_vec = [x] * len(nums)
    

df = upload_prep(nums,x_vec)
upload(df)

