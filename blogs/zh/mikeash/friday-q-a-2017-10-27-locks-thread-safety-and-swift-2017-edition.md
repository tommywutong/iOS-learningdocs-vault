---
title: 'Friday Q&A 2017-10-27：锁、线程安全与 Swift：2017 版'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2017-10-27-locks-thread-safety-and-swift-2017-edition.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2a655cff4076eb77'
translated: true
---

> 原文：[Friday Q&A 2017-10-27: Locks, Thread Safety, and Swift: 2017 Edition](https://www.mikeash.com/pyblog/friday-qa-2017-10-27-locks-thread-safety-and-swift-2017-edition.html)　·　mikeash.com Friday Q&A

发布于 2017-10-27 11:28 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2017-11-10: 观察 A11 的异构核心](https://www.mikeash.com/pyblog/friday-qa-2017-11-10-observing-the-a11s-heterogenous-cores.html)  
上一篇：[The Complete Friday Q&A Volumes II and III Are Out!](https://www.mikeash.com/pyblog/the-complete-friday-qa-volumes-ii-and-iii-are-out.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift) [threading](https://www.mikeash.com/pyblog/?tag=threading)

Friday Q&A 2017-10-27：锁、线程安全与 Swift：2017 版

作者：[Mike Ash](https://www.mikeash.com/)

本文也提供[中文版（李孛翻译）](http://kylinroc.github.io/friday-qa-2017-10-27-locks-thread-safety-and-swift-2017-edition.html)。

本文将重复旧文章中的部分内容，并进行更新，同时讨论一些变化。在阅读本文之前，不需要先阅读之前的文章。

**锁的快速回顾**  
锁（lock），或称互斥锁（mutex），是一种保证在某一时刻只有一个线程（thread）能在特定代码区域中活跃的结构。它们通常用于确保多个线程访问可变数据结构时，都能看到一致的数据视图。锁有几种类型：

1. 阻塞锁（blocking lock）——线程在等待另一个线程释放锁时休眠。这是通常的行为。
2. 自旋锁（spinlock）——使用忙等待循环持续检查锁是否已释放。如果等待很少发生，这种方式效率更高，但如果等待频繁，则会浪费 CPU 时间。
3. 读写锁（reader/writer lock）——允许多个“读”线程同时进入区域，但当“写”线程获取锁时，会排除所有其他线程（包括读线程）。这在许多数据结构中很有用，因为多个线程同时读取是安全的，但在其他线程读或写时写入则不安全。
4. 可重入锁（recursive lock）——允许单个线程多次获取同一把锁。非可重入锁在同一个线程中重入时可能会发生死锁、崩溃或其他异常行为。

**API**  
Apple 的 API 提供了多种互斥机制。以下是常见但不完全的列表：

1. `pthread_mutex_t`。
2. `pthread_rwlock_t`。
3. `DispatchQueue`。
4. 配置为串行的 `OperationQueue`。
5. `NSLock`。
6. `os_unfair_lock`。

此外，Objective-C 提供了 `@synchronized` 语言构造，目前它是在 `pthread_mutex_t` 之上实现的。与其他锁不同，`@synchronized` 不使用显式的锁对象，而是将任意一个 Objective-C 对象视为锁。`@synchronized(someObject)` 段将阻止任何使用相同对象指针的其他 `@synchronized` 段进行访问。这些不同的机制具有不同的行为和功能：

1. `pthread_mutex_t` 是一个阻塞锁，可以选择配置为可重入锁。
2. `pthread_rwlock_t` 是一个阻塞的读写锁。
3. `DispatchQueue` 可以用作阻塞锁。通过将其配置为并发队列并使用屏障 block，它可以作为读写锁使用。它还支持锁定区域的异步执行。
4. `OperationQueue` 可以用作阻塞锁。与 `dispatch_queue_t` 一样，它支持锁定区域的异步执行。
5. `NSLock` 是一个 Objective-C 类的阻塞锁。其配套类 `NSRecursiveLock` 顾名思义是一个可重入锁。
6. `os_unfair_lock` 是一个较简单、较低级的阻塞锁。

最后，`@synchronized` 是一个阻塞的可重入锁。

**自旋锁的缺失**  
我提到了自旋锁作为一种锁的类型，但这里列出的 API 中没有一个自旋锁。这与之前的文章有很大不同，也是我撰写这篇更新的主要原因。

自旋锁非常简单，并且在合适的场合下效率很高。不幸的是，对于现代世界的复杂性来说，它们有点过于简单了。

问题在于线程优先级。当可运行的线程数超过 CPU 核心数时，优先级高的线程会获得优先权。这是一个有用的概念，因为 CPU 核心始终是有限的资源，你不希望某个对时间不敏感的后台网络操作在用户试图使用界面时窃取时间。

当一个高优先级线程被卡住，必须等待低优先级线程完成某些工作时，而高优先级线程又阻止了低优先级线程实际执行该工作，则可能导致长时间的挂起甚至永久死锁。

死锁的场景如下所示，其中 H 是高优先级线程，L 是低优先级线程：

1. L 获取自旋锁。
2. L 开始执行一些工作。
3. H 准备就绪运行，并抢占 L。
4. H 尝试获取自旋锁，但失败了，因为 L 仍然持有它。
5. H 开始在自旋锁上愤怒地旋转，反复尝试获取它，并独占 CPU。
6. H 在 L 完成工作之前无法继续。L 无法完成工作，除非 H 停止在自旋锁上愤怒地旋转。
7. 悲剧。

有一些方法可以解决这个问题。例如，H 可以在第 4 步将其优先级捐赠给 L，从而让 L 及时完成其工作。可以制造一种解决此问题的自旋锁，但 Apple 旧的自旋锁 API `OSSpinLock` 并没有这样做。

这在很长时间内都没问题，因为线程优先级在 Apple 平台上使用不多，而且优先级系统使用动态优先级，使得死锁场景不会持续太久。后来，[服务质量（QoS）类](https://developer.apple.com/library/content/documentation/Performance/Conceptual/EnergyGuide-iOS/PrioritizeWorkWithQoS.html) 使得不同优先级更加普遍，也使死锁场景更有可能持续存在。

曾长期表现良好的 `OSSpinLock`，在 iOS 8 和 macOS 10.10 发布后就不再是一个好选择了。现在它已被正式废弃（deprecated）。替代品是 `os_unfair_lock`，它作为低级、简单、廉价的锁，服务于同样的总体目的，但足够复杂以避免优先级问题。

**值类型**  
注意 `pthread_mutex_t`、`pthread_rwlock_t` 和 `os_unfair_lock` 是值类型，而非引用类型。这意味着如果你对它们使用 `=`，就会创建一个副本。这一点很重要，因为这些类型**不能被复制**！如果你复制了某个 `pthread` 类型，副本将不可用，尝试使用时可能会崩溃。操作这些类型的 `pthread` 函数假定这些值位于它们初始化的相同内存地址，之后把它们放到别处是个坏主意。`os_unfair_lock` 不会崩溃，但你会得到一个完全独立的锁，这绝不是你想要的结果。

如果你使用这些类型，必须小心不要复制它们，无论是显式使用 `=` 运算符，还是隐式地，例如将它们嵌入 `struct` 或在闭包（closure）中捕获它们。

此外，由于锁本质上是可变对象，这意味着你需要用 `var` 而非 `let` 来声明它们。

其余的都是引用类型，意味着它们可以随意传递，并且可以用 `let` 声明。

**初始化**  
使用 `pthread` 锁时必须小心，因为你可以使用空的 `()` 初始化器创建一个值，但这个值不会是有效的锁。这些锁必须使用 `pthread_mutex_init` 或 `pthread_rwlock_init` 单独初始化：

```
    var mutex = pthread_mutex_t()
    pthread_mutex_init(&mutex, nil)
```

人们很自然会想为这些类型编写一个封装初始化的扩展（extension）。但是，无法保证初始化器直接作用于变量本身，而不是作用于一个副本。由于这些类型不能被安全复制，除非让初始化器返回一个指针或包装类，否则无法安全地编写这种扩展。

如果你使用这些 API，别忘了在需要销毁锁时调用相应的 `destroy` 函数。

**使用**  
`DispatchQueue` 有一个基于回调的 API，这使得安全使用它非常自然。根据你希望受保护的代码同步还是异步运行，调用 `sync` 或 `async`，并将要运行的代码传递给它：

```
    queue.sync(execute: { ... })
    queue.async(execute: { ... })
```

对于 `sync` 情况，该 API 足够友好，会捕获受保护代码的返回值，并将其作为 `sync` 方法的返回值提供：

```
    let value = queue.sync(execute: { return self.protectedProperty })
```

你甚至可以在受保护的 block 内 `throw` 错误，它们会传播出去。

`OperationQueue` 类似，尽管它没有内置的方式传播返回值或错误。你需要自己实现，或者使用 `DispatchQueue` 代替。

其他 API 需要单独的锁定和解锁调用，当你忘记其中之一时，可能会带来麻烦。这些调用看起来像这样：

```
    pthread_mutex_lock(&mutex)
    ...
    pthread_mutex_unlock(&mutex)

    nslock.lock()
    ...
    nslock.unlock()

    os_unfair_lock_lock(&lock)
    ...
    os_unfair_lock_unlock(&lock)
```

由于这些 API 几乎相同，我将在后续示例中使用 `nslock`。其他 API 也一样，只是名称不同。

当受保护的代码很简单时，这没问题。但如果更复杂呢？例如：

```
    nslock.lock()
    if earlyExitCondition {
        return nil
    }
    let value = compute()
    nslock.unlock()
    return value
```

哎呀，有时你忘记解锁了！这是造成难以发现 bug 的好方法。也许你对 `return` 语句总是很自律，从不这样做。那如果你抛出错误呢？

```
    nslock.lock()
    guard something else { throw error }
    let value = compute()
    nslock.unlock()
    return value
```

同样的问题！也许你非常自律，也从不这样做。那么你是安全的，但即便如此代码也有点丑陋：

```
    nslock.lock()
    let value = compute()
    nslock.unlock()
    return value
```

这个问题的明显解决方法是使用 Swift 的 `defer` 机制。一旦锁定，就推迟解锁。这样无论你如何退出代码，锁都会被释放：

```
    nslock.lock()
    defer { nslock.unlock() }
    return compute()
```

这对于提前返回、抛出错误或者普通代码都有效。

仍然需要编写两行代码，这有点烦人，所以我们可以把所有东西包装在一个基于回调的函数中，就像 `DispatchQueue` 那样：

```
    func withLocked<T>(_ lock: NSLock, _ f: () throws -> T) rethrows -> T {
        lock.lock()
        defer { lock.unlock() }
        return try f()
    }

    let value = withLocked(lock, { return self.protectedProperty })
```

当为值类型实现时，你需要确保是获取锁的**指针**而不是锁本身。记住，你不希望复制这些东西！`pthread` 版本看起来像这样：

```
    func withLocked<T>(_ mutexPtr: UnsafeMutablePointer<pthread_mutex_t>, _ f: () throws -> T) rethrows -> T {
        pthread_mutex_lock(mutexPtr)
        defer { pthread_mutex_unlock(mutexPtr) }
        return try f()
    }

    let value = withLocked(&mutex, { return self.protectedProperty })
```

**选择你的锁 API**  
`DispatchQueue` 是一个明显的首选。它有很好的 Swifty API，用起来很令人愉快。Dispatch 库得到了 Apple 的大量关注，这意味着它有望性能良好、工作可靠，并获得大量很酷的新功能。

`DispatchQueue` 允许许多巧妙的进阶用法，比如安排定时器或事件源在用作锁的队列上直接触发，确保处理程序与使用该队列的其他事物同步。设置目标队列的能力允许表达复杂的锁层级。自定义并发队列可以轻松用作读写锁。你只需要改变一个字母，就可以在后台线程上异步执行受保护代码，而不是同步执行。并且该 API 易于使用且难以误用。这是全方位的胜利。GCD 很快成为我最喜欢的 API 之一并且至今仍位列其中，这是有原因的。

和大多数事物一样，它并不完美。分发队列由内存中的一个对象表示，因此有一些开销。它们缺少一些特定功能，比如条件变量或可重入性。偶尔，能够进行单独的锁定和解锁调用会很有用，而不是被迫使用基于回调的 API。`DispatchQueue` 通常是正确的选择，如果你不知道选什么，它是一个很好的默认选择，但偶尔也有理由使用其他锁。

当每个锁的开销很重要时（因为出于某种原因你有大量的锁），并且你不需要高级功能时，`os_unfair_lock` 可以是一个好选择。它被实现为一个单一的 32 位整数，你可以将它放在任何需要的地方，因此开销很小。

正如其名所暗示的，`os_unfair_lock` 缺少的功能之一是公平性。锁的公平性意味着至少有某种尝试来确保不同的等待锁的线程都有机会获取它。没有公平性，一个快速释放并重新获取锁的线程有可能在其他线程等待时独占地占用它。

这是否是问题取决于你在做什么。有些使用场景需要公平性，有些则完全无关紧要。缺乏公平性允许 `os_unfair_lock` 有更好的性能，因此在不需要公平性的情况下可以提供优势。

`pthread_mutex` 位于中间某处。它比 `os_unfair_lock` 大得多，为 64 字节，但你仍然可以控制它的存储位置。它实现了公平性，尽管这是 Apple 实现的细节，而不是 API 规范的一部分。它还提供了各种其他高级特性，例如使互斥锁可重入，以及高级的线程优先级处理。

`pthread_rwlock` 提供了一个读写锁。它占用了高达 200 字节，并且没有提供多少有趣的功能，因此似乎没有太多理由使用它而不是并发 `DispatchQueue`。

`NSLock` 是 `pthread_mutex` 的包装。很难想出需要使用它的场景，但如果你需要显式的 lock/unlock 调用，又不想麻烦地手动初始化和销毁 `pthread_mutex`，它可能会很有用。

`OperationQueue` 提供了类似于 `DispatchQueue` 的基于回调的 API，带有一些高级功能，比如操作之间的依赖管理，但缺少 `DispatchQueue` 提供的许多其他功能。几乎没有理由将 `OperationQueue` 用作锁定 API，尽管它可能对其他事情有用。

简而言之：`DispatchQueue` 可能是正确的选择。在某些情况下，`os_unfair_lock` 可能更好。其他几种通常不推荐使用。

**结论**  
Swift 没有用于线程同步的语言设施，但 API 弥补了这一点。GCD 仍然是 Apple 的皇冠上的明珠之一，而且它的 Swift API 非常棒。在极少数它不适合的情况下，还有许多其他选择。我们没有 `@synchronized` 或原子属性（atomic property），但我们有更好的东西。

本次内容就到此为止。请回来查看更多有趣的东西。如果你在此期间感到无聊，[买一本我的书吧！](https://www.mikeash.com/book.html) Friday Q&A 由读者的想法驱动，所以如果你有一个想在这里看到的话题，请[发送过来](mailto:mike@mikeash.com)！

你喜欢这篇文章吗？我正在销售装满它们的书籍！第二卷和第三卷现已出版！它们提供 ePub、PDF、印刷版，以及在 iBooks 和 Kindle 上。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2017-10-27-locks-thread-safety-and-swift-2017-edition.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
