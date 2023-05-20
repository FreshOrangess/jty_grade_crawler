from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By


options = webdriver.EdgeOptions()
options.add_argument('--headless')
options.add_argument('window-size=1920x1080')
options.add_argument('--start-maximized')
options.add_argument('--disable-gpu')
wd = webdriver.Edge(service=Service('msedgedriver.exe'), options=options)
with open('student_numbers.txt', 'r') as f:
    for line in f:
        student_number = line.split()[0]
        password = student_number[4:]
        wd.get('http://jtyjy.onlyets.com/')
        wd.implicitly_wait(5)
        element = wd.find_element(By.ID, 'btnLeft')
        element.click()
        wd.implicitly_wait(5)
        element = wd.find_element(By.ID, 'txbUserName')
        element.send_keys(student_number)
        element = wd.find_element(By.ID, 'txbPassword')
        element.send_keys(password)
        element = wd.find_element(By.ID, 'btnSubmit')
        element.click()
        wd.implicitly_wait(5)
        try:
            element = wd.find_element(By.CLASS_NAME, 'btn-report')
            element.click()
            wd.implicitly_wait(5)
            # 姓名
            element = wd.find_element(By.XPATH, '//*[@id="FrameNav-Main"]/div[1]/div/div[2]/ul')
            student_name = element.text.split('，')[1].split(' ')[0]
            # 总成绩
            element = wd.find_element(By.XPATH, '//*[@id="tab_score"]/tbody/tr[1]/td[2]')
            overall_grade = element.get_attribute('textContent').replace('\\','\\\\')
            assign = overall_grade.split('\\\\')[1]
        except:
            continue
        # subject_1
        try:
            element = wd.find_element(By.XPATH, '//*[@id="tab_score"]/tbody/tr[3]/td[1]')
            subject_1 = element.get_attribute('textContent')+':'
            element = wd.find_element(By.XPATH, '//*[@id="tab_score"]/tbody/tr[3]/td[2]')
            if '\\' in element.get_attribute('textContent'):
                subject_grade_1 = element.get_attribute('textContent').replace('\\', '\\\\')
            else:
                subject_grade_1 = element.get_attribute('textContent')
        except:
            subject_1_garde = ""
        # subject_2
        try:
            element = wd.find_element(By.XPATH, '//*[@id="tab_score"]/tbody/tr[2]/td[1]')
            subject_2 = element.get_attribute('textContent')+':'
            element = wd.find_element(By.XPATH, '//*[@id="tab_score"]/tbody/tr[2]/td[2]')
            if '\\' in element.get_attribute('textContent'):
                subject_grade_2 = element.get_attribute('textContent').replace('\\', '\\\\')
            else:
                subject_grade_2 = element.get_attribute('textContent')
        except:
            subject_2_grade = ""
        # subject_3
        try:
            element = wd.find_element(By.XPATH, '//*[@id="tab_score"]/tbody/tr[4]/td[1]')
            subject_3 = element.get_attribute('textContent')+':'
            element = wd.find_element(By.XPATH, '//*[@id="tab_score"]/tbody/tr[4]/td[2]')
            if '\\' in element.get_attribute('textContent'):
                subject_grade_3 = element.get_attribute('textContent').replace('\\', '\\\\')
            else:
                subject_grade_3 = element.get_attribute('textContent')
        except:
            subject_3_grade = ""
        # subject_4
        try:
            element = wd.find_element(By.XPATH, '//*[@id="tab_score"]/tbody/tr[5]/td[1]')
            subject_4 = element.get_attribute('textContent')+':'
            element = wd.find_element(By.XPATH, '//*[@id="tab_score"]/tbody/tr[5]/td[2]')
            if '\\' in element.get_attribute('textContent'):
                subject_grade_4 = element.get_attribute('textContent').replace('\\', '\\\\')
            else:
                subject_grade_4 = element.get_attribute('textContent')
        except:
            subject_4 = ""
            subject_grade_4 = ""
        # subject_5
        try:
            element = wd.find_element(By.XPATH, '//*[@id="tab_score"]/tbody/tr[6]/td[1]')
            subject_5 = element.get_attribute('textContent')+':'
            element = wd.find_element(By.XPATH, '//*[@id="tab_score"]/tbody/tr[6]/td[2]')
            if '\\' in element.get_attribute('textContent'):
                subject_grade_5 = element.get_attribute('textContent').replace('\\', '\\\\')
            else:
                subject_grade_5 = element.get_attribute('textContent')
        except:
            subject_5 = ""
            subject_grade_5 = ""
        # subject_6
        try:
            element = wd.find_element(By.XPATH, '//*[@id="tab_score"]/tbody/tr[7]/td[1]')
            subject_6 = element.get_attribute('textContent')+':'
            element = wd.find_element(By.XPATH, '//*[@id="tab_score"]/tbody/tr[7]/td[2]')
            if '\\' in element.get_attribute('textContent'):
                subject_grade_6 = element.get_attribute('textContent').replace('\\', '\\\\')
            else:
                subject_grade_6 = element.get_attribute('textContent')
        except:
            subject_6 = ""
            subject_grade_6 = ""
        print("INSERT INTO `2023年4月金太阳联考` (`姓名`, `考号`,`总分`, `subject_1`, `subject_1_grade`, `subject_2`, `subject_2_grade`, `subject_3`, "
              "`subject_3_grade`,"
              "`subject_4`, `subject_4_grade`,`subject_5`, `subject_5_grade`, `subject_6`, `subject_6_grade`,"
              "`赋分总分`) VALUES"
              "('%s','%s', '%s', '%s', '%s', '%s', '%s',"
              "'%s', '%s', '%s', '%s', '%s','%s','%s','%s','%s');" % (student_name, student_number, overall_grade,subject_1,subject_grade_1,subject_2, subject_grade_2, subject_3, subject_grade_3,subject_4,subject_grade_4, subject_5,subject_grade_5,subject_6,subject_grade_6,assign))
