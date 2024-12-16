@echo off
chcp 1251
setlocal

:: Проверка наличия файла help.txt
if exist "C:\Users\Пользо\Documents\help.txt" (
    echo Файл help.txt найден.
    echo.
    type "C:\Users\Пользо\Documents\help.txt"  :: Выводим содержимое help.txt
    echo.

    :: Проверка наличия файла if_help.txt
    if exist "C:\Users\Пользо\Documents\if_help.txt" (
        echo Файл if_help.txt найден.
        type "C:\Users\Пользо\Documents\if_help.txt"  :: Выводим содержимое if_help.txt
        echo.
    ) else (
        echo Файл if_help.txt не найден.
    )

    :: Проверка наличия файла goto_help.txt
    if exist "C:\Users\Пользо\Documents\goto_help.txt" (
        echo Файл goto_help.txt найден.
        type "C:\Users\Пользо\Documents\goto_help.txt"  :: Выводим содержимое goto_help.txt
        echo.
    ) else (
        echo Файл goto_help.txt не найден.
    )

    :: Объединение содержимого файлов if_help.txt и goto_help.txt в новый файл combined.txt
    if exist "C:\Users\Пользо\Documents\if_help.txt" (
        type "C:\Users\Пользо\Documents\if_help.txt" >> "C:\Users\Пользо\Documents\combined.txt"
    )
    if exist "C:\Users\Пользо\Documents\goto_help.txt" (
        type "C:\Users\Пользо\Documents\goto_help.txt" >> "C:\Users\Пользо\Documents\combined.txt"
    )

    :: Вывод содержимого объединённого файла combined.txt
    echo.
    echo Содержимое объединённого файла combined.txt:
    type "C:\Users\Пользо\Documents\combined.txt"
) else (
    echo Файл help.txt не найден в каталоге bat_file.
)

endlocal