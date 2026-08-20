---
title: 'Friday Q&A 2011-03-04: OSAtomic 漫游'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-03-04-a-tour-of-osatomic.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:adfc834d710a1a58'
translated: true
---

> 原文：[Friday Q&A 2011-03-04: A Tour of OSAtomic](https://www.mikeash.com/pyblog/friday-qa-2011-03-04-a-tour-of-osatomic.html)　·　mikeash.com Friday Q&A

发布于 2011-03-04 18:24 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[来西雅图 Voices That Matter 大会看我的演讲](https://www.mikeash.com/pyblog/see-me-speak-at-voices-that-matter-in-seattle.html)  
上一篇文章：[Friday Q&A 2011-02-18: 复合字面量](https://www.mikeash.com/pyblog/friday-qa-2011-02-18-compound-literals.html)  
标签：[atomic](https://www.mikeash.com/pyblog/?tag=atomic) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [threading](https://www.mikeash.com/pyblog/?tag=threading)

Friday Q&A 2011-03-04: OSAtomic 漫游

作者：[Mike Ash](https://www.mikeash.com/)

**多线程编程与原子操作**  
 凡是做过线程（thread）编程的人都知道，这很困难。真的非常困难。多线程执行时，多个线程之间交互的时间点高度不可预测。结果就是，看起来正确、能通过测试的代码，可能会以一种罕见到诡异的方式失败，潜藏着微妙的缺陷。

编写多线程代码时有许多规则要遵循，但最重要的一条是：**锁住所有对共享数据的访问**。

共享数据就是任何可能被超过一个线程访问的数据。如果你有共享数据，那么你_必须_使用锁来同步这些访问。多线程编程的另一种方法是放弃共享数据，改用消息传递（message passing），这意味着同一时间只有一个线程会访问消息和任何共享数据。

原子操作（atomic operations）让你可以绕过这一要求，无需使用锁就能访问共享数据。这里的“atomic”一词不是原子弹或原子反应堆那个意思，而是源自希腊语的“不可分割”。原子操作是一次性完成的操作，在执行过程中不会被其他线程中断。`OSAtomic` 就是 OS X 中提供这类原子操作（atomic operation）的库。

**头文件**  
 OSAtomic 函数位于 `OSAtomic.h` 头文件中，路径是 `/usr/include/libkern/OSAtomic.h`。请注意，尽管路径里含有 `kern`，这些函数在普通的用户态代码中也完全可以正常使用。你可以这样导入该文件：

```
    #import <libkern/OSAtomic.h>
```

这些函数可以划分为五个基本类别：

- 整数操作（Integer operations）
- 基础操作（Fundamental operations）
- 自旋锁（Spinlocks）
- 队列（Queues）
- 内存屏障（Memory barriers）

我将按这个顺序逐一讨论这些类别。

在开始之前，我想先简要谈一下内存屏障（memory barriers）。前两类中的所有函数都有两种变体。一种是基本函数，另一种是相同的函数但在名称末尾加上了 `Barrier`。目前我先忽略这两者之间的区别，在关于内存屏障的小节中再详细讨论。在此之前，我先说明一个关于这些变体的简单事实：使用 `Barrier` 变体来代替基本变体总是安全的，唯一的问题是一点点性能损失，所以除非你确切知道自己在做什么，否则就用 `Barrier` 版本。

**关于数据类型与对齐的简单说明**  
 由于原子操作的性质精细且底层，数据类型的长度和对齐方式有严格限制。原子操作只支持 32 位和 64 位数据类型，在某些平台上（据我所知，OS X 上只有 PowerPC），甚至只支持 32 位。始终使用尺寸确定的类型，比如 `int32_t`，而不是像 `int` 这样的内置类型。

这些值还必须按其尺寸对齐。这意味着值的地址必须是其尺寸的整数倍。通常情况下，这由系统为你处理。OS X 上的对象和内存分配是按 16 字节边界对齐的，编译器会确保各个数据成员在该范围内分配。只有当你胡乱摆弄地址，试图实现自己的压缩排列或使用压缩结构体（packed structs）时，才需要考虑对齐问题。嗯，不要对这些使用原子操作。

**整数操作**  
 整数操作是头文件中最先出现的一类，它们的操作方式与标准 C 整数操作类似。它们都就地修改值，因此实际上等同于 C 的复合赋值运算符，比如 `+=`。

既然 C 已经提供了这些运算符，为什么还需要这些函数呢？和本头文件中的其他函数一样，关键在于原子性（atomicity）。考虑以下代码：

```
    x += 1;
```

然后考虑一下，如果有多个线程同时执行这段代码，操作同一个 `x`，会发生什么。在底层，这一行代码会被分解成多个操作：

```
    fetch value of x
    add 1
    store new value of x
```

在某些架构上，这发生在汇编层面，在某些架构上则发生在硬件层面，但这确实可能发生。两个线程可能同时获取了 x 的当前值，各自加 1，然后存储，导致一次递增被遗漏。等价的 `OSAtomic` 函数不会出现这个问题，两个线程执行后的结果保证是正确的。

`+=` 的原子等价物是 `OSAtomicAdd32`（在支持的平台上也有对应的 64 位版本）。它接受一个要加上的量和一个指向要修改的值的指针。它还会返回新值，这能让你更好地在线程之间协调。例如，你可能有好几个线程，每个线程都想处理数组中的一个单独元素。通过使用返回值，你可以为每个线程分配唯一的索引：

```
    // 初始化，在线程启动之前
    int32_t sharedIndex = 0;
    
    // 在每个线程中获取索引
    int index = OSAtomicAdd32(1, &sharedIndex) - 1;
    // 减去 1，因为它返回的是 NEW（新）值
```

如果有必要，你可以通过传递一个负数来使用这个方法执行减法。

还有一些便捷函数，等价于 `++` 和 `--`，即 `OSAtomicIncrement` 和 `OSAtomicDecrement`。使用 `OSAtomicIncrement32` 可以让上面的代码稍微简化一些。

还有用于执行按位逻辑运算的函数。`|=`、`&=` 和 `^=` 运算符对应的原子版本是 `OSAtomicOr`、`OSAtomicAnd` 和 `OSAtomicXor`。这些函数的用途比较特殊，但在以线程安全的方式操作位域（bitfields）时非常有用。

**基础操作**  
 上述所有整数操作，至少从概念上讲，都构建在一个单一的基础原子操作之上：比较并交换（compare and swap）。比较并交换函数接受一个旧值、一个新值以及一个指向变量的指针。当且仅当该变量的当前值与旧值匹配时，它会用新值替换变量的内容。它还会返回操作是成功（变量匹配旧值）还是失败（变量不匹配）。为了更清楚地说明，可以想象这样一个函数：

```
    bool CompareAndSwap(int old, int new, int *value)
    {
        if(*value == old)
        {
            *value = new;
            return true;
        }
        else
            return false;
    }
```

比较并交换操作就是这样的工作方式，区别在于比较并交换是一个原子操作。它不能在中间被中断或抢占。如果新值被赋值并且函数返回 `true`，那么你可以绝对确定，这个值直接从 `old` 变成了 `new`，中间没有经过任何其他中间值。

这为我们构建更复杂、更有用的原子操作提供了基础。使用比较并交换的基本模型是“事务（transaction）”模型，就像你在数据库中看到的一样。概念上，你编写代码：开始一个事务，执行一个本地修改，然后尝试提交这个事务。提交是通过比较并交换来完成的。如果提交失败，会表现为比较并交换返回 `false`，那么你就回到起点，开始一个新的事务再试一次。

`OSAtomic` 通过 `OSAtomicCompareAndSwap` 系列函数提供了这个操作。有针对 32 位整数的、有针对指针的、有针对 `int` 和 `long` 的。在支持的平台上，还有针对 64 位整数的版本。

为了看看如何使用这些函数，让我们考虑如何用比较并交换来实现 `OSAtomicAdd32`。同样，它使用事务模型。首先，获取原始值。然后进行加法运算得到新值。最后，用原始值和新值进行比较并交换。如果失败，就回去重试所有步骤。代码实现如下：

```
    int32_t OSAtomicAdd32(int32_t howmuch, volatile int32_t *value)
    {
        bool success;
        int32_t new;
        
        do {
            int32_t orig = *value;
            new = orig + howmuch;
            success = OSAtomicCompareAndSwap32(orig, new, value);
        } while(!success);
        
        return new;
    }
```

真正的实现可能会更高效，例如使用直接执行原子加法的 CPU 原语。出于这个原因，而且仅仅是为了避免重复代码，你更愿意调用内置函数而不是写出上面那个长版本。然而，比较并交换的存在创造了灵活性，因为你不仅限于加法、或、与和异或。你可以编写类似的函数来实现原子乘法或除法。此外，你还可以对指针使用比较并交换，这才是真正开始大显身手的地方。

例如，这是一个将节点添加到链表头部的函数：

```
    void AddNode(ListNode *node, ListNode * volatile *head)
    {
        bool success;
        
        do {
            ListNode *orig = *head;
            node->next = orig;
            success = OSAtomicCompareAndSwapPtrBarrier(orig, node, (void *)head);
        } while(!success);
    }
```

注意我这里使用了 `Barrier` 变体。这是因为比较并交换操作使 `node` 中包含的数据对其他线程可见，而屏障（barrier）是确保所有线程在能够看到这些数据之前，数据已经正确更新所必需的。正如我之前提到的，稍后我会更详细地讨论屏障。

这是一个配套函数，用于“窃取”链表。它把链表替换成空链表（也就是 `NULL`），并返回旧的链表头，以便进行操作：

```
    ListNode *StealList(ListNode * volatile *head)
    {
        bool success;
        ListNode *orig;
        
        do {
            orig = *head;
            success = OSAtomicCompareAndSwapPtrBarrier(orig, NULL, (void *)head);
        } while(!success);
        
        return orig;
    }
```

这种结构在多线程编程中非常有用。许多线程可以安全地使用 `AddNode` 向结构中添加新节点。然后，一个工作线程可以使用 `StealList` 抓取链表并进行处理。

**ABA 问题**  
 你可能想知道为什么我实现的是 `StealList`，而不是比如说 `RemoveNode`。答案是，`RemoveNode` 比看起来要难。你可能认为可以像这样实现它：

```
    ListNode *RemoveNode(ListNode * volatile *head)
    {
        bool success;
        ListNode *orig;
        
        do {
            orig = *head;
            ListNode *next = orig->next;
            success = OSAtomicCompareAndSwapPtrBarrier(orig, next, (void *)head);
        } while(!success);
        
        return orig;
    }
```

麻烦在于，有一种微妙的场景会导致它严重失败。假设链表开始时看起来像这样：

```
    A -> B -> C
```

这个函数开始执行。`orig` 指向 A，`next` 指向 B。但是，在执行到比较并交换之前，它被抢占，另一个线程开始运行。那个线程调用了两次 `RemoveNode`，使链表变成这样：

```
    C
```

然后那个线程将 A 重新添加回链表，并销毁了 B。链表现在看起来像这样：

```
    A -> C
```

最后，原来的线程恢复执行。它执行比较并交换，用 B 替换 A。由于链表头是 A，所以比较并交换成功了。然而，结果是一场灾难！链表头现在变成了 B，而 B 已经被销毁了。C 丢失了，接下来任何操作链表的代码都会尝试访问 B 并崩溃。哎呀。

这是一个相当罕见的场景，但正是这种罕见性使其变得严重。编写多线程代码时，你最不想要的就是写出很少出错的代码。它最好经常出错，或者根本不出错，否则将很难追踪和修复。

**测试并设置（Test and Set）**  
 测试并设置是一种有些专门化的基础原子操作。它不如比较并交换有用，但在某些情况下很方便。不过，我自己从未有机会使用它，它通常仅限于实现锁和信号量（semaphores）。通常，最好使用那些更高层次的抽象，而不是尝试自己实现它们。

**自旋锁（Spinlocks）**  
 自旋锁（spinlock）是一种原始类型的锁，不使用任何操作系统设施。锁（lock）总的来说是一种提供线程间互斥（mutual exclusion）的设施。两个线程尝试获取一个锁。一个成功，另一个等待。当第一个线程解锁后，第二个线程就获取它。

通常，当第二个线程在等待时，我们希望它被阻塞（blocked），这样在它被阻塞时就不会消耗任何 CPU 时间。这需要操作系统介入来停止该线程，并在解锁时重新启动它。这种操作系统介入会带来一定量的开销，而这并不总是我们想要的。

自旋锁非常轻量，完全在用户态运行。缺点是，当一个线程等待时，它不会被阻塞，而是不断检查自旋锁，直到它被解锁。当锁没有竞争（一次只有一个线程访问）时，自旋锁性能非常好，但当锁被长时间争用时，性能会很差。

自旋锁是一个类型为 `OSSpinLock` 的原始值。然后，你将指向自旋锁的指针传给 `OSSpinLockTry`、`OSSpinLockLock` 或 `OSSpinLockUnlock` 来完成各种操作。就基本语义而言，它们与 `pthread_mutex` 或 `NSLock` 相同，只是实现方式不同。通常你应该使用那些更高层次的抽象，但当性能绝对关键且竞争很少发生时，自旋锁就很有用。

**队列（Queues）**  
 这个名称有点误导，因为它提供的设施实际上是栈（stack），而不是队列。但是，OSAtomic 把它们叫做 `OSQueue`，所以就叫“队列”了。

不幸的是，经过进一步调查，我发现 `OSQueue` 并非完全线程安全，因此不应该使用。由于我不知道这会不会、或者什么时候会被修复，你应该避免使用 `OSQueue`。

**内存屏障（Memory Barriers）**  
 多线程编程的一个主要挑战是处理这样一个事实：不仅由于时序和操作系统问题会有很多奇怪的行为，而且硬件有时也会引发问题。某些架构会重排内存读取和写入以获取额外速度。这些重排对 CPU 来执行程序的代码是隐藏的，但对同时在其他 CPU 上执行的代码_并_不隐藏。这可能导致严重的问题。

举一个可能导致麻烦的场景示例，考虑以下代码：

```
    volatile Structure *gStructure;
    
    // 线程 1
    Structure *s = malloc(sizeof(s));
    s->field1 = 0;
    s->field2 = 42;
    gStructure = s;
    
    // 线程 2
    Structure *s;
    while((s = gStructure) == NULL)
        /* 轮询 */;
    printf("%d\n", s->field2);
```

这段代码很可能导致线程 2 打印出错误的值。如果 CPU 重排了线程 1 中的写入，使得对 `gStructure` 的赋值发生在对字段的赋值之前，就可能发生这种情况。将东西标记为 `volatile` 并不能解决这个问题，因为那只能控制潜在的_编译器_重排，而不是 CPU 重排。

内存屏障（Memory barriers）是解决这个问题的一种方法。内存屏障强制执行：屏障之前的所有读取都完成之前，屏障之后的任何读取都不能开始。写入也是如此。技术上，可以有独立的读写屏障，但 OSAtomic 将它们合并为一个单一的概念。

如果你只想要一个普通的内存屏障，可以使用 `OSMemoryBarrier`。这个函数不接受参数，也不返回任何值，它存在的唯一目的就是充当内存屏障。上面的代码可以重构为：

```
    // 线程 1
    Structure *s = malloc(sizeof(s));
    s->field1 = 0;
    s->field2 = 42;
    OSMemoryBarrier();
    gStructure = s;
    
    // 线程 2
    Structure *s;
    while((s = gStructure) == NULL)
        /* 轮询 */;
    OSMemoryBarrier();
    printf("%d\n", s->field2);
```

这是安全的。技术上，第二个线程中的屏障可能不是必需的，因为第二次读取依赖于第一次读取。（在获取 `s->field2` 的值之前，`s` 的值必须可用。）然而，这些事情很难推理透彻，我通常宁愿求稳，而不是试图弄清楚是否_真的_需要。

除了这个函数之外，OSAtomic 还为其所有原子操作提供了内存屏障。所有原子函数的 `Barrier` 变体意味着，它们不仅完成给定的原子操作，而且还整合了一个内存屏障。当你执行一个原子操作，该操作的影响超出了你正在操作的那一个数据块时，这非常有用。

作为一般经验法则，独立的计数器、标志位以及其他自包含的、存在于你正在操作的单个 32 位或 64 位值内的数据块不需要屏障。任何原子操作表明关于该操作值之外的数据的信息时，都需要一个屏障。

当你不确定时，请使用屏障。仅有的缺点就是一点点性能代价。

**结论**  
 多线程编程很困难。共享数据让它更难。没有锁的共享数据则难上加难。然而，在某些情况下，以这种方式编程可能很有用，当你绝对需要无锁的多线程代码时，`OSAtomic` 为你提供了构建模块。

今天就到这里。14 天后，欢迎回来阅读友好的社区 Friday Q&A 的下一期精彩内容。一如既往，Friday Q&A 由读者驱动，所以如果你有想在这里看到的话题创意，[请发送过来](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我出版了几本包含全部文章的书！第二卷和第三卷现已上市！它们有 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-03-04-a-tour-of-osatomic.html)

发表你的想法，添加评论：

垃圾邮件和离题帖子将恕不另行通知即被删除。违规者可能由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
