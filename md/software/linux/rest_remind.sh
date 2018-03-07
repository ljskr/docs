#!/bin/bash
# This will wait one second and then steal focus and make the Zenity dialog box always-on-top (aka. 'above').

# 一秒后运行wmctrl，把zenity的窗口置顶，注意title要一致
(sleep 1 && wmctrl -F -a "take a rest :)" -b add,above) &

# 显示提示框
# zenity --info --title="take a rest :)" --width=800 --height=600 --text="休息时间到了，活动一下筋骨吧！"

# 显示时间进度条
# 提示文字要加#号
(
rest_time=120
for ((i=1;i<${rest_time};i++)); do
    echo "# 休息时间到了，活动一下筋骨吧！剩余时间 $((rest_time-i)) s"
    echo $((i*100/rest_time))
    sleep 1
done
) |
zenity --progress \
    --title="take a rest :)" \
    --width=800 \
    --height=600 \
    --percentage=0 \
    --text="休息时间到了，活动一下筋骨吧！" 
