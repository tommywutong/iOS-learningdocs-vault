---
title: Objective-C 编程语言
apple_id: TP30001163
resource_type: Guide
platform: iOS|macOS
topic: Languages & Utilities
technology: Foundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocThreading.html
archived_at: '2026-07-15T07:17:31.927436Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Objective-C 编程语言](Introduction.md)


[下一页](Document%20Revision%20History.md)[上一页](Exception%20Handling.md)

# 线程

Objective-C 为线程同步和异常处理提供了支持，本章和[异常处理](Exception%20Handling.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrtfvbuqmjtfvjvomi)一章都对此做了说明。要开启对这些特性的支持，需使用 GNU 编译器集合（GCC）3.3 及更高版本的 `-fobjc-exceptions` 开关。

Objective-C 在应用程序中支持多线程。因此，两个线程可能会同时尝试修改同一个对象，这种情况可能会给程序带来严重问题。为了保护某段代码不被多个线程同时执行，Objective-C 提供了 `@synchronized()` 指令。

`@synchronized()` 指令会锁定一段代码，使其在同一时间只能被一个线程使用。其他线程会被阻塞，直到该线程退出被保护的代码——也就是执行流程越过 `@synchronized()` 块中最后一条语句之后。

`@synchronized()` 指令唯一的参数可以是任意 Objective-C 对象，包括 `self`。这个对象被称为_互斥信号量_（mutual exclusion semaphore）或_互斥锁_（mutex）。它让一个线程能够锁定一段代码，阻止其他线程使用这段代码。你应当为程序中不同的临界区使用各自独立的信号量。为了避免竞态条件，最安全的做法是在应用程序变为多线程之前，就创建好所有的互斥对象。

清单 11-1 展示了使用 `self` 作为互斥锁，来同步访问当前对象实例方法的代码。你可以采用类似的方法，使用类对象而不是 `self`，来同步相关类的类方法。当然，在后一种情况下，同一时间只允许一个线程执行某个类方法，因为所有调用者共享的类对象只有一个。

__清单 11-1__  使用 self 锁定方法

```objc
- (void)criticalMethod
{
    @synchronized(self) {
        // 临界代码。
        ...
    }
}
```

清单 11-2 展示了一种通用的做法。在执行临界过程之前，代码从 `Account` 类获取一个信号量，并用它来锁定临界区。`Account` 类可以在其 `initialize` 方法中创建这个信号量。

__清单 11-2__  使用自定义信号量锁定方法

```objc
Account *account = [Account accountFromString:[accountField stringValue]];

// 获取信号量。
id accountSemaphore = [Account semaphore];

@synchronized(accountSemaphore) {
    // 临界代码。
    ...
}
```

Objective-C 的同步特性支持递归和可重入的代码。一个线程可以以递归方式多次使用同一个信号量；其他线程会被阻塞而无法使用该信号量，直到该线程释放了用它获取的所有锁——也就是说，直到每一个 `@synchronized()` 块都正常退出，或者通过异常退出。

当 `@synchronized()` 块中的代码抛出异常时，Objective-C 运行时会捕获该异常，释放信号量（以便被保护的代码可以被其他线程执行），然后把异常重新抛给下一个异常处理器。

[下一页](Document%20Revision%20History.md)[上一页](Exception%20Handling.md)

