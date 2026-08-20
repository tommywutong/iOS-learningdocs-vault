---
title: Objective-C 运行时编程指南
apple_id: TP40008048
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtForwarding.html
archived_at: '2026-07-15T07:17:28.428166Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 运行时编程指南](Introduction.md)


[下一页](Type%20Encodings.md)[上一页](Dynamic%20Method%20Resolution.md)

# 消息转发

向一个不处理某条消息的对象发送该消息是一个错误。不过，在报告这个错误之前，运行时（runtime）系统会再给接收消息的对象一次处理该消息的机会。

如果你向一个不处理某条消息的对象发送该消息，运行时在报错之前会先给该对象发送一条 `forwardInvocation:` 消息，并以一个 `NSInvocation` 对象作为其唯一参数——这个 `NSInvocation` 对象封装了原始消息以及随之传递的参数。

你可以实现 `forwardInvocation:` 方法，对该消息给出一个默认响应，或者以其他方式避免这个错误。正如其名称所暗示的，`forwardInvocation:` 常被用来把消息转发给另一个对象。

为了看清转发的适用范围和意图，设想以下场景：首先，假设你正在设计一个能响应名为 `negotiate` 的消息的对象，并且希望它的响应中包含另一种对象的响应。要做到这一点很容易，只需在你实现的 `negotiate` 方法体内某处向另一个对象发送一条 `negotiate` 消息即可。

再进一步，假设你希望你的对象对 `negotiate` 消息的响应恰好就是另一个类中实现的那个响应。实现这一点的一种办法是让你的类从那个类继承该方法。然而，事情未必能这样安排。你的类与实现 `negotiate` 的那个类分处继承体系的不同分支，可能是有充分理由的。

即便你的类无法继承 `negotiate` 方法，你仍然可以“借用”它：实现一个版本的该方法，简单地把消息转交给另一个类的实例：

```objc
- (id)negotiate
{
    if ( [someOtherObject respondsTo:@selector(negotiate)] )
        return [someOtherObject negotiate];
    return self;
}
```

这种做法可能会有些笨重，尤其是当你想让自己的对象转交给另一个对象的消息数量较多时。你不得不为每一个想从另一个类借用的方法都实现一个方法。而且，如果在你编写代码时还不知道可能要转发的消息的完整集合，这种做法就无法应对了。那个集合可能取决于运行时发生的事件，也可能随着未来实现新的方法和类而发生变化。

`forwardInvocation:` 消息所提供的这第二次机会为该问题给出了一个不那么临时凑合的解决方案，而且是动态的而非静态的。它的工作方式是这样的：当一个对象因为没有与消息中选择器相匹配的方法而无法响应该消息时，运行时系统会给它发送一条 `forwardInvocation:` 消息来告知它这一情况。每个对象都从 `NSObject` 类继承了一个 `forwardInvocation:` 方法。然而，`NSObject` 版本的该方法只是调用 `doesNotRecognizeSelector:`。通过覆盖 `NSObject` 的版本并实现你自己的版本，你就能利用 `forwardInvocation:` 消息提供的这个机会，把消息转发给其他对象。

要转发一条消息，`forwardInvocation:` 方法所需要做的只是：

- 确定该消息应该去往何处，以及
- 带着它原本的参数把它发送到那里。

可以用 `invokeWithTarget:` 方法来发送该消息：

```objc
- (void)forwardInvocation:(NSInvocation *)anInvocation
{
    if ([someOtherObject respondsToSelector:
            [anInvocation selector]])
        [anInvocation invokeWithTarget:someOtherObject];
    else
        [super forwardInvocation:anInvocation];
}
```

被转发消息的返回值会返回给原始发送者。所有类型的返回值都能送达发送者，包括 `id`、结构体和双精度浮点数。

`forwardInvocation:` 方法可以充当无法识别的消息的分发中心，把它们分派给不同的接收者。它也可以充当中转站，把所有消息都发往同一个目的地。它可以把一条消息翻译成另一条消息，或者干脆“吞掉”某些消息，使之既无响应也无错误。`forwardInvocation:` 方法还可以把若干条消息合并成单一的一个响应。`forwardInvocation:` 具体做什么，取决于实现者。不过，它所提供的把对象串联成转发链的可能性，为程序设计打开了新的思路。

关于转发和调用（invocation）的更多信息，参见 Foundation 框架参考中的 `NSInvocation` 类说明。

转发模仿了继承，可以用来为 Objective-C 程序带来多重继承的部分效果。如 [图 5-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqguwtqnztge3q) 所示，一个通过转发来响应消息的对象看上去像是借用或“继承”了另一个类中定义的方法实现。

__图 5-1__  转发

!

在这幅插图中，Warrior 类的一个实例把 `negotiate` 消息转发给了 Diplomat 类的一个实例。Warrior 看上去会像 Diplomat 那样谈判。它似乎响应了 `negotiate` 消息，而且就实际效果而言它确实做出了响应（尽管真正干活的是 Diplomat）。

