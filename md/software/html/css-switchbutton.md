# 纯 css 制作 switch button

## css 代码

```css
/* The switch - the box around the slider */
.switch-button {
  position: relative;
  display: inline-block;
  width: 48px;
  height: 24px;
}

/* Hide default HTML checkbox */
.switch-button input {
  display:none;
}

/* The slider */
.switch-button .slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #aaa;
  -webkit-transition: .4s;
  transition: .4s;
}

.switch-button .slider:before {
  position: absolute;
  content: "";
  height: 80%;
  width: 40%;
  left: 10%;
  bottom: 10%;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

.switch-button input:checked + .slider {
  background-color: #2196F3;
}

.switch-button input:focus + .slider {
  box-shadow: 0 0 1px #2196F3;
}

.switch-button input:checked + .slider:before {
  -webkit-transform: translateX(100%);
  -ms-transform: translateX(100%);
  transform: translateX(100%);
}

.switch-button input:checked[disabled] + .slider {
  background-color: #96cbf5;
  cursor: not-allowed;
}

.switch-button input[disabled] + .slider {
  background-color: #ccc;
  cursor: not-allowed;
}

/* Rounded sliders */
.switch-button .slider.round {
  border-radius: 30px;
}

.switch-button .slider.round:before {
  border-radius: 50%;
}

```

## 使用方式

使用如下 html 代码结构，可以得到一个直角的 switch button

```html
<label class="switch-button">
    <input type="checkbox">
    <span class="slider"></span>
</label>
```

如果需要圆角的 switch button ， 则在 slider 中增加 round 类

```html
<label class="switch-button">
    <input type="checkbox">
    <span class="slider round"></span>
</label>
```


