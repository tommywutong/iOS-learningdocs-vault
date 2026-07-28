---
title: 方法调配
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/method-swizzling/'
original_language: en
published: 2014-02-17
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:6782577fffffd827'
translated: true
---

> 原文：[Method Swizzling](https://nshipster.com/method-swizzling/)　·　NSHipster (Mattt)

# [方法调配](https://nshipster.com/method-swizzling/)

作者：[Mattt](https://nshipster.com/authors/mattt/)　2014 年 2 月 17 日

> 假如轻轻一按就能引爆世界  
> 你会这么做吗？  
> 假如让你变得富有，代价是让所有人都陷入贫困  
> 你会这么做吗？  
> 假如你躺着无所事事，却能看着所有人辛苦劳作  
> 你会这么做吗？  
> 假如你只索取爱，从不需要回报  
> 你会这么做吗？  
> 所以我们无法真正了解自己，也不知道自己会怎么做……  
> 拥有如此力量……你会怎么做？  
> **烈焰红唇乐队（The Flaming Lips）**，_[《Yeah Yeah Yeah 之歌（凭借你全部的力量）》](https://en.wikipedia.org/wiki/The_Yeah_Yeah_Yeah_Song_(With_All_Your_Power))_

在上周关于[关联对象（associated objects）](https://nshipster.com/associated-objects/)的文章中，我们开始探索 Objective-C 运行时的暗黑艺术。本周，我们将更进一步，讨论运行时 hack 技术中最具争议的话题之一：方法调配（method swizzling）。

---

方法调配是改变现有选择器（selector）实现的过程。这项技术之所以可行，是因为 Objective-C 中的方法调用可以在运行时改变，通过更改选择器如何映射到类分发表中的底层函数来实现。

例如，假设我们想追踪 iOS App 中每个视图控制器向用户展示的次数：

每个视图控制器可以在自己的 `viewDidAppear:` 实现中添加追踪代码，但这会产生大量重复的样板代码。子类化是另一种可能性，但需要子类化 `UIViewController`、`UITableViewController`、`UINavigationController` 以及所有其他视图控制器类——这种方法同样存在代码重复的问题。

幸运的是，还有另一条路：在分类（category）中做**方法调配**。下面是具体做法：

```
#import <objc/runtime.h>

@implementation UIViewController (Tracking)

+ (void)load {
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        Class class = [self class];

        SEL originalSelector = @selector(viewWillAppear:);
        SEL swizzledSelector = @selector(xxx_viewWillAppear:);

        Method originalMethod = class_getInstanceMethod(class, originalSelector);
        Method swizzledMethod = class_getInstanceMethod(class, swizzledSelector);

        // 当调配类方法时，请使用以下代码：
        // Method originalMethod = class_getClassMethod(class, originalSelector);
        // Method swizzledMethod = class_getClassMethod(class, swizzledSelector);

        IMP originalImp = method_getImplementation(originalMethod);
        IMP swizzledImp = method_getImplementation(swizzledMethod);

        class_replaceMethod(class,
                swizzledSelector,
                originalImp,
                method_getTypeEncoding(originalMethod));
        class_replaceMethod(class,
                originalSelector,
                swizzledImp,
                method_getTypeEncoding(swizzledMethod));

    });
}

#pragma mark - Method Swizzling

- (void)xxx_viewWillAppear:(BOOL)animated {
    [self xxx_viewWillAppear:animated];
    NSLog(@"viewWillAppear: %@", self);
}

@end
```

现在，当 `UIViewController` 或其任何子类的实例调用 `viewWillAppear:` 时，都会打印出一条日志信息。

向视图控制器生命周期、响应者事件、视图绘制或 Foundation 网络栈中注入行为，都是方法调配可以发挥巨大作用的典型例子。还有许多其他场景也适合使用调配技术，随着 Objective-C 开发经验的增长，这些场景会变得越来越明显。

无论选择在 _何处_ 以及 _为何_ 使用调配，_如何_ 实现仍然是绝对关键的：

## +load 与 +initialize

**调配总应在 `+load` 中进行。**

对于每个类，Objective-C 运行时都会自动调用两个方法。`+load` 在类被初始加载时发送，而 `+initialize` 则在 App 首次对该类或其实例调用方法之前被调用。两者都是可选的，并且仅在方法被实现时才会执行。

由于方法调配会影响全局状态，因此尽可能减少竞争条件（race condition）的可能性至关重要。`+load` 保证在类初始化期间被加载，这为改变系统行为提供了一定程度的一致性。相比之下，`+initialize` 无法保证何时执行——事实上，如果 App 从未直接向该类发送消息，它可能 _永远_ 不会被调用。

## dispatch_once

**调配总应在 `dispatch_once` 中进行。**

再次强调，由于调配会改变全局状态，我们需要在运行时采取一切可用的预防措施。原子性（atomicity）是其中之一，同时还要确保代码只精确执行一次，即使跨多个线程也是如此。Grand Central Dispatch 的 `dispatch_once` 同时提供了这两种理想行为，它应当被视为方法调配的标准做法，就像用于[初始化单例（singleton）](https://nshipster.com/c-storage-classes/)一样。

## 选择器（Selector）、方法（Method）与实现（Implementation）

在 Objective-C 中，_选择器_、_方法_ 和 _实现_ 指向运行时的特定方面，不过在平常的交谈中，这些术语经常互换使用，泛指消息发送的过程。

以下是 Apple 的 [Objective-C 运行时参考](https://developer.apple.com/library/mac/documentation/Cocoa/Reference/ObjCRuntimeRef/Reference/reference.html#//apple_ref/c/func/method_getImplementation)中对它们的描述：

> - 选择器（`typedef struct objc_selector *SEL`）：选择器用于在运行时表示方法的名称。方法选择器是一个经过 Objective-C 运行时注册（或“映射”）的 C 字符串。编译器生成的选择器在类加载时由运行时自动映射。
> - 方法（`typedef struct objc_method *Method`）：一种不透明类型，表示类定义中的一个方法。
> - 实现（`typedef id (*IMP)(id, SEL, ...)`）：此数据类型是一个指向实现该方法的函数起始地址的指针。该函数采用当前 CPU 架构实现的标准 C 调用约定。第一个参数是指向 self 的指针（即该类特定实例的内存，或者对于类方法，指向元类的指针）。第二个参数是方法选择器。随后是方法参数。

理解这些概念之间关系的最佳方式如下：一个类（`Class`）维护着用于解决运行时消息发送的分发表；表中的每个条目都是一个方法（`Method`），它将一个特定的名称——选择器（`SEL`）——映射到一个实现（`IMP`），后者是一个指向底层 C 函数的指针。

调配方法就是更改类的分发表，以便将现有选择器的消息解析到不同的实现，同时将原始方法实现别名到一个新的选择器。

## 调用 `_cmd`

以下代码看起来可能会导致无限循环：

```
- (void)xxx_viewWillAppear:(BOOL)animated {
    [self xxx_viewWillAppear:animated];
    NSLog(@"viewWillAppear: %@", NSStringFromClass([self class]));
}
```

令人惊讶的是，它不会。在调配过程中，`xxx_viewWillAppear:` 已经被重新分配为 `UIViewController -viewWillAppear:` 的原始实现。在自身的实现中调用 `self` 上的方法，程序员的本能会发出警告，但在这个例子里，如果我们记住 _真正_ 发生了什么，它其实是合理的。然而，如果在这个方法中调用 `viewWillAppear:`，它_就会_导致无限循环，因为该方法的实现将在运行时被调配到 `viewWillAppear:` 选择器。

## 注意事项

方法调配被广泛认为是一种巫毒技术，容易导致不可预测的行为和无法预见的后果。虽然它不是最安全的做法，但只要采取以下预防措施，方法调配还是相当安全的：

### 始终调用方法的原始实现（除非你有充分的理由不这样做）

API 提供了输入和输出的契约，但中间的实现是一个黑盒。调配一个方法而不调用原始实现，可能会导致对私有状态的底层假设被破坏，进而影响你的 App 其余部分。

### 避免冲突

给分类方法加上前缀，并绝对确保代码库（或任何依赖项）中没有其他东西在搞同一块功能。

### 理解正在发生的事情

仅仅复制粘贴调配代码而不理解其工作原理不仅危险，而且会浪费一个深入学习 Objective-C 运行时的机会。通读 [Objective-C 运行时参考](https://developer.apple.com/library/mac/documentation/Cocoa/Reference/ObjCRuntimeRef/Reference/reference.html#//apple_ref/c/func/method_getImplementation)并浏览 `<objc/runtime.h>`，以深入理解事情是如何以及为什么发生的。_始终努力用理解取代魔法思维。_

### 谨慎行事

无论你对调配 Foundation、UIKit 或任何其他内置框架多么有信心，要知道一切可能在下一个版本中就崩溃。对此做好准备，并付出额外努力确保玩火时，不会烧到自己（`NSBurned`）。

---

与[关联对象](https://nshipster.com/associated-objects/)一样，方法调配是在你需要时非常强大的技术，但应谨慎使用。
