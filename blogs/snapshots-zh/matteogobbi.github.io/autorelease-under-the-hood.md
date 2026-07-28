---
title: Autorelease 实现原理探析
source_url: 'http://matteogobbi.github.io/blog/2014/09/28/autorelease-under-the-hood/'
source_domain: matteogobbi.github.io
source_group: single-site
original_language: en
published: 2014-09-28
archived_at: 2026-07-27
content_hash: 'sha256:d9c305bf83e0993e'
plan_ref: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 3｜AutoreleasePool 放回事件循环中理解（对应 W4-01）
plan_week: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期
plan_day: Day 3｜AutoreleasePool 放回事件循环中理解（对应 W4-01）
container: //article
container_source: guess
translated: true
---

> 原文：[Autorelease - Under the Hood](http://matteogobbi.github.io/blog/2014/09/28/autorelease-under-the-hood/)

# Autorelease 实现原理探析

本文归类于：[arc](http://matteogobbi.github.io/blog/categories/arc/)、[ios](http://matteogobbi.github.io/blog/categories/ios/)、[mrc](http://matteogobbi.github.io/blog/categories/mrc/)、[objective-c](http://matteogobbi.github.io/blog/categories/objective-c/)、[underthehood](http://matteogobbi.github.io/blog/categories/underthehood/)

由于这是一个鲜少被触及但至关重要的主题，我决定撰写一篇文章来梳理相关信息，并解释 `autorelease`（或者说更准确地说，**自动释放池**（`autorelease pool`））的内部工作原理。

本文的主要目的并非解释自动释放池的基本概念以及何时使用 `autorelease`，但为了后续深入探讨，理解这些概念确实至关重要。因此，第一部分将专门讲解这些基础知识。经验丰富的开发者可以根据需要直接跳过。

## 是什么与何时用

正如 [Apple 官方文档](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmAutoreleasePools.html) 所述：

> 自动释放池区块提供了一种机制，使你能够放弃对象的所有权（ownership），同时避免它被立即释放（例如当你从一个方法返回对象时）。通常，你无需创建自己的自动释放池区块，但在某些情况下，要么你必须这样做，要么这样做会带来好处。

让我们看几个例子：

在 **ARC** 之前，有我们不太喜欢的 **[MRC](https://developer.apple.com/library/ios/releasenotes/objectivec/rn-transitioningtoarc/introduction/introduction.html)**，即**手动引用计数（Manual Reference Counting）**。尽管如今它在 Xcode 中仍存在，但已不再使用，而使用 `retain`、`release` 和 `autorelease` 这些“苦差事”已交由编译器处理。不过，让我们暂时想象一下处于 MRC 环境中，并有以下方法：

```
/* MGClassA */

- (void)method

{

    MGClassB *objB = [MGClassB new];

    NSObject *newObj = [objB getAnObject];

    // 做一些事情...

    [objB release];

}

/* MGClassB */

- (NSObject *)getAnObject

{

    NSObject *newObj = [NSObject new];

    return newObj;

}
```

在第一个方法中，创建了一个类型为 `MGClassB` 的对象，并暂由类型为 `MGClassA` 的对象持有（retain）；然后向 `objB` 请求分配、初始化并返回一个新对象。于是此时我们面临这种情况：

`objA` —**持有**—\> `objB`

`objB` —**持有**—\> `newObj`

请注意，`objA` 在获得 `newObj` 后并未调用 `retain`，因此它没有所有权，而 `newObj` 的引用计数（retain count）仍然为 1。
此时，`method` 执行完毕并释放了 `objB`，`objB` 不再被引用，但它仍然持有 `newObj`。因此这个对象将继续占用内存，造成**内存泄漏**（memory leak）。根据 [Apple 官方文档](https://developer.apple.com/library/ios/documentation/performance/conceptual/managingmemory/articles/FindingLeaks.html)：

> 内存泄漏是指程序不再引用的已分配内存块。

这意味着，由于 `newObj` 仅被 `objB` 指向，而 `objB` 不再被任何人指向，将再也无法获得一个引用来释放 `newObj`，它将在应用程序关闭前一直占用内存。

我们该如何解决这个问题？`autorelease` 可以使对象在**一段时间内保持存活**，然后该对象会被自动释放，从而避免内存泄漏：

```
/* MGClassB */

- (NSObject *)getAnObject

{

    NSObject *newObj = [NSObject new];

    return [newObj autorelease];

}
```

下一节我们将深入探讨为什么在这个例子中没有出现**自动释放池**，但在此之前，我们先看看另一个需要创建自动释放池的情况。
**自动释放池**是一个容器，用于放置被标记为 `autorelease` 的对象。当池被排空（drain）时，容器中的每个对象都会被释放。在以下情况下，这会非常有用：

```
- (NSObject *)method

{

    for (int i = 0; i < 10000; i++) {

        NSAutoreleasePool *myPool = [NSAutoreleasePool new];

        /* 执行某些操作，这些操作会创建大量自动释放的临时对象。 */

        [myPool drain];

    }

}
```

在现代 **Objective-C** 中，它变成了：

```
- (NSObject *)method

{

    for (int i = 0; i < 10000; i++) {

        @autoreleasepool {

            /* 执行某些操作，这些操作会创建大量自动释放的临时对象。 */

        }

    }

}
```

这个循环执行了 10,000 次。你可能不知道代码中会分配多少对象，但如果不使用 `@autoreleasepool`，内存会被大量不再使用的对象分配填满，进而影响 App 的性能，并可能导致内存警告的风险。
而使用 `@autoreleasepool`，对象将在自动释放作用域结束时被释放。

请注意，使用 ARC 时，你不能直接调用 `release` 或 `autorelease`，因此 `@autoreleasepool` 有时会更有用。

## 内部实现原理

我们知道，一个被标记为 `autorelease` 的对象会进入一个自动释放池，但请记住这个例子：

```
/* MGClassB */

- (NSObject *)getAnObject

{

    NSObject *newObj = [NSObject new];

    return [newObj autorelease];

}
```

问题是：**`newObj` 进入了哪个自动释放池？**
答案很简单，它就在任何 Xcode 项目中 `Supporting Files` 文件夹下的 `main.m` 文件里：

```
int main(int argc, char * argv[]) {

    @autoreleasepool {

        return UIApplicationMain(argc, argv, nil, NSStringFromClass([AppDelegate class]));

    }

}
```

是的，`main` 方法拥有整个项目的**第一个自动释放池**。因此在我们的例子中，`newObj` 会进入这个主自动释放池，该池会在当前[运行循环](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/Multithreading/RunLoopManagement/RunLoopManagement.html)（Run Loop）结束时被排空。
我们当然假设正在主线程（main thread）上运行，但总的来说，**每个线程都有自己的主自动释放池**。

了解了理论之后，下一个问题是：**自动释放的对象是如何找到正确的自动释放池的指针的？** 正如 [Apple 官方文档](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmAutoreleasePools.html) 所述：

> 在 Cocoa 应用中，每个线程都维护着自己的自动释放池区块栈（stack）。

就是这样。简单明了！
因此，当对象调用 `autorelease` 时，它大致会执行以下操作：

```
- (void)autorelease

{

    AutoreleasePool *pool = /* Get the most recet autorelease pool from the stack */

    [pool add:self];

}
```

确实，由于自动释放池可以有多个且是嵌套的，**所以必须有一个栈**。
这当然是用高级代码来帮助理解，Apple 开源的 autorelease 实现可以在[这里](http://opensource.apple.com/source/objc4/objc4-493.9/runtime/objc-arr.mm)找到。

最后需要强调的一点是关于自动释放池的容器。
**自动释放池使用什么数据结构来存储待释放的对象？**
让我们思考一下：

- `NSMutableArray`：不行，因为它会通过调用 `-addObject` 来持有（retain）对象，这会使自动释放失去意义；
- `NSMutableDictionary`：不行，原因同上；
- `NSMutableSet`：不行，原因同上，而且它不接受重复对象。

那么它使用了什么呢？
很简单：任何**不持有对象**并且**接受重复对象**的数据结构，例如使用弱对象引用的 `NSPointerArray`、`LinkedList`（链表）等。

## 结语

希望这篇文章能消除你对 `autorelease` 方法和**自动释放池**的所有疑虑。即使自动释放池的管理始终是系统负责的职责，理解其工作原理仍然非常重要。

**在 [Twitter](https://twitter.com/matteo_gobbi) 上关注我**！

干杯！

---

# 评论
