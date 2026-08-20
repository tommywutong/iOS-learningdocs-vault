---
title: 'Friday Q&A 2009-02-06：使用 Shark 进行性能分析'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-02-06-profiling-with-shark.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0c4b1cd2324296cf'
translated: true
---

> 原文：[Friday Q&A 2009-02-06: Profiling With Shark](https://www.mikeash.com/pyblog/friday-qa-2009-02-06-profiling-with-shark.html)　·　mikeash.com Friday Q&A

发布于 2009-02-06 17:30 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Late Night Cocoa: NSOperationQueue Problems](https://www.mikeash.com/pyblog/late-night-cocoa-nsoperationqueue-problems.html)  
上一篇文章：[Friday Q&A 2009-01-30: Code Injection](https://www.mikeash.com/pyblog/friday-qa-2009-01-30-code-injection.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [performance](https://www.mikeash.com/pyblog/?tag=performance) [shark](https://www.mikeash.com/pyblog/?tag=shark)

Friday Q&A 2009-02-06：使用 Shark 进行性能分析

作者：[Mike Ash](https://www.mikeash.com/)

**工具**  
你已经超越了优化的第一法则（不要做），并决定在第二法则（先别做）上花费了足够的时间。在优化这件事上，你很明智地知道，在实际修改代码之前，首先要做的就是对代码进行测量（measurement）。

测量主要分为两类：

1.  整体性能。通常以每秒操作次数来定义，无论你在做什么。如果是动画（animation），很可能是每秒帧数（FPS）。如果是某种查找系统，可能是每秒的搜索次数。更特殊的情况可能会关注 CPU 使用率或内存消耗。无论是什么，你都需要得出一个数字，以便进行前后对比，看看代码改动带来多少提升（或性能下降）。
2.  性能分析（Profiling）。它告诉你计算机在代码的每一部分上花费了多少时间。你需要这些信息来知道应该优化代码的哪些部分。

整体性能测量相当容易，因此我不打算深入讨论。更有趣的是性能分析。第一个问题是，你应该使用什么工具？

你可能会想用 Instruments。它很新，很酷，Apple 也大力宣传它。**别用**。在性能分析方面，Instruments 可以说是糟糕透顶。它难以使用、臃肿且提供的信息不足。更糟的是，在多线程（thread）应用中，它经常提供完全错误的信息。不要用 Instruments 做这个工作。

（实际上它在其他类型的性能分析上表现得还不错，比如内存使用。但对于减少 CPU 使用，Instruments 不仅无用，甚至有害。）

系统上还有其他工具，例如 Activity Monitor（活动监视器）的 sample 命令，或 `sample` 命令行工具（Activity Monitor 使用的就是它），但真正值得用于此工作的工具只有一个：Shark。

可能意见不一，但我的观点很坚定：Shark 是做这件事**唯一**值得考虑的工具。其他的工具还算不错（Instruments 除外），但 Shark 是纯金。实际上，我遇到过一些从未碰过 Mac 的人，在我向他们演示这个程序 30 秒后，他们就告诉我需要买一台 Mac。它就是这么好。

**需要优化的代码**  
在讨论 Shark 之前，我们需要一个用它来分析的示例程序。我写了一个小程序，它会在操作系统自带的单词列表 `/usr/share/dict/words` 中搜索子字符串（substring）。程序如下：

```
    #import <Foundation/Foundation.h>
    
    
    @interface Dict : NSObject
    {
        NSArray *_words;
    }
    - (NSArray *)find:(NSString *)toFind;
    @end
    
    @implementation Dict
    - (id)init
    {
        if((self = [super init]))
        {
            NSString *str = [NSString stringWithContentsOfFile:@"/usr/share/dict/words"];
            _words = [[str componentsSeparatedByString:@"\n"] copy];
        }
        return self;
    }
    
    - (void)dealloc
    {
        [_words release];
        [super dealloc];
    }
    
    - (NSArray *)find:(NSString *)toFind
    {
        NSMutableArray *array = [NSMutableArray array];
        for(NSString *word in _words)
        {
            if([[word lowercaseString] rangeOfString:[toFind lowercaseString]].location != NSNotFound)
                [array addObject:word];
        }
        return array;
    }
    @end
    
    int main(int argc, char **argv)
    {
        NSAutoreleasePool *outerPool = [[NSAutoreleasePool alloc] init];
        
        NSTimeInterval start = [NSDate timeIntervalSinceReferenceDate];
        NSTimeInterval lastPrinted = start;
        unsigned counter = 0;
        while(1)
        {
            NSAutoreleasePool *innerPool = [[NSAutoreleasePool alloc] init];
            Dict *dict = [[Dict alloc] init];
            [dict find:@"bob"];
            [dict release];
            counter++;
            
            NSTimeInterval now = [NSDate timeIntervalSinceReferenceDate];
            if(now - lastPrinted >= 1.0)
            {
                NSLog(@"%.1f/sec", counter / (now - start));
                lastPrinted = now;
            }
            [innerPool release];
        }
        
        [outerPool release];
        return 0;
    }
```

我还为今天的文章准备了一个完整的压缩包，包含了这段源代码、整篇文章中我要做的改动的源代码、每次改动的 Shark 跟踪结果，以及预编译的 x86 二进制文件。你应该下载下来跟着一起操作。[点此下载](https://www.mikeash.com/pyblog/friday-qna-dictfind.zip)。

这段代码有很多显而易见的性能问题，但它是为了说明 Shark 的用法，而不是一个完美的真实示例。

首先，让我们运行程序来建立一个基线。你会注意到，我测量了每秒执行的查找次数并定期打印出来。这就是我们接下来要关注的整体性能数字。在我的 Mac Pro 上，这段代码大约是每秒 1.6 次。

让我们用 Shark 分析它：

![](https://www.mikeash.com/pyblog/friday-qna-2009-02-05-shark-start.png)

这是 Shark 的起始窗口，你可以在这里控制 Shark 的行为。我们将其设置为 Time Profile（时间分析），Process（进程），并指定我们的 `dictfind1` 程序（它已经在 shell 中运行了）。其他设置保持不变。然后点击 Start（开始）按钮，等待 30 秒，再等待一段时间让它处理数据，然后我们就可以查看结果了：

![](https://www.mikeash.com/pyblog/friday-qna-2009-02-05-shark-profile.png)

我选择了 Tree (Top-Down)（树形，自顶向下）模式，这通常是性能分析的最佳模式。它自顶向下显示被分析到的调用栈（call stacks）。你可以看到 `start` 调用了 `main`，`main` 又调用了 `-[Dict find:]`、`-[Dict init]` 和其他一些函数。

这里的 Self（自身）和 Total（总计）列很重要。Self 列显示了在该函数中花费的 CPU 时间。Total 列显示了在该函数及其所有子调用中花费的总时间。我们可以看到 `-[Dict find:]` 占了总 CPU 时间的 40.8%。但注意，只有 0.8% 的时间花在 `-[Dict find:]` 函数本身。另外 40% 的时间花在了从该函数调用的其他代码上。这说明我们可以通过改变调用的方式来优化这个方法，但试图让 `-[Dict find:]` 本身的代码跑得更快，收益不会很大。

这里有一个明显的缓慢点，可能只看代码就很明显了，当看到分析结果后就更清楚了：这段代码在每次循环中都重新初始化了字典（dictionary）！如果我们的实际场景是每次运行要查找大量单词，那么这样做很不明智。让我们在循环之前创建 `Dict` 的单个实例（instance），然后在每次循环中重复使用它。你可以在压缩包的 `dictfind2.m` 中找到修改后的代码。

编译并运行。结果：每秒 2.7 次。不错！仅通过移动两行代码，速度相比原始代码提升了约 70%。

当然，这个速度仍然很慢，所以我们看看还能做些什么。分析这个版本，我们发现大约 70% 的时间花在 `-[Dict find:]` 上，大约 26% 的时间花在 `NSPopAutoreleasePool` 上。后者表明我们创建了太多临时对象。如果我们展开 `-[Dict find:]`，就能立刻看到原因：一半的时间花在了调用 `-[NSString lowercaseString]` 上，而每次调用都会产生一个临时对象，然后需要被销毁。因此我们可以猜测，这个程序大约 75% 的时间都花在了对这个方法的两次调用上。

不过很容易修复：NSString 支持不区分大小写的搜索。我们可以不用比较小写字符串，而是使用不区分大小写的选项（case insensitive option）来比较原始字符串。压缩包中的 `dictfind3` 包含了这个改动。

编译并运行。结果：每秒 17.5 次。相比 `dictfind2` 提升了 6.5 倍，基本符合预期。（移除占 75% 时间的代码应该可以带来 4 倍的提速，而数字的精度不足以让我们排除这个因素。）相比原始代码，这是一个 11 倍的提速。已经很不错了。

但是，每秒不到 20 次查找仍然不够理想。让我们也分析一下这个版本。我们发现 90% 的时间花在了 `-[NSString rangeOFString:options:]` 上。我们无法控制那段代码，而且很难想象我们能写出更快的自定义版本。优化剩下的代码最多能为我们赢得 10% 的提升。所以现在我们遇到了瓶颈。

如果不能加快 `-[NSString rangeOFString:options:]` 的速度，或许我们可以减少它的调用次数。让我们开始思考算法上的改进。每次搜索，我们都要对整个字典进行线性搜索。我们能减少吗？

这很棘手，因为我们做的是子字符串搜索，所以像把所有单词放进 NSDictionary 这种简单做法是行不通的。经典的二分查找（binary search）也不行。但如果愿意付出内存代价，改进的二分查找可以做到。我们不把每个单词直接存入数组进行搜索，而是存储**成对**的数据。一对中的第一部分是单词的后缀，第二部分是整个单词。然后我们对后缀进行二分查找，就可以快速找到所有包含搜索词的单词。内存代价会很大：一个 10 个字符的单词会在数组中产生 10 个条目，且所有这些后缀字符串都会驻留在内存中。但如果我们真的追求速度，这个权衡可能是值得的。

`dictfind4` 包含了二分查找版本。字典初始化现在变得相当复杂，需要构建所有子字符串。在 `find` 例程中，我们利用了 CoreFoundation 的无缝桥接（toll-free bridging），使用了 `CFArrayBSearchValues` 函数。

编译并运行。结果：初始化花费了**极长**的时间，在我的电脑上超过 10 秒。但一旦完成，回报是巨大的，约为每秒 24500 次。相比上一个版本，这是一个 1400 倍的提速，相比原始代码，是一个 15000 倍的提速。

为了好玩，我们也分析一下这个版本。我们发现 22.5% 的时间仅仅花在了 `-[NSCFArray addObject:]` 上。这段代码将近四分之一的时间都花费在找到结果后将结果添加到数组上！毫无疑问，这里还有进一步优化的空间，但此时我们已经遇到了收益递减（diminishing returns）。我们已经获得了相比原始慢速版本 15000 倍的提速，这对我来说已经足够了。

在今天结束之前，让我们把 Shark 切换到 "Heavy (Bottom-Up)"（重量级，自底向上）模式：

![](https://www.mikeash.com/pyblog/friday-qna-2009-02-05-shark-heavy.png)

这基本上把所有东西颠倒过来了。它不显示每个栈的顶部以及每个条目下面调用了什么，而是先显示栈底。然后显示哪些函数调用了它，哪些函数调用了那些函数，依此类推。这种模式通常不如自顶向下模式有用，但有时非常方便，因为有时候你会遇到一个重要的瓶颈（bottleneck），它被分散在代码各处的许多位置调用。

这正好说明了其中一种情况。我们看到 `objc_msgSend` 现在占用了我们 25% 的时间。当然，我们很难改进 libobjc，但如果追求更高的速度，我们可能会采取措施来减少消息发送的次数。

**总结**  
希望这篇文章能帮你入门 Shark，但我才刚触及它能力的皮毛。如果你双击分析列表中的任何条目，Shark 会显示相关函数的源代码。（有源码显示源码，没有则显示汇编。）在该视图中，它会给你一个**逐行的清单**，精确显示你的时间花在了哪里。更神奇的是，Shark 有一个常见性能问题的大型数据库，有时它甚至会**给你提供关于什么慢了以及如何修复的建议**。（寻找那个小小的感叹号，点击它以获取建议。）还有更多的功能不限于此。这是 Apple 创造的一个真正精彩的工具。（熟悉我的人会对此评论感到惊讶，但这是真的！）

本周就到这里。你有关于优化大战的精彩故事要分享吗？认为我对 Instruments 的抨击完全不公平？请在下面评论。下周同一时间回来，期待另一个激动人心的周五问答。

一如既往，Friday Q&A 的力量来自你的点子捐赠。如果你有希望在这里讨论的话题，请留在评论中或[发邮件给我](mailto:mike@mikeash.com)，并告诉我你是否不希望我使用你的名字。

喜欢这篇文章吗？我正在出售收录了这些文章的完整书籍！第二卷和第三卷现已出版！有 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里获取更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-02-06-profiling-with-shark.html)

发表你的想法，留下评论：

垃圾邮件和离题评论将被删除，恕不另行通知。违规者可能会在我自行判断下被公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
