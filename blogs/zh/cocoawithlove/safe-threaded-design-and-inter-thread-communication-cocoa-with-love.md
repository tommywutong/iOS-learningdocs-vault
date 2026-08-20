---
title: 安全的多线程设计与线程间通信 | Cocoa with Love
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/08/safe-threaded-design-and-inter-thread.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:ec186dd0e5e7553a'
translated: true
---

> 原文：[Safe, threaded design and inter-thread communication | Cocoa with Love](https://www.cocoawithlove.com/2009/08/safe-threaded-design-and-inter-thread.html)　·　Cocoa with Love (Matt Gallagher)

Foundation 框架提供了进行线程间通信所需的一切工具——无需自行处理锁和同步。我将展示 Cocoa 在线程间通信、通知和简单同步方面的工具——包括在主线程上发送 `NSNotification` 的代码，比 Cocoa 文档中建议的简单得多。

## 概述

多线程代码以难以编写、容易死锁、存在竞态条件和不可预测行为而著称。

如果你被迫自行处理锁，这些情况确实存在；但 Foundation 提供了管理典型多线程场景所需的一切工具，让你可以完全避免锁的风险。

这篇文章源于我对 Apple 建议的震惊（在其 [将通知投递到特定线程](http://developer.apple.com/documentation/Cocoa/Conceptual/Notifications/Articles/Threading.html) 中）：像从一个线程向另一个线程发送 `NSNotification` 这样简单的事，竟需要几十行代码和一个专门的类来实现。

其实没那么难。在线程之间发送数据（包括通知）只需要一行代码。

## 安全简单的多线程规则

Cocoa 中简单的线程安全只需要两条规则：

1. 每个变量或对象在名义上必须属于一个线程（虽然可以完全移交给另一个线程），并且未经移交不得在多线程中使用（除非它在 [明确线程安全的类列表](http://developer.apple.com/documentation/Cocoa/Conceptual/Multithreading/ThreadSafetySummary/ThreadSafetySummary.html) 上）。
2. 线程之间的所有通信（线程启动后）应使用 `performSelector:onThread:withObject:waitUntilDone:`，并且接收者和“对象”都应属于（或移交给）目标线程。

这种方法的唯一限制是，任何*接收*通信的线程必须运行一个 `NSRunLoop`。由于构造后的通信通常是单向的（从工作线程回到主线程），这很少是重大限制。其他线程可以调用 `[NSRunLoop currentRunLoop]` 的 `runMode:beforeDate` 来处理运行循环并接收消息。

很多多线程代码并不遵循这些规则。很多多线程代码使用一套精心的锁系统、同步段、volatile 变量和原子操作，让单个对象可以从多个线程同时访问。这确实能工作，但一般来说：你不应该以这种方式设计代码。它棘手、混乱且容易出错。为了说明这一点，你可以看看我在 [第一版](https://www.cocoawithlove.com/2008/09/streaming-and-playing-live-mp3-stream.html) 和 [第二版](https://www.cocoawithlove.com/2009/06/revisiting-old-post-streaming-and.html) 的 AudioStreamer 代码之间做了多少改动——坚如磐石的手动锁定代码写起来既烦人又困难。

相反，你应该尽可能地将所有对象隔离到单个线程中，并将线程之间的通信限制为使用 `performSelector:onThread:withObject:waitUntilDone:` 的方法调用。为了解释其工作原理，我将展示一个在单独线程中运行的示例，并说明它如何仅使用现有的 Foundation 方法自动处理所有线程安全问题，来完成所有线程间通信。

## 场景：在工作线程中向网络 NSFileHandle 写入数据

你可能需要多线程的最简单情形之一，就是写入网络 socket 的 `NSFileHandle`。这是一个同步操作（阻塞直到完成），因此最好在工作线程中执行，这样你的程序的主线程可以保持响应。

下面的类是一个 `NSOperation` 子类。如果你不了解 `NSOperation`，它是一个可以添加到 `NSOperationQueue` 的对象，让对象的 `main` 方法在单独的线程中运行（参见 [Apple 的线程编程指南](http://developer.apple.com/documentation/Cocoa/Conceptual/Multithreading/OperationObjects/OperationObjects.html)）。虽然 `NSThread` 的 `detachNewThreadSelector:toTarget:withObject:` 是启动单个工作线程的最佳方式，但 `NSOperation` 是运行一系列线程化任务的最佳方式（或者自从 [其中的严重 bug 在 10.5.7 中修复后](http://www.mikeash.com/?page=pyblog/use-nsoperationqueue.html) 一直如此）。

这个类的初始化方法在构造时接受一个 `NSFileHandle` 和一个 `NSData` 对象，并在其 `main` 方法中将数据写入文件句柄。

```objc
@interface FileWriteOperation : NSOperation
{
    NSFileHandle *fileHandle;
    NSData *data;
}
@end

@implementation FileWriteOperation

- (id)initWithFileHandle:(NSFileHandle *)aFileHandle data:(NSData *)aData
{
    self = [super init];
    if (self != nil)
    {
        fileHandle = [aFileHandle retain];
        data = [aData retain];
    }
    return self;
}

- (void)main
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    @try
    {
        [fileHandle writeData:data];
        // At this point, the write has succeeded
    }
    @catch (NSException *e)
    {
        // At this point, the write has failed
    }
    @finally
    {
        [pool drain];
    }
}

- (void)dealloc
{
    [fileHandle closeFile];
    [fileHandle release];
    [data release];
    [super dealloc];
}

@end
```

`NSOperation` 的创建及其线程的启动如下：

```objc
// 假设 operationQueue、fileHandle 和 fileData 已经存在
[operationQueue
    addOperation:
        [[[FileWriteOperation alloc]
            initWithFileHandle:fileHandle
            data:fileData]
        autorelease]];
```

为了遵循线程安全的第一条规则，在 `FileWriteOperation` 构造之后，传递给其 `initWithFileHandle:data:` 方法的 `fileHandle` 值不能在 `NSOperationQueue` 的工作线程之外再次使用。

## 传达成功或失败

上面的类可以工作，但没有任何方式来传达结果。如果能在 `write has succeeded` 那行发送 `writeFinishedWithSuccess:YES`，并在 `write has failed` 那行发送 `writeFinishedWithSuccess:NO`，那就好了。

不安全的方式是在另一个对象上调用一个方法并发送结果：

```objc
    [responseHandler writeFinishedWithSuccess:YES]; // BAD!!
```

如果 `responseHandle` 属于另一个线程，那么这个方法可能会导致任意数量的竞态条件和其他多线程问题。

但解决方案异常简单：

```objc
    [responseHandler
        performSelectorOnMainThread:@selector(writeFinishedWithSuccess:)
        withObject:[NSNumber numberWithBool:YES]
        waitUntilDone:NO];
```

这假设 `responseHandler` 是一个名义上的“主线程”对象。如果需要在其他位置发送响应，你可以使用 `performSelector:onThread:withObject:waitUntilDone:` 方法并指定不同的线程。

你会注意到，在这种情况下参数必须是对象（`[NSNumber numberWithBool:YES]` 而不是简单的 `YES`），并且你传递给另一个线程的任何参数，都不应在当前线程中再次使用。

## 将通知投递到特定线程

当然，上面展示的 `FileWriteOperation` 类没有可以在完成时通知的 `responseHandle` 对象，因此我宁愿使用 `NSNotificationCenter` 发送 `NSNotification`，这样任何对象都可以接收通知。

`NSNotificationCenter` 本身是线程安全的，但它会在你调用 `postNotification:` 的线程上投递通知，因此如果你期望该通知的观察者属于不同线程，你就破坏了这些对象的线程安全。

通常，在主线程上投递所有通知是个好主意。我们可以这样做：

```objc
// 某个类的方法中的一行代码...
[[self class]
    performSelectorOnMainThread:@selector(postNotification:)
    withObject:
        [NSNotification
            notificationWithName:@"FileWriteOperationSucceeded"
            object:self]];

+ (void)postNotification:(NSNotification *)aNotification
{
    [[NSNotificationCenter defaultCenter] postNofication:aNotification];
}
```

注意，直到我们在主线程上之前，我们没有调用 `+[NSNotificationCenter defaultCenter]`。如果我们在其他线程上调用它，它会返回那个其他线程的通知中心。

某些类遵循不同的行为，将通知投递到它们被构造的线程（不一定是主线程）。要遵循此行为，只需在构造时保存 `[NSThread currentThread]`，并在那个线程上执行 `postNotification:` 选择器。

你可能已经注意到，通知将 `self` 从一个线程传递到另一个线程——这打破了 `self` 的线程所有权。这仅在以下情况之一才真正安全：

- **移交**——该参数将永远不再在这个线程上使用。
  在此情况下，如果 `self` 在工作线程上已完全处理完毕（例如上面展示的 `main` 方法的底部）。在这种情况下，对象将自己传递回另一个线程。
- **线程安全**——如果该类或特定方法保证是线程安全的。
  在此情况下，如果对 `self` 调用的唯一方法是 `retain`、`release` 和默认的指针比较方法 `isEqual:`（这些是在从 `NSMutableArray` 中移除时调用的方法）。这些是保证线程安全的方法。

如果这两条都不成立，那么你无法安全地在线程之间传递 `self`（或任何其他参数）。

## 结论

本文的目的是传达两个想法：

- 仔细地锁定和同步使编程变得困难，但如果你将对象设计为一次只在一个线程上使用，那么它们无需锁或同步就是线程安全的（如果需要，将你的对象拆分为针对不同线程的组件）。
- 使用线程间通信来保持不同线程中的对象彼此同步。在 Cocoa 中，这非常简单，但你确实需要确保你传递的所有参数要么是线程安全的对象，要么是移交对象。

Apple 的[将通知投递到特定线程](http://developer.apple.com/documentation/Cocoa/Conceptual/Notifications/Articles/Threading.html)代码已经严重过时了。我很乐意看到它被彻底更改——你绝不应该为了实现仅仅将通知投递到另一个线程而实现如此复杂的代码。

当然，总会有一些情况你无法运行 `NSRunLoop` 来处理 `performSelector:onThread:withObject:waitUntilDone:` 消息。也有些情况你觉得某个对象必须是多线程的（而不是单线程独占）。这两种情况都需要同步或锁定的解决方案，但我建议首先尝试找到 `NSRunLoop` 和线程独占的解决方案，因为它们更容易管理且潜在问题更少。
