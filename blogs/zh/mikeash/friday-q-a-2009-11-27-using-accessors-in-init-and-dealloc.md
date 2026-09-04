---
title: 'Friday Q&A 2009-11-27：在 init 和 dealloc 中使用存取方法'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-11-27-using-accessors-in-init-and-dealloc.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6e284c24b3e23ce5'
translated: true
---

> 原文：[Friday Q&A 2009-11-27: Using Accessors in Init and Dealloc](https://www.mikeash.com/pyblog/friday-qa-2009-11-27-using-accessors-in-init-and-dealloc.html)　·　mikeash.com Friday Q&A

发表于 2009-11-27 16:32 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2009-12-04：构建独立的 iPhone Web 应用](https://www.mikeash.com/pyblog/friday-qa-2009-12-04-building-standalone-iphone-web-apps.html)  
上一篇：[Friday Q&A 2009-11-20：用 PyObjC 探测 Cocoa](https://www.mikeash.com/pyblog/friday-qa-2009-11-20-probing-cocoa-with-pyobjc.html)  
标签：[accessors](https://www.mikeash.com/pyblog/?tag=accessors) [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2009-11-27：在 init 和 dealloc 中使用存取方法

作者：[Mike Ash](https://www.mikeash.com/)

**引言**  
过去几年里，Cocoa 社区的风气发生了一个变化：在 `init`/`dealloc` 中使用存取方法（accessor）遭到非议、不被推荐，甚至被直接视为错误。他们说，直接访问实例变量（instance variable）要好得多。换句话说，这条建议就是让你写出这样的代码：

```
    - (id)initWithWhatever: (id)whatever
    {
        if((self = [self init]))
        {
            _whatever = [whatever retain];
        }
        return self;
    }
    
    - (void)dealloc
    {
        [_whatever release];
        
        [super dealloc];
    }
```

另一种做法是使用存取方法，像这样：

```
    - (id)initWithWhatever: (id)whatever
    {
        if((self = [self init]))
        {
            [self setWhatever: whatever];
        }
        return self;
    }
    
    - (void)dealloc
    {
        [self setWhatever: nil];
        
        [super dealloc];
    }
```

**存取方法的优点**  
在 `init`/`dealloc` 中使用存取方法的优点，与在其他任何地方使用它们的优点基本相同。它们让代码与你的实现解耦，尤其能帮上内存管理的忙。你有多少次不小心写出过这样的代码？

```
    - (id)init
    {
        _ivar = [NSArray arrayWithObjects:...];
        return self;
    }
```

我预计答案会五花八门（这个具体的错误我已经很久没犯过了），但使用存取方法能确保你不犯这个错误：

```
    - (id)init
    {
        [self setIvar: [NSArray arrayWithObjects:...]];
        return self;
    }
```

此外，你可能还有一些辅助状态，比如缓存、摘要等，需要在对象值变化时建立和拆除。正确使用存取方法可以确保这一切在对象创建和销毁时按需发生，而无需重复的代码。

**存取方法的缺点**  
以这种方式使用存取方法的缺点可以概括为一句话：存取方法可能有副作用（side effect）。有时这些副作用对 `init`/`dealloc` 来说是不受欢迎的。

编写 setter 时，如果你打算从 `init`/`dealloc` 中调用它，它就需要表现正确。这意味着要处理只构造了一部分的对象。

更糟的是，如果你在子类中重写（override）某个 setter，就需要把它写成能应对「超类正用这个 setter 初始化或销毁自己的实例变量」的情况。例如，下面这段看起来无害的代码就潜藏着危险：

```
    - (void)setSomeObj: (id)obj
    {
        [anotherObj notifySomething];
        [super setSomeObj: obj];
    }
    
    - (void)dealloc
    {
        [anotherObj release];
        [super dealloc];
    }
```

如果超类使用存取方法来销毁 `someObj`，那么这段重写的代码会在 `dealloc` 已经执行完之后才运行，导致它访问指向 `anotherObj` 的悬空引用（dangling reference），很可能造成一次漂亮的崩溃。

把这段代码修好、让它从容应对这种情况并不难。只要在 `dealloc` 中释放 `anotherObj` 之后补上一句 `anotherObj = nil`，一切就恢复正常了。总的来说，确保你的重写方法表现正确并不困难，但如果你打算这样使用存取方法，就必须记得去做，而这才是不容易的地方。

**键值观察**  
在这类讨论中经常被提起的一个话题是键值观察（key-value observing），因为 KVO 是存取方法产生副作用的常见途径。和其他情况一样，如果 KVO 的副作用在对象只完成部分初始化或已经开始销毁时被触发，而那段代码又没有写成能容忍这种对象的形式，就会出乱子。我个人认为这多半是个干扰项（red herring）。

之所以说它多半是干扰项，是因为在 99% 的情况下，KVO 都要等到对象完全初始化之后才会被建立，并且在对象销毁之前就已经停止。让 KVO 激活得更早、终止得更晚_倒是可以想象_，但实践中不太可能发生。

在对象完全初始化之前，外部代码不可能对它做任何事情，除非你的初始化方法自己就把指针传给了外部对象。同样地，当对象正在执行 `dealloc` 方法时，外部代码也不可能维持对它的 KVO 引用，因为此时对它来说移除引用已经太迟了，除非你的 `dealloc` 触发了某些事，让它得以这么做。超类的代码确实会在这些时间段内执行，但超类代码极不可能做出任何事情，去让外部对象观察那些连超类自己都没有的属性。

**结论**  
现在你了解了优点和缺点；那么，该在 `init` 和 `dealloc` 中使用存取方法吗？在我看来，两种做法都行得通。优点通常没那么大，缺点也很轻微。我的实例变量中绝大多数都不用存取方法，但在某些情况下——因为我正在对某个实例变量做特殊处理——优点会变得举足轻重，这时我会毫不犹豫地让存取方法替我省去一些头疼事。

本周就到这里，下周请再来新一轮。如果你有希望在这里看到的主题，[请发给我！](mailto:mike@mikeash.com) Friday Q&A 由你的建议驱动，我收到的建议越多，你能读到的主题就越好。

喜欢这篇文章吗？我正在销售收录这些文章的整套书！第二卷和第三卷现已出版，提供 ePub、PDF、印刷版、iBooks 和 Kindle 版本。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-11-27-using-accessors-in-init-and-dealloc.html)

分享你的想法，发表评论：

垃圾评论和离题内容将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
