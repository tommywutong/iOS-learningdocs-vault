---
title: '不要使用 NSOperationQueue'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/dont-use-nsoperationqueue.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:47d9df4dafc7fb38'
translated: true
---

> 原文：[Don't Use NSOperationQueue](https://www.mikeash.com/pyblog/dont-use-nsoperationqueue.html)　·　mikeash.com Friday Q&A

发表于 2008-11-30 23:36 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[RAOperationQueue, an open-source replacement for NSOperationQueue](https://www.mikeash.com/pyblog/raoperationqueue-an-open-source-replacement-for-nsoperationqueue.html)  
上一篇：[Key-Value Observing Done Right](https://www.mikeash.com/pyblog/key-value-observing-done-right.html)  
标签：[nsoperationqueue](https://www.mikeash.com/pyblog/?tag=nsoperationqueue) [osbug](https://www.mikeash.com/pyblog/?tag=osbug)

不要使用 NSOperationQueue

作者：[Mike Ash](https://www.mikeash.com/)

**这个 Bug**

这个 bug 可以通过以下代码非常简单地演示：

```
    #import <Foundation/Foundation.h>
    
    @interface Tester : NSObject
    {
        NSOperationQueue *_queue;
    }
    
    - (void)test;
    
    @end
    
    @implementation Tester
    
    - (id)init
    {
        if((self = [super init]))
        {
            _queue = [[NSOperationQueue alloc] init];
            [_queue setMaxConcurrentOperationCount:1];
        }
        return self;
    }
    
    - (void)test
    {
        NSInvocationOperation *op = [[NSInvocationOperation alloc]
    initWithTarget:self selector:_cmd object:nil];
        [_queue addOperation:op];
        [op release];
    }
    
    @end
    
    int main(int argc, char **argv)
    {
        [NSAutoreleasePool new];
    
        NSMutableArray *testers = [NSMutableArray array];
        int i;
        for(i = 0; i < 10; i++)
            [testers addObject:[[[Tester alloc] init] autorelease]];
    
        for(Tester *tester in testers)
            [tester test];
    
        while(1) sleep(1000);
    }
```

在我的机器上，这段代码会在 10 秒内崩溃，并抛出以下异常：

```
    *** -[NSInvocationOperation start]: receiver has already started or finished
```

抛出异常的调用栈如下：

```
    #0  0x96480ff4 in ___TERMINATING_DUE_TO_UNCAUGHT_EXCEPTION___ ()
    #1  0x9207ee3b in objc_exception_throw ()
    #2  0x92db74de in -[NSOperation start] ()
    #3  0x92db7112 in __runop ()
    #4  0x902ae1f7 in _pthread_wqthread ()
    #5  0x902ae0aa in start_wqthread ()
```

请注意，这个 bug 似乎依赖于硬件。很多人尝试过这段代码，但至今没有人在 PowerPC 机器上让它崩溃过，看起来它只在 Intel 机器上出现。

这个 bug 也非常罕见。我在一些音频处理代码中发现了它，这些代码每秒大约入队 500 个 NSOperation。大约需要一小时才会崩溃。可以想象，调试起来非常刺激。

即使将上面的代码修改为单独入队 NSOperations，而不是采用一个 NSOperation 入队另一个 NSOperation 这种不常见的技巧，崩溃仍然会发生。去掉对 `setMaxConcurrentOperationCount:` 的调用也无效。实际上，似乎唯一有效的方法就是保证一次只运行一个 NSOperationQueue。但既然你无法阻止框架代码运行自己的 NSOperationQueue，这个方案是不可行的。

**原因**

NSOperationQueue 通过管理一个线程池来工作。这个线程池是全局的，也就是说，它在一个进程内的所有 NSOperationQueues 之间共享。NSOperationQueue 使用私有 API 来检查系统负载，并根据需要生成更多工作线程或杀死多余的线程，以便在不过度开销的情况下充分利用系统。

从我检查崩溃程序时能够确定的情况来看，问题似乎出在工作线程池中的竞态条件。它们从一组内部队列中取出 NSOperations，当时间片恰好不对时，同一个 NSOperation 可能会被两个工作线程同时取出。由于这种情况本不应发生，因此导致了混乱。

**你可以做什么**

不幸的是，答案是“没什么可做的”。这个 bug 牢牢地存在于 Apple 的代码中，而且现在看来他们不太可能在 Leopard 中修复它。你的选择有：

1. **提交 bug。** Apple 可能不会在 Leopard 中修复它，但如果足够多的人投诉，他们也许会改变主意。如果你提交 bug，可以引用我提交的 bug，ID 是 [6332143](rdar://6332143)。
2. **等待 10.6。** 看起来 10.6 很可能不会存在这个 bug。如果你能等到 10.6 发布，那么让你的软件要求 10.6 是一个简单的“修复”方法。
3. **回到更老的并发模型。** 切换到原始线程，你就（基本上）只需要应对自己的 bug，而不是 Apple 的。根据你的需求，实现一个支持你所需 NSOperationQueue 功能子集的替代品可能并不困难。对于导致我发现这个 bug 的软件，我在一天之内编写了自己的队列子类，为单个工作线程提供了优先级访问，并且让它成为了[无锁](https://www.mikeash.com/pyblog/late-night-cocoa.html)的。
4. **消除并发。** 有时 NSOperation 仅仅被用作一种优化手段来利用多核优势，或避免阻塞线程。在这种情况下，简单地退回到较慢的串行方法，或者直接阻塞直到工作完成，可能是合理的。

这个 bug 真的很不幸，因为 NSOperation/NSOperationQueue 提供了一个相当不错的 API（虽然太过于依赖 [KVO](https://www.mikeash.com/pyblog/key-value-observing-done-right.html)），而且没有很好的变通方法，在 Snow Leopard 发布之前修复的可能性也很低。但至少你现在知道它了！

喜欢这篇文章吗？我正在出售整本整本都是这类文章的书！第二卷和第三卷现已面世！有 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/dont-use-nsoperationqueue.html)

添加你的想法，发表评论：

垃圾评论和离题评论将被删除，恕不另行通知。违规者可能会被我单方面公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
