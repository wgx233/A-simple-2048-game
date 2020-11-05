# A-simple-2048-game-by-python
用python实现了一个简单的带有UI界面的2048小游戏。

这学期选了门计算中心开的python语法课(就是类似大一新生学的那种), 期末作业要求交一个简单的python项目上去。

无奈最近期末事情非常多, 本打算直接交一份在计网上做好的socket项目, 但又觉得"杀鸡用了牛刀"不太好。

于是在github上随便找了一份2048小游戏的python实现, 拿下来以后发现编译过不了, 改了改能运行了, 但还是有warning, 仔细看看代码实现发现它的方格主体是我没用过的numpy库里的ndarray, 里面一堆骚操作

这时, 我这样一个只会python基础语法的人看不下去了, 然后把方格的主体改成二维list, 自己重写移动合并算法和类的大部分实现, 不过ui界面主体大部分还是用的原来的

运行截图:

![image](https://github.com/wgx233/A-simple-2048-game-by-python/blob/main/image/1.png)
![image](https://github.com/wgx233/A-simple-2048-game-by-python/blob/main/image/2.png)
![image](https://github.com/wgx233/A-simple-2048-game-by-python/blob/main/image/3.png)

参考项目: https://github.com/frombeijingwithlove/mini2048
