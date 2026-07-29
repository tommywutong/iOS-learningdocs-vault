---
title: 'Friday Q&A 2011-09-16：让我们构建引用计数'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-09-16-lets-build-reference-counting.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a787a3653b86b426'
translated: true
---

> 原文：[Friday Q&A 2011-09-16: Let's Build Reference Counting](https://www.mikeash.com/pyblog/friday-qa-2011-09-16-lets-build-reference-counting.html)　·　mikeash.com Friday Q&A

发布于 2011-09-16 14:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2011-09-30：自动引用计数](https://www.mikeash.com/pyblog/friday-qa-2011-09-30-automatic-reference-counting.html)  
上一篇文章：[Friday Q&A 2011-09-02：让我们构建 NSAutoreleasePool](https://www.mikeash.com/pyblog/friday-qa-2011-09-02-lets-build-nsautoreleasepool.html)  
标签：[cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [memory](https://www.mikeash.com/pyblog/?tag=memory)

Friday Q&A 2011-09-16：让我们构建引用计数

作者 [Mike Ash](https://www.mikeash.com/)

**背景**  
读到这里的读者大概已经对什么是引用计数（reference counting）有了基本的了解，但详细讨论一下有助于确保相关概念清晰明确。

每个 Objective-C 对象都有一个关联的引用计数。在 Cocoa 术语中，这被称为“retain count”，但我认为这只会造成混淆，所以我会使用“引用计数”。一个新创建的对象初始引用计数为 `1`。`retain` 消息会递增它，而 `release` 消息会递减它。如果 `release` 将引用计数递减到零，对象会通过发送 `dealloc` 消息被销毁。

由于引用计数是通过普通的 Objective-C 消息实现的，因此特定类可以覆盖该行为。只要覆盖遵循上述语义，一切都能正常工作。

出于现在很大程度上已成为历史的原因，`NSObject` 中的默认引用计数实现并不将引用计数存储在对象本身中。相反，引用计数存储在外部表中。这可以以速度为代价节省一些内存。我将在我的引用计数重实现中复制这种基于表的方法。

Core Foundation 对象和许多其他 Cocoa 对象会覆盖 `retain` 和 `release`，以便将引用计数存储在对象本身中，从而提高一些性能。

**Lion 和 ARC**  
Lion 和 ARC 都对 Cocoa 内存管理（memory management）系统进行了一些重大更改，但上述基础知识仍然成立。Lion 重新实现了基于表的引用计数系统，使其大大加快，但基本思想仍然相同。

ARC 仍然会在幕后进行 `retain` 和 `release`。出于性能原因，它实际上会调用运行时函数来执行 `retain` 和 `release`，这些函数在某些情况下能够绕过 Objective-C 消息发送。然而，它仍然尊重 `retain` 和 `release` 的覆盖，并且_在概念上_ ARC 仍然只是向其管理的对象发送 `retain` 和 `release` 消息。

**源代码**  
和往常一样，今天的代码可在 GitHub 上获取：[https://github.com/mikeash/refcounting](https://github.com/mikeash/refcounting)

**设计**  
在深入代码本身之前，让我们先讨论一下这个设计的具体细节。有两个方法需要实现。为了将它们与 Cocoa 的区分开，我将它们命名为 `ma_retain` 和 `ma_release`。

引用计数表将使用 `CFMutableDictionary` 实现，将对象指针映射到整数。这提供了一种相当快速和直接的方法。

为了简化操作，引用计数 `1` 将通过表中完全没有条目来表示。换句话说，任何指针的引用计数默认为 `1`。这意味着新对象会自动获得正确的引用计数 `1`。Cocoa 的实现也是这么做的。

线程安全性（Thread safety）对于任何引用计数实现都至关重要。一个类通常无法控制它在哪些线程上被 retain 和 release，即使是一个在其他方面不是线程安全的类也需要能够承受同时在多个线程上被 retain 和 release，因为跟踪和控制 retain 和 release 发生在哪里极其困难。为了使 `CFMutableDictionary` 安全，我使用 `OSSpinLock` 保护它。任何锁都可以，但自旋锁（spinlock）非常适合这种情况，只要临界区够快，它们的开销就很低。

表上有两个基本操作：`GetRefcount` 和 `SetRefcount`。它们负责操作表的繁重工作，包括将缺少条目视为 `1`、在其引用计数降到 `2` 以下时从表中移除对象，等等。它们不锁定自旋锁，这留待调用者处理。这是必需的，因为 `ma_retain` 和 `ma_release` 都需要在表上原子地执行两个操作，所以它们需要将两者都锁定。

在这两个基本操作之上，有两个稍高层次的函数：`IncrementRefcount` 和 `DecrementRefcount`。`IncrementRefcount` 接受一个指针，并简单地增加该指针在表中的引用计数。`DecrementRefcount` 接受一个指针并递减其引用计数。它还返回新的计数，这对于实现对象释放（deallocation）很重要。

最后是方法，它们是这些高层函数的薄包装。`ma_retain` 只调用 `IncrementRefcount`。`ma_release` 调用 `DecrementRefcount`，如果返回值是 `0`，则调用 `[self dealloc]`。

**代码**  
厌倦了文字？让我们来看一些代码。

两个全局变量用于引用计数表。一个是表本身的字典，另一个是自旋锁：

```
    static CFMutableDictionaryRef gRefcountDict;
    static OSSpinLock gRefcountDictLock;
```

`GetRefcount` 函数检索给定指针的当前引用计数。`gRefcountDict` 变量被延迟初始化，按需进行，所以这个函数首先检查字典是否已经初始化。如果没有，那么它知道_没有_对象有引用计数，所以这个对象的引用计数_必定_是 `1`：

```
    static uintptr_t GetRefcount(void *key)
    {
        if(!gRefcountDict)
            return 1;
```

如果字典确实存在，它就从其中获取值。如果该值不存在，则再次返回 `1`。否则返回字典中的任何值：

```
        const void *value;
        if(!CFDictionaryGetValueIfPresent(gRefcountDict, key, &value))
            return 1;

        return (uintptr_t)value;
    }
```

`SetRefcount` 函数将给定指针的引用计数设置为给定值。如果该值为 `1` 或 `0`，它会简单地将对象从表中移除：

```
    static void SetRefcount(void *key, uintptr_t count)
    {
        if(count <= 1)
        {
            if(gRefcountDict)
                CFDictionaryRemoveValue(gRefcountDict, key);
        }
```

如果表尚未创建，则无需执行任何操作，因为不可能有要移除的条目。

如果要设置的值大于 `1`，它首先延迟初始化表，然后在表中设置对象的值：

```
        else
        {
            if(!gRefcountDict)
                gRefcountDict = CFDictionaryCreateMutable(NULL, 0, NULL, NULL);
            CFDictionarySetValue(gRefcountDict, key, (void *)count);
        }
    }
```

`IncrementRefcount` 函数接受一个指针并递增其在表中的值。为此，它首先获取自旋锁。持有锁后，它获取当前值，加一，然后设置该新值。最后，它释放自旋锁：

```
    static void IncrementRefcount(void *key)
    {
        OSSpinLockLock(&gRefcountDictLock);
        uintptr_t count = GetRefcount(key);
        SetRefcount(key, count + 1);
        OSSpinLockUnlock(&gRefcountDictLock);
    }
```

`DecrementRefcount` 函数非常相似。唯一的真正区别是它需要返回新的计数。为了实现这一点，它将新计数保存在一个临时变量中，然后在函数末尾返回它：

```
    static uintptr_t DecrementRefcount(void *key)
    {
        OSSpinLockLock(&gRefcountDictLock);
        uintptr_t count = GetRefcount(key);
        uintptr_t newCount = count - 1;
        SetRefcount(key, newCount);
        OSSpinLockUnlock(&gRefcountDictLock);

        return newCount;
    }
```

接下来是包装这些函数的方法。它们很简单，大部分不言自明：

```
    @implementation NSObject (MARefcounting)

    - (id)ma_retain
    {
        IncrementRefcount(self);
        return self;
    }

    - (void)ma_release
    {
        uintptr_t newCount = DecrementRefcount(self);
        if(newCount == 0)
            [self dealloc];
    }

    @end
```

注意 `ma_retain` 返回 `self` 以遵循 Cocoa 允许如下语句的传统：

```
    object = [otherObject retain];
```

这不是引用计数系统的内在要求。

这就是自定义引用计数系统的全部内容！

为了测试它，我编写了一些快速代码，生成一堆对象，在压力测试中 retain 和 release 它们，并确保它们被 dealloc 掉。我不在这里复现它，但你可以在 GitHub 上查看该代码：[https://github.com/mikeash/refcounting/blob/master/refcounting.m#L80](https://github.com/mikeash/refcounting/blob/master/refcounting.m#L80)

**结论**  
和自动释放池（autorelease pool）一样，通过这个简单的实现，我们可以揭开 Cocoa 内存管理的面纱，看到幕后没有魔法，也没有神秘。它只是一个使用标准 Objective-C 消息传递的简单计数系统。Cocoa 的系统有很多技巧来使其快速，但本质上它与这个快速简单的版本是一样的。同样，我们可以看到诸如“如果我 retain 一个对象两次会发生什么？”或“我可以在一个线程上 retain 一个对象并在另一个线程上 release 它吗？”等简单问题的答案。如果你 retain 一个对象两次，你需要 release 它两次，因为它只是简单的递增和递减。Retain 和 release 不关心你在哪个线程上，只要它们平衡并正确同步，一切都能正常工作。

今天的探索到此结束。两周后再来参加这个 Cocoa 内存管理系统之旅的第三部分，我们将讨论 ARC、它是如何工作的以及如何使用它。和往常一样，Friday Q&A 由读者建议驱动，所以如果你有希望看到的话题，[请发送过来](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我整本整本地卖书！第二卷和第三卷现已出版！它们有 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-09-16-lets-build-reference-counting.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会被我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
