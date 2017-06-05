from setuptools import setup

setup(
    name='spreadsheetToHtml',
    version='1.0.0',
    packages=['spreadsheetToHtml.styling', 'spreadsheetToHtml.excelConverse'],
    install_requires=['openpyxl','odfpy','xlrd'],
    url='',
    license='apache license 2.0',
    author='Tien Nguyen Khac',
    author_email='crazycat194hb@gmail.com',
    description='generating styled html table from spreadsheet'
)
