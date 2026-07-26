---
title: iOS开发那些事-iOS常用设计模式–委托模式
source_url: 'https://www.cnblogs.com/iOS-Blog/archive/2013/02/21/2920926.html'
source_domain: cnblogs.com
source_group: platform
original_language: zh
published: 2013-02-21
archived_at: 2026-07-27
content_hash: 'sha256:6068e6f6c9bea971'
plan_ref: 第三周：Runtime 行为与 Cocoa 对象通信 / Day 6｜最后才比较对象通信模式（对应 W3-01、W6-07）
plan_week: 第三周：Runtime 行为与 Cocoa 对象通信
plan_day: Day 6｜最后才比较对象通信模式（对应 W3-01、W6-07）
container: '//div[@id=''cnblogs_post_body'']'
container_source: map
---

> 原文：[iOS开发那些事-iOS常用设计模式–委托模式](https://www.cnblogs.com/iOS-Blog/archive/2013/02/21/2920926.html)

对于iOS开发,举例Cocoa框架下的几个设计模式为大家分析。当然，Cocoa框架下关于设计模式的内容远远不止这些，我们选择了常用的几种：单例模式、委托模式、观察者模式、MVC模式。

委托模式

委托模式从GoF 设计装饰（Decorator）、适配器（Adapter）和模板方法（Template Method）等模式演变而来。几乎每一个应用都会或多或少地使用到委托模式。不只是CocoaTouch框架，在Cocoa框架中委托模式也得到了广泛的应用。

问题提出

[![1](http://iosbook1.com/wp-content/uploads/2013/02/11.png)](http://iosbook1.com/?attachment_id=139)

对于应用生命周期的非运行状态——应用启动场景，我们把从点击图标到第一个画面启动的过程细化了一下

假设上图这一系列的处理，都是在一个上帝类UIApplication完成的。之所以叫“上帝类（God Class）”，是因为它“无所不能”、“包含所有”。 在面向对象的软件设计中“上帝类”不是很友好， 需要重构。在编程过程中要尽量避免上帝类的使用，因为上帝类是高耦合的，职责不清，所以难以维护。我们需要“去除上帝类”，把看似功能很强且很难维护的 类，按照职责把自己的属性或方法分派到各自的类中或分解成功能明确的类，从而去掉“上帝类”。

幸运的是苹果没有把UIApplication类设计成“上帝类”，苹果处理分割到两个不同的角色类中，其中一个扮演框架类角色，框架类具有通用、 可重复使用、与具体应用无关等特点。另一个扮演应用相关类的角色，应用相关类与具体应用有关，由于要受到框架类的控制，常常被设计成为“协议”，在 Java中称之为“接口”。开发人员需要在具体的应用中实现这个“协议”。

将application:didFinishLaunchingWithOptions:和 applicationDidBecomeActive:完成功能提取出来，定义在UIApplicationDelegate协议中，这样 UIApplication类就变成了框架类。

[![2](http://iosbook1.com/wp-content/uploads/2013/02/21.png)](http://iosbook1.com/?attachment_id=140)

在具体使用时候需要实现UIApplicationDelegate协议，HelloWorld应用的类图。UIApplication不直接依赖 于AppDelegate类，而是依赖于UIApplicationDelegate协议，这在面向对象软件设计原则中叫做“面向接口的编程”。 AppDelegate类实现协议UIApplicationDelegate，它是委托类。

[![3](http://iosbook1.com/wp-content/uploads/2013/02/31.png)](http://iosbook1.com/?attachment_id=141)

我们给出委托的定义，委托是为了降低一个对象的复杂度和耦合度，使其能够更具通用性将其中一些处理置于委托对象中的编码方式。通用类因为通用性即与 具体应用的无关性而变为框架类，框架类保持委托对象的引用，并在特定时刻向委托对象发送消息。消息可能只是通知委托对象做一些事情，也可能是对委托对象进 行控制。

实现原理

我们通过一个案例介绍委托设计模式实现原理和应用场景，重新绘制委托设计模式类图。

[![4](http://iosbook1.com/wp-content/uploads/2013/02/41.png)](http://iosbook1.com/?attachment_id=142)

在古希腊有一个哲学家，他毕生只做三件事情：“睡觉”、“吃饭”和“工作”。为更好的生活，工作效率更高，他会找一个徒弟，把这些事情委托给徒弟做。然而要成为他的徒弟，需要实现一个协议，协议要求能够处理“睡觉”、“吃饭”和“工作”问题。 三者之间的关系。

[![5](http://iosbook1.com/wp-content/uploads/2013/02/51.png)](http://iosbook1.com/?attachment_id=138)

哲学家类图中， 通用类（Philosopher）保持指向委托对象（ViewController）的“弱引用” （id\<PhilosopherDelegate\> delegate），委托对象（ViewController）就是哲学家的“徒弟”，他实现了协议 PhilosopherDelegate，PhilosopherDelegate规定了3个方法：-(void) sleep、-(void) eat和-(void) work方法。

下面我们看看实现代码，委托协议PhilosopherDelegate.h代码如下：

```
@protocol PhilosopherDelegate

@required

-(void) sleep;

-(void) eat;

-(void) work;

@end
```

委托协议PhilosopherDelegate定义了3个方法，协议没有m文件，它的定义可以放在别的h文件中。它的实现类就是委托类ViewController的代码如下：

```
//

//  ViewController.h

//

@interface ViewController : UIViewController<PhilosopherDelegate>

@end

//

//  ViewController.m

//

@implementation ViewController

- (void)viewDidLoad

{

    [super viewDidLoad];

    Philosopher *obj = [[Philosopher alloc ] init];

    obj.delegate = self;

    [obj start];

}

#pragma — PhilosopherDelegate 方法实现

-(void) sleep

{

    NSLog(@”sleep…”);

}

-(void) eat

{

     NSLog(@”eat…”);

}

-(void) work

{

     NSLog(@”work…”);

}

@end
```

委托对象如何与通用类建立引用关系呢？我们通过viewDidLoad方法中的obj.delegate = self语句来指定委托对象和通用类间的引用关系。 一般情况下通用类由框架直接提供，在这个例子中我们根据需要自己实现了通用类Philosopher，Philosopher.h的代码：

```
//

//  Philosopher.h

//  DelegatePattern

//

#import “PhilosopherDelegate.h”

@interface Philosopher : NSObject

{

    NSTimer *timer;

    int count;

}

@property  (nonatomic, weak) id<PhilosopherDelegate> delegate;

-(void) start;

-(void) handle;

@end
```

Philosopher.h中定义delegate属性，它的类型是id\<PhilosopherDelegate\>，它可以保存委托对象的引用，属性weak说明是“弱引用”。Philosopher.m文件代码如下：

```
//

// Philosopher.m

//  DelegatePattern

#import “Philosopher.h”

@implementation Philosopher

@synthesize delegate;

-(void) start

{

    count= 0;

    timer = [NSTimer scheduledTimerWithTimeInterval:3.0

               target:self selector:@selector(handle)userInfo:nil repeats:YES];

}

-(void)handle

{

    switch (count)

    {

        case 0:

            [self.delegate sleep];

            count++;

            break;

        case 1:

            [self.delegate eat];

            count++;

            break;

        case 2:

            [self.delegate work];

            [timer  invalidate];

            break;

    }

}

@end
```

在本例中Philosopher模拟一些通用类发出调用，这个调用的发出是通过NSTimer每3秒发出一个，依次向委托对象发出消息sleep、 eat和work。代码中self.delegate是指向委托对象ViewController的引用，[self.delegate sleep]是调用ViewController中的sleep方法。
