
# User parameters
meeting_id = '123123123'  # edit this
MINUTES = 120  # how long your classes are (eg. 120 minutes = 2 hours)



# 0. Import Libraries
try:
    import pyautogui  # automate mouse/key
    import openpyxl  # extract from excel
except ModuleNotFoundError as err:
    print("necessary libraries are not installed, refer to README")
    input()
    
import time, datetime, os



# 1. open feishu
def openFeishu():
    pyautogui.press('esc',interval=0.1)
    time.sleep(0.2)
    pyautogui.press('win',interval=0.1)
    pyautogui.write('feishu')
    pyautogui.press('enter',interval=1)
    time.sleep(2)



# 2. join meeting
def joinMeeting():
    x,y=pyautogui.locateCenterOnScreen('feishu_meeting.png', confidence=0.8)
    print(x,y)
    pyautogui.click(x,y)
    pyautogui.press('enter',interval=6)

    x,y=pyautogui.locateCenterOnScreen('feishu_join.png', confidence=0.9)
    pyautogui.click(x,y)
    pyautogui.press('enter',interval=12)

    for i in meeting_id: # why use for loop? Feishu only allows writing 1 number at a time
        pyautogui.write(i)

    pyautogui.press('enter',interval=1)



# 3. Extract meeting info from excel sheet
meetings = []
wb = openpyxl.load_workbook('List.xlsx')
sheet = wb['Sheet1']

for i in sheet.iter_rows(values_only = True):
    if i[0]!=None:  # iterate until the row is empty
        meetings.append(i)
meetings.pop(0)  # remove the descriptions in excel (eg. Time(in format: dd-mm...))
meetings.sort()



# 4. Wait eg. 3 hours until first meeting
for i,v in enumerate(meetings):
    curmeeting = v  # eg. ('24-08-2021 12:30 PM', None, '123123123', None)

    now = int(time.time())  # time right now, Add 8hrs since UTC + 8hrs in China
    temp = datetime.datetime.strptime(curmeeting[0], "%d-%m-%Y %I:%M %p").timestamp() # meeting time

    print(f'now: {time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(now))}')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(temp)))
    print(f'you have {(temp-now)/3600} hours left before meeting starts')
    
    if now<temp-60:
        time.sleep(temp-now-60) # wait eg. 3 hours & join 1 minute earlier

    openFeishu()
    joinMeeting()

# 5. Terminate Feishu when class ends
    while True:
        if time.time() - temp >= MINUTES * 60:  # if 2 hours of class have passed
            os.system("taskkill /f /im Feishu.exe")
        else:
            time.sleep(600)

    
    




