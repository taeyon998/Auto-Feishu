# Auto-Feishu
This python script lets you automatically join your Feishu classes in pre-set time

Input format:
  Time: dd-mm-yyyy hh:mm AM/PM
  Meeting ID: eg. 123456123
  
How to use:
  1. Install libraries  (skip if already installed)
        '''  
        pip install pyautogui  
        pip install openpyxl  
        '''  
  2. Open "List.xlsx" and insert your (1) Time and (2) Meeting ID for your feishu classes. 
  3. Make sure to completely close feishu (terminate feishu), or else it might or might not work
  4. Run joinFeishu.py  (make sure to (1) download the two image files, feishu_join.png and feishu_meeting.png, and (2) PLACE THEM IN THE SAME FOLDER/location AS joinFeishu.py)  
        Open cmd (for windows)  
        Navigate to where your joinFeishu.py file is  (eg. cd Desktop)  
        python joinFeishu.py  
  5. Do not close the command prompt, it is where the program is running
  
This project was inspired by:  
  https://github.com/Kn0wn-Un/Auto-Zoom  
 Since this was for zoom, I made a feishu version.
