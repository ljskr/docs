# cron 用法

## 一、 cron 简介

crond 是 linux 下用来周期性的执行某种任务或等待处理某些事件的一个守护进程，与 windows 下的计划任务类似。

linux 默认会安装此服务工具，并自动启动 crond 进程。

Linux 下的任务调度分为两类，系统任务调度和用户任务调度。

### 1. 系统任务调度

系统周期性所要执行的工作，比如写缓存数据到硬盘、日志清理等。在 /etc 目录下有一个 crontab 文件，这个就是系统任务调度的配置文件。（尽量不要动该文件）

### 2. 用户任务调度

所有用户定义的 crontab 文件都被保存在 /var/spool/cron  目录中。其文件名与用户名一致。（管理员查看有哪些用户设置了 cron 任务，可以到该目录下查看）

## 二、 crond 服务

```
service crond start //启动服务

service crond stop //关闭服务

service crond restart //重启服务

service crond reload //重新载入配置

service crond status //查看服务状态
```

## 三、 crontab 命令

用户需要通过 crontab 命令来操作定时任务。

命令格式：

```
crontab [-u user] file

crontab [-u user] [ -e | -l | -r ]
```

- **-u user**： 以某个用户来运行任务。此参数一般由 root 用户来使用。

- **file**： file 是命令文件的名字,表示将 file 做为 crontab 的任务列表文件并载入 crontab 。如果在命令行中没有指定这个文件， crontab 命令将接受标准输入（键盘）上键入的命令，并将它们载入 crontab 。（键盘上的命令需要结束时按 ctrl+d ）

- **-e**： 编辑某个用户的 crontab 文件内容。如果不指定用户，则表示编辑当前用户的 crontab 文件。

- **-l**： 显示某个用户的crontab文件内容，如果不指定用户，则表示显示当前用户的crontab文件内容。

- **-r**： 从 /var/spool/cron 目录中删除某个用户的 crontab 文件，如果不指定用户，则默认删除当前用户的 crontab 文件。

- **-i**： 在删除用户的crontab文件时给确认提示。

每次编辑完某个用户的 cron 设置后， cron 自动在 /var/spool/cron 下生成一个与此用户同名的文件，此用户的 cron 信息都记录在这个文件中，这个文件是不可以直接编辑的，只可以用 crontab -e  来编辑。 cron 启动后每过一份钟读一次这个文件，检查是否要执行里面的命令。因此此文件修改后不需要重新启动 cron 服务。

## 四、 crontab 文件含义

用户所建立的 crontab 文件中，每一行都代表一项任务，每行的每个字段代表一项设置，它的格式共分为六个字段，格式如下：

```
minute   hour   day   month   week   command
```

其中：

- **minute**： 表示分钟，可以是从0到59之间的任何整数。

- **hour**：表示小时，可以是从0到23之间的任何整数。

- **day**：表示日期，可以是从1到31之间的任何整数。

- **month**：表示月份，可以是从1到12之间的任何整数。

- **week**：表示星期几，可以是从0到7之间的任何整数，这里的0或7代表星期日。

- **command**：要执行的命令，可以是系统命令，也可以是自己编写的脚本文件

时间部分还可以使用以下特殊字符：

- 星号(*)： 代表所有可能的值。

- 逗号(,)： 可以用逗号隔开的值指定一个列表范围。如"2,4,6,7"

- 中杠(-)： 可以用整数之间的中杠表示一个整数范围。如"2-5"表示"2,3,4,5"

- 正斜线(/)： 可以用正斜线指定时间的间隔频率。如分钟设置为"*/5"表示每隔5分钟执行。

## 五、 实例

- 每1分钟执行一次
```
* * * * * command
```

- 每小时的第3和第15分钟执行
```
3,15 * * * * command
```

- 在上午8点到11点的第3和第15分钟执行
```
3,15 8-11 * * * command
```

- 每隔两天的上午8点到11点的第3和第15分钟执行
```
3,15 8-11 */2 * * command
```

- 每个星期一的上午8点到11点的第3和第15分钟执行
```
3,15 8-11 * * 1 command
```

- 每晚的21:30重启smb 
```
30 21 * * * /etc/init.d/smb restart
```

- 每月1、10、22日的4:45重启smb 
```
45 4 1,10,22 * * /etc/init.d/smb restart
```

- 每周六、周日的1:10重启smb
```
10 1 * * 6,0 /etc/init.d/smb restart
```

- 每天18:00至23:00之间每隔30分钟重启smb
```
0,30 18-23 * * * /etc/init.d/smb restart
```

- 每一小时重启smb 
```
* */1 * * * /etc/init.d/smb restart
```

- 晚上11点到早上7点之间，每隔一小时重启smb 
```
* 23-7/1 * * * /etc/init.d/smb restart
```

- 每月的4号与每周一到周三的11点重启smb 
```
0 11 4 * mon-wed /etc/init.d/smb restart
```

- 一月一号的4点重启smb
```
0 4 1 jan * /etc/init.d/smb restart
```