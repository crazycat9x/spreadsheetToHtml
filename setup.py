from distutils.core import setup

setup(
    name='spreadsheetToHtml',
    version='1.0.0',
    install_requires=['openpyxl','odfpy','xlrd']
    packages=['spreadsheetToHtml.styling', 'spreadsheetToHtml.excelConverse'],
    url='',
    license='apache license 2.0',
    author='Tien Nguyen Khac',
    author_email='crazycat194hb@gmail.com',
    description='generating styled html table from spreadsheet'
)
