@echo off
chcp 1251
REM ������� ������ ����� Lab2, ���� ��� ����������
rmdir /S /Q C:\Lab2

REM ������� �������� ����� Lab2 � �������� FAM
mkdir C:\Lab2\FAM
cd C:\Lab2\FAM

REM ������� ����������� 1, 2 � 3
mkdir 1
mkdir 2
mkdir 3

REM ��������� � ����� 1 � ������� ����� 11.txt � 12.txt
cd 1
echo ������ ������������� > 11.txt
echo ��������� ������������� > 12.txt

REM ������������ � FAM
cd ..

REM ��������� � ����� 2 � ������� ���� 2.txt
cd 2
echo ���� � �������� 2 > 2.txt

REM ������������ � FAM
cd ..

REM ��������� � ����� 3 � ������� ����� 31.txt � 32.txt
cd 3
echo ����� ������ > 31.txt
echo ������ ��������� ��������� > 32.txt

REM ������������ � FAM
cd ..

REM ������� ������ ��������� � ������
echo ��������� ��������� � ������ �������:
tree C:\Lab2\FAM /F
pause