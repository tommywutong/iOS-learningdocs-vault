---
title: Objective-C 运行时编程指南
apple_id: TP40008048
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtHowMessagingWorks.html
archived_at: '2026-07-15T07:17:28.874604Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 运行时编程指南](Introduction.md)


[下一页](Dynamic%20Method%20Resolution.md)[上一页](Interacting%20with%20the%20Runtime.md)

# 消息传递

本章介绍消息表达式是如何被转换成 [objc_msgSend](https://developer.apple.com/documentation/objectivec/1456712-objc_msgsend) 函数调用的，以及你如何按名称引用方法。随后会说明如何利用 `objc_msgSend`，以及——在确有需要时——如何绕过动态绑定。

在 Objective-C 中，消息直到运行时才与方法实现绑定。编译器会把一条消息表达式，

```objc
[receiver message]
```

转换成对消息传递函数 [objc_msgSend](https://developer.apple.com/documentation/objectivec/1456712-objc_msgsend) 的调用。该函数以消息的接收者和消息中提到的方法名称——也就是方法选择器——作为它的两个主要参数：

```c
objc_msgSend(receiver, selector)
```

消息中传递的任何参数也会一并交给 `objc_msgSend`：

```c
objc_msgSend(receiver, selector, arg1, arg2, ...)
```

这个消息传递函数完成了动态绑定所需的一切工作：

- 它首先找到选择器所指向的过程（即方法实现）。由于同一个方法可以由不同的类以不同的方式实现，它究竟找到哪个过程取决于接收者的类。
- 然后它调用该过程，把接收消息的对象（一个指向其数据的指针）以及为该方法指定的所有参数传递给它。
- 最后，它把该过程的返回值作为自己的返回值传出。

消息传递的关键在于编译器为每个类和对象所构建的那些结构。每个类结构都包含以下两个基本要素：

- 一个指向超类的指针。
- 一张类的 _分发表_（dispatch table）。这张表中的条目把方法选择器与它们所标识的方法在该类中的具体地址关联起来。`setOrigin::` 方法的选择器与（实现 `setOrigin::` 的过程的）地址关联，`display` 方法的选择器与 `display` 的地址关联，以此类推。

当一个新对象被创建时，会为它分配内存，并初始化它的实例变量。该对象的变量中排在最前面的是一个指向其类结构的指针。这个指针名为 `isa`，它让对象能够访问自己的类，并通过这个类访问它所继承的所有类。

类结构与对象结构的这些要素如图 3-1 所示。

__图 3-1__  消息传递框架

!

当一条消息被发送给某个对象时，消息传递函数会沿着该对象的 `isa` 指针找到类结构，并在其分发表中查找方法选择器。如果在那里找不到该选择器，`objc_msgSend` 就沿着指向超类的指针继续在超类的分发表中查找。一次次查找失败会使 `objc_msgSend` 沿类层次结构一路向上，直至到达 `NSObject` 类。一旦定位到该选择器，函数就调用表中登记的那个方法，并把接收消息对象的数据结构传给它。

这就是方法实现在运行时被选定的方式——用面向对象编程的行话来说，就是方法被动态绑定到消息上。

为了加快消息传递过程，运行时系统会在方法被使用时缓存其选择器和地址。每个类都有一份独立的缓存，其中既可以包含该类自身定义方法的选择器，也可以包含继承来的方法的选择器。在搜索分发表之前，消息传递例程会先检查接收消息对象所属类的缓存（其依据是：用过一次的方法很可能会再次被用到）。如果方法选择器就在缓存中，那么消息传递只比一次函数调用略慢一点。程序运行足够长时间把缓存“预热”之后，它发出的几乎所有消息都能命中缓存中的方法。随着程序运行，缓存会动态增长以容纳新的消息。

当 [objc_msgSend](https://developer.apple.com/documentation/objectivec/1456712-objc_msgsend) 找到实现某方法的过程时，它会调用该过程，并把消息中的所有参数传给它。它还会向该过程传入两个隐藏参数：

- 接收消息的对象
- 该方法的选择器

这两个参数向每一个方法实现明确提供了调用它的那条消息表达式的两个组成部分的信息。之所以说它们是“隐藏”的，是因为它们并未在定义该方法的源代码中声明。它们是在代码编译时被插入到实现中的。

尽管这些参数没有显式声明，源代码仍然可以引用它们（就像可以引用接收消息对象的实例变量一样）。方法用 `self` 引用接收消息的对象，用 `_cmd` 引用自己的选择器。在下面的示例中，`_cmd` 指向 `strange` 方法的选择器，`self` 指向接收 `strange` 消息的那个对象。

```objc
- strange
{
    id  target = getTheReceiver();
    SEL method = getTheMethod();

    if ( target == self || method == _cmd )
        return nil;
    return [target performSelector:method];
}
```

两个参数中 `self` 更为有用。实际上，正是通过它，接收消息对象的实例变量才得以在方法定义中可用。

绕过动态绑定的唯一办法是取得某个方法的地址，然后像调用函数那样直接调用它。在少数情况下这样做是合适的：某个特定方法要连续执行很多次，而你想避免每次执行时的消息传递开销。

借助 `NSObject` 类中定义的一个方法 `methodForSelector:`，你可以请求得到实现某个方法的过程的指针，然后用这个指针调用该过程。`methodForSelector:` 返回的指针必须小心地强制转换成正确的函数类型。返回值类型和参数类型都应包含在这个类型转换中。

下面的示例展示了如何调用实现 `setFilled:` 方法的那个过程：

```objc
void (*setter)(id, SEL, BOOL);
int i;

setter = (void (*)(id, SEL, BOOL))[target
    methodForSelector:@selector(setFilled:)];
for ( i = 0 ; i < 1000 ; i++ )
    setter(targetList[i], @selector(setFilled:), YES);
```

传给该过程的头两个参数是接收消息的对象（`self`）和方法选择器（`_cmd`）。这两个参数在方法语法中是隐藏的，但当把方法当作函数来调用时就必须显式写出。

用 `methodForSelector:` 绕过动态绑定可以省下消息传递所需的大部分时间。不过，只有当某条特定消息被重复很多次时，这种节省才会显著，比如上面展示的 `for` 循环。

请注意，`methodForSelector:` 由 Cocoa 运行时系统提供，它并不是 Objective-C 语言本身的特性。

[下一页](Dynamic%20Method%20Resolution.md)[上一页](Interacting%20with%20the%20Runtime.md)

