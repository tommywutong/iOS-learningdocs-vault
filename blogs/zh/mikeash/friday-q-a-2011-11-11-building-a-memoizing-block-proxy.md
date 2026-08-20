---
title: 'Friday Q&A 2011-11-11：构建一个记忆化 Block 代理'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-11-11-building-a-memoizing-block-proxy.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e5aa00b665a47ea5'
translated: true
---

> 原文：[Friday Q&A 2011-11-11: Building a Memoizing Block Proxy](https://www.mikeash.com/pyblog/friday-qa-2011-11-11-building-a-memoizing-block-proxy.html)　·　mikeash.com Friday Q&A

发布于 2011-11-11 16:06 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[No Article For you!](https://www.mikeash.com/pyblog/no-article-for-you.html)  
上一篇文章：[Friday Q&A 2011-10-28: Generic Block Proxying](https://www.mikeash.com/pyblog/friday-qa-2011-10-28-generic-block-proxying.html)  
标签：[blocks](https://www.mikeash.com/pyblog/?tag=blocks) [evil](https://www.mikeash.com/pyblog/?tag=evil) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hack](https://www.mikeash.com/pyblog/?tag=hack) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2011-11-11：构建一个记忆化 Block 代理

作者：[Mike Ash](https://www.mikeash.com/)

**记忆化到底是什么？**  
简而言之，记忆化（memoization）就是在函数前面加一个缓存。想象一个纯函数，也就是说没有副作用，对于相同的参数你总是得到相同的结果。再想象这个函数计算成本很高，并且会用相同的参数多次调用。如果相同参数的结果总是相同，那么不断重新计算就是一种浪费。

对此的标准答案就是缓存。每当函数计算出结果时，它可以将该结果放入一个以参数为键的字典中。每当函数被调用时，它首先检查字典中是否已经存在该结果。如果存在，它就可以返回先前计算的值。

记忆化就是在包装函数中执行此缓存的过程。你不需要把缓存代码写进每一个符合此特征的函数，而是只写一次缓存代码，作为任意函数外部的包装器。包装器不知道函数是如何工作的，但它知道如何缓存返回值，如果一组特定参数已经计算过，就绕过该函数。

**代码**  
和之前一样，代码可在 GitHub 上获取：

[https://github.com/mikeash/MABlockForwarding](https://github.com/mikeash/MABlockForwarding)

**方法**  
之前的探索最终生成了一个 `MAForwardingBlock`，它接受一个 block 和一个 interposer，并返回一个新的 block。当新 block 被调用时，interposer 首先被调用，并传入一个代表此次调用的 `NSInvocation`。然后 interposer 可以随意操作该 `NSInvocation`，选择性地调用原始 block，然后将 `NSInvocation` 的返回值返回给调用者。

这里的目标是编写一个 `MAMemoize` 函数。该函数接受一个 block，并返回一个包装原始 block 的新 block。新 block 对原始 block 进行记忆化，根据传入的参数缓存值。`MAMemoize` 将使用 `MAForwardingBlock` 在原始 block 前面进行拦截，并使用一个 interposer block 来执行记忆化。

为了实现这一点，interposer 需要将 `NSInvocation` 的所有参数解包成一个可以作为字典键使用的对象。它还需要能够将返回值转换为可以作为字典值使用的对象，并进行反向转换。

一旦能够做到这一点，剩下的就简单了。维护一个存放记忆结果的字典。解包参数，检查字典是否有对应的条目。如果有，获取这些参数的值并返回。否则，调用原始 block，然后获取返回值并将其存入记忆字典，再返回。

**实现**  
首先，我们定义 `MAMemoize` 函数。它接受并返回 `id`，因为它处理的是任意 block，而不仅仅是特定类型：

```
    id MAMemoize(id block) {
```

接下来，创建记忆字典。这只是一个局部变量，但它会被 interposer block 捕获，因此最终会持久存在。Block 可以这样有趣。你可以把 block 想象成一个只有一个方法的对象，其中捕获的变量就是实例变量。

```
        NSMutableDictionary *memory = [NSMutableDictionary dictionary];
```

现在调用 `MAForwardingBlock`，并传入我们的 interposer。Interposer block 接受一个 `NSInvocation` 和一个调用原始 block 的 block。以下是调用的开始部分：

```
        return MAForwardingBlock(^(NSInvocation *inv, void (^call)(void)) {
```

从这里开始的所有代码都在返回的 block 被调用时运行。`inv` 参数包含该调用的 `NSInvocation`，`call` block 则调用原始函数。

首先要做的是将参数提取到一个可以用作字典键的对象中。这里，我选择使用 `NSArray`。虽然这可能不是一个非常高效的字典键，但这部分代码本身效率也不高，而且它能很好地完成工作。该数组将填充代表每个参数的对象。

提取参数还需要知道调用的方法签名，因此我们同时获取它：

```
            NSMethodSignature *sig = [inv methodSignature];
            NSMutableArray *args = [NSMutableArray array];
```

现在，遍历参数并将它们添加到数组中。请注意，循环从参数 `1` 开始，因为参数 `0` 是隐式的 block 指针参数，不需要包含在缓存中：

```
            for(unsigned i = 1; i < [sig numberOfArguments]; i++)
            {
```

对于参数是对象的情况，任务很简单：使用 `getArgument:atIndex:` 提取它，然后将其存入数组。对于非对象参数，情况就复杂了。实际上，不可能处理每一种可能的类型，因为像指针类型这样的东西，根本无法被充分内省以理解它们是如何被使用的。

我的方法是将 C 字符串作为特例处理，因为它们似乎是一种常见的参数类型。对于所有其他参数类型，将原始参数提取到 `NSData` 中，并将其视为参数，甚至不尝试解释其含义。实际上，这意味着所有原始值都可以工作，一些结构体以及少数指针（如 `SEL`，可以用 `==` 比较并在 App 的整个生命周期中持久存在）也可以工作。

首先，我创建一个 `arg` 局部变量，用于保存提取出的对象，无论它是什么。我还获取描述此参数类型的字符串：

```
                id arg = nil;
                const char *type = [sig getArgumentTypeAtIndex: i];
```

首先要检查这个参数是否是一个对象。我们可以通过将 `type` 的第一个字符与 `@encode(id)` 的第一个字符进行比较来实现：

```
                if(type[0] == @encode(id)[0])
                {
```

对于这种情况，只需将参数提取到 `arg` 中。我添加了一个小的额外处理：如果参数符合 `NSCopying` 协议，则在放入数组之前先拷贝它：

```
                    [inv getArgument: &arg atIndex: i];
                    if([arg conformsToProtocol: @protocol(NSCopying)])
                        arg = [arg copy];
                }
```

接下来，使用相同技术检查是否为 C 字符串（任何 `char *` 参数都被认为是 C 字符串）。如果是，将其内容提取到 `NSData` 中：

```
                else if(type[0] == @encode(char *)[0])
                {
                    char *str;
                    [inv getArgument: &str atIndex: i];
                    arg = [NSData dataWithBytes: str length: strlen(str)];
                }
```

最后，作为回退情况，直接将参数提取到 `NSData` 中。`NSGetSizeAndAlignment` 函数可以告诉我们参数的大小，从而知道 `NSData` 需要多大：

```
                else
                {
                    NSUInteger size;
                    NSGetSizeAndAlignment(type, &size, NULL);
                    arg = [NSMutableData dataWithLength: size];
                    [inv getArgument: [arg mutableBytes] atIndex: i];
                }
```

现在我们在 `arg` 中有了这个参数。在将其添加到数组之前，由于 `NSArray` 不接受 `nil`，需要检查这种情况，并使用 `NSNull` 代替：

```
                if(!arg)
                    arg = [NSNull null];
```

现在将参数添加到数组中，并继续循环，直到所有参数都被处理完毕：

```
                [args addObject: arg];
            }
```

接下来，我们检查 `memory` 字典中是否有这些参数。如果有，提取返回值并将其放入 `NSInvocation`。如果没有，调用原始 block，然后从 `NSInvocation` 中提取返回值。在这两种情况下，我们都需要方法的返回类型，并且需要知道它是对象、C 字符串还是其他类型，因此我们预先计算这些信息：

```
            const char *type = [sig methodReturnType];
            BOOL isObj = type[0] == @encode(id)[0];
            BOOL isCStr = type[0] == @encode(char *)[0];
```

接下来，检查 `memory` 字典。这一步在 `@synchronized` 块中完成，以确保此代码是线程安全的：

```
            id result;
            @synchronized(memory)
            {
                result = [[[memory objectForKey: args] retain] autorelease];
            }
```

如果字典中存在该组参数，则 `result` 将包含返回值的对象表示。否则，`result` 将为 `nil`。首先，让我们看一下 `memory` 中没有条目的情况：

```
            if(!result)
            {
```

由于没有保存的值，首先要做的是调用原始 block 来计算返回值：

```
                call();
```

一旦完成，返回值将包含在 `NSInvocation` 中。我们需要将其提取到一个对象中，以便可以将其存储在 `memory` 中。如果返回值是一个对象，这非常简单。只需使用 `getReturnValue:` 即可：

```
                if(isObj)
                {
                    [inv getReturnValue: &result];
                }
```

如果是 C 字符串，我们需要获取字符串指针，然后将其转换为 `NSData`。请注意，与参数保存代码不同，我向字符串的长度加 `1`，以便同时拷贝字符串的终止 `NUL` 字节。由于此指针需要返回给调用者，且调用者期望终止 `NUL` 字节，这种保存方式避免了额外转换：

```
                else if(isCStr)
                {
                    char *str;
                    [inv getReturnValue: &str];
                    result = str ? [NSData dataWithBytes: str length: strlen(str) + 1] : NULL;
                }
```

最后是回退情况。像之前一样，我们将其提取到 `NSData` 中，使用 `NSGetSizeAndAlignment` 来确定需要的长度：

```
                else
                {
                    NSUInteger size;
                    NSGetSizeAndAlignment(type, &size, NULL);
                    result = [NSMutableData dataWithLength: size];
                    [inv getReturnValue: [result mutableBytes]];
                }
```

同样，如果对象是 `nil`，用 `NSNull` 替换：

```
                if(!result)
                    result = [NSNull null];
```

现在我们有了结果，将其存储在 `memory` 中。到此为止，此特定代码路径就完成了。正确的返回值已经在 `NSInvocation` 中，将返回给调用者：

```
                @synchronized(memory)
                {
                    [memory setObject: result forKey: args];
                }
            }
```

现在，让我们看一下在 `memory` 中找到结果的情况。在这种情况下，我们所需要做的就是用 `setReturnValue:` 将 `result` 的内容填充到 `NSInvocation` 中。在这里，我们对 `nil` 进行反向转换，检查 `result` 是否为 `NSNull`，并将其改为 `nil`：

```
            else
            {
                if(result == [NSNull null])
                    result = nil;
```

如果返回类型是对象，直接调用 `setReturnValue:` 即可完成任务：

```
                if(isObj)
                {
                    [inv setReturnValue: &result];
                }
```

如果是 C 字符串，我们必须将字符串指针提取到局部变量中，然后设置它：

```
                else if(isCStr)
                {
                    const char *str = [result bytes];
                    [inv setReturnValue: &str];
                }
```

否则，`result` 是一个包含返回值的适当长度的 `NSData`。我们可以直接将指针传递给 invocation，仅此而已！

```
                else
                {
                    [inv setReturnValue: [result mutableBytes]];
                }
            }
        }, block);
    }
```

如果你已经跟丢了，最后这个 `block` 是传入 `MAMemoize` 的原始 block，它告诉 `MABlockForwarding` 要包装哪个 block。

**示例**  
作为记忆化的一个示例，我们来看一个计算量很大的简单 block：

```
    __block uint64_t (^fib)(int) = ^uint64_t (int n) {
        if(n <= 1)
            return 1;
        else
            return fib(n - 1) + fib(n - 2);
    }
```

这个 `fib` block 使用递归计算著名的斐波那契函数。这种方法极其缓慢。`else` 子句中的两个递归调用导致计算呈指数级增长。这两个递归调用中的每一个又会生成两个递归调用，以此类推。

然而，几乎所有调用都是多余的。如果你分析一下，你会看到 `fib(5)` 调用了 `fib(4)` 和 `fib(3)`，但随后 `fib(4)` 又再次调用了 `fib(3)`。对 `fib` 进行记忆化会使其快得多，因为后续对 `fib(3)` 的调用将被缓存，而不是重新计算。当然，有更好的方法来计算斐波那契函数，但这仍然是一个有趣的例子。

要记忆化 `fib`，我们只需调用 `MAMemoize` 并将结果赋值回 `fib`：

```
    fib = MAMemoize(fib);
```

由于 `fib` 被声明为 `__block`，递归调用会采用记忆化版本，并且对于较大的值，其结果比原始版本快得多。

**结论**  
这个记忆化包装器并非完全有用。首先，它基于我那个庞大的 block 代理 hack，而那个 hack 实际上不能用于你打算发布的代码中。即使忽略这一点，所有与 `NSInvocation` 相关的操作都很慢，这对于本质上是一种优化的代码来说是一个大问题。

尽管如此，这是一次很棒的学习经历。即使不实用，这个记忆化包装器也展示了如何在复杂情况下处理 `NSInvocation`，以及如何处理你在实际中可能遇到的各种参数和返回类型。除此之外，这种 hack 本身就是一种乐趣。

今天就到这里。请继续提出你的建议。Friday Q&A（通常）由读者提交的主题驱动，所以如果你有想要涵盖的主题，[请发过来](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我正在出售包含这些文章的全套书籍！第二卷和第三卷现已上市！它们提供 ePub、PDF、印刷版，并在 iBooks 和 Kindle 上销售。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-11-11-building-a-memoizing-block-proxy.html)

添加你的想法，发表评论：

垃圾邮件和与主题无关的帖子将被删除，恕不另行通知。违规者可能由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