于是，转发消息的那个对象就从继承体系的两个分支“继承”了方法——它自己所在的分支，以及响应该消息的那个对象所在的分支。在上面的例子中，看起来就好像 Warrior 类除了继承自己的超类之外，还继承了 Diplomat。

转发提供了你通常想从多重继承中获得的大部分特性。不过两者之间有一个重要区别：多重继承是把不同的能力合并到单个对象中，它倾向于产生庞大而多面的对象。而转发则是把各自独立的职责分派给不同的对象，它把问题分解为更小的对象，同时又以一种对消息发送者透明的方式把这些对象关联起来。

转发不仅模仿多重继承，还使得开发代表或“覆盖”更重量级对象的轻量级对象成为可能。这个替身对象代替另一个对象出面，并把消息导流给它。

_[Objective-C 编程语言](../The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_ 中“Remote Messaging”一节讨论的代理（proxy）就是这样一个替身。代理负责处理把消息转发给远程接收者的各种事务细节，确保参数值能跨连接复制和取回，等等。但它并不试图做更多的事；它并不复制远程对象的功能，只是给远程对象一个本地地址，一个可以在另一个应用程序中接收消息的位置。

其他种类的替身对象也是可能的。例如，假设你有一个要处理大量数据的对象——也许它要生成一幅复杂的图像，或者要读取磁盘上某个文件的内容。把这个对象设置起来可能相当耗时，所以你更愿意惰性地完成——等到真正需要它时，或者等到系统资源暂时空闲时再做。与此同时，你至少需要为这个对象准备一个占位者，好让应用程序中的其他对象能正常工作。

在这种情况下，你可以先创建的不是那个完备的对象，而是它的一个轻量级替身。这个替身对象可以自己做一些事，比如回答关于数据的问题，但它主要只是替更大的那个对象占位，并在时机成熟时把消息转发给它。当替身的 `forwardInvocation:` 方法第一次收到发往另一个对象的消息时，它会确保那个对象已经存在，若不存在就创建它。发往那个更大对象的所有消息都要经过替身，因此对程序的其余部分来说，替身和那个更大的对象就是同一个东西。

尽管转发模仿了继承，`NSObject` 类却从不把两者混为一谈。像 `respondsToSelector:` 和 `isKindOfClass:` 这样的方法只查看继承体系，绝不查看转发链。举例来说，如果去问一个 Warrior 对象它是否响应 `negotiate` 消息，

```objc
if ( [aWarrior respondsToSelector:@selector(negotiate)] )
    ...
```

答案是 `NO`，即便它能够毫无错误地接收 `negotiate` 消息，并且在某种意义上通过把它们转发给 Diplomat 做出了响应。（参见 [图 5-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danbyfvbuqmjqguwtqnztge3q)。）

在许多情况下，`NO` 是正确的答案。但也未必总是如此。如果你用转发来搭建一个替身对象，或者用它来扩展某个类的能力，那么转发机制大概应该像继承那样透明。如果你希望自己的对象表现得就像真的继承了它们所转发消息的目标对象的行为，你就需要重新实现 `respondsToSelector:` 和 `isKindOfClass:` 方法，把你的转发算法也纳入其中：

```objc
- (BOOL)respondsToSelector:(SEL)aSelector
{
    if ( [super respondsToSelector:aSelector] )
        return YES;
    else {
        /* 在这里判断 aSelector 消息能否被转发给          *
         * 另一个对象，以及那个对象能否响应它。           *
         * 如果可以，就返回 YES。                         */
    }
    return NO;
}
```

除了 `respondsToSelector:` 和 `isKindOfClass:` 之外，`instancesRespondToSelector:` 方法也应当反映转发算法。如果用到了协议，`conformsToProtocol:` 方法同样应该加入这个名单。类似地，如果一个对象会转发它收到的任何远程消息，它就应该有一个版本的 `methodSignatureForSelector:`，能够返回对最终响应被转发消息的那些方法的准确描述；例如，如果某个对象能把消息转发给它的替身，你就应当像下面这样实现 `methodSignatureForSelector:`：

```objc
- (NSMethodSignature*)methodSignatureForSelector:(SEL)selector
{
    NSMethodSignature* signature = [super methodSignatureForSelector:selector];
    if (!signature) {
       signature = [surrogate methodSignatureForSelector:selector];
    }
    return signature;
}
```

你可以考虑把转发算法放在某处的私有代码里，让上述所有方法（包括 `forwardInvocation:`）都去调用它。

本节提到的方法都记录在 Foundation 框架参考中的 [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject) 类说明里。关于 `invokeWithTarget:` 的信息，参见 Foundation 框架参考中的 [NSInvocation](https://developer.apple.com/documentation/foundation/nsinvocation) 类说明。

[下一页](Type%20Encodings.md)[上一页](Dynamic%20Method%20Resolution.md)

