---
title: 一篇关于 Swift 中锁与线程安全的文章
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-02-06-locks-thread-safety-and-swift.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a145ce48fc0cec4a'
translated: true
---

> 原文：[一篇关于 Swift 中锁与线程安全的文章](https://www.mikeash.com/pyblog/friday-qa-2015-02-06-locks-thread-safety-and-swift.html)　·　mikeash.com Friday Q&A

发表于 2015-02-06 14:23 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2015-02-20: 让我们来构建 @synchronized](https://www.mikeash.com/pyblog/friday-qa-2015-02-20-lets-build-synchronized.html)  
上一篇文章：[Friday Q&A 2015-01-23: 让我们来构建 Swift Notifications](https://www.mikeash.com/pyblog/friday-qa-2015-01-23-lets-build-swift-notifications.html)  
标签： [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift) [threading](https://www.mikeash.com/pyblog/?tag=threading)

Friday Q&A 2015-02-06: 锁、线程安全与 Swift

作者： [Mike Ash](https://www.mikeash.com/)

本文也提供 [波斯尼亚语（Vlada Catalic 翻译）](http://vladacatalic.com/locks-thread-safety-and-swift/) 和 [马其顿语（Vlada Catalic 翻译）](http://balkanscience.com/locks-thread-safety-and-swift/) 版本。

**锁的快速回顾**  
锁（lock），或称互斥锁（mutex），是一种构造，它确保在任意时刻，只有一个线程活跃在给定的代码区域内。它们通常用于保证多个线程访问同一个可变数据结构时，都能看到该数据结构的一致视图。锁有几种类型：

1. **阻塞锁** 会让线程在等待另一个线程释放锁时休眠。这是通常的行为。
2. **自旋锁** 使用忙等待循环不停地检查锁是否已被释放。如果等待很少发生，这种方式更高效；但如果等待很常见，则会浪费 CPU 时间。
3. **读写锁** 允许多个「读取」线程同时进入一个区域，但在「写入」线程获取锁时，会排除所有其他线程（包括读取线程）。这种方式很有用，因为许多数据结构可以安全地让多个线程同时读取，但如果有其他线程正在读取或写入时，进行写入则是不安全的。
4. **递归锁** 允许单个线程多次获取同一个锁。当同一个线程重入时，非递归锁可能会导致死锁、崩溃或其他异常行为。

**API**  
Apple 的 API 中有许多不同的互斥工具。以下是一个很长的但并非详尽的列表：

1. `pthread_mutex_t`。
2. `pthread_rwlock_t`。
3. `dispatch_queue_t`。
4. 配置为串行的 `NSOperationQueue`。
5. `NSLock`。
6. `OSSpinLock`。

除此之外，Objective-C 还提供了 `@synchronized` 语言构造，目前它在 `pthread_mutex_t` 之上实现。与其他方式不同，`@synchronized` 不使用显式的锁对象，而是将任意一个 Objective-C 对象当作锁来对待。一个 `@synchronized(someObject)` 区域会阻止对任何使用同一对象指针的其他 `@synchronized` 区域的访问。这些不同的工具有不同的行为和能力：

1. `pthread_mutex_t` 是一个阻塞锁，可以选择配置为递归锁。
2. `pthread_rwlock_t` 是一个阻塞的读写锁。
3. `dispatch_queue_t` 可以用作阻塞锁。通过将其配置为并发队列并使用屏障 `block`，它可以用作读写锁。它还支持对锁定区域进行异步执行。
4. `NSOperationQueue` 可以用作阻塞锁。与 `dispatch_queue_t` 一样，它支持对锁定区域进行异步执行。
5. `NSLock` 是一个 Objective-C 类形式的阻塞锁。它的伴生类 `NSRecursiveLock` 顾名思义是一个递归锁。
6. `OSSpinLock` 顾名思义是一个自旋锁。

最后，`@synchronized` 是一个阻塞递归锁。

**值类型**  
请注意，`pthread_mutex_t`、`pthread_rwlock_t` 和 `OSSpinLock` 是值类型，而非引用类型。这意味着如果你对它们使用 `=`，你会得到一个副本。这一点非常重要，因为这些类型**不能被复制**！如果你复制了一个 `pthread` 类型，副本将不可用，并且当你试图使用它时可能会崩溃。处理这些类型的 `pthread` 函数假定这些值位于它们初始化时的同一内存地址，之后将它们移动到别处是个坏主意。`OSSpinLock` 不会崩溃，但你得到的是一个完全独立的锁，而这绝不会是你想要的。

如果你使用这些类型，必须小心永远不要复制它们，无论是显式地使用 `=` 运算符，还是隐式地（例如，将它们嵌入到 `struct` 中或在闭包中捕获它们）。

此外，由于锁本质上是可变对象，这意味着你需要用 `var` 而不是 `let` 来声明它们。

其他锁是引用类型，这意味着它们可以随意传递，并且可以用 `let` 声明。

**初始化**  
**2015-02-10 更新：** 本节描述的问题已经以惊人的速度过时了。Apple 昨日发布了 Xcode 6.3b1，其中包含 Swift 1.2。在其他变化中，C 结构体现在以一个空初始化器导入，该初始化器将所有字段设置为零。简而言之，你现在可以编写 `pthread_mutex_t()` 而无需我下面讨论的扩展。本节将保留以作为历史参考，但已不再适用于该语言。

在 Swift 中使用 `pthread` 类型很麻烦。它们被定义为包含大量存储的不透明 `struct`，例如：

```
    struct _opaque_pthread_mutex_t {
        long __sig;
        char __opaque[__PTHREAD_MUTEX_SIZE__];
    };
```

其意图是你声明它们，然后使用一个接受指向该存储的指针并填充它的 `init` 函数来初始化它们。在 C 中，它看起来像这样：

```
    pthread_mutex_t mutex;
    pthread_mutex_init(&mutex, NULL);
```

只要你记得调用 `pthread_mutex_init`，这就能正常工作。然而，Swift 非常非常不喜欢未初始化的变量。等效的 Swift 代码无法编译：

```
    var mutex: pthread_mutex_t
    pthread_mutex_init(&mutex, nil)
    // error: address of variable 'mutex' taken before it is initialized
```

Swift 要求变量在使用前必须被初始化。`pthread_mutex_init` 并没有使用传入变量的值，它只是覆盖了该变量，但 Swift 并不知道这一点，因此会产生一个错误。为了满足编译器，变量需要用某种方式初始化，但这比看起来要难。在类型后面使用 `()` 是行不通的：

```
    var mutex = pthread_mutex_t()
    // error: missing argument for parameter '__sig' in call
```

Swift 需要那些不透明字段的值。`__sig` 很容易，我们可以直接传零。`__opaque` 则比较烦人。以下是它被桥接到 Swift 中的方式：

```
    struct _opaque_pthread_mutex_t {
        var __sig: Int
        var __opaque: (Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8)
    }
```

没有简单的方法来获得一个全零的大元组，所以你必须全部写出来：

```
    var mutex = pthread_mutex_t(__sig: 0,
                             __opaque: (0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 0, 0))
```

这很糟糕，但我找不到一个好的变通方法。我能做的最好的办法就是把它包装在一个扩展（extension）中，这样空的 `()` 就能用了。以下是我创建的两个扩展：

```
    extension pthread_mutex_t {
        init() {
            __sig = 0
            __opaque = (0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0)
        }
    }

    extension pthread_rwlock_t {
        init() {
            __sig = 0
            __opaque = (0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0)
        }
    }
```

有了这些扩展，以下代码可以工作了：

```
    var mutex = pthread_mutex_t()
    pthread_mutex_init(&mutex, nil)
```

也许也可以将对 `pthread_mutex_init` 的调用合并到扩展初始化器中，但不能保证 `struct` 初始化器中的 `self` 指向正在被初始化的变量。由于这些值在被初始化后不能在内存中移动，我想将初始化作为一个单独的调用来保留。

**锁的包装（Wrapper）**  
为了更容易地使用这些不同的 API，我编写了一系列小的包装函数。我选择了 `with` 作为简洁、短小、类似语法的名字，灵感来自 Python 的 `with` 语句。Swift 的函数重载（overloading）允许对所有这些不同类型使用相同的名称。基本形式如下：

```
    func with(lock: SomeLockType, f: Void -> Void) { ...
```

这会在持有锁的情况下执行 `f`。让我们为所有这些类型实现它。

对于值类型，它需要接受一个指向锁的指针，以便锁定/解锁函数可以修改它。`pthread_mutex_t` 的实现只是调用适当的锁定和解锁函数，中间调用 `f`：

```
    func with(mutex: UnsafeMutablePointer<pthread_mutex_t>, f: Void -> Void) {
        pthread_mutex_lock(mutex)
        f()
        pthread_mutex_unlock(mutex)
    }
```

`pthread_rwlock_t` 的实现几乎相同：

```
    func with(rwlock: UnsafeMutablePointer<pthread_rwlock_t>, f: Void -> Void) {
        pthread_rwlock_rdlock(rwlock)
        f()
        pthread_rwlock_unlock(rwlock)
    }
```

我为这个还创建了一个配套函数，它接受一个写锁，看起来也非常相似：

```
    func with_write(rwlock: UnsafeMutablePointer<pthread_rwlock_t>, f: Void -> Void) {
        pthread_rwlock_wrlock(rwlock)
        f()
        pthread_rwlock_unlock(rwlock)
    }
```

`dispatch_queue_t` 的那个甚至更简单。它只是 `dispatch_sync` 的一个包装：

```
    func with(queue: dispatch_queue_t, f: Void -> Void) {
        dispatch_sync(queue, f)
    }
```

事实上，如果有人想聪明反被聪明误并混淆他人，他可以利用 Swift 的函数式特性，简单地写成：

```
    let with = dispatch_sync
```

这样做是不明智的，原因有几个，其中之一是它会打乱我们在这里尝试使用的基于类型的重载。

`NSOperationQueue` 在概念上是相似的，但没有直接等同于 `dispatch_sync` 的功能。相反，我们创建一个操作，将其添加到队列，并显式地等待它完成：

```
    func with(opQ: NSOperationQueue, f: Void -> Void) {
        let op = NSBlockOperation(f)
        opQ.addOperation(op)
        op.waitUntilFinished()
    }
```

`NSLock` 的实现看起来像 `pthread` 版本，只是锁定调用略有不同：

```
    func with(lock: NSLock, f: Void -> Void) {
        lock.lock()
        f()
        lock.unlock()
    }
```

最后，`OSSpinLock` 的实现又是类似的操作：

```
    func with(spinlock: UnsafeMutablePointer<OSSpinLock>, f: Void -> Void) {
        OSSpinLockLock(spinlock)
        f()
        OSSpinLockUnlock(spinlock)
    }
```

**模仿 @synchronized**  
有了这些包装，模仿 `@synchronized` 的基本功能就相当简单了。在你的类中添加一个持有锁的属性，然后在之前使用 `@synchronized` 的地方使用 `with`：

```
    let queue = dispatch_queue_create("com.example.myqueue", nil)

    func setEntryForKey(key: Key, entry: Entry) {
        with(queue) {
            entries[key] = entry
        }
    }
```

不幸的是，从 `block` 中获取数据就不那么令人愉快了。`@synchronized` 允许你从其中 `return`，但这在 `with` 里行不通。相反，你必须使用一个 `var` 并在 `block` 内对其赋值：

```
    func entryForKey(key: Key) -> Entry? {
        var result: Entry?
        with(queue) {
            result = entries[key]
        }
        return result
    }
```

应该可以将这个样板代码包装在一个泛型函数中，但我当时在让 Swift 编译器的类型推断配合工作时遇到了麻烦，目前还没有解决方案。

**模仿原子属性（Atomic Properties）**  
原子属性通常不太有用。问题在于，与代码的其他许多有用属性不同，原子性（atomicity）不具有组合性。例如，如果函数 `f` 不泄露内存，函数 `g` 也不泄露内存，那么仅仅调用 `f` 和 `g` 的函数 `h` 同样不会泄露内存。但原子性并非如此。举个例子，假设你有一组原子性的、线程安全的 `Account` 类：

```
    let checkingAccount = Account(amount: 100)
    let savingsAccount = Account(amount: 0)
```

现在你把钱转到储蓄账户：

```
    checkingAccount.withDraw(100)
    savingsAccount.deposit(100)
```

在另一个线程中，你汇总余额并告诉用户：

```
    println("Your total balance is: \(checkingAccount.amount + savingsAccount.amount)")
```

如果这发生在错误的时间点，它会打印出 0 而不是 100，尽管 `Account` 对象本身是完全原子性的，并且用户一直有 100 的余额。因此，通常更好的做法是构建整个子系统为原子性的，而不是单个属性。

在某些罕见的情况下，原子属性是有用的，因为那确实是一个独立的、只需要线程安全的实体。要在 Swift 中实现这一点，你需要一个将执行锁定操作的计算属性，以及一个实际持有值的普通属性：

```
    private let queue = dispatch_queue_create("...", nil)
    private var _myPropertyStorage: SomeType

    var myProperty: SomeType {
        get {
            var result: SomeType?
            with(queue) {
                result = _myPropertyStorage
            }
            return result!
        }
        set {
            with(queue) {
                _myPropertyStorage = newValue
            }
        }
    }
```

**选择你的锁 API**  
由于在 Swift 中使用 `pthread` API 比较困难，而且它们做不了其他 API 做不到的事情，所以可以立即排除它们。我经常在 C 和 Objective-C 中使用它们，因为它们相当直接快速，但在这里不值得，除非某些情况真的需要。

读写锁通常不值得担心。对于常见的情况，即读写操作很快，读写锁所使用的额外开销会超过允许多个并发读取的能力。

递归锁大部分情况下是在招致死锁。有些情况下它们是有用的，但如果你发现自己处在一个需要获取当前线程上已被锁定的锁的设计中，这很可能是一个好迹象，表明你**应该**重新考虑，以免去这种需求。

我的观点是，当有疑问时，默认选择 `dispatch_queue_t`。它们更重量级，但这很少有关系。API 相当方便，并且它们确保你永远不会忘记将锁定调用与解锁调用配对。它们提供了大量便捷的功能，随时可能派上用场，例如能够使用单个 `dispatch_async` 调用在后台运行锁定代码，或者能够设置计时器或其他针对队列本身的事件源，以便它们自动执行锁定。你甚至可以通过 `NSOperationQueue` 的 `underlyingQueue` 属性（OS X 10.10 和 iOS 8 中新增）将其用作 `NSNotificationCenter` 观察者和 `NSURLSession` 委托的目标等。

`NSOperationQueue` 希望它能像 `dispatch_queue_t` 一样酷，但将它用作锁 API 的理由少之又少（如果有的话）。它使用起来更麻烦，并且在作为锁定 API 的典型使用中不提供任何优势，尽管操作的自动依赖管理在其他上下文中有时会很有用。

`NSLock` 是一个简单的锁定类，易于使用且相当快。如果你出于某种原因想要显式的锁定和解锁调用，而不是 `dispatch_queue_t` 基于 `block` 的 API，它是一个不错的选择，但在大多数情况下几乎没有理由使用它。

`OSSpinLock` 是一个极佳的选择，适用于锁经常被获取、竞争低、锁定代码运行迅速的场合。它的开销要低得多，这有助于提升热代码路径的性能。另一方面，它不适用于代码可能长时间持有锁，或者竞争很常见的场景，因为这会浪费 CPU 时间。总的来说，默认选择 `dispatch_queue_t`，但如果 `OSSpinLock` 开始在分析器中显现出来，可以考虑它作为一种相当容易的优化。

**结论**  
Swift 没有用于线程同步的语言设施，但这个缺陷被 Apple 框架中丰富的锁定 API 充分弥补了。GCD 和 `dispatch_queue_t` 仍然是一个杰作，并且该 API 在 Swift 中运行得非常好。我们没有 `@synchronized` 或原子属性，但我们有更好的东西。

今天就到这里。下次回来，我们将进行更多激动人心的冒险。Friday Q&A 建立在像你这样读者的主题建议之上，所以如果你有希望在这里看到的内容，请 [发送过来](mailto:mike@mikeash.com)！

你喜欢这篇文章吗？我正在销售装满这些文章的书籍！卷 II 和卷 III 现已出版！它们有 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。 [点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2015-02-06-locks-thread-safety-and-swift.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
