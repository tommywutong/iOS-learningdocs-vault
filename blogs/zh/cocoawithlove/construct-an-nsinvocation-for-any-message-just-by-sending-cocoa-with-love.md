---
title: '仅凭发送消息，为任意消息构造 NSInvocation | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/03/construct-nsinvocation-for-any-message.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:77c5ac28ecd1d29a'
translated: true
---

> 原文：[Construct an NSInvocation for any message, just by sending | Cocoa with Love](https://www.cocoawithlove.com/2008/03/construct-nsinvocation-for-any-message.html)　·　Cocoa with Love (Matt Gallagher)

我将向你展示如何利用对象转发（forwarding），仅仅通过向对象发送消息，就把任意消息记录到一个 NSInvocation 里。与别处展示的技巧不同，这种做法能让你记录任何消息，包括 NSObject 的消息，甚至包括转发消息本身。

## 构造 NSInvocation 是件痛苦的事

本文看起来是我正在写的 Cocoa 临时系列（ad hoc series）的第二篇。如果是的话，这个系列的标题也许可以叫：

> 用一行代码在 Cocoa 里把棘手的事情简单做

推荐你看我早先的文章[Core Data：一行获取](https://www.cocoawithlove.com/2008/03/core-data-one-line-fetch.html)，我在里面展示了用一行代码完成 Core Data 获取，而不是建议采用的 10 行通用写法。

NSInvocation 有非常类似的问题：用默认方法写出的最短用法也要 4 行，常见情形则接近 6 行。

所以，我要把它压缩成 1 行（复合语句），并让代码在概念上也更干净。

## 用默认方法创建 NSInvocation

根据 Apple 文档页面[分布式对象编程主题：使用 NSInvocation](http://developer.apple.com/documentation/Cocoa/Conceptual/DistrObjects/Tasks/invocations.html)的说明，要为 MyCalendar 方法创建一个调用（invocation）：

```objc
– (BOOL)updateAppointmentsForDate:(NSDate *)aDate
```

目标与参数分别是：

```objc
MyCalendar *userDatebook;    /* 假定它已存在。 */
NSDate *todaysDate;          /* 假定它已存在。 */
```

将需要如下代码：

```objc
SEL theSelector;
NSMethodSignature *aSignature;
NSInvocation *anInvocation;
 
theSelector = @selector(updateAppointmentsForDate:);
aSignature = [MyCalendar instanceMethodSignatureForSelector:theSelector];
anInvocation = [NSInvocation invocationWithMethodSignature:aSignature];
[anInvocation setSelector:theSelector];
[anInvocation setTarget:userDatebook];
[anInvocation setArgument:&todaysDate atIndex:2];
```

这不是最庞大、最笨重的代码块，但为了包装一次方法调用，它确实显得有点长。

显然，你可以只把 theSelector、目标 userDatebook 和所有参数（放在一个以 nil 结尾的可变参数列表里）传给一个构造方法。我以前见过这种做法。它能让代码整洁许多，但它假定了你的所有参数都不是 nil。它构造出的方法调用也很笨拙、缺乏结构。

## 消息转发

先剧透一下结局：我要展示一种把这一整段代码砍到一行的方法。就像这样：

```objc
NSInvocation *anInvocation;
[[NSInvocation invocationWithTarget:userDatebook invocationOut:&anInvocation]
    updateAppointmentsForDate:todaysDate];
```

这种做法最大的优点是：你像平常一样发送 updateAppointmentsForDate: 消息，带着参数。

这并不是什么革命性的概念。Cocoa 的设计者们在 NSUndoManager 类里用到了一种类似但更受限的技巧。出自 Apple 的[撤销架构：注册撤销操作](http://developer.apple.com/documentation/Cocoa/Conceptual/UndoArchitecture/Tasks/RegisteringUndo.html)：

```objc
[[myUndoManager prepareWithInvocationTarget:drawObject]
    setFont:[drawObject font] color:[drawObject color]];
```

这就是针对下面这条消息的 1 行版 NSInvocation 创建：

```objc
[drawObject setFont:[drawObject font] color:[drawObject color]]
```

这个 NSInvocation 并不会返回给调用函数（它由 NSUndoManager 内部持有），但它确实是在创建这个 NSInvocation 供自己内部使用——仅仅靠记录那条未被处理的消息。

它依赖于这两个 Objective-C 方法：

- - (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector
- - (void)forwardInvocation:(NSInvocation *)anInvocation

来捕获发送给对象、而对象自身又不处理的任何消息，并保存 anInvocation 参数。

这是一个非常好的方案，但它无法应付所有情形。它只能让你捕获对象尚未自行处理的消息。NSUndoManager 无法处理 NSObject 的实例方法，也无法处理任何 NSUndoManager 自己的实例方法。

例如，NSUndoManager 无法为下面这些方法创建 NSInvocation：

- init
- class
- release

或任何其他 NSObject 或 NSUndoManager 方法，因为它本身已经有这些方法了。就算我们创建一个不继承自 NSObject 的类，它仍然无法用这种办法为下面两个方法创建 NSInvocation：

- methodSignatureForSelector:
- forwardInvocation:

因为转发系统无法自动捕获并转发它自己的方法。

## 如何捕获任何消息

捕获任何消息的诀窍在于：把要捕获的消息发送给一个只响应下面两个方法的对象：

- - (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector
- - (void)forwardInvocation:(NSInvocation *)anInvocation

而对这两个方法本身，对象必须能够区分被转发的消息（此时只需保存 anInvocation 参数）与直接发送给这两个方法的消息（此时必须手动构造一个 NSInvocation）。

通过在这两种情形下区分“转发”与“直接调用”，我们就能为任何有效消息构建 NSInvocation。

## 总体思路

把所有步骤概括起来，我们需要：

1. 一个不继承自任何其他类的基类（base class）
2. 实例方法只有：

    - - (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector
    - - (void)forwardInvocation:(NSInvocation *)anInvocation

  其余工作都必须通过类方法完成。
3. 一种区分“经 methodSignatureForSelector: 转发的消息”与“直接调用 methodSignatureForSelector:”的办法
4. 一种区分“经 forwardInvocation: 转发的消息”与“直接调用 forwardInvocation:”的办法

第 1、2 步是直白的类构建。分配一个基类有点少见，但并不困难。

第 4 步可以这样完成：在方法内部检查 anInvocation 参数的“目标（target）”是否等于 self 参数。如果相等，就是直接调用；否则是被转发的消息。

第 3 步更棘手一些。无论是常规调用还是被转发的调用，传入的参数都没有区别。为此，我们得用一点更“脏”的手段：我们可以在受控的情形下，故意发送一条未被处理的消息（它会走转发代码），并记录下返回地址（return address）。把这个已知的返回地址登记到转发代码里，我们就能把后续被转发的调用与直接调用区分开。返回地址可以用一个 gcc 内建函数获得——[我以前用过它](https://www.cocoawithlove.com/2008/02/imp-of-current-method.html)——__builtin_return_address(0)。

当然，并不能绝对保证不会出现穿过转发代码的多条路径（那会带来不同的返回地址）。出于这个原因，我们会采用一种容忍错误的方案。由于被转发的调用总是先调用 methodSignatureforSelector: 再调用 forwardInvocation:，即使出现了误判为直接调用的情况，我们之后也可以用覆盖结果的方式加以纠正。

## 解决方案

我们有一个结构如下的分类：

```objc
@interface NSInvocation (ForwardedConstruction)

+ (id)invocationWithTarget:(id)target
    invocationOut:(NSInvocation **)invocationOut;
+ (id)retainedInvocationWithTarget:(id)target
    invocationOut:(NSInvocation **)invocationOut;

@end
```

它们既是我们的入口，也是出口。invocationOut 参数只会在要记录的消息发送 _之后_ 才被设置。

返回的 id 实际上是下面这个类的实例：

```objc
@interface InvocationProxy
{
    Class isa;
    NSInvocation **invocation;
    id target;
    BOOL retainArguments;
    NSUInteger forwardingAddress;
}

+ (id)alloc;
+ (void)setValuesForInstance:(InvocationProxy *)instance
    target:(id)target
    destinationInvocation:(NSInvocation **)destinationInvocation
    retainArguments:(BOOL)retain;
- (NSMethodSignature *)methodSignatureForSelector:(SEL)aSelector;
- (void)forwardInvocation:(NSInvocation *)forwardedInvocation;

@end
```

这就是我们特殊的基类。它自己处理自己的 alloc。它还要求在分配之后向它发送 init（尽管这个类并没有实现 init），以便记录消息转发的返回地址。

setValues... 方法会配置好这个实例，使得发送给它的下一条消息的调用会被记录并存入 destinationInvocation；而两个实例方法 methodSignatureForSelector: 和 forwardInvocation: 则按前文所述完成捕获被转发消息的工作。

实现里还有一个私有声明的类，名叫 DeallocatorHelper。使用这个类是因为 InvocationProxy 没有 autorelease、release 或 dealloc 方法，却又需要由 NSAutoreleasePool 来释放。于是我们改为创建 DeallocatorHelper 并将其放入自动释放池（autorelease pool），由它在自己的 dealloc 方法里释放 InvocationProxy。在垃圾回收（garbage collection）下编译时，这部分代码全部被 #ifdef 排除。

## 结语

代码在这里获取：[NSInvocationForwardedConstruction.zip](https://www.cocoawithlove.com/assets/objc-era/NSInvocationForwardedConstruction.zip)（4kb）

它能让你像下面这样创建 NSInvocation：

```objc
NSInvocation *anInvocation;
[[NSInvocation invocationWithTarget:target invocationOut:&anInvocation]
    methodParam1:argument1
    methodParam2:argument2
    methodParam3:argument3
    methodParam4:argument4];
```

适用于任何方法，无论参数的数量与类型如何，参数值只要是有效的都可以。如果你想让 NSInvocation 保留（retain）其参数，就调用 retainedInvocationWithTarget:invocationOut:。

如果你想为某个选择器（selector，例如 aSelector）而不是方法创建 NSInvocation，且参数已知，可以像下面这样调用：

```objc
NSInvocation *invocation;
id proxy = [NSInvocation invocationWithTarget:target invocationOut:&invocation];
objc_msgSend(proxy, aSelector, argument1, argument2, argument3, argument4);
```

对于返回结构体或 double 的方法，你需要分别改用 objc_msgSend_stret 或 objc_msgSend_fpret 来代替 objc_msgSend。
