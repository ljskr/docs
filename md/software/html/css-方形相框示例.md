# css 制作方形相框，并让图片居中

## css

container 方案一：
```css
.square-container {
    position: relative;
    width: 100%;
    padding-bottom: 100%;
    overflow: hidden;
    background-color: #e9eef1;
    border: 1px solid #aaa;
    border-radius: 4px;
    box-shadow: 3px 3px 3px #ccc;
}
```

container 方案二： （更优，可以解决 min-height 无效的问题）
```css
.square-container {
    position: relative;
    width: 100%;
    overflow: hidden;
    background-color: #e9eef1;
    border: 1px solid #aaa;
    border-radius: 4px;
    box-shadow: 3px 3px 3px #ccc;
}
.square-container:after {
    content: '';
    display: block;
    margin-top: 100%;
}
```

原理： padding 和 margin 的百分比是以容器的宽度为基数的，因此 padding-bottom 和 margin-top 的 100% 大小和宽度一致。

item:
```css
.square-container-item {
    position: absolute;
    max-width: 100%;
    max-height: 100%;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    margin: auto;
}
```

## html:

```
<div class="square-container">
    <img class="square-container-item" src="img.jpg">
</div>
```

