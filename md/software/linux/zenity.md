# zentiy

可以帮助你使用脚本创建常用的gtk+对话框。

1、使用日历控件：

szDate=$(zenity --calendar --text "Pick a day" --title "Medical Leave" --day 13 --month 5 
--year 2010); echo $szDate

2、创建一个Entry对话框：

szAnswer=$(zenity --entry --text "where are you?" --entry-text "at home"); echo $szAnswer

3、创建一个错误对话框：

zenity --error --text "Installation failed! "

4、创建一个Info对话框：

zenity --info --text "Join us at irc.freenode.net #lbe."

5、创建一个文件选择对话框：

szSavePath=$(zenity --file-selection --save --confirm-overwrite);echo $szSavePath

6、创建一个通知对话框：

zenity  --notification  --window-icon=update.png  --text "Please update your system."

7、创建一个进度对话框：

gksudo lsof | tee >(zenity --progress --pulsate) >lsof.txt

8、创建一个question对话框：

zenity --question --text "Are you sure you want to shutdown?"; echo $?

9、创建一个警告对话框：

zenity --warning --text "This will kill, are you sure?";echo $?

10、创建一个滑动scale对话框：

ans=$(zenity --scale --text "pick a number" --min-value=2 --max-value=100 --value=2 
--step 2);echo $ans

11、创建一个文本信息对话框：

gksudo lsof | zenity --text-info --width 530

12、创建一个列表对话框：
radiolist:

ans=$(zenity  --list  --text "Is linux.byexamples.com helpful?" --radiolist  --column "Pick" 
--column "Opinion" TRUE Amazing FALSE Average FALSE "Difficult to follow" FALSE "Not helpful"); 
echo $ans

checklist:

ans=$(zenity  --list  --text "How linux.byexamples can be improved?" --checklist  
--column "Pick" --column "options" TRUE "More pictures" TRUE "More complete post" FALSE "
Includes Installation guidelines" FALSE "Create a forum for question queries" 
--separator=":"); echo $ans

