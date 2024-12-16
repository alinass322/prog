@echo off
chcp 1251
REM Удаляем старую папку Lab2, если она существует
rmdir /S /Q C:\Lab2

REM Создаем основную папку Lab2 и подпапку FAM
mkdir C:\Lab2\FAM
cd C:\Lab2\FAM

REM Создаем подкаталоги 1, 2 и 3
mkdir 1
mkdir 2
mkdir 3

REM Переходим в папку 1 и создаем файлы 11.txt и 12.txt
cd 1
echo начало стихотворения > 11.txt
echo окончание стихотворения > 12.txt

REM Возвращаемся в FAM
cd ..

REM Переходим в папку 2 и создаем файл 2.txt
cd 2
echo файл в каталоге 2 > 2.txt

REM Возвращаемся в FAM
cd ..

REM Переходим в папку 3 и создаем файлы 31.txt и 32.txt
cd 3
echo номер группы > 31.txt
echo список изучаемых предметов > 32.txt

REM Возвращаемся в FAM
cd ..

REM Выводим дерево каталогов и файлов
echo Структура каталогов и файлов создана:
tree C:\Lab2\FAM /F
pause