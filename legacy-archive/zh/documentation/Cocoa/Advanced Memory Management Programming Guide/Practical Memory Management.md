---
title: 高级内存管理编程指南
apple_id: 10000011i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Performance
technology: Foundation
published: '2012-07-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmPractical.html
archived_at: '2026-07-15T07:16:40.632649Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [高级内存管理编程指南](About%20Memory%20Management.md)


[下一页](Using%20Autorelease%20Pool%20Blocks.md)[上一页](Memory%20Management%20Policy.md)

# 内存管理实践

虽然[内存管理策略](Memory%20Management%20Policy.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe4tilkciffeqrsci5ea)中描述的基本概念很简单，但仍有一些实用的做法可以让内存管理更轻松，并帮助你在把资源需求降到最低的同时，确保程序保持可靠、健壮。

如果你的类有一个对象类型的属性，你必须确保被设置为该属性值的对象不会在你使用它期间被释放。因此，你必须在它被设置进来时取得它的所有权。同时你还必须放弃当前持有的那个值的所有权。

有时候这看上去繁琐或者迂腐，但只要你始终如一地使用存取方法（accessor），出现内存管理问题的几率就会大幅下降。如果你在代码中到处对实例变量直接使用 `retain` 和 `release`，那你几乎可以肯定是做错了。

考虑一个 Counter 对象，你希望设置它的计数值。

```objc
@interface Counter : NSObject
@property (nonatomic, retain) NSNumber *count;
@end;
```

这个[属性](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13)声明了两个存取方法。通常你应该让编译器来合成这两个方法；不过，看看它们可能是如何实现的仍然很有启发。

在“get”存取方法中，你只需返回合成出来的实例变量，因此不需要 `retain` 或 `release`：

```objc
- (NSNumber *)count {
    return _count;
}
```

在“set”方法中，如果其他人都按同样的规则行事，那么你必须假定新的 count 对象随时可能被处置掉，所以你必须取得该对象的所有权——向它发送 `retain` 消息——以确保它不会被处置。你还必须在这里向旧的 count 对象发送 `release` 消息，放弃它的所有权。（在 Objective-C 中允许向 `nil` 发送消息，所以即便 `_count` 尚未被设置过，这个实现依然能正常工作。）这条 `release` 必须放在 `[newCount retain]` 之后发送，以防这两者是同一个对象——你可不想一不小心把它给释放掉。

```objc
- (void)setCount:(NSNumber *)newCount {
    [newCount retain];
    [_count release];
    // 进行新的赋值。
    _count = newCount;
}
```


假设你想实现一个方法来重置计数器。有几种做法可供选择。第一种实现用 `alloc` 创建 `NSNumber` 实例，因此你要用一次 `release` 与之配平。

```objc
- (void)reset {
    NSNumber *zero = [[NSNumber alloc] initWithInteger:0];
    [self setCount:zero];
    [zero release];
}
```

第二种实现使用便利构造方法来创建新的 `NSNumber` 对象。因此不需要 `retain` 或 `release` 消息

```objc
- (void)reset {
    NSNumber *zero = [NSNumber numberWithInteger:0];
    [self setCount:zero];
}
```

注意这两种实现都使用了 set 存取方法。

下面这种写法在简单情形下几乎肯定能正确工作，但无论绕开存取方法看起来多么诱人，这么做几乎肯定会在某个阶段引出错误（例如当你忘了 retain 或 release，或者该实例变量的内存管理语义发生变化时）。

```objc
- (void)reset {
    NSNumber *zero = [[NSNumber alloc] initWithInteger:0];
    [_count release];
    _count = zero;
}
```

