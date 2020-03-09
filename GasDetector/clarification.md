## 界面 Scenes

### 主页面 MainMenu

![](https://github.com/liuchengyuan123/project/blob/master/GasDetector/M7RCRC4%5DU7G0%6041%604Q0U%5BW4.png)

主界面里有转到另外三个界面的按钮。
主要内容就是模型在旋转。

### 设置界面 SettingMenu

![](https://github.com/liuchengyuan123/project/blob/master/GasDetector/NEMWIUV3HS2%5D6S%60SU6S5V%7BR.png)

设置界面可以设置虚拟环境中的二氧化碳和甲烷气体浓度，三个进度条中前两个确定之后，第三个也就确定了。
这个界面是供打分的人操作的（比如老师在考核前先调好浓度，之后作为给学生打分的标准）

`Back`按钮返回主界面。

### 打分界面 PracticeMenu

https://github.com/liuchengyuan123/project/blob/master/GasDetector/DVH3YD%246IV)W(ZY)(1PDREY.png

这个界面是打分的主界面，打分分为两个部分：操作和问答。
右侧关联的是三项操作环节的分数，满分一百分，完成相应操作后分数会显示。

- 调零
  这一步是模拟在目镜中调零（请看下面调零、读数界面），再次返回这个界面之后会显示调零得分，一旦调零结束，就不可以再回去更改了。
 - 测量
  主要步骤是按压橡皮气球5-10次，用来将气体吸入管中，称取气体质量增加量。
 - 读数
  这一步会再次跳转到调零、读数界面中，校准测得数字，然后读数即可。
 
 以上三步必须按顺序进行。

#### 调零、读数界面

https://github.com/liuchengyuan123/project/blob/master/GasDetector/UES$%]XG336_00M%5UK]7]I.png

拉动拉条操作

#### 问答界面
```
https://github.com/liuchengyuan123/project/blob/master/GasDetector/_M(((UV8~J3D2KAOBH(J31J.png
```

这个界面是用来问答打分的，在后面的输入框中输入答案，老师判题。     

https://github.com/liuchengyuan123/project/blob/master/GasDetector/BDO5L%25FDE~J~Y~%5BQHVWZS(E.png
播放动画，说明模型的各个零件，对应文字出现的时候，该物件略微放大。

## 脚本Scripts

`MainMenuButton.cs`
包含主页面里所有按钮的动作函数

`MainMenuRotate.cs`
主页面模型旋转

`ControlDense.cs`
在设置界面退出时触发，保存此时设置好的气体浓度各是多少。

`SettingMenuButton.cs`
设置界面的拉条控制、数字变化以及退出按钮的响应。

`PracticeMenuBack.cs`
打分界面的按钮响应

`P2Controller.cs`
调零读数界面对拉条的控制，以及将读数转化为相应的分数，还有控制操作顺序。读数的显示值可以在设置界面中由教师设置。

`ScoreDataController.cs`
打分界面的右侧分数控制，顺序控制，以及按压吸气球次数统计，转化成分数。

`ExtraController.cs`
打分系统中的问答部分控制

`PlayMenuBackButton.cs`
演示系统的退出按钮控制

### 动画 Animation
涉及Animation的部分有：
- 设置界面的弹出动画
- 调零、读数界面的弹出动画
- 演示界面的timeline（其中包含很多文字动画和零件缩放）
