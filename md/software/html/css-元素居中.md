# css使元素居中

## relative 元素水平居中
居中的首要条件就是指定宽度。使用以下css：
``` css
margin: 0, auto;
```

## relative 元素绝对居中
待补充。

## absolute 元素绝对居中

* 方案一： 

absolutea 元素一般都会指定了宽高，使用以下css可以绝对居中：
``` css
position: absolute;
left: 0;
right: 0;
top: 0;
bottom: 0;
margin: auto;
```

* 方案二：

据说此方案在某些情况下会有bug，尽量少用。
``` css
position: absolute;
left: 50%;
top: 50%;
transform: translate(-50%, -50%);
```
