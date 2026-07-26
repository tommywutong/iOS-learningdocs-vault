---
title: 你真的了解NSNotificationCenter吗？
source_url: 'https://www.cnblogs.com/wujy/p/5825690.html'
source_domain: cnblogs.com
source_group: platform
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:ed3ded4ca93d549f'
plan_ref: 第三周：Runtime 行为与 Cocoa 对象通信 / Day 6｜最后才比较对象通信模式（对应 W3-01、W6-07）
plan_week: 第三周：Runtime 行为与 Cocoa 对象通信
plan_day: Day 6｜最后才比较对象通信模式（对应 W3-01、W6-07）
container: '//div[@id=''cnblogs_post_body'']'
container_source: map
---

> 原文：[你真的了解NSNotificationCenter吗？](https://www.cnblogs.com/wujy/p/5825690.html)

**一：首先查看一下关于NSNotificationCenter的定义**

```
@interface NSNotificationCenter : NSObject {
    @package
    void * __strong _impl;
    void * __strong _callback;
    void *_pad[11];
}

//单例获得消息中心对象
+ (NSNotificationCenter *)defaultCenter;

//增加消息监听 第一个参数是观察者为本身，第二个参数表示消息回调的方法，第三个消息通知的名字，第四个为nil表示表示接受所有发送者的消息
- (void)addObserver:(id)observer selector:(SEL)aSelector name:(nullable NSString *)aName object:(nullable id)anObject;

//发送通知 三种方式
- (void)postNotification:(NSNotification *)notification;
- (void)postNotificationName:(NSString *)aName object:(nullable id)anObject;
- (void)postNotificationName:(NSString *)aName object:(nullable id)anObject userInfo:(nullable NSDictionary *)aUserInfo;

//移除监听
- (void)removeObserver:(id)observer;
//移除监听特定消息
- (void)removeObserver:(id)observer name:(nullable NSString *)aName object:(nullable id)anObject;

//增加监听 又提供了一个以block方式实现的添加观察者的方法
- (id <NSObject>)addObserverForName:(nullable NSString *)name object:(nullable id)obj queue:(nullable NSOperationQueue *)queue usingBlock:(void (^)(NSNotification *note))block NS_AVAILABLE(10_6, 4_0);

@end
```

每一个程序都有一个自己的通知中心，即NSNotificationCenter对象。NSNotificationCenter这个也是我们平常用到的相关消息内容操作；NSNotificationCenter是一个单列，我们可以通过defaultCenter来获取到通知中心这个单列；通知中心实际上是iOS程序内部之间的一种消息广播机制，主要为了解决应用程序内部不同对象之间解耦而设计。它是基于观察者模式设计的，不能跨应用程序进程通信，当通知中心接收到消息之后会根据内部的消息转发表，将消息发送给订阅者；

知识点1：消息的运用步骤

1：创建通知并发送

```
        NSNotification *notification =[NSNotification notificationWithName:@"qjwallet" object:nil userInfo:nil];
        //通过通知中心发送通知
        [[NSNotificationCenter defaultCenter] postNotification:notification];
```

2：在接收的页面注册消息通知

```
  [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(qjwalletNotification:) name:@"qjwallet" object:nil];
```

3：处理接收到的内容，并进行操作

```
- (void)qjwalletNotification:(NSNotification *)text{
    //NSLog(@"%@",text.userInfo[@"orderid"]);
    NSLog(@"－－－－－接收到通知------");
}
```

4：移除消息通知

```
-(void)dealloc
{
    [[NSNotificationCenter defaultCenter]removeObserver:self name:@"qjwallet" object:nil];
}
```

知识点2：关于创建通知并发送另外两个方法

```
方法1：[[NSNotificationCenter defaultCenter] postNotificationName:@"First" object:@"博客园"]; 

方法2：
NSDictionary *dict=[[NSDictionary alloc]initWithObjects:@[@"keso"] forKeys:@[@"key"]]; 
[[NSNotificationCenter defaultCenter] postNotificationName:@"Second" object:@"http://www.cnblogs.com" userInfo:dict];
```

上面两个方法已经把NSNotification对象封装一层，所以只要传入相关的对象属性就可以；

知识点3：通过NSNotificationCenter注册通知NSNotification，viewDidLoad中

```
[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(notificationFirst:) name:@"First" object:nil];

[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(notificationSecond:) name:@"Second" object:nil];
```

```
-(void)notificationFirst:(NSNotification *)notification{
    NSString  *name=[notification name];
    NSString  *object=[notification object];
    NSLog(@"名称:%@----对象:%@",name,object);
}

-(void)notificationSecond:(NSNotification *)notification{
    NSString  *name=[notification name];
    NSString  *object=[notification object];
    NSDictionary  *dict=[notification userInfo];
    NSLog(@"名称:%@----对象:%@",name,object);
    NSLog(@"获取的值:%@",[dict objectForKey:@"key"]);
}
```

知识点4：移除通知消息

```
-(void)dealloc{
    NSLog(@"观察者销毁了");
    [[NSNotificationCenter defaultCenter] removeObserver:self];
}

也可以针对某一个进行移除：

[[NSNotificationCenter defaultCenter] removeObserver:self name:@"First" object:nil];
```

知识点5：如果notificationName为nil，则会接收所有的通知(如果notificationSender不为空，则接收所有来自于notificationSender的所有通知)。如代码清单1所示。如果notificationSender为nil，则会接收所有notificationName定义的通知；否则，接收由notificationSender发送的通知。监听同一条通知的多个观察者，在通知到达时，它们执行回调的顺序是不确定的，所以我们不能去假设操作的执行会按照添加观察者的顺序来执行

知识点6：addObserverForName监听消息处理跟addObserver的差别

在前面addObserver有介绍它的四个参数作用，分别指定了通知的观察者、处理通知的回调、通知名及通知的发送对象；而addObserverForName同样是监听消息处理，只是它并没有观察者，却多出一个队列跟一个block的处理；addObserverForName参数说明，name和obj为nil时的情形与前面一个方法addObserver是相同的。如果queue为nil，则消息是默认在post线程中同步处理，即通知的post与转发是在同一线程中；但如果我们指定了操作队列，情况就变得有点意思了，我们一会再讲。block块会被通知中心拷贝一份(执行copy操作)，以在堆中维护一个block对象，直到观察者被从通知中心中移除。所以，应该特别注意在block中使用外部对象，避免出现对象的循环引用。如果一个给定的通知触发了多个观察者的block操作，则这些操作会在各自的Operation Queue中被并发执行。所以我们不能去假设操作的执行会按照添加观察者的顺序来执行。该方法会返回一个表示观察者的对象，记得在不用时释放这个对象。

实例在指定队列中接收通知：

```
@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];

    [[NSNotificationCenter defaultCenter] addObserverForName:TEST_NOTIFICATION object:nil queue:[NSOperationQueue mainQueue] usingBlock:^(NSNotification *note) {

        NSLog(@"receive thread = %@", [NSThread currentThread]);
    }];

    dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
       
        NSLog(@"post thread = %@", [NSThread currentThread]);
        [[NSNotificationCenter defaultCenter] postNotificationName:TEST_NOTIFICATION object:nil];
    });
}

@end
```

在这里，我们在主线程里添加了一个观察者，并指定在主线程队列中去接收处理这个通知。然后我们在一个全局队列中post了一个通知。我们来看下输出结果：

```
post thread = <NSThread: 0x7ffe0351f5f0>{number = 2, name = (null)}
receive thread = <NSThread: 0x7ffe03508b30>{number = 1, name = main}
```

可以看到，消息的post与接收处理并不是在同一个线程中。如上面所提到的，如果queue为nil，则消息是默认在post线程中同步处理；

**二：关于NSNotification的定义**

```
@interface NSNotification : NSObject <NSCopying, NSCoding>
//这个成员变量是这个消息对象的唯一标识，用于辨别消息对象
@property (readonly, copy) NSString *name;
// 这个成员变量定义一个对象，可以理解为针对某一个对象的消息，代表通知的发送者
@property (nullable, readonly, retain) id object;
//这个成员变量是一个字典，可以用其来进行传值
@property (nullable, readonly, copy) NSDictionary *userInfo;

// 初始化方法
- (instancetype)initWithName:(NSString *)name object:(nullable id)object userInfo:(nullable NSDictionary *)userInfo NS_AVAILABLE(10_6, 4_0) NS_DESIGNATED_INITIALIZER;
- (nullable instancetype)initWithCoder:(NSCoder *)aDecoder NS_DESIGNATED_INITIALIZER;

@end
```

NSNotification顾名思义就是通知的作用，一个对象通知另外一个对象，可以用来传递参数、通信等作用，与delegate的一对一不同，通知是一对多的。在一个对象中注册了通知，那么其他任意对象都可以来对这个对象发出通知。因为属性都是只读的，如果要创建消息时要用下面NSNotification (NSNotificationCreation)分类相应的方法进行初始化；

**三：NSNotification (NSNotificationCreation)分类**

```
@interface NSNotification (NSNotificationCreation)

+ (instancetype)notificationWithName:(NSString *)aName object:(nullable id)anObject;
+ (instancetype)notificationWithName:(NSString *)aName object:(nullable id)anObject userInfo:(nullable NSDictionary *)aUserInfo;

- (instancetype)init /*NS_UNAVAILABLE*/;    /* do not invoke; not a valid initializer for this class */

@end
```

上面为初使化NSNotification对象，用于消息的发送对象；

最近有个妹子弄的一个关于扩大眼界跟内含的订阅号，每天都会更新一些深度内容，在这里如果你感兴趣也可以关注一下(嘿对美女跟知识感兴趣)，当然可以关注后输入：github 会有我的微信号，如果有问题你也可以在那找到我；当然不感兴趣无视此信息；

![](https://images2017.cnblogs.com/blog/80291/201708/80291-20170814153921225-1140887099.jpg)
