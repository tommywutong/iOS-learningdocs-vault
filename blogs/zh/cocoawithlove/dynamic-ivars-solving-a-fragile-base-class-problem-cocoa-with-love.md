---
title: '动态 ivar：解决一个脆弱基类问题 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/03/dynamic-ivars-solving-fragile-base.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:d624cb1238af7fe9'
translated: true
---

> 原文：[Dynamic ivars: solving a fragile base class problem | Cocoa with Love](https://www.cocoawithlove.com/2010/03/dynamic-ivars-solving-fragile-base.html)　·　Cocoa with Love (Matt Gallagher)

在“现代”（modern）Objective-C 运行时（也就是 iPhone OS 或 64 位 Mac OS X）中，你可以动态地给类添加 ivar（instance variable，实例变量）而不必事先声明它们。这为常见的“脆弱基类（fragile base class）”问题中涉及 ivar 布局的那一类提供了一种解法。动态 ivar 还有助于数据隐藏和抽象，甚至能制造出一种令人困惑的情形：基类和子类各自拥有同名的 ivar，但它们并不指向同一份底层数据。

## 引言

本文讨论 Objective-C 中的动态 ivar。动态 ivar 的存在是为了解决一类常见的脆弱基类问题，具体来说，就是 ivar 布局（ivar layout）问题。

[脆弱基类](http://en.wikipedia.org/wiki/Fragile_base_class)问题指的是：对基类的微小改动就可能弄坏子类的情形。ivar 布局问题是一种脆弱基类问题：只要往基类里添加一个 ivar，所有子类就得重新编译。

涉及 ivar 布局的脆弱基类问题之所以会出现，是因为访问一个 ivar 需要把该 ivar 在对象内的偏移量加到对象指针上。由于子类的 ivar 总是排在基类的 ivar 之后，指向子类 ivar 的偏移量必然等于基类 ivar 区域的总大小加上它们自己的相对偏移。由于这些偏移量在传统上是固定的、编译期之后不可更改，这意味着：只要改变了基类 ivar 区域的总大小，就必须重新编译所有子类来更新它们的 ivar 偏移量。

现实是：在大多数面向对象语言里（包括还没有动态 ivar 时的 Objective-C），在保持向后二进制兼容（backwards binary compatibility）的同时给既有类添加 ivar，几乎是不可能的。

Objective-C 加上 Objective-C 现代运行时，是少数解决了这个问题的编译型语言环境之一。

> **_动态_并不意味着“随时”**：我说的动态，是指 ivar 的绝对布局在编译期并不可知。确切地说，我说的是从子类的视角看会动态出现的 ivar（对基类而言，它们看起来就像普通 ivar）。虽然额外的 ivar 可以在运行时添加到类上，但只能在类对（class pair）注册之前添加（也就是在类还没有任何实例之前）。更多信息参见 [Apple 关于 class_addIvar 的文档](http://developer.apple.com/mac/library/documentation/Cocoa/Reference/ObjCRuntimeRef/Reference/reference.html#//apple_ref/c/func/class_addIvar)。

## ivar 布局的脆弱基类问题

让我们通过一个例子，看看 ivar 布局的脆弱基类问题会造成什么麻烦。

### 给基类添加一个 ivar 会弄坏所有子类

设想这样一个例子：某个动态库的作者（例如编写 Mac OS X 或 iPhone OS Cocoa 库的 Apple）发布了一个允许被派生子类的类：

```objc
@interface LibraryBaseObject : NSObject
{
    NSString *baseObjectIVar;
}
@end
```

这个库类的使用者随后基于基类做出自己的子类：

```objc
@interface UserSubObject : LibraryBaseObject
{
    NSString * userSubObjectIVar;
}
@end
```

一切都相安无事，直到库的作者想给 LibraryBaseObject 添加一个需要额外 ivar 的新功能：

```objc
@interface LibraryBaseObject : NSObject
{
    NSString *baseObjectIVar;
    id newFeatureObject;
}
@end
```

按照传统做法，这会弄坏 `LibraryBaseObject` 的每一个既有子类，因为没有任何既有子类分配了足够的内存来容纳这个新 ivar，而且指向 `userSubObjectIVar` 的偏移量也会出错——这些偏移量在编译时纳入的是 `NSObject` + `LibraryBaseObject` 的旧实例内存大小，如今会偏移一个错误的量。

是的，代码当然可以用新头文件重新编译，所有偏移量会自动修正为新值，但在重新编译之前，所有以子类化方式使用 `LibraryBaseObject` 的既有程序都会出问题。

> Greg Parker 的 _Hamster Emporium: [objc explain]_ 有一篇好文章，题为[非脆弱 ivar（Non-fragile ivars）](http://www.sealiesoftware.com/blog/archive/2009/01/27/objc_explain_Non-fragile_ivars.html)，里面有更多展示 ivar 布局问题的图示。

### 脆弱基类问题以前的权宜之计

针对 ivar 布局的脆弱基类问题，常见的权宜之计是像这样声明你的类：

```objc
@interface LibraryBaseObject : NSObject
{
    id private;
}
@end
```

然后把所有数据实际存储在私有的类里，你可以在不影响真正的 ` LibraryBaseObject ` 的情况下改变它的大小，因为这个私有 ivar 永远只占一个指针的大小。

不过，这带来了三个问题：

- 你必须从一开始就有先见之明，把这个 `private` 指针放进去
- 它涉及两次解引用（dereference）——参见下文的性能注记，我在其中解释了解引用是 ivar 访问中最慢的部分
- 在这种无类型的场景下它很难用：所有代码在使用前都必须把这个 `private` ivar 转换成它的实际类。你可以前向声明一个 `@class` 并改用它，以消除这个麻烦。

## 要修复问题，必须让某个编译期数值变成动态的

前面我说过，我们访问一个 ivar 的方式是：

1. 把该 ivar 在对象内的偏移量加到对象的指针值上
2. 解引用（从偏移指针值所指的内存位置读取或写入）

自 Algol 时代以来的任何程序员都不该对此感到陌生：在大多数编译型语言里，访问 `struct`、记录或实例变量中的数据，走的都是这条路子。

问题在于：任何子类的 ivar 偏移量都必须包含基类 ivar 区域的总大小，而这一切在运行时都无法改变。

显然，要解决问题，必须有东西在运行时是可变的。Objective-C 的现代运行时的修法，是把“基类 ivar 区域的大小”变成一个可以在运行时查到的值。

因此，“现代”Objective-C 运行时要求访问 ivar 改用下面这个修订过的流程：

1. 把子类实例值区域的偏移量加到对象的指针值上
2. 加上从子类实例区域到该 ivar 的偏移量
3. 解引用（从偏移指针值所指的内存位置读取或写入）

这样一来，基类的 ivar 区域就可以增长，子类的偏移量会随之移动以适应变化。

> **现代运行时中所有 ivar 都是动态的**：既然所有 ivar 都走这套流程，那就意味着现代 Objective-C 运行时里的所有 ivar 都是动态的——它们的绝对偏移量在编译期永远不可知。

### 性能注记

你可能担心“现代”运行时会让一件非常常见的任务（访问 ivar）变慢。

没错，额外的偏移量确实可能拖慢一些代码，但对大多数代码而言，现实是这个差异小到无法测量。

理论上，如果额外的偏移量需要从描述类 ivar 布局的结构体里取，新方案可能让耗时翻倍。不过，当前子类的偏移量通常已经存放在 `rip` 寄存器里，这个寄存器正是为这种双重偏移解引用设计的，可能把额外偏移的影响降到零。即便真的需要额外的一个周期来加偏移，速度影响也最多 20%（假定 ivar 位于 L1 缓存：1 个周期的影响，对比在较新的 Intel CPU 上仅从 L1 取值就要 4 个周期）；对 L2 不足 10%（那里取值要 10 个周期）；对主存访问约 1%。

除此之外，编译器本来就会消除不必要的解引用，对同一个 ivar 的多次访问会被优化，使这个额外偏移只出现一次。

## 合成 ivar

下一个问题是：我们如何利用这一点，给一个已经定型的既有类添加额外的 ivar？现实是：既然现代运行时里所有 ivar 都是动态的，你直接往基类里加额外的 ivar 就行，不会给既有子类带来任何问题。

但动态 ivar 还带来了另一种创建 ivar 的方式，对既有类的干扰更小，因为它完全不需要改头文件——你可以使用一个没有匹配 ivar 的合成属性（synthesized property）。这会在实现里创建一个额外的 ivar，它不会出现在其他类看到的声明里。

例如，从下面这个类开始：

```objc
@interface MyIvarlessObject : NSObject
{
}
@end
```

你可以把声明改成这样来添加动态 ivar：

```objc
@interface MyIvarlessObject : NSObject
{
}
@property (nonatomic, copy) NSString *myProperty;
@property (nonatomic, copy) NSString *anotherProperty;
@end
```

并在实现里加上：

```objc
@synthesize myProperty=myIvar; // 将生成名为 myIvar 的动态 ivar
@synthesize anotherProperty;   // 将生成名为 anotherProperty 的动态 ivar
```

由于 `myIvar` 和 `anotherProperty` 都没有匹配的 ivar，`@synthesize` 语句会为它们各生成一个动态 ivar，而这条 `@synthesize` 语句本身就成了这些 ivar 的声明。

由于 `@synthesize` 语句起到了声明的作用，你现在可以在实现里引用 `myIvar` 或 `anotherProperty`，就像它们是普通声明过的 ivar 一样。例如，你可以写：

```objc
- (id)init
{
    self = [super init];
    if (self)
    {
        myIvar = [[NSString alloc] initWithString:@"someString"];
        anotherProperty = [[NSString alloc] initWithString:@"someOtherString"];
    }
    return self;
}
```

如果你想把属性声明隐藏起来，或者完全不想动头文件，可以改在实现文件里用一个私有分类来声明这些属性，而不是放在接口文件里：

```objc
@interface MyIvarlessObject ()
@property (nonatomic, copy) NSString *myProperty;
@property (nonatomic, copy) NSString *anotherProperty;
@end
```

它需要放在 `MyIvarlessObject` 实现块的上方。

## 同名的多个 ivar

设想有下面这个基类：

```objc
@interface BaseObject : NSObject
{
}
@property (nonatomic, copy) NSString *propertyOne;
@end

@implementation BaseObject
@synthesize propertyOne=myIvar;
@end
```

以及一个子类：

```objc
@interface SubObject : BaseObject
{
}
@property (nonatomic, copy) NSString *propertyTwo;
@end

@implementation SubObject
@synthesize propertyTwo=myIvar;
@end
```

这个基类和子类都 `@synthesize` 了一个名为 `myIvar` 的 ivar。

一个有点罕见的怪癖是：`BaseObject` 里的 `myIvar` 和 `SubObject` 里的 `myIvar` 并不是同一个值——它们实际上是两个不同的 ivar，在实例内存区域里有着不同的偏移量。

需要这个怪癖，是为了妥善处理另一个脆弱基类问题：如果 `@synthesize` 出来的 ivar 可能与子类的 ivar 冲突，那基类的 ivar 就依然是脆弱的。为了支持这一设计，`@synthesize` 出来的 ivar 总是 `@private` 的。

不过，这并不意味着它们被限制在 `@implementation` 的作用域内。你可以在分类实现里访问它们，前提是这个分类位于合成该 ivar 的 `@implementation` 之下，因而能看到那份隐式声明。

这也意味着，如果 `BaseObject` 和 `SubObject` 实现在同一个文件里，它们将无法通过编译。为什么？因为如果实现在同一个文件里，`SubObject` 就会看到来自其超类 `BaseObject` 的 `myIvar` 隐式声明，进而试图直接使用它而不是合成自己的 ivar，最终因为 `BaseObject` 的 `myIvar` 是 `@private` 而失败。

## 结语

往自己的类里添加 ivar 时，你通常不必担心 ivar 布局问题。只有当你在编写或更新动态库、并且想要维持向后二进制兼容时，这才是一个需要关心的问题。

动态 ivar 是“现代”运行时的特性；如果你的目标是 32 位 Mac OS X，则不支持它们。

对其他 Cocoa 平台来说，你想用 `@synthesize` 生成 ivar 的理由有很多：

- 它们很方便（不需要 ivar 声明，只需要属性声明）。
- 与 `@private` 声明相比，它们对子类隐藏信息的能力更强，因为它们不公开声明任何东西。
- 你可以把它们加到基类上，而不需要重新编译子类。

动态 ivar 确实要在运行时付出额外指针偏移的代价，但无论你用不用它们，这笔代价你都已经在付了（它是 iPhone OS 和 64 位 Mac OS X Objective-C 运行时的必备组成部分）。无论如何，你几乎不可能察觉到这笔开销。
