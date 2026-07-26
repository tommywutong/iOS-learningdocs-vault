---
title: 一个丝滑的全屏滑动返回手势 · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2015/06/07/fullscreen-pop-gesture/'
original_language: zh
published: 2015-06-07
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:7378567b3fb9fc85'
translated: n/a
---

> 原文：[一个丝滑的全屏滑动返回手势 · sunnyxx的技术博客](http://blog.sunnyxx.com/2015/06/07/fullscreen-pop-gesture/)　·　sunnyxx (孙源)

# 一个丝滑的全屏滑动返回手势

2015年6月7日

# [#全屏返回手势](#全屏返回手势)全屏返回手势

自 iOS7 之后，Apple 增加了**屏幕边缘右划返回**交互的支持，再配合上 UINavigationController 的交互式动画，pop 到上一级页面的操作变的非常顺畅和丝滑，从此，我很少再使用点击左上角导航栏上的返回按钮的方式返回了，因为这对单手操作十分不友好；如果一个 App 居然胆敢不支持滑动返回，那离被卸载就不远了。

说到**全屏返回手势**，首先我感觉这件事本身可能就有问题，毕竟有点反苹果官方的交互，让用户从任意的地方都能够滑动返回这个交互在国内的 App 中非常普遍，比如我手机中的手Q、微博、网易新闻、大众点评等，当然还有百度知道- -。这里得对微信的产品经理们得点个赞，从整个 App 来看，不论是交互还是 UI 结构和样式都非常的 iOS，没有什么特别奇葩的页面和交互，以至于使用 UIKit 原生的框架可以非常简单的搭建起来，这也符合我个人对 App 的一个愿景：**一个优秀的 App 不论从用户角度看还是从代码角度看都应该是简单且优雅的**，呼吁各家产品经理可以多借鉴下像微信这样很本色的 App 设计。（以后可以分享下如何使用 Storyboard 在一小时内快速搭建起微信 UI）

# [#FDFullscreenPopGesture](#FDFullscreenPopGesture)FDFullscreenPopGesture

工作毕竟是工作，于是乎所以就被迫实现了套 pan 手势处理加截图和视差，虽然在运动曲线上、bar 截图处理上下了不少功夫，但距离系统的丝滑效果还是差距挺远。随时间推移，终于能够最低支持 iOS7 后，我们把这个问题再次拿出来讨论和研究，直到在微博上看到了 **J_雨**同学的[这篇文章](http://www.jianshu.com/p/d39f7d22db6c) 后才找到了这个迄今为止最简单的解决方案。于是乎在他的授权下，我们在 forkingdog 上把这个返回手势开源，[github地址](https://github.com/forkingdog/FDFullscreenPopGesture)，并果断应用到了百度知道 App 内，这是 Demo 效果：

![](https://raw.githubusercontent.com/forkingdog/FDFullscreenPopGesture/master/Snapshots/snapshot0.gif)

利用了系统自己的边缘返回手势处理函数后，一切动画和曲线都和原生效果一毛一样了。  
于是乎发布了 `FDFullscreenPopGesture` 1.0 版本，而且提供了一个 AOP 形式的 API，把它添加到工程里面，什么代码都不用写，所有 UINavigationController 就自带这个全屏返回效果了。

# [#丝滑的处理导航栏的显示和隐藏](#丝滑的处理导航栏的显示和隐藏)丝滑的处理导航栏的显示和隐藏

接下来我们发现利用系统的 UINavigationBar 时，返回手势中若碰到前一个页面有 bar，后一个页面没 bar，或者反过来时，动画就非常难看，举两个反例：

手Q iOS：

![](http://ww2.sinaimg.cn/large/51530583jw1esvbwqgawtg208w0fvu0x.gif)

它的个人中心页面上面的 bar 是隐藏状态，然后做了个和其他页面很像的假 bar，但返回手势一开始就露馅了，为了弥补，还做了下后面真 bar 的 alpha 值动画，两个返回按钮还是重叠在了一起。

新浪微博 iOS：

![](http://ww4.sinaimg.cn/large/51530583jw1esvbwfphj8g208w0fv4qp.gif)

和手Q一样的实现方式，只不过没做 alpha 动画，所以就非常明显了。

为啥会这样呢？这可能就是 UINavigationController 在导航栏控制 API 上设计的缺陷了。 一个 UINavigationController 管理了串行的 N 个 UIViewController 栈式的 push 和 pop，而 UINavigationBar 由 UINavigationController 管理，这就导致了 UIViewController 无法控制自己上面的 bar 单独的隐藏或显示。 这非常像 UIApplication 全局的 status bar，牵一发还得动全身，不过 Apple 在 iOS7 之后为 vc 控制自己的 status bar 提供了下面几个方法：

```objc
- (UIStatusBarStyle)preferredStatusBarStyle NS_AVAILABLE_IOS(7_0);
- (BOOL)prefersStatusBarHidden NS_AVAILABLE_IOS(7_0);
- (UIStatusBarAnimation)preferredStatusBarUpdateAnimation NS_AVAILABLE_IOS(7_0);
```

终于让这个**全局变量**变成了**局部变量**，虽然写起来费劲了些。  
但是对 UINavigationBar 的控制，依然是全局的，可能 Apple 觉得 App 不应该有这种奇怪的页面结构？

解决这个问题的方法也不难，在滑动返回的后要出现的那个 view controller 中写下面的代码：

```objc
- (void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];
    [self.navigationController setNavigationBarHidden:YES animated:animated];
}
```

系统就会把有 bar 和 无 bar 的 transition 动画衔接起来。但是如上面所说，这是个全局变量，还得在所有由这个没有 bar 的特殊页面能 push 和 pop 的页面都进行反向的处理，代码非常的乱乎。于是乎，我们试着解决了这个问题，先看效果：

![](http://ww2.sinaimg.cn/large/51530583jw1esvbwmjck8g208w0ft7wj.gif)

我特意挑了个从真 bar 到假 bar，再从假 bar 到 真 bar 的页面，还算蛮丝滑的，transition 动画全是系统自己搞定的。  
就事把 `FDFullscreenPopGesture` 更新到了 1.1 版本，贯彻我们一向的精简 API，你只需要在 bar 要隐藏的 view controller 中写一句话：

```objc
- (void)viewDidLoad
    [super viewDidLoad];
    self.navigationController.fd_prefersNavigationBarHidden = YES;
}
```

或者喜欢重载的写法也行：

```objc
- (BOOL)fd_prefersNavigationBarHidden {
    return YES;
}
```

刻意的模仿了下系统的命名风格，就这一句话，剩下的就都不用操心了。

# [#关于私有API](#关于私有API)关于私有API

大家会质疑说，这用到了 UIKit 的私有属性和私有 API，要是系统升级变了咋办？要是审核被拒了咋办？  
首先，iOS 系统的 SDK 为了向下兼容，一般只会增加方法或者修改方法实现，不太可能直接删除一个共有方法，而私有方法的行为确实可能有变化，但系统 release 频率毕竟很低，每当新版本发布时 check 下原来的功能是否能 work 就好了，大可不必担心这么远，SDK 是死的人是活的。  
另一个就是审核问题，FDFullscreenPopGesture 的实现中有主要有两处触碰到了私有 API：

```objc
// 1. 私有变量标志transition动画是否正在进行
[self.navigationController valueForKey:@"_isTransitioning"];
// 2. 一个内部的selector
NSSelectorFromString(@"handleNavigationTransition:");
```

不论是 kvc 还是 selector 反射，都是利用 objc runtime 完成的，而到了这一层，真的就没啥公有私有可言了。设想你就是开发 Apple 私有 API 检查工具的工程师，给你一个 ipa 的包，你会如何检查出其中有没有私有 API 呢？

首先，这个检查一定是个静态检查吧，不可能是运行时检查，因为代码逻辑那么复杂，把程序跑起来看所有 objc_msgSend 中包不包括私有调用这件事太不现实了。  
对 ipa 文件做静态检查的话肯定是去分析 Mach-O 可执行文件，因为这时很多源代码级别的信息已经丢失，经分析可以采取下面几种手段：

- 是否 link 了私有 framework 或者公开 framework 中的私有符号，这可以防止开发者把私有 header 都 dump 出来供程序直接调用。
- 加上

  的方式直接调用私有 API。
- 扫描所有符号，查看是否有继承自私有类，重载私有方法，方法名是否有重合。
- ，看字符串常量段是否出现和私有 API 对应的。

我觉得前三条被 catch 住的可能性最高，也最容易被检查出来。再来看我们用到用字符串的方法 kvc 和 反射 selector，应该属于最后一条，这时候就很难抉择了，拿 `handleNavigationTransition:` 来说，看上去人畜无害啊，我自己类里面的方法也完全可能命名出这个来，所以单单凭借字符串命中私有 API 判定，苹果很容易误伤一大票开发者。  
综上，我觉得使用字符串的方式使用私有 API 是相对安全的，我们的 App 马上要提交审核，如果过了几天你还能读到这段文字，说明我的猜想是木有错的，大家可以放心使用。

# [#0-代码的-Demo](#0-代码的-Demo)0 代码的 Demo

还有一个有意思的事，我们在 github 上的 [demo工程](https://github.com/forkingdog/FDFullscreenPopGesture) 木有写一行代码，就实现了下面的效果：

![](https://raw.githubusercontent.com/forkingdog/FDFullscreenPopGesture/master/Snapshots/snapshot1.gif)

工程长这个样子，view controller 类也没写，为了体现 `FDFullscreenPopGesture` 的 AOP 性质：

![](http://ww3.sinaimg.cn/large/51530583jw1esveprvnvfj20ju0d2tbm.jpg)

页面由 Storyboard 构建：

![](http://ww3.sinaimg.cn/large/51530583jw1esvepscqomj212m10eq5a.jpg)

而控制页面隐藏 bar 的属性也能用 Runtime Attributes 模拟调用：

![](http://ww2.sinaimg.cn/large/51530583jw1esvetev633j20ig05ydgl.jpg)

这样就完成了一个非常干净的 Demo

# [#加入到你的工程中](#加入到你的工程中)加入到你的工程中

首先要求最低支持 iOS7，我想在 WWDC 2015 结束，iOS9 发布后，主流的 App 就都会 iOS7 起跳了。  
依然是熟悉的 cocoapods 安装：

```
pod 'FDFullscreenPopGesture', '~> 1.1'
```

要是没有搜到就 `pod setup` 下。

# [#广告时间](#广告时间)广告时间

我这边正在招聘 iOS，坐标北京，希望找到一个代码规范的、爱用 IB 的、懒得写重复代码、不爱加班的同学，相信这里有很大空间供你学习和提升，还可以参与到 forkingdog 开源小组中做点屌屌的东西，欢迎私聊或把简历丢到 sunyuan01@baidu.com

![](https://cloud.githubusercontent.com/assets/219689/7244961/4209de32-e816-11e4-87bc-b161c442d348.png)
