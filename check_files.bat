@echo off
chcp 1251
setlocal

:: �������� ������� ����� help.txt
if exist "C:\Users\������\Documents\help.txt" (
    echo ���� help.txt ������.
    echo.
    type "C:\Users\������\Documents\help.txt"  :: ������� ���������� help.txt
    echo.

    :: �������� ������� ����� if_help.txt
    if exist "C:\Users\������\Documents\if_help.txt" (
        echo ���� if_help.txt ������.
        type "C:\Users\������\Documents\if_help.txt"  :: ������� ���������� if_help.txt
        echo.
    ) else (
        echo ���� if_help.txt �� ������.
    )

    :: �������� ������� ����� goto_help.txt
    if exist "C:\Users\������\Documents\goto_help.txt" (
        echo ���� goto_help.txt ������.
        type "C:\Users\������\Documents\goto_help.txt"  :: ������� ���������� goto_help.txt
        echo.
    ) else (
        echo ���� goto_help.txt �� ������.
    )

    :: ����������� ����������� ������ if_help.txt � goto_help.txt � ����� ���� combined.txt
    if exist "C:\Users\������\Documents\if_help.txt" (
        type "C:\Users\������\Documents\if_help.txt" >> "C:\Users\������\Documents\combined.txt"
    )
    if exist "C:\Users\������\Documents\goto_help.txt" (
        type "C:\Users\������\Documents\goto_help.txt" >> "C:\Users\������\Documents\combined.txt"
    )

    :: ����� ����������� ������������ ����� combined.txt
    echo.
    echo ���������� ������������ ����� combined.txt:
    type "C:\Users\������\Documents\combined.txt"
) else (
    echo ���� help.txt �� ������ � �������� bat_file.
)

endlocal