另外还要注意，如果你使用[键值观察](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KVO.html#//apple_ref/doc/uid/TP40008195-CH16)，那么以这种方式改变变量是不符合 KVO 规范的。

唯一不应该使用存取方法来设置实例变量的地方，是[初始化方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MultipleInitializers.html#//apple_ref/doc/uid/TP40008195-CH33)和 `dealloc`。要用一个表示零的数字对象来初始化 counter 对象，你可以像下面这样实现 `init` 方法：

```objc
- init {
    self = [super init];
    if (self) {
        _count = [[NSNumber alloc] initWithInteger:0];
    }
    return self;
}
```

要允许用零以外的计数值来初始化 counter，你可以像下面这样实现 `initWithCount:` 方法：

```objc
- initWithCount:(NSNumber *)startingCount {
    self = [super init];
    if (self) {
        _count = [startingCount copy];
    }
    return self;
}
```

由于 Counter 类有一个对象类型的实例变量，你还必须实现 `dealloc` 方法。它应当向各个实例变量发送 `release` 消息以放弃其所有权，并且最后要调用超类的实现：

```objc
- (void)dealloc {
    [_count release];
    [super dealloc];
}
```


保留（retain）一个对象会创建对该对象的一个_强引用_（strong reference）。只有当一个对象的所有强引用都被释放之后，它才能被释放。因此，如果两个对象之间存在循环引用——也就是它们互相持有强引用（可以是直接持有，也可以是通过一条对象链，链上每个对象都对下一个持有强引用，最终又绕回第一个）——就会引发一个称为_保留循环_（retain cycle）的问题。

[图 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinbxfuytambqha3dmlkcijbuusski5ba) 中所示的对象关系就演示了一个潜在的保留循环。Document 对象为文档中的每一页各持有一个 Page 对象。每个 Page 对象都有一个属性用于记录自己属于哪个文档。如果 Document 对象对 Page 对象持有强引用，而 Page 对象又对 Document 对象持有强引用，那么这两个对象谁也无法被释放。在 Page 对象被释放之前，Document 的引用计数不可能降为零；而 Page 对象又要等到 Document 对象被释放之后才会被释放。

__图 1__  循环引用示意图

![保留循环示意图](attachments/Art/retaincycles_2x.png)

解决保留循环问题的办法是使用弱引用。_弱引用_（weak reference）是一种非拥有关系，源对象不会保留它所引用的那个对象。

不过，为了让对象图保持完整，某些地方必须存在强引用（如果全都是弱引用，那么这些页面和段落就可能没有任何拥有者，从而被释放掉）。为此，Cocoa 确立了一条约定：“父”对象应当对它的“子”对象持有强引用，而子对象应当对父对象持有弱引用。

因此，在[图 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dinbxfuytambqha3dmlkcijbuusski5ba) 中，document 对象对它的 page 对象持有强引用（即保留它们），而 page 对象对 document 对象持有弱引用（即不保留它）。

Cocoa 中弱引用的例子包括但不限于：表格数据源、大纲视图条目、[通知](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35)观察者，以及各种目标（target）和[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)。

向那些你只持有弱引用的对象发送消息时必须格外小心。如果你在某个对象已被释放之后还向它发送消息，应用程序就会崩溃。你必须为“该对象何时有效”定义明确的条件。在大多数情况下，被弱引用的那个对象知道另一个对象对它持有弱引用（循环引用的情形就是如此），并负责在自己被释放时通知对方。例如，当你把一个对象注册到通知中心时，通知中心会存储对该对象的弱引用，并在相应通知发布时向它发送消息。当该对象被释放时，你需要把它从通知中心注销，以防通知中心继续向这个已经不存在的对象发送消息。同样地，当一个委托对象被释放时，你需要向另一个对象发送参数为 `nil` 的 `setDelegate:` 消息，从而解除委托关联。这些消息通常是在该对象的 `dealloc` 方法中发送的。

Cocoa 的所有权策略规定，接收到的对象通常应当在调用方法的整个作用域内保持有效。你还应当能够把接收到的对象从当前作用域返回出去，而不必担心它被释放。对你的应用程序来说，某个对象的 getter 方法返回的是缓存的实例变量还是计算出来的值，本不该有任何影响。真正要紧的是，这个对象在你需要它的那段时间里保持有效。

这条规则偶尔会有例外，主要可归为两类。

1. 当一个对象被从某个基础[集合类](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10)中移除时。

```objc
heisenObject = [array objectAtIndex:n];
[array removeObjectAtIndex:n];
// heisenObject 现在可能已经无效了。
```

   当一个对象被从某个基础集合类中移除时，它收到的是 `release` 消息（而不是 `autorelease`）。如果该集合是被移除对象的唯一拥有者，那么被移除的对象（例子中的 `heisenObject`）就会被立即释放。
2. 当一个“父对象”被释放时。

```objc
id parent = <#create a parent object#>;
// ...
heisenObject = [parent child] ;
[parent release]; // 或者，例如：self.parent = nil;
// heisenObject 现在可能已经无效了。
```

   在某些情况下，你从另一个对象那里取得了一个对象，然后又直接或间接地释放了那个父对象。如果释放父对象导致它被销毁，而父对象又是该子对象的唯一拥有者，那么这个子对象（例子中的 `heisenObject`）也会同时被释放（前提是父对象的 `dealloc` 方法中向它发送的是 `release` 而不是 `autorelease` 消息）。

要防范这些情况，你应当在取得 `heisenObject` 时保留它，并在用完之后释放它。例如：

```objc
heisenObject = [[array objectAtIndex:n] retain];
[array removeObjectAtIndex:n];
// 使用 heisenObject……
[heisenObject release];
```


通常，你不应该在 `dealloc` 方法中管理文件描述符、网络连接、缓冲区或缓存这类稀缺资源。尤其不要把类设计成依赖于“`dealloc` 会在我预期的时刻被调用”。`dealloc` 的调用可能会被推迟，甚至被完全跳过，原因可能是某个 bug，也可能是应用程序正在拆解退出。

正确的做法是：如果某个类的实例管理着稀缺资源，那么你应当把应用程序设计成能明确知道自己何时不再需要这些资源，并在那个时刻告诉该实例去“清理”。之后你通常会释放这个实例，`dealloc` 随之被调用，但即便它没有被调用，也不会给你带来额外的麻烦。

如果你试图把资源管理搭载在 `dealloc` 之上，可能会出现以下问题。例如：

1. [对象图](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectGraph.html#//apple_ref/doc/uid/TP40008195-CH54)拆解过程中的顺序依赖。

   对象图的拆解机制本质上是无序的。虽然你通常会预期——而且也确实得到——某个特定的顺序，但这么做等于引入了脆弱性。举例来说，如果某个对象出乎意料地被自动释放而不是被释放，拆解顺序就可能改变，从而导致出人意料的结果。
2. 稀缺资源得不到回收。

   内存泄漏是应该修复的 bug，但通常不会立刻致命。然而，如果稀缺资源没有在你预期的时刻被释放，你可能会遇到更严重的问题。例如，如果应用程序把文件描述符耗尽了，用户可能就无法保存数据。
3. 清理逻辑在错误的线程上执行。

   如果某个对象在意料之外的时刻被自动释放，它就会在恰好包含它的那个自动释放池块所在的线程上被释放。对于那些只能在单一线程上访问的资源来说，这很容易造成致命后果。

当你把一个对象加入某个[集合](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10)（例如数组、字典或 set）时，该集合就取得了这个对象的所有权。当该对象被从集合中移除，或者集合本身被释放时，集合就会放弃所有权。因此，举例来说，如果你想创建一个数字数组，可以采用下面两种写法之一：

```objc
NSMutableArray *array = <#Get a mutable array#>;
NSUInteger i;
// ...
for (i = 0; i < 10; i++) {
    NSNumber *convenienceNumber = [NSNumber numberWithInteger:i];
    [array addObject:convenienceNumber];
}
```

在这种写法中，你并没有调用 `alloc`，所以不需要调用 `release`。也不需要保留这些新创建的数字（`convenienceNumber`），因为数组会替你保留它们。

```objc
NSMutableArray *array = <#Get a mutable array#>;
NSUInteger i;
// ...
for (i = 0; i < 10; i++) {
    NSNumber *allocedNumber = [[NSNumber alloc] initWithInteger:i];
    [array addObject:allocedNumber];
    [allocedNumber release];
}
```

在这种写法中，你_确实_需要在 `for` 循环的作用域内向 `allocedNumber` 发送 `release` 消息，以便与 `alloc` 配平。由于数组在 `addObject:` 把这个数字加进来时保留了它，所以只要它还在数组里，就不会被释放。

要理解这一点，不妨设身处地把自己当成实现这个集合类的人。你希望确保交给你保管的对象不会在你不知情的情况下消失，所以在它们被传进来时，你会向它们发送 `retain` 消息。如果它们被移除了，你就要发送一条配平的 `release` 消息；而在你自己的 `dealloc` 方法中，还要向所有剩下的对象发送 `release` 消息。

所有权策略是通过引用计数实现的——因为有 [retain](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/retain) 方法，它通常被称为“保留计数”（retain count）。每个对象都有一个保留计数。

- 当你创建一个对象时，它的保留计数为 1。
- 当你向一个对象发送 `retain` 消息时，它的保留计数加 1。
- 当你向一个对象发送 [release](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/release) 消息时，它的保留计数减 1。

  当你向一个对象发送 [autorelease](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/autorelease) 消息时，它的保留计数会在当前自动释放池块结束时减 1。
- 如果一个对象的保留计数降为零，它就会被释放。

[下一页](Using%20Autorelease%20Pool%20Blocks.md)[上一页](Memory%20Management%20Policy.md)

