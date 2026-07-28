---
title: 'Friday Q&A 2011-09-02：让我们构建 NSAutoreleasePool'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-09-02-lets-build-nsautoreleasepool.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:df788907df6e1ce1'
translated: true
---

> 原文：[Friday Q&A 2011-09-02: Let's Build NSAutoreleasePool](https://www.mikeash.com/pyblog/friday-qa-2011-09-02-lets-build-nsautoreleasepool.html)　·　mikeash.com Friday Q&A

发表于 2011-09-02 16:30 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)）| [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2011-09-16: Let's Build Reference Counting](https://www.mikeash.com/pyblog/friday-qa-2011-09-16-lets-build-reference-counting.html)  
上一篇文章：[Friday Q&A 2011-08-19: Namespaced Constants and Functions](https://www.mikeash.com/pyblog/friday-qa-2011-08-19-namespaced-constants-and-functions.html)  
标签：[autorelease](https://www.mikeash.com/pyblog/?tag=autorelease) [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild)

Friday Q&A 2011-09-02：让我们构建 NSAutoreleasePool

作者：[Mike Ash](https://www.mikeash.com/)

**高层概述**  
当向对象发送 `autorelease` 消息时，整个流程便启动了。`autorelease` 在 `NSObject` 上实现，它只是接着调用 `[NSAutoreleasePool addObject: self]`。这是一个类方法，它需要找到正确的实例（instance）进行通信。

`NSAutoreleasePool` 的实例存储在每个线程（thread）的栈中。当创建一个新池时，它会被推入栈顶。当销毁一个池时，它会从栈中弹出。当 `NSAutoreleasePool` 类方法需要查找当前池时，它会获取当前线程的栈并取出栈顶的池。

一旦找到正确的池，就使用 `addObject:` 实例方法将对象添加到池中。当一个对象被添加到池中时，它只是被添加到了该池维护的一个对象列表中。

当池被销毁时，它会遍历这个对象列表，向每个对象发送 `release` 消息。基本上这就是全部内容了。还有一个小的额外复杂之处：如果被销毁的池不在池栈的顶部，它还会销毁位于其上方的所有其他池。简而言之，`NSAutoreleasePool` 实例是嵌套的，如果你没有销毁一个内部池，外部池在销毁时会处理它。

**垃圾回收（Garbage Collection）**  
`NSAutoreleasePool` 在垃圾回收机制下仍然存在，甚至还能发挥一点作用。如果你使用 `drain` 消息而不是 `release` 消息，那么在垃圾回收机制下销毁一个池会向回收器发出信号，表明现在可能是运行一次回收周期的好时机。然而除此之外，`NSAutoreleasePool` 在垃圾回收机制下什么也不做，因此不值得过多考虑。在本文中，我将忽略垃圾回收机制，专注于传统的内存管理。

**10.7 和 ARC**  
10.7 对自动释放池进行了重大的内部改造，Apple 也正在引入一套全新的自动引用计数（Automatic Reference Counting）系统。尽管细节变化很大，但自动释放池的工作原理概念并未改变，因此这里的所有内容仍然有效。

**接口（Interface）**  
我的自动释放池类版本将命名为 `MAAutoreleasePool`。如果你想查看完整代码，它[托管在 GitHub 上](https://github.com/mikeash/MAAutoreleasePool)。

这个类拥有用于 `addObject:` 的类方法和实例方法，以及一个用于保存自动释放对象列表的 `CFMutableArray`。使用 `CFMutableArray` 而不是 `NSMutableArray`，是因为 `NSMutableArray` 自动的 `retain` 和 `release` 行为会干扰我们在这里要做的事情。此外，`NSMutableArray` 内部有可能使用 `autorelease`，这会让事情变得非常混乱。`CFMutableArray` 可以被配置为不处理其内容的任何内存管理，这正是我们想要的。

接口如下所示：

```
    @interface MAAutoreleasePool : NSObject
    {
        CFMutableArrayRef _objects;
    }

    + (void)addObject: (id)object;

    - (void)addObject: (id)object;

    @end
```

另外，为了匹配官方实现，需要在 `NSObject` 上有一个辅助方法。我将其命名为 `ma_autorelease` 以区别于真正的实现并避免名称冲突：

```
    @interface NSObject (MAAutoreleasePool)

    - (id)ma_autorelease;

    @end
```

正如我上面提到的，它的实现只是对类方法的一个封装：

```
    @implementation NSObject (MAAutoreleasePool)

    - (id)ma_autorelease
    {
        [MAAutoreleasePool addObject: self];
        return self;
    }

    @end
```

**池栈（Pool Stack）**  
自动释放池保存在一个栈中。每个线程都有自己的池栈，当对象被自动释放时，用它来确定将该对象放入哪个池。

为了封装对栈的管理，我编写了一个私有方法 `+_threadPoolStack`，它返回当前线程的 `MAAutoreleasePool` 实例栈，必要时会创建它。与每个池包含的对象列表一样，池栈也是一个 `CFMutableArray`，以防止 `NSMutableArray` 的自动内存管理造成问题。

在 Cocoa 中处理线程本地存储的最简单方式是使用 `NSThread` 的 `threadDictionary` 方法。这个方法返回一个 `NSMutableDictionary`，它对于当前线程是唯一的，并且在线程终止时会自动销毁。

因此，这个方法首先获取该字典，并声明一个唯一键来关联池栈：

```
    + (CFMutableArrayRef)_threadPoolStack
    {
        NSMutableDictionary *threadDictionary = [[NSThread currentThread] threadDictionary];

        NSString *key = @"MAAutoreleasePool thread-local pool stack";
```

接下来，它从该字典中获取栈（作为 `CFMutableArray`）：

```
        CFMutableArrayRef array = (CFMutableArrayRef)[threadDictionary objectForKey: key];
```

在任何给定线程上首次运行此方法时，栈还不存在。这种情况下，需要创建它并存储到字典中：

```
        if(!array)
        {
            array = CFArrayCreateMutable(NULL, 0, NULL);
            [threadDictionary setObject: (id)array forKey: key];
            CFRelease(array);
        }
```

最后，无论是检索到的还是新创建的数组，都将其返回：

```
        return array;
    }
```

现在，这个方法已经就位，其他方法就可以实现了。`+addObject:` 方法基本上就是调用上述方法，然后将 `addObject:` 转发给栈顶的池。我添加了一些偏执的检查，以确保栈不为空，并在为空时打印错误信息：

```
    + (void)addObject: (id)object
    {
        CFArrayRef stack = [self _threadPoolStack];
        CFIndex count = CFArrayGetCount(stack);
        if(count == 0)
        {
            fprintf(stderr, "Object of class %s autoreleased with no pool, leaking\n", class_getName(object_getClass(object)));
        }
        else
        {
            MAAutoreleasePool *pool = (id)CFArrayGetValueAtIndex(stack, count - 1);
            [pool addObject: object];
        }
    }
```

**实例方法（Instance Methods）**  
这个类的 `-init` 方法非常简单。初始化 `_objects` 数组，将 `self` 添加到池栈顶部，然后返回：

```
    - (id)init
    {
        if((self = [super init]))
        {
            _objects = CFArrayCreateMutable(NULL, 0, NULL);
            CFArrayAppendValue([[self class] _threadPoolStack], self);
        }
        return self;
    }
```

`-addObject:` 方法更简单：只需将给定的对象添加到 `_objects` 的末尾：

```
    - (void)addObject: (id)object
    {
        CFArrayAppendValue(_objects, object);
    }
```

由于需要处理池的嵌套，`-dealloc` 方法变得更复杂一些。它开始时相当简单：遍历 `_objects` 数组并向其中的每个对象发送 `release` 消息：

```
    - (void)dealloc
    {
        if(_objects)
        {
            for(id object in (id)_objects)
                [object release];
            CFRelease(_objects);
        }
```

接下来，它将 `self` 从池栈中移除。此外，还需要移除那些位于池栈中 `self` 上方的任何池。因为此过程需要向后迭代，并且需要在迭代过程中修改栈，所以它使用了一个手动基于索引的循环：

```
        CFMutableArrayRef stack = [[self class] _threadPoolStack];
        CFIndex index = CFArrayGetCount(stack);
        while(index-- > 0)
        {
            MAAutoreleasePool *pool = (id)CFArrayGetValueAtIndex(stack, index);
```

如果 `pool` 是 `self`，那么循环就结束了。需要做的就是将该条目从栈中移除，然后跳出循环。当前池以下的所有池都保持不变：

```
            if(pool == self)
            {
                CFArrayRemoveValueAtIndex(stack, index);
                break;
            }
```

如果是其他池，则需要销毁它。只需向它发送一个 `release` 消息即可。其他所有必要操作都会自动完成：

```
            else
            {
                [pool release];
            }
        }
```

这可能一开始有点难以理解，我花了一点时间才意识到这段代码需要如何编写。当执行到这行代码时，`pool` 必然在栈顶。当它被释放时，它会被回收（retain 自动释放池是不合法的）。当它被回收时，它会调用自己的 `-dealloc`，后者再次进入同一个循环。这个循环会立即命中 `pool == self` 条件，将该池从栈中移除并退出。因此，栈中当前正在销毁的池上方的所有池也会被销毁并从栈中移除。

循环现在结束了，剩下的就是调用 `super` 方法：

```
        [super dealloc];
    }
```

这个类现在完成了！

**经验教训**  
从这个练习中可以学到一些很好的经验。最重要的是，`NSAutoreleasePool` 是一个相当直接的类，没有太多隐藏的陷阱。幕后没有什么复杂的事情发生。刚接触 Cocoa 内存管理的人经常认为 `autorelease` 比实际情况复杂得多，会问诸如“如何判断一个对象是否已被自动释放？”或“如果我两次自动释放一个对象会怎样？”之类的问题。具体来说，我们现在可以看到：

- 没有办法判断一个对象是否已被自动释放。池是一个相当简单的容器，对它所包含的内容只有最模糊的认识。它实际上只是维护一个列表，以便稍后向这些对象发送 `release` 消息。这完全没问题，因为你的代码永远不需要关心一个对象是否已经被自动释放了。
- 被自动释放两次的对象只会被添加到池中两次，然后当池被销毁时，它们会被释放两次。
- 自动释放的对象会在当前自动释放池被销毁时被释放。池的销毁发生在创建它的代码显式销毁它的时候。如果你不管理自己的池，那么自动释放的对象至少会存活到你将控制权交还给你不拥有的代码（例如 Cocoa）之时。
- 如果你在一个线程上自动释放一个对象，然后将其传递给另一个线程，不会发生什么特殊的事情。当第一个线程的池被销毁时，该对象仍然会被释放，无论新线程上发生了什么。如果你需要一个对象在传递过程中存活下来，需要在发送之前 retain 它，并在接收之后 release 它。（幸运的是，你可能用于对象的跨线程消息传递机制，如 GCD/block 和 Cocoa 的 `perform...` 方法，会为你处理这些。）

**结论**  
以上就是今天对 Cocoa 内部机制的探索。现在你大概了解了 `NSAutoreleasePool` 是如何完成其工作以及它是如何运作的了。具体实现细节会有所不同（尤其是在 Lion 上），但基本思想是相同的。通过了解内存管理的内部工作原理，你可以编写更好、更不易出错的代码。

除非你是这个博客的新读者，否则你可能已经知道 Friday Q&A 是由读者提交驱动的。就此而言，如果你有希望被涵盖的主题，请[发送给我](mailto:mike@mikeash.com)！

你喜欢这篇文章吗？我正在出售包含这些文章的整套书！第二卷和第三卷现已上市！格式包括 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-09-02-lets-build-nsautoreleasepool.html)

发表你的想法，发表评论：

垃圾邮件和无关话题的帖子将被删除，恕不另行通知。违规者可能会由我自行决定被公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
