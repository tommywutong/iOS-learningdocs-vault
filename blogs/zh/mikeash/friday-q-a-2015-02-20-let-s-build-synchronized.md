---
title: 'Friday Q&A 2015-02-20：我们来构建 @synchronized'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-02-20-lets-build-synchronized.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a9326de12f1337bd'
translated: true
---

> 原文：[Friday Q&A 2015-02-20: Let's Build @synchronized](https://www.mikeash.com/pyblog/friday-qa-2015-02-20-lets-build-synchronized.html)　·　mikeash.com Friday Q&A

发表于 2015-02-20 14:26 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2015-03-20：预处理器的滥用与可选括号](https://www.mikeash.com/pyblog/friday-qa-2015-03-20-preprocessor-abuse-and-optional-parentheses.html)  
上一篇：[Friday Q&A 2015-02-06：锁、线程安全性与 Swift](https://www.mikeash.com/pyblog/friday-qa-2015-02-06-locks-thread-safety-and-swift.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [swift](https://www.mikeash.com/pyblog/?tag=swift) [threading](https://www.mikeash.com/pyblog/?tag=threading)

Friday Q&A 2015-02-20：我们来构建 @synchronized

作者：[Mike Ash](https://www.mikeash.com/)

**回顾**  
`@synchronized` 是 Objective-C 中的一种控制（control）构造。它接受一个对象指针作为参数，后跟一段代码块。该对象指针充当锁的角色，在任意时刻，只有一个线程（thread）被允许进入基于该对象指针的 `@synchronized` 代码块。

这是一种用于多线程编程的更简单的锁使用方式。例如，你可以用一个 `NSLock` 来保护对 `NSMutableArray` 的访问：

```
    NSMutableArray *array;
    NSLock *arrayLock;

    [arrayLock lock];
    [array addObject: obj];
    [arrayLock unlock];
```

或者，你也可以使用 `@synchronized`，直接用数组本身作为锁：

```
    @synchronized(array) {
        [array addObject: obj];
    }
```

我个人更偏爱显式锁，既是为了让事情的运作更清晰，也是因为 `@synchronized` 在性能上稍逊一筹，具体原因我们稍后会看到。不过，它确实很方便，并且构建它也很有意思。

**实现理论**  
`@synchronized` 的 Swift 版本是一个函数，它接受一个对象和一个闭包（closure），并在持有锁的情况下调用这个闭包：

```
    func synchronized(obj: AnyObject, f: Void -> Void) {
        ...
    }
```

问题在于，如何将一个任意对象变成一个锁？

在一个理想的世界（从实现此函数的角度看）里，每个对象都会预留一小块额外空间用于存放锁。然后 `synchronized` 就可以在那块小空间上使用适当的 lock 和 unlock 函数。然而，这样的额外空间并不存在——这可能是幸运的，因为如果为了一个大多数对象永远不会用到的功能而膨胀系统中每个对象的内存大小，那将是得不偿失的。

另一种方案是使用一个将对象映射到锁的表。`synchronized` 可以在这个表中查找对应的锁，然后对其进行加锁和解锁。这种方法的问题在于，表本身需要是线程安全的，这要么需要它自己的锁，要么需要某种奇特的免锁数据结构（lockless data structure）。为这个表单独加一把锁要简单得多。

为了防止锁无限积累，这个表需要跟踪锁的使用情况，并在不再需要时销毁或重用这些锁。

**实现**  
对于存储对象到锁映射的表，`NSMapTable` 非常合适。它可以配置为使用原始对象地址作为键，并且可以对键和值都持有弱引用，这使得系统能够自动回收未使用的锁。设置如下：

```
    let locksTable = NSMapTable.weakToWeakObjectsMapTable()
```

锁的对象将是 `NSRecursiveLock` 的实例。因为它是一个类，所以与 `NSMapTable` 配合良好，不像 `pthread_mutex_t` 这类结构。`@synchronized` 提供递归语义，这里也是如此。

这个表本身也需要一把锁。自旋锁（spinlock）在这里很好用，因为对表的访问会很短暂：

```
    var locksTableLock = OS_SPINLOCK_INIT
```

表就绪后，我们可以实现这个函数：

```
    func synchronized(obj: AnyObject, f: Void -> Void) {
```

它首先在 `locksTable` 中查找与 `obj` 对应的锁。这一步必须在持有 `locksTableLock` 的情况下完成：

```
        OSSpinLockLock(&locksTableLock)
        var lock = locksTable.objectForKey(obj) as! NSRecursiveLock?
```

如果表中没有条目，就创建一个新的锁并设置它：

```
        if lock == nil {
            lock = NSRecursiveLock()
            locksTable.setObject(lock!, forKey: obj)
        }
```

拿到锁后，可以释放主表锁。**必须**在调用 `f` 之前完成这一步，以避免潜在的死锁：

```
        OSSpinLockUnlock(&locksTableLock)
```

现在我们可以调用 `f`，并在调用前后对 `lock` 进行加锁和解锁：

```
        lock!.lock()
        f()
        lock!.unlock()
    }
```

**与 Apple 实现的比较**  
Apple 对 `@synchronized` 的实现作为 Objective-C 运行时（runtime）源码发行版的一部分提供。具体代码位于：

[http://www.opensource.apple.com/source/objc4/objc4-646/runtime/objc-sync.mm](http://www.opensource.apple.com/source/objc4/objc4-646/runtime/objc-sync.mm)

它追求的是速度而非简洁性，与上述玩具般的实现不同。看看它在哪些方面相同、哪些方面不同会很有趣。

基本概念是相同的。有一个将对象指针映射到锁的全局表，然后在 `@synchronized` 代码块前后对这个锁进行加锁和解锁。

对于底层的锁对象，Apple 的版本使用了配置为递归锁的 `pthread_mutex_t`。既然 `NSRecursiveLock` 很可能也是用 `pthread_mutex_t` 实现的，这样就省去了中间环节，并避免了运行时对 Foundation 的依赖。

这个表本身是用链表而非散列表（hash table）实现的。由于在常见情况下，任意时刻只有少量锁存在，链表仍然能良好运行，并且可能比散列表性能更好，因为散列表的性能优势在数据集较大时才显现。性能还通过一个每线程缓存（per-thread cache）得到了进一步提升，该缓存保存了在当前线程上最近查找过的锁。

Apple 的实现没有使用一个单一的全局表，而是有一个包含 16 个表的数组。对象根据其地址映射到不同的表。这减少了作用于不同对象的 `@synchronized` 代码块之间不必要的争用，因为它们很可能会使用不同的全局表。

Apple 的实现没有使用会增加大量额外开销的弱指针，而是为每个锁维护一个内部引用计数。当引用计数归零时，该锁就可以被一个新对象重用。未使用的锁不会被销毁，但通过重用，锁的总数被限制在任何时刻活跃锁的最大数量内，而不是随着新对象的使用而无限制增长。

Apple 的实现就其功能而言是智能且快速的，但与使用独立的显式锁相比，它仍然不可避免地带来了一些额外的开销。具体来说：

1. 不相关的对象如果碰巧被分配到同一个全局表中，仍然可能发生争用。
2. 在查找锁（常见情况是锁不在每线程缓存中）时，必须获取和释放自旋锁。
3. 需要在全局表中查找与该对象对应的锁，这带来了额外的工作。
4. 即使不需要递归语义，每次加锁/解锁周期也会因为递归特性而产生开销。

不过，这些问题或多或少是 `@synchronized` 功能所固有的，实现本身当然不应为此受到指责。这是一段优秀的代码，非常值得一读。

**结论**  
`@synchronized` 是一个有趣的、在实现上存在一些挑战的语言构造。从根本上说，它提供了线程安全性（thread safety），但其自身的实现也需要同步来保证安全。在幕后使用一个全局锁来保护对锁表的访问解决了这个两难问题。Apple 实现中那些巧妙的手法使其能够保持可观的运行速度。

今天就到这里。下次回来，我们会有更多有趣的话题。Friday Q&A 由读者建议驱动，如果你有想看到被覆盖的内容，请[发过来](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我写了整本的书！第二卷和第三卷现已出版！提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2015-02-20-lets-build-synchronized.html)

添加你的想法，发表评论：

垃圾邮件和跑题评论将被无提示删除。违规者可能会被我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
