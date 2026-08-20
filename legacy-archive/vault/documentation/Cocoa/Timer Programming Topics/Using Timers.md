---
title: 定时器编程主题
apple_id: 10000061i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2009-07-14'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Timers/Articles/usingTimers.html
archived_at: '2026-07-15T07:20:40.798319Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [定时器编程主题](Introduction%20to%20Timers.md)


[下一页](Document%20Revision%20History.md)[上一页](Timers.md)

# 使用定时器

使用定时器（timer）涉及好几个方面。创建定时器时，你必须对它进行配置，让它知道触发（fire）时该向哪个对象发送哪个消息。然后你必须把它与某个运行循环（run loop）关联起来，这样它才会触发——有些创建方法会自动替你完成这一步。最后，如果你创建的是重复定时器，那么在希望它停止触发时，你必须让它失效。

大体来说，创建定时器有三种方式：

1. 把定时器调度到当前运行循环上；
2. 先创建定时器，稍后再把它注册到某个运行循环；
3. 用给定的触发日期初始化定时器。

无论采用哪种方式，你都必须配置定时器，告诉它触发时该向哪个对象发送哪个消息，以及它是否应该重复。在某些方法中，你还可以提供一个用户信息字典。凡是定时器触发时所调用的方法可能用得上的东西，你都可以放进这个字典里。

要告诉定时器该发送什么消息、以及该把消息发给哪个对象，有两种做法——分别单独指定两者，或者（在某些情况下）使用 `NSInvocation` 的实例。如果你直接指定消息的[选择器](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)，那么方法叫什么名字并不重要，但它必须具有如下签名：

```objc
- (void)targetMethod:(NSTimer*)theTimer
```

