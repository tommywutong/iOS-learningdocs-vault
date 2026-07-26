---
title: 0代码ViewController · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2014/07/17/ios_0code_vc/'
original_language: zh
published: 2014-07-17
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b13f56f8ad86cb7c'
translated: n/a
---

> 原文：[0代码ViewController · sunnyxx的技术博客](http://blog.sunnyxx.com/2014/07/17/ios_0code_vc/)　·　sunnyxx (孙源)

# 0代码ViewController

2014年7月17日

# 我是前言

看了`objc.io`中的[《Behaviors in iOS Apps》](http://www.objc.io/issue-13/behaviors.html)（objccn上也有[中文翻译版](http://objccn.io/issue-13-3/)）后，终于**如梦初醒**了IB中的这个低调的`Object`存在的意义：

![](http://ww1.sinaimg.cn/large/51530583gw1eifvg6elgrj20jk060js7.jpg)

再加上同样被轻视的Runtime Attributes:

![](http://ww4.sinaimg.cn/large/51530583gw1eifvtsgrgpj20dq05w0sv.jpg)

有了这些，IB才算完整和强大。  
最近看了一些文章，加上工程中也遇到的坑，矛头都指向了**MVC(Massive View Controller)**：臃肿的ViewController所引发的不爽，`objc.io`也是以一个[《Lighter View Controllers》](http://www.objc.io/issue-1/)开篇。从把DataSource和Delegte从VC中分离，到把Model逻辑整个分离的`MVVM`，VC一步步瘦身，再到这篇Behavior模式巧妙的组件式的分离了功能。但有没有想过，为啥往一个页面写点啥东西就一定要子类化一个VC呢，使用上面两个IB的功能，我们可以激进地实验一次`0代码ViewController`

---

# Top Level Objects

首先必须说明Top Level Objects这个概念，根据apple文档：

> The top-level objects are the subset of these objects that do not have a parent object. The top-level objects typically include only the windows, menubars, and custom controller objects that you add to the nib file. (Objects such as File’s Owner, First Responder, and Application are placeholder objects and not considered top-level objects.)

所以，IB里面的`Object`控件其实就是向Controller中添加`Custom Top Level Object`，在storyboard中被摆在下面的位置：

![](http://ww4.sinaimg.cn/large/51530583gw1eifwvsnandj20es08kaaw.jpg)

事实上任何Object都可以添加，这里出现了一个LoginViewModel对象、一个菊花、一个Tap手势。

### Nib对象的创建顺序

1. 自定义的Top Level Objects收到`- init`消息
2. ViewController收到`- initWithCoder:`消息
3. 自定义的Top Level Objects 收到`- awakeFromNib`消息
4. ViewController收到`- awakeFromNib`消息
5. 子View分别收到`- initWithCoder:`消息
6. 子View分别收到`- awakeFromNib`消息

可见自定义的Object的创建时间是早于VC的，至于为什么`- awakeFromNib`收到的晚于VC的创建，是因为**创建出来的Object需要被VC强引用**

### VC对自定义Objects的强引用

创建出来的Object必须保证不被释放，这个强引用由VC实现，虽说没有显示的API，但从`UIViewController.h`中可以看到马脚：

```objc
@interface UIViewController : UIResponder {
    @package
    // ...
    NSDictionary  *_externalObjectsTableForViewLoading;
    NSArray       *_topLevelObjectsToKeepAliveFromStoryboard;
    // ...
}
```

通过KVC可以很轻松的取出来：

```objc
NSArray *objs = [vc valueForKey:@"_topLevelObjectsToKeepAliveFromStoryboard"];
NSDictionary *dict = [vc valueForKey:@"_externalObjectsTableForViewLoading"];
```

这些objects就是被这个数组强引用的，感兴趣的可以打印下看看结果。  
_注：只在storyboard下生效，在xib下，被创建的Object因为没有被强引用而随后被释放。_

---

# 构建0代码VC的简单登录场景

**storyboard中拉出个VC，随便摆摆：**  
![](http://ww3.sinaimg.cn/large/51530583gw1eig0usoroej209k076t8p.jpg)

**创建一个ViewModel类（也就是Behavior类），里面写需要的IBOutlet和IBAction**

```objc
@interface XXLoginViewModel : NSObject
@property (nonatomic, weak) IBOutlet UIViewController *ownerViewController;
@property (nonatomic, weak) IBOutlet UITextField *usernameTextField;
@property (nonatomic, weak) IBOutlet UITextField *passwordTextField;
@property (nonatomic, weak) IBOutlet UIActivityIndicatorView *spinner;
- (IBAction)loginAction:(id)sender;
@end
```

**storyboard中拖出来一个Object到左边，设置类为这个`XXLoginViewModel`, 将所有IBOutlet和IBAction连接好**

![](http://ww2.sinaimg.cn/large/51530583gw1eig0zjf4gpj20wi0ecdid.jpg)

**这样，就可以在自定义Object中为所欲为了，需要什么就从storyboard里面Outlet出来就好了，比如点击之后的跳转：**

```objc
- (IBAction)loginAction:(id)sender {
    [self.ownerViewController performSegueWithIdentifier:@"LoginSegue" sender:nil];
}
```

具体的代码不show了，Demo的效果如下：

![](http://ww1.sinaimg.cn/large/51530583gw1eig8tuzciig208r0d5n18.gif)

当然，TableView的delegate和data source也都是可以托管到自定义Object中，同时，Object之间也可以有Outlet关系哦，剩下的就纯靠想象力了。

**这个简单的demo从[-\>这里下载\<-](https://github.com/sunnyxx/XXZeroCodeViewControllerDemo)**

---

# What’s more

- 首先，这次实验并非表明我们应该写0代码的VC，UIViewController本身被设计作为一个`模板类`，继承+重载无可非议（但像UITableView这种被设计成`配置类`的类，我们更应该去配置它，而非继承它，更别说NSArray，NSString这种类簇的工具类了）
- 组合模式以十分灵活的方式划分功能，Demo中只用了一个ViewModel，其实完全可以组合一个Animation类实现动画，组合一个HTTP类来发请求？，组合一个处理旋转屏幕的类等等，而且**完成这些子功能的代码集中在一个类中，而不是分散在VC的各个角落，两个功能的小模块间可以说没有耦合**
- VC没有代码，但storyboard已经干了VC该干的事，如创建和布局子View、设置Autolayout、设置action，定义跳转等。我想，Apple祭出storyboard的目的就在于将纯视图和纯代码逻辑分离，VC本该Control它的View，而不是自己就是那个View

---

# References

[https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/LoadingResources/CocoaNibs/CocoaNibs.html](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/LoadingResources/CocoaNibs/CocoaNibs.html)  
[http://www.objc.io/issue-13/behaviors.html](http://www.objc.io/issue-13/behaviors.html)
