---
title: iOS开发 -- KVO的实现原理与具体应用
source_url: 'https://www.jianshu.com/p/e59bb8f59302'
source_domain: jianshu.com
source_group: platform
original_language: zh
published: 2018-08-30
archived_at: 2026-07-27
content_hash: 'sha256:9e3cab052136f1f4'
plan_ref: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 8｜架构是前七天代码的职责重排（对应 W6-06、W6-07）
plan_week: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天）
plan_day: Day 8｜架构是前七天代码的职责重排（对应 W6-06、W6-07）
container: //article
container_source: map
---

> 原文：[iOS开发 -- KVO的实现原理与具体应用](https://www.jianshu.com/p/e59bb8f59302)

本文分为2个部分：**`概念`**与**`应用`**。  
 **`概念`**部分旨在剖析 KVO 这一设计模式的实现原理；  
 **`应用`**部分通过创建的项目，以说明 KVO 技术在 iOS 开发中所带来的作用；  
 如果是作为刚接触 KVO 的初学者，可以在了解第一部分的**基本原理**后粗略看几遍**底层实现原理**，再认真阅读第二部分的应用内容“**学会**”**怎么去使用 KVO**，往后再慢慢深入了解 KVO 这一“_黑魔法_”技术的实现原理。  
 _【本次开发环境:Xcode:7.2 iOS Simulator:iphone6 By:啊左；_   
 本文 Demo下载链接(不忙的话麻烦点个星星😅)：[KVO演示Demo](https://github.com/Azuo520/KVO-Demo)】

---

> **[概念部分]**

## 一、KVO 是什么？

KVO 是 Objective-C 对**_观察者设计模式_**的一种实现。【另外一种是：通知机制（notification），详情参考：_[iOS 趣谈设计模式——通知](https://www.jianshu.com/p/ebd1953a655d)_】；  
 KVO 提供一种机制，指定一个被观察对象(例如 A 类)，当对象某个属性(例如 A 中的字符串 name)发生更改时，对象会获得通知，并作出相应处理；【且不需要给被观察的对象添加任何额外代码，就能使用 KVO 机制】

在 MVC 设计架构下的项目，KVO 机制很适合实现 mode 模型和 view 视图之间的通讯。  
 例如：代码中，在模型类A创建属性数据，在控制器中创建观察者，一旦属性数据发生改变就收到观察者收到通知，通过 KVO 再在控制器使用回调方法处理实现视图 B 的更新；(本文中的应用就是这样的例子.)

## 二、**实现原理？**

KVO 在 Apple 中的 API 文档如下：

```
     Automatic key-value observing is implemented using a technique called 
isa-swizzling… When an observer is registered for an attribute of an object the 
isa pointer of the observed object is modified, pointing to an intermediate class 
rather than at the true class …
```

KVO 的实现依赖于 Objective-C 强大的 Runtime，从以上 Apple 的文档可以看出苹果对于 KVO 机制的实现是一笔带过，而具体的细节没有过多的描述，但是我们可以通过 Runtime 的所提供的方法去探索【可参考：_[Runtime的几个小例子](https://www.jianshu.com/p/ed65518ec8db)_】，关于KVO 机制的底层实现原理。为此啊左从网上的一些关于 KVO 的资料总结了有关的内容：

##### 基本的原理：

当观察某对象 A 时，KVO 机制动态创建一个对象A当前类的子类，并为这个新的子类重写了被观察属性 keyPath 的 setter 方法。setter 方法随后负责通知观察对象属性的改变状况。

##### **深入剖析**：

Apple 使用了 isa 混写（isa-swizzling）来实现 KVO 。当观察对象A时，KVO机制动态创建一个新的名为：**NSKVONotifying_A** 的新类，该类继承自对象A的本类，且 KVO 为 NSKVONotifying_A 重写观察属性的 setter 方法，setter 方法会负责在调用原 setter 方法之前和之后，通知所有观察对象属性值的更改情况。  
 （备注： isa 混写（isa-swizzling）isa：is a kind of ； swizzling：混合，搅合；）

**①NSKVONotifying_A 类剖析：**在这个过程，被观察对象的 isa 指针从指向原来的 A 类，被 KVO 机制修改为指向**系统新创建的子类 **NSKVONotifying_A 类，来**实现当前类属性值改变的监听**；  
 所以当我们从应用层面上看来，完全没有意识到有新的类出现，这是系统“隐瞒”了对 KVO 的底层实现过程，让我们误以为还是原来的类。但是此时如果我们创建一个新的名为“NSKVONotifying_A”的类，就会发现系统运行到注册 KVO 的那段代码时程序就崩溃，因为系统在注册监听的时候**动态**创建了名为 NSKVONotifying_A 的中间类，并指向这个中间类了。  
 （**isa** 指针的作用：每个对象都有 isa 指针，指向该对象的类，它告诉 Runtime 系统这个对象的类是什么。所以对象注册为观察者时，isa 指针指向新子类，那么**这个被观察的对象就神奇地变成新子类的对象（或实例）了。**） 因而在该对象上对 setter 的调用就会调用已重写的 setter，从而激活键值通知机制。  
 —\>我猜，这也是 KVO 回调机制，为什么都俗称KVO技术为黑魔法的原因之一吧：内部神秘、外观简洁。  
 **②子类setter方法剖析：**KVO 的键值观察通知依赖于 NSObject 的两个方法:willChangeValueForKey:和 didChangevlueForKey:，在存取数值的前后分别调用 2 个方法：  
 被观察属性发生**_改变之前_**，willChangeValueForKey:被调用，通知系统该 keyPath 的属性值即将变更；当**_改变发生后_**， didChangeValueForKey: 被调用，通知系统该 keyPath 的属性值已经变更；**_之后_**， observeValueForKey:ofObject:change:context: 也会被调用。且重写观察属性的 setter 方法这种继承方式的注入是在**运行时**而不是**编译时**实现的。  
 KVO 为子类的观察者属性重写调用存取方法的工作原理在代码中相当于：

```
-(void)setName:(NSString *)newName{
    [self willChangeValueForKey:@"name"];    //KVO 在调用存取方法之前总调用
    [super setValue:newName forKey:@"name"]; //调用父类的存取方法
    [self didChangeValueForKey:@"name"];     //KVO 在调用存取方法之后总调用
}
```

## **三、特点：**

观察者观察的是属性，只有遵循 KVO 变更属性值的方式才会执行 KVO 的回调方法，例如是否执行了 setter 方法、或者是否使用了 KVC 赋值。  
 如果赋值没有通过 setter 方法或者 KVC，而是直接修改属性对应的成员变量，例如：仅调用 _name = @"newName"，这时是不会触发 KVO 机制，更加不会调用回调方法的。  
 所以使用 KVO 机制的前提是遵循 KVO 的属性设置方式来变更属性值。

---

> **[应用部分]**

## 四、步骤

- 1.注册观察者，实施监听；
- 2.在回调方法中处理属性发生的变化；
- 3.移除观察者

## 五.实现方法（苹果 API 文档中的方法）：

**A.注册观察者：**

```
//第一个参数 observer：观察者 （这里观察self.myKVO对象的属性变化）
//第二个参数 keyPath： 被观察的属性名称(这里观察 self.myKVO 中 num 属性值的改变)
//第三个参数 options： 观察属性的新值、旧值等的一些配置（枚举值，可以根据需要设置，例如这里可以使用两项）
//第四个参数 context： 上下文，可以为 KVO 的回调方法传值（例如设定为一个放置数据的字典）
[self.myKVO addObserver:self
             forKeyPath:@"num"
                options:NSKeyValueObservingOptionOld|NSKeyValueObservingOptionNew
                context:nil];
```

**B. 属性(keyPath)的值发生变化时，收到通知，调用以下方法:**

```
//keyPath:属性名称
//object:被观察的对象
//change:变化前后的值都存储在 change 字典中
//context:注册观察者时，context 传过来的值
-(void)observeValueForKeyPath:(NSString *)keyPath
                     ofObject:(id)object
                       change:(NSDictionary<NSString *,id> *)change
                      context:(void *)context
{
}
```

## 六、上代码~:

### 1.新建项目

UI界面设计如下：  
 第一个是便签，用于显示 num 数值，关联 ViewController 并命名为：**_label_**；  
 第二个是按钮，用于改变 num 的数值，关联 ViewController 并命名为：**_changeNum_**。

### 2.模型创建

【新建一个 File，选择 Cocoa Touch Class，命名为“myKVO”，记得选择Subclass of “NSObject”.】代码如下：

（myKVO.h）：

```
@interface myKVO : NSObject
@property (nonatomic,assign)int num; //属性设置为int类型的
num@end
```

（myKVO.m）：

```
#import "myKVO.h"
@implementation myKVO
@synthesize num;
@end
```

### 3.在 ViewController 中监听并响应属性改变。

（ViewController.h）：

```
#import <UIKit/UIKit.h>
@interface ViewController : UIViewController

@property (weak, nonatomic) IBOutlet UILabel *label;//便签 label
- (IBAction)changeNum:(UIButton *)sender;           //按钮事件 

@end
```

（ViewController.m）：

```
#import "ViewController.h"
#import "myKVO.h"
@interface ViewController ()
@property (nonatomic,strong)myKVO *myKVO;
@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    self.myKVO = [[myKVO alloc]init];
    
    /*1.注册对象myKVO为被观察者: option中，
     NSKeyValueObservingOptionOld 以字典的形式提供 “初始对象数据”;
     NSKeyValueObservingOptionNew 以字典的形式提供 “更新后新的数据”; */
    [self.myKVO addObserver:self
                 forKeyPath:@"num"
                    options: NSKeyValueObservingOptionOld|NSKeyValueObservingOptionNew
                    context:nil];
}

/* 2.只要object的keyPath属性发生变化，就会调用此回调方法，进行相应的处理：UI更新：*/
-(void)observeValueForKeyPath:(NSString *)keyPath
                     ofObject:(id)object
                       change:(NSDictionary<NSString *,id> *)change
                      context:(void *)context
{
    // 判断是否为self.myKVO的属性“num”:
    if([keyPath isEqualToString:@"num"] && object == self.myKVO) {
        // 响应变化处理：UI更新（label文本改变）
        self.label.text = [NSString stringWithFormat:@"当前的num值为：%@",
                           [change valueForKey:@"new"]];
        
        //change的使用：上文注册时，枚举为2个，因此可以提取change字典中的新、旧值的这两个方法
        NSLog(@"\\noldnum:%@ newnum:%@",
              [change valueForKey:@"old"],
              [change valueForKey:@"new"]);
    }
}

/*KVO以及通知的注销，一般是在-(void)dealloc中编写。
至于很多小伙伴问为什么要在didReceiveMemoryWarning？因为这个例子是在书本上看到的，所以试着使用它的例子。
但小编还是推荐把注销行为放在-(void)dealloc中。(严肃脸😳)
*/
- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    /* 3.移除KVO */
    [self.myKVO removeObserver:self
                    forKeyPath:@"num"
                       context:nil];
}
//按钮事件
- (IBAction)changeNum:(UIButton *)sender {
    //按一次，使num的值+1
    self.myKVO.num = self.myKVO.num + 1;
}
@end
```

**调试**：便签label初始化没有数值，当每次点击按钮后，label记录的num随之增加，表明按钮使属性num增加的同时，KVO机制发送通知，并调用observeValueForKeyPath:方法使UI更新。（本文Demo下载链接：[KVO演示Demo](https://github.com/Azuo520/KVO-Demo)）

## 七、拓展--\>

#### 1.KVC 与 KVO 的不同？

KVC(键值编码)，即 Key-Value Coding，一个非正式的 Protocol，使用字符串(键)访问一个对象实例变量的机制。而不是通过调用 Setter、Getter 方法等显式的存取方式去访问。  
 KVO(键值监听)，即 Key-Value Observing，它提供一种机制,当指定的对象的属性被修改后,对象就会接受到通知，前提是执行了 setter 方法、或者使用了 KVC 赋值。

#### 2.和 notification(通知)的区别？

notification 比 KVO 多了发送通知的一步。  
 两者都是一对多，但是对象之间直接的交互，notification 明显得多，需要notificationCenter 来做为中间交互。而 KVO 如我们介绍的，设置观察者-\>处理属性变化，至于中间通知这一环，则隐秘多了，只留一句“交由系统通知”，具体的可参照以上实现过程的剖析。

notification 的优点是监听不局限于属性的变化，还可以对多种多样的状态变化进行监听，监听范围广，例如键盘、前后台等系统通知的使用也更显灵活方便。  
 （参照[通知机制](https://www.jianshu.com/p/ebd1953a655d)第五节系统通知名称内容）

#### **3.与 delegate 的不同？**

和 delegate 一样，KVO 和 NSNotification 的作用都是类与类之间的通信。但是与 delegate 不同的是：  
 这两个都是负责发送接收通知，剩下的事情由系统处理，所以不用返回值；而 delegate 则需要通信的对象通过变量(代理)联系；  
 delegate 一般是一对一，而这两个可以一对多。

#### **4.涉及技术：**

KVC/KVO 实现的根本是 Objective-C 的动态性和 Runtime ，以及访问器方法的实现；

> ### **总结:**

对比其他的回调方式，KVO 机制的运用的实现，更多的由系统支持，相比 notification、delegate 等更简洁些，并且能够提供观察属性的最新值以及原始值；但是相应的在创建子类、重写方法等等方面的内存消耗是很巨大的。所以对于两个类之间的通信，我们可以根据实际开发的环境采用不同的方法，使得开发的项目更加简洁实用。  
   
  
 另外需要注意的是，由于这种继承方式的注入是在运行时而不是编译时实现的，如果给定的实例没有观察者，那么 KVO 不会有任何开销，因为此时根本就没有 KVO 代码存在。但是即使没有观察者，委托和 NSNotification 还是得工作，这也是KVO此处零开销观察的优势。

---

（转载请标明原文出处，谢谢支持 ~ ^- ~）  
  by：啊左~
