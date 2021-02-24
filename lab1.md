1. Основные принципы Unix-way:
  ---
  - Все есть - файл
  - Написание программы, которое делает что-то одно
  - Есть множество путей решения
  
2. Линус Торвальдс является разработчиком чего
  ---
  Ядра ОС Linux

3. Как посмотреть название ядра системы из консоли?
  ---
  uname -ar
  
4. Промежутки измерения загрузки системы для команды uptime следующие
  ---
  1, 5 и 15 минут
  
5. Какой командой узнать сколько занято на HDD
  ---
  df -H
  
6. Какие разделы содержит вывод команды vmstat:
  ---
  procs, memory, swap, io, system, cpu
  
7. Описать работу своего Linux дистрибутива: какое ядро, архитектура, размеры hdd, объеме ОЗУ, загрузке процессора и т.д:
  ---
  
  Linux shinen-Aspire-VN7-791G 5.8.0-25-generic #26-Ubuntu SMP Thu Oct 15 10:30:38 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
  
  ---
  
  Файл.система |  Размер | Использовано | Дост | Использовано% | Cмонтировано в
  tmpfs        |    1,7G |        2,2M | 1,7G  |          1% | /run
  /dev/sdb3    |    210G |         13G | 187G  |          7% | /
  tmpfs        |    8,4G |         39M | 8,4G  |          1% | /dev/shm
  tmpfs        |    5,3M |        4,1k | 5,3M  |          1% | /run/lock
  tmpfs        |    4,2M |           0 | 4,2M  |          0% | /sys/fs/cgroup
  /dev/sda1    |    101M |         35M |  67M  |         35% | /boot/efi
  tmpfs        |    1,7G |        132k | 1,7G  |          1% | /run/user/1000
  /dev/sdc1    |    121G |         44G |  78G  |         37% | /media/shinen/flash
 
  ---
 
  procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
  r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
  0  0      0 10561260 117756 3813604    0    0   274   250  269  870  4  2 84 11  0
  
  ---
  
   13:05:35 up 18 min,  1 user,  load average: 0,57, 0,83, 1,22

  ![screenshot](https://github.com/Shinen99/Linux_administration/blob/lab1/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202021-02-24%2013-11-07.png)
