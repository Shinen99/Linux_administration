1 Как отобразить 4 последних выполненных команды?  
history 4  
2 Перевести задание в фоновый режим в bash можно командой  
bg \<pid\>  
3 Какая комбинация клавиш переключит вас на 4-ю виртуальную консоль?  
ctrl+alt+f4  
4 Какая переменная среды содержит путь к домашнему каталогу?  
HOME  
5 Установить в bash переменную MYVAR в качестве системной можно командой?  
export MYVAR  
6 Какие комбинации клавиш позволят выделить несколько файлов в Midnight Commander?  
ctrl+t  

7 Что выведет на экран этот сценарий?  
#!/bin/bash  
VAR=\`echo 'test'\`  
VAR2=\`echo '$VAR'\`  
echo $VAR2  
 
  Переменную $VAR

8 Что выведет на экран это сценарий?  
#!/bin/bash  
cd /etc  
VAR="$PWD"  
if [ -n "$VAR" ]; then  
 echo "$VAR"  
else  
 echo '$VAR'  
fi   
 
  Выведет /etc

9 Что выведет на экран этот сценарий?  
#!/bin/bash  
A=1  
B=2  
if [ $A -eq $B  ]; then  
 echo '$A'  
else  
 echo "$B"  
fi   

  2  
  

Практическое задание. Работа с tmux  
Создаем сессию в tmux. Разделяем экран с помощью ctrl+b + " горизотально и ctrl+b + % - вертикально. Для управления мышью добавляем в tmux.conf "set -g mouse on". Для выхода ctrl+b + d  
![tmux](https://github.com/Shinen99/Linux_administration/blob/lab5/lab5/tmux.png)
