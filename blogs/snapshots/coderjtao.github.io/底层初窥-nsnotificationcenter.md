---
title: 底层初窥——NSNotificationCenter
source_url: 'https://coderjtao.github.io/2019/07/26/%E5%BA%95%E5%B1%82%E5%88%9D%E7%AA%A5%E2%80%94%E2%80%94NSNotificationCenter/'
source_domain: coderjtao.github.io
source_group: single-site
original_language: zh
published: 2019-07-26
archived_at: 2026-07-27
content_hash: 'sha256:0f65cda08be6fa4c'
plan_ref: 第三周：Runtime 行为与 Cocoa 对象通信 / Day 6｜最后才比较对象通信模式（对应 W3-01、W6-07）
plan_week: 第三周：Runtime 行为与 Cocoa 对象通信
plan_day: Day 6｜最后才比较对象通信模式（对应 W3-01、W6-07）
container: '//*[contains(@class,''post-content'')]'
container_source: guess
---

> 原文：[底层初窥——NSNotificationCenter](https://coderjtao.github.io/2019/07/26/%E5%BA%95%E5%B1%82%E5%88%9D%E7%AA%A5%E2%80%94%E2%80%94NSNotificationCenter/)

# 底层初窥——NSNotificationCenter

Posted on 2019-07-26      In  [iOS底层初窥](https://coderjtao.github.io/categories/iOS%E5%BA%95%E5%B1%82%E5%88%9D%E7%AA%A5/)

- [介绍](#introduce)
- [数据结构](#struct)
- [工作流程](#workflow)
- [一些问题](#qa)

## 介绍

消息通知在项目中使用是很频繁的，但是我们平常之事关注于使用，这篇文章我们稍微深入了解一下消息中心是怎么运作的。

通知机制的核心是一个与线程关联的单例对象叫通知中心（NSNotificationCenter）。通知中心发送通知给观察者是同步的，也可以用通知队列（NSNotificationQueue）异步发送通知。

苹果并没有开源相关代码，但是可以读下[GNUStep的源码](https://github.com/gnustep/libs-base/blob/master/Source/NSNotificationCenter.m)，基本上实现方式很具有参考性。

> [官方文档地址](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Articles/Notifications.html#//apple_ref/doc/uid/20000215-BCICIHGE)

## 数据结构

这里我们的数据结构及流程分析，都是基于 [GNUStep的源码](https://github.com/gnustep/libs-base/blob/master/Source/NSNotificationCenter.m)。

#### NSNotificationCenter：消息中心

```plaintext
typedef struct NCTbl {
  Observation		*wildcard;	/* Get ALL messages.		*/
  GSIMapTable		nameless;	/* Get messages for any name.	*/
  GSIMapTable		named;		/* Getting named messages only.	*/
  ...
} NCTable;
```

- wildcard

    - wildcard是链表的数据结构，如果在注册观察者时既没有传入NotificationName，也没有传入object，就会添加到wildcard的链表中。注册到这里的观察者能接收到 所有的系统通知。
- nameless

    - 添加观察者时没有传入 NoficationName 的表
- named

    - 添加观察者时传入了 NotificationName 的表

#### named

在 named 表中，NotifcationName 作为表的 key，因为我们在注册观察者的时候是可以传入一个参数 object 用于只监听指定该对象发出的通知，并且一个通知可以添加多个观察者，所以还需要一张表来保存 object 和 Observer 的对应关系。这张表的是 key、Value 分别是以 object 为 Key，Observer 为 value。用了链表这种数据结构实现保存多个观察者的情况。

> 在实际开发过程中 object 参数我们经常传 nil，这时候系统会根据 nil 自动生成一个 key，相当于这个 key 对应的 value（链表）保存的就是当前通知传入了 NotificationName 没有传入 object 的所有观察者。

![](https://coderjtao.github.io/2019/07/26/%E5%BA%95%E5%B1%82%E5%88%9D%E7%AA%A5%E2%80%94%E2%80%94NSNotificationCenter/Notification-named.jpg)

#### nameless

nameless 表，较 named 表就简单了许多。因为少了 NSNotificationName 作为 Key 值，所以少了一层嵌套。

![](https://coderjtao.github.io/2019/07/26/%E5%BA%95%E5%B1%82%E5%88%9D%E7%AA%A5%E2%80%94%E2%80%94NSNotificationCenter/Notification-nameless.jpg)

#### wildcard

在注册观察者时既没有传入 NSNotificationName，也没有传入 object，就会添加到 wildcard 的链表中。**注册到这里的观察者能接收到所有的系统通知**。

#### Observation：保存了观察者信息

```plaintext
typedef	struct	Obs {
  id		observer;	/* Object to receive message.	*/
  SEL		selector;	/* Method selector.		*/
  struct Obs	*next;		/* Next item in linked list.	*/
  int		retained;	/* Retain count for structure.	*/
  struct NCTbl	*link;		/* Pointer back to chunk table	*/
} Observation;
```

![](https://coderjtao.github.io/2019/07/26/%E5%BA%95%E5%B1%82%E5%88%9D%E7%AA%A5%E2%80%94%E2%80%94NSNotificationCenter/Notification-observer.jpg)

## 工作流程

- 添加观察者流程

    1. 首先会根据传入的参数实例化一个 Observation，Observation 对象保存了观察者对象，接收到通知观察者所执行的方法，以及下一个 Observation 对象的地址。
    2. 根据是否传入 NotificationName 选择操作 Named Table 还是 Nameless Table。
    3. 若传入了 NotificationName，则会以 NotificationName 为 key 去查找对应的 Value，若找到 value，则取出对应的 value；若未找到对应的 value，则新建一个 table，然后将这个 table 以 NotificationName 为 key 添加到 Named Table 中。
    4. 若在保存 Observation 的 table 中，以 object 为 key 取对应的链表。若找到了则直接在链接末尾插入之前实例化好的 Observation；若未找到则以之前实例化好的 Observation 对象作为头节点插入进去。
- 发送通知流程

    1. 首先会创建一个数组 observerArray 用来保存需要通知的 observer。
    2. 遍历 wildcard 链表，将 observer 添加到 observerArray 数组中。
    3. 若存在 object，在 nameless table 中找到以 object 为 key 的链表，然后遍历找到的链表，将 observer 添加到 observerArray 数组中。
    4. 若存在 NotificationName，在 named table 中以 NotificationName 为 key 找到对应的 table，然后再在找到的 table 中以 object 为 key 找到对应的链表，遍历链表，将 observer 添加到 observerArray 数组中。如果 object 不 为nil，则以 nil 为 key 找到对应的链表，遍历链表，将 observer 添加到 observerArray 数组中。
    5. 至此所有关于当前通知的 observer（wildcard+nameless+named）都已经加入到了数组 observerArray 中。遍历 observerArray 数组，取出其中 的observer 节点（包含了观察者对象和 selector），调用形式如下：

  ```plaintext
  [o->observer performSelector: o->selector withObject: notification];
  ```
- 移除通知流程

    1. 若 NotificationName 和 object 都为 nil，则清空 wildcard 链表。
    2. 若 NotificationName 为 nil，遍历 named table，若 object 为 nil，则清空 named table，若 object 不为 nil，则以 object 为 key 找到对应的链表，然后清空链表。在 nameless table 中以 object 为 key 找到对应的 observer 链表，然后清空，若 object 也为 nil，则清空 nameless table。
    3. 若 NotificationName 不为nil，在 named table 中以 NotificationName 为 key 找到对应的 table，若 object 为 nil，则清空找到的 table，若 object 不为 nil，则以 object 为 key 在找到的 table 中取出对应的链表，然后清空链表。

## 一些问题

这一节收集了几个常见的 NSNotificationCenter 相关的问题。

#### 通知的发送时同步的，还是异步的？发送消息与接收消息的线程是同一个线程么？

通知中心发送通知给观察者是同步的，也可以用通知队列（NSNotificationQueue）异步发送通知。

在抛出通知以后，观察者在通知事件处理完成以后（可以通过休眠3秒来测试），抛出者才会往下继续执行，也就是说这个过程默认是同步的；当发送通知时，通知中心会一直等待所有的 observer 都收到并且处理了通知才会返回到 poster。

接收通知的线程，和发送通知所处的线程是同一个线程。也就是说如果如果要在接收通知的时候更新 UI，需要注意发送通知的线程是否为主线程。

```plaintext
- (void)viewDidLoad {
    [super viewDidLoad];
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(test) name:@"NotificationName" object:nil];
}

- (void)touchesBegan:(NSSet<UITouch *> *)touches withEvent:(UIEvent *)event {

    dispatch_queue_t queue = dispatch_queue_create("test.queue", DISPATCH_QUEUE_SERIAL);
    dispatch_async(queue, ^{    // 异步执行 + 串行队列
        NSLog(@"--current thread: %@", [NSThread currentThread]);
        NSLog(@"Begin post notification");
        [[NSNotificationCenter defaultCenter] postNotificationName:@"NotificationName" object:nil];
        NSLog(@"End");
    });

}

- (void)test {
    NSLog(@"--current thread: %@", [NSThread currentThread]);
    NSLog(@"Handle notification and sleep 3s");
    sleep(3);
}

---- 输出结果 ----
13:49:05.364262+0800 --current thread: <NSThread: 0x600000960d00>{number = 3, name = (null)}
13:49:05.364445+0800 Begin post notification
13:49:05.364621+0800 --current thread: <NSThread: 0x600000960d00>{number = 3, name = (null)}
13:49:05.364750+0800 Handle notification and sleep 3s
13:49:08.370804+0800 End
```

#### 如何异步发送消息？

1. 让通知事件处理方法在子线程中执行.

```plaintext
- (void)viewDidLoad {
    [super viewDidLoad];
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(test) name:@"NotificationName" object:nil];
}

- (void)touchesBegan:(NSSet<UITouch *> *)touches withEvent:(UIEvent *)event {
    NSLog(@"--current thread: %@", [NSThread currentThread]);
    NSLog(@"Begin post notification");
    [[NSNotificationCenter defaultCenter] postNotificationName:@"NotificationName" object:nil];
    NSLog(@"End");
}

- (void)test {
    dispatch_queue_t queue = dispatch_queue_create("test.queue", DISPATCH_QUEUE_SERIAL);
    dispatch_async(queue, ^{    // 异步执行 + 串行队列
        NSLog(@"--current thread: %@", [NSThread currentThread]);
        NSLog(@"Handle notification and sleep 3s");
        sleep(3);
    });
}

---- 输出结果 ----
13:54:25.336948+0800 --current thread: <NSThread: 0x6000007e4b00>{number = 1, name = main}
13:54:25.337177+0800 Begin post notification
13:54:25.337360+0800 End
13:54:25.337391+0800 --current thread: <NSThread: 0x60000079a940>{number = 6, name = (null)}
13:54:25.337492+0800 Handle notification and sleep 3s
```

1. 可以通过 NSNotificationQueue 的 enqueueNotification: postingStyle: 和 enqueueNotification: postingStyle: coalesceMask: forModes: 方法将通告放入队列，实现异步发送，在把通告放入队列之后，这些方法会立即将控制权返回给调用对象。

```plaintext
- (void)viewDidLoad {
    [super viewDidLoad];
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(test) name:@"NotificationName" object:nil];
}

- (void)touchesBegan:(NSSet<UITouch *> *)touches withEvent:(UIEvent *)event {
    NSLog(@"--current thread: %@", [NSThread currentThread]);
    NSLog(@"Begin post notification");
    NSNotification *notification = [NSNotification notificationWithName:@"NotificationName"
                                                                     object:nil];
    [[NSNotificationQueue defaultQueue] enqueueNotification:notification postingStyle:NSPostASAP];
    NSLog(@"End");
}

- (void)test {
    NSLog(@"--current thread: %@", [NSThread currentThread]);
    NSLog(@"Handle notification and sleep 3s");
    sleep(3);
}

---- 输出结果 ----
13:57:18.686405+0800 --current thread: <NSThread: 0x600001e88780>{number = 1, name = main}
13:57:18.686588+0800 Begin post notification
13:57:18.686762+0800 End
13:57:18.687007+0800 --current thread: <NSThread: 0x600001e88780>{number = 1, name = main}
13:57:18.687116+0800 Handle notification and sleep 3s
```

#### NSNotificationQueue 和 runloop 的关系？

postringStyle 参数就是定义通知调用和 runloop 状态之间关系。  
该参数的三个可选参数：

1. NSPostWhenIdle：通知回调方法是等待到当下线程 runloop 进入等待状态才会调用。
2. NSPostASAP：通知回调方法是等待到当下线程 runloop 开始接收事件源的时候就会调用。
3. NSPostNow：其实和直接用默认的通知中心添加通知是一样的，通知马上调用回调方法。

#### 如何保证通知接收的线程在主线程？

[官方示例-在指定线程处理通知消息](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Notifications/Articles/Threading.html#//apple_ref/doc/uid/20001289-CEGJFDFG)

#### 页面销毁时不移除通知会崩溃吗？

在观察者对象释放之前，需要调用 ==removeOberver== 方法将观察者从通知中心移除，否则程序可能会出现崩溃。但从 iOS9 开始，即使不移除观察者对象，程序也不会出现异常。

> If your app targets iOS 9.0 and later or macOS 10.11 and later, you don’t need to unregister an observer in its dealloc method.

这是因为在 iOS9 以后，通知中心持有的观察者由 ==unsafe_unretained== 引用变为 ==weak== 引用。即使不对观察者手动移除，持有的观察者的引用也会在观察者被回收后自动置空。但是通过 addObserverForName:object: queue:usingBlock: 方法注册的观察者需要手动释放，因为通知中心持有的是它们的强引用。

```plaintext
- (id <NSObject>)addObserverForName:(nullable NSNotificationName)name object:(nullable id)obj queue:(nullable NSOperationQueue *)queue usingBlock:(void (^)(NSNotification *note))block API_AVAILABLE(macos(10.6), ios(4.0), watchos(2.0), tvos(9.0));
    // The return value is retained by the system, and should be held onto by the caller in
    // order to remove the observer with removeObserver: later, to stop observation.
```

---

#### 多次添加同一个通知会是什么结果？多次移除通知呢？

- 多次添加同一个通知，会导致观察者方法被执行多次。
- 多次移除通知，没有关系。
- **移除通知**

```plaintext
// 添加
[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(test) name:@"aa" object:nil];

// 移除
[[NSNotificationCenter defaultCenter] removeObserver:self];

/// Block
// 添加
_noty =  [[NSNotificationCenter defaultCenter] addObserverForName:URLookExpandCloth object:nil queue:nil usingBlock:^(NSNotification * _Nonnull note) {
    // 执行你想做的事情
    }];

// 移除
[[NSNotificationCenter defaultCenter] removeObserver:_noty];
```

---

#### 下面的方式能接收到通知吗？为什么

```plaintext
// 添加观察
[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(handleNotification:) name:@"TestNotification" object:@1];
// 通知发送
[NSNotificationCenter.defaultCenter postNotificationName:@"TestNotification" object:nil];
```

不会，上文介绍 NSNotificationCenter 时介绍了 center 的结构。

- 注册通知在添加observer时，路径为 TestNotification -\> @1 -\> self
- 发送通知在查找observer时，路径为 TestNotification -\> nil -\> observer list
