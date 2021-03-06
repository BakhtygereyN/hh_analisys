# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YkzLs8NTko3ppXXt86MSLUwxT41N0vkz
"""

def Salary(salary):
        try:
            if 'USD' in salary.text.strip():
                nsalary = re.sub("[\D]", "", str(
                    salary.text.strip()))  # https://coderoad.ru/1450897/%D0%A3%D0%B4%D0%B0%D0%BB%D0%B8%D1%82%D1%8C-%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D1%8B-%D0%BA%D1%80%D0%BE%D0%BC%D0%B5-%D1%86%D0%B8%D1%84%D1%80-%D0%B8%D0%B7-%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B8-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-Python
                if len(nsalary) >= 6:
                    nsalary = (float(str(nsalary)[len(nsalary) // 2:]) + float(str(nsalary)[:len(nsalary) // 2])) / 2
                else:
                    nsalary = float(nsalary)
            elif 'бел.' in salary.text.strip():
                nsalary = re.sub("[\D]", "", str(salary.text.strip()))
                if len(nsalary) >= 6:
                    nsalary = ((float(str(nsalary)[len(nsalary) // 2:]) + float(str(nsalary)[:len(nsalary) // 2])) / 2) * 0.39
                else:
                    nsalary = float(nsalary) * 0.39
            elif 'руб.' in salary.text.strip():
                nsalary = re.sub("[\D]", "", str(salary.text.strip()))
                if len(nsalary) >= 9:
                    nsalary = ((float(str(nsalary)[len(nsalary) // 2:]) + float(str(nsalary)[:len(nsalary) // 2])) / 2) * 0.013
                else:
                    nsalary = float(nsalary) * 0.013
            elif 'грн.' in salary.text.strip():
                nsalary = re.sub("[\D]", "", str(salary.text.strip()))
                if len(nsalary) >= 8:
                    nsalary = ((float(str(nsalary)[len(nsalary) // 2:]) + float(str(nsalary)[:len(nsalary) // 2])) / 2) * 0.036
                else:
                    nsalary = float(nsalary) * 0.036
            elif 'KZT' in salary.text.strip():
                nsalary = re.sub("[\D]", "", str(salary.text.strip()))
                if len(nsalary) >= 9:
                    nsalary = ((float(str(nsalary)[len(nsalary) // 2:]) + float(str(nsalary)[:len(nsalary) // 2])) / 2) * 0.0023
                else:
                    nsalary = float(nsalary) * 0.0023
            elif 'EUR' in salary.text.strip():
                nsalary = re.sub("[\D]", "", str(salary.text.strip()))
                if len(nsalary) >= 6:
                    nsalary = ((float(str(nsalary)[len(nsalary) // 2:]) + float(str(nsalary)[:len(nsalary) // 2])) / 2) * 1.20
                else:
                    nsalary = float(nsalary) * 1.20

        except:
            nsalary = None
        return nsalary

def pageparse():
    count = 0
    for url in alllinks:
        count += 1
        print(count)
        response = requests.get(url[0], headers=headers).text
        content = BeautifulSoup(response, "lxml")
        try:
            company = content.find('span', {'class':'bloko-section-header-2 bloko-section-header-2_lite'})
            allcompany.append(company)
        except:
            company = None
            allcompany.append(company)
        name = content.find('h1', {'data-qa':'vacancy-title'})
        salary = content.find('span', {'data-qa':'bloko-header-2'})
        city = url[1]
        experience = content.find('span', {'data-qa':'vacancy-experience'})
        skills = content.findAll('span', {'data-qa':'bloko-tag__text'})
        try:
            nexp = re.sub(r'[А-Яа-я]+', r'', experience.text.strip()) #https://evileg.com/ru/post/642/

            if len(nexp) > 2:
                nexp = (float(str(nexp)[0]) + float(str(nexp)[2]))/2
            else: nexp = float(nexp)
        except:
            nexp = 0
for i in range(len(skills)):
            skills[i] = skills[i].text.strip()
        newsalary = Salary(salary)
        try:
            allnames.append(name.text.strip())
        except:
            allnames.append(None)
        allskills.append(skills)
        allexp.append(nexp)
        allurl.append(url[0])
        allcity.append(city)
        allsalary.append(newsalary)
        try:
            print(name.text.strip(), newsalary, skills, nexp, url[0], city)
        except:
            print('neseychas')
        time.sleep(random.uniform(0.5, 2))


regionparse()
linkparse()
print(len(alllinks))
pageparse()
df = pd.DataFrame({'name':allnames,'salary': allsalary,'city':allcity, 'exp': allexp,'company':allcompany, 'skills': allskills})
print(df)

writer = pd.ExcelWriter("123.xlsx", engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

format1 = workbook.add_format({'num_format': '#,##0.00'})
format2 = workbook.add_format({'num_format': '#,##0.00'})
format3 = workbook.add_format({'num_format': '#,##0.00'})
format4 = workbook.add_format({'num_format': '#,##0.00'})
format5 = workbook.add_format({'num_format': '#,##0.00'})
worksheet.set_column('B:B', 30, format1)
worksheet.set_column('C:C', 30, format2)
worksheet.set_column('B:B', 30, format3)
worksheet.set_column('C:C', 30, format4)
worksheet.set_column('B:B', 30, format5)
writer.save()

df.to_csv('123.csv', encoding='utf-32', index=False)