如果你创建了 invocation 对象，那就可以指定任意你想要的消息。（关于 invocation 对象的更多内容，请参阅 _[分布式对象编程主题](../Distributed%20Objects%20Programming%20Topics/Introduction%20to%20Distributed%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyde2i)_ 中的 [使用 NSInvocation](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/Tasks/invocations.html#//apple_ref/doc/uid/20000744)。）

由于运行循环会持有定时器，从对象生命周期的角度看，在_把定时器调度出去之后_，通常并不_需要_再保留对它的引用。（因为当你以选择器的形式指定定时器的方法时，定时器本身会作为参数传入，所以你可以在那个方法内部适时地让重复定时器失效。）不过在很多场合下，你还是希望保留让定时器失效的余地——甚至可能在它开始之前就让它失效。这种情况下，你_确实_需要保留对定时器的引用，以便在合适的时候停止它。如果你创建的是未调度的定时器（参阅 [未调度的定时器](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaydolktk4zq)），那么你必须对它保持一个强引用，以免它在你使用之前就被释放。

定时器会对它的目标（target）保持强引用。这意味着只要定时器仍然有效，它的目标就不会被释放。由此可以推出：让定时器的目标在自己的 `dealloc` 方法中试图让该定时器失效是没有意义的——只要定时器有效，`dealloc` 方法就不会被调用。

在接下来的示例中，设想有一个定时器控制器对象，它声明了若干方法，用来启动（在某些情况下还用来停止）四个以不同方式配置的定时器。它为其中两个定时器提供了属性（property）；还有一个属性用来统计其中某个定时器已触发过多少次，以及三个与定时器相关的方法（`targetMethod:`、`invocationMethod:` 和 `countedTimerFireMethod:`）。该控制器还提供了一个方法来给出用户信息字典。

```objc
@interface TimerController : NSObject

// 重复定时器是一个 weak 属性。
@property (weak) NSTimer *repeatingTimer;
@property (strong) NSTimer *unregisteredTimer;
@property NSUInteger timerCount;

- (IBAction)startOneOffTimer:sender;

- (IBAction)startRepeatingTimer:sender;
- (IBAction)stopRepeatingTimer:sender;

- (IBAction)createUnregisteredTimer:sender;
- (IBAction)startUnregisteredTimer:sender;
- (IBAction)stopUnregisteredTimer:sender;

- (IBAction)startFireDateTimer:sender;

- (void)targetMethod:(NSTimer*)theTimer;
- (void)invocationMethod:(NSDate *)date;
- (void)countedTimerFireMethod:(NSTimer*)theTimer;

- (NSDictionary *)userInfo;

@end
```

用户信息方法以及定时器所调用的两个方法，其实现可以像下面这样（`countedTimerFireMethod:` 在 [停止定时器](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaydolktk42q) 中介绍）：

```objc
- (NSDictionary *)userInfo {
    return @{ @"StartDate" : [NSDate date] };
}

- (void)targetMethod:(NSTimer*)theTimer {
    NSDate *startDate = [[theTimer userInfo] objectForKey:@"StartDate"];
    NSLog(@"Timer started on %@", startDate);
}

- (void)invocationMethod:(NSDate *)date {
    NSLog(@"Invocation for timer started on %@", date);
}
```


下面这两个类方法会自动把新建的定时器以默认模式（[NSDefaultRunLoopMode](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSDefaultRunLoopMode)）注册到当前的 `NSRunLoop` 对象上：

- [scheduledTimerWithTimeInterval:invocation:repeats:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimer/Description.html#//apple_ref/occ/clm/NSTimer/scheduledTimerWithTimeInterval:invocation:repeats:)
- [scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimer/Description.html#//apple_ref/occ/clm/NSTimer/scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:)

下面的示例展示了如何调度一个使用选择器的一次性定时器：

```objc
- (IBAction)startOneOffTimer:sender {

    [NSTimer scheduledTimerWithTimeInterval:2.0
             target:self
             selector:@selector(targetMethod:)
             userInfo:[self userInfo]
             repeats:NO];
}
```

2 秒之后，运行循环会自动触发该定时器，随后把它从运行循环中移除。

下一个示例展示了如何调度一个重复定时器，它同样使用选择器（让定时器失效的做法在 [停止定时器](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaydolktk42q) 中介绍）：

```objc
- (IBAction)startRepeatingTimer:sender {

    // 取消已经存在的定时器。
    [self.repeatingTimer invalidate];

    NSTimer *timer = [NSTimer scheduledTimerWithTimeInterval:0.5
                              target:self selector:@selector(targetMethod:)
                              userInfo:[self userInfo] repeats:YES];
    self.repeatingTimer = timer;
}
```

如果你创建了重复定时器，通常需要保存对它的引用，以便日后能够停止它（关于无需这样做的例子，参阅 [用触发日期初始化定时器](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaydolktk42a)）。

下面这些方法创建的定时器，你可以在稍后向 `NSRunLoop` 对象发送 [addTimer:forMode:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSRunLoop/Description.html#//apple_ref/occ/instm/NSRunLoop/addTimer:forMode:) 消息来对它进行调度。

- [timerWithTimeInterval:invocation:repeats:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimer/Description.html#//apple_ref/occ/clm/NSTimer/timerWithTimeInterval:invocation:repeats:)
- [timerWithTimeInterval:target:selector:userInfo:repeats:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTimer/Description.html#//apple_ref/occ/clm/NSTimer/timerWithTimeInterval:target:selector:userInfo:repeats:)

下面的示例展示了如何在一个方法中创建使用 invocation 对象的定时器，然后在另一个方法中把它添加到运行循环，从而启动该定时器：

```objc
- (IBAction)createUnregisteredTimer:sender {

    NSMethodSignature *methodSignature = [self methodSignatureForSelector:@selector(invocationMethod:)];
    NSInvocation *invocation = [NSInvocation invocationWithMethodSignature:methodSignature];
    [invocation setTarget:self];
    [invocation setSelector:@selector(invocationMethod:)];
    NSDate *startDate = [NSDate date];
    [invocation setArgument:&startDate atIndex:2];

    NSTimer *timer = [NSTimer timerWithTimeInterval:0.5 invocation:invocation repeats:YES];
    self.unregisteredTimer = timer;
}

- (IBAction)startUnregisteredTimer:sender {

    if (self.unregisteredTimer != nil) {
        NSRunLoop *runLoop = [NSRunLoop currentRunLoop];
        [runLoop addTimer:self.unregisteredTimer forMode:NSDefaultRunLoopMode];
    }
}
```


你可以自己分配一个 `NSTimer` 对象，并向它发送 [initWithFireDate:interval:target:selector:userInfo:repeats:](https://developer.apple.com/documentation/foundation/nstimer/1415700-initwithfiredate) 消息。这样你就可以独立于重复间隔来指定初始的触发日期。定时器一旦创建完成，你唯一还能修改的属性就是它的触发日期（使用 `setFireDate:`）。其他所有参数在定时器创建之后都是不可变的。要让定时器开始触发，你必须把它添加到某个运行循环中。

下面的示例展示了如何创建一个带有给定起始时间（本例中是 1 秒之后）的定时器，然后把它添加到运行循环来启动它：

```objc
- (IBAction)startFireDateTimer:sender {

    NSDate *fireDate = [NSDate dateWithTimeIntervalSinceNow:1.0];
    NSTimer *timer = [[NSTimer alloc] initWithFireDate:fireDate
                                      interval:0.5
                                      target:self
                                      selector:@selector(countedTimerFireMethod:)
                                      userInfo:[self userInfo]
                                      repeats:YES];

    self.timerCount = 1;
    NSRunLoop *runLoop = [NSRunLoop currentRunLoop];
    [runLoop addTimer:timer forMode:NSDefaultRunLoopMode];
}
```

在这个示例中，虽然定时器被配置为重复触发，但它所调用的 `countedTimerFireMethod:` 会在它触发三次之后把它停掉——参阅 [停止定时器](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaydolktk42q)。

如果你创建的是非重复定时器，就无需再做任何额外处理。它在触发之后会自动停止自己。例如，[用触发日期初始化定时器](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaydolktk42a) 中创建的那个定时器就不需要去停止。不过，如果你创建的是重复定时器，那就要向它发送 `invalidate` 消息来停止它。你也可以在非重复定时器触发之前向它发送 `invalidate` 消息，以阻止它触发。

下面的示例给出了前面各示例中所创建定时器的停止方法：

```objc
- (IBAction)stopRepeatingTimer:sender {
    [self.repeatingTimer invalidate];
    self.repeatingTimer = nil;
}

- (IBAction)stopUnregisteredTimer:sender {
    [self.unregisteredTimer invalidate];
    self.unregisteredTimer = nil;
}
```

你也可以在定时器所调用的方法中让它失效。例如，[用触发日期初始化定时器](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhaydolktk42a) 中那个定时器所调用的方法可以写成这样：

```objc
- (void)countedTimerFireMethod:(NSTimer*)theTimer {

    NSDate *startDate = [[theTimer userInfo] objectForKey:@"StartDate"];
    NSLog(@"Timer started on %@; fire count %d", startDate, self.timerCount);

    self.timerCount++;
    if (self.timerCount > 3) {
        [theTimer invalidate];
    }
}
```

这段代码会在定时器触发三次之后让它失效。由于定时器会作为参数传给它所调用的方法，因此可能没有必要再把定时器保存为一个变量。不过通常你还是会保留对定时器的引用，以便在需要时能提前停止它。

[下一页](Document%20Revision%20History.md)[上一页](Timers.md)

