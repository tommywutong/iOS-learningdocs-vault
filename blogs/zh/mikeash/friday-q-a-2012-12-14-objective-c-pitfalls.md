---
title: 'Friday Q&A 2012-12-14：Objective-C 陷阱'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-12-14-objective-c-pitfalls.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5e1e81c873ce1da2'
translated: true
---

> 原文：[Friday Q&A 2012-12-14: Objective-C Pitfalls](https://www.mikeash.com/pyblog/friday-qa-2012-12-14-objective-c-pitfalls.html)　·　mikeash.com Friday Q&A

发表于 2012-12-14 14:38 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)
下一篇：[Friday Q&A 2012-12-28：当你加载一个内存字节时会发生什么](https://www.mikeash.com/pyblog/friday-qa-2012-12-28-what-happens-when-you-load-a-byte-of-memory.html)
上一篇：[Friday Q&A 2012-11-30：让我们构建一个 Mach-O 可执行文件](https://www.mikeash.com/pyblog/friday-qa-2012-11-30-lets-build-a-mach-o-executable.html)
标签：[cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2012-12-14：Objective-C 陷阱

作者 [Mike Ash](https://www.mikeash.com/)

**引言**
我采用与 Horstmann 相同的定义：陷阱是指能够编译、链接、运行，但行为与你的预期不符的代码。他提供了这个例子，这个例子在 Objective-C 中与在 C++ 中同样成问题：

```
    if (-0.5 <= x <= 0.5) return 0;
```

对这段代码的天真解读法是，它检查 `x` 是否在 [-0.5, 0.5] 范围内。然而，事实并非如此。实际上，比较会被这样求值：

```
    if ((-0.5 <= x) <= 0.5)
```

在 C 语言中，比较表达式的值是一个 `int`，要么是 `0`，要么是 `1`，这是 C 语言在还没有内建布尔类型时留下的遗产。与 0.5 比较的是这个 `0` 或 `1`，而不是 `x` 的值。实际上，第二次比较的作用就像是一个措辞极其古怪的否定运算符，导致 `if` 语句的代码体只有在 `x` 小于 -0.5 时才会执行。

**nil 比较**
Objective-C 非常独特的一点是，向 `nil` 发送消息不会做任何事，只是简单地返回 `0`。在你可能接触到的几乎所有其他语言中，等效的操作要么会被类型系统禁止，要么会产生运行时错误。这既是好事也是坏事。鉴于本文的主题，我们将重点关注坏事。

首先，让我们看看相等性测试：

```
    [nil isEqual: @"string"]
```

向 `nil` 发送消息返回 `0`，在这里相当于 `NO`。这碰巧是正确的答案，所以我们开头不错！然而，考虑一下这个：

```
    [nil isEqual: nil]
```

这*也*返回 `NO`。参数是否是完全相同的值并不重要。参数的值*根本*不重要，因为向 `nil` 发送消息总是返回 `0`，无论参数是什么。所以，根据 `isEqual:` 来看，`nil` 永远不等于任何东西，包括它自己。大部分情况下是正确的，但并非总是如此。

最后，考虑另一种涉及 `nil` 的情况：

```
    [@"string" isEqual: nil]
```

这会做什么？嗯，我们无法确定。它可能返回 `NO`。它可能抛出异常。它可能直接崩溃。将 `nil` 传递给一个没有明确说明允许 `nil` 的方法是个坏主意，而 `isEqual:` 并没有说明它接受 `nil`。

许多 Cocoa 类还包含一个 `compare:` 方法。这个方法接受另一个同类的对象，并返回 `NSOrderedAscending`、`NSOrderedSame` 或 `NSOrderedDescending`，分别表示小于、等于或大于。

如果我们用 `nil` 进行比较会发生什么？

```
    [nil compare: nil]
```

这返回 `0`，碰巧等于 `NSOrderedSame`。与 `isEqual:` 不同，`compare:` 认为 `nil` 等于 `nil`。真方便！然而：

```
    [nil compare: @"string"]
```

这*也*返回 `NSOrderedSame`，这绝对是错误的答案。`compare:` 会认为 `nil` 等于任何东西和一切东西。

最后，就像 `isEqual:` 一样，将 `nil` 作为参数传递也是个坏主意：

```
    [@"string" compare: nil]
```

简而言之，要小心使用 `nil` 和比较操作。它真的无法正常工作。如果你的代码有可能遇到 `nil`，你*必须*在使用 `isEqual:` 或 `compare:` 之前，单独检查并处理它。

**哈希**
你编写了一个小类来包含一些数据。你有这个类的多个等价实例，所以你实现了 `isEqual:`，以便这些实例被视为相等。然后你开始将你的对象添加到 `NSSet` 中，事情开始变得奇怪。这个集合声称在你刚刚添加一个对象后，包含了多个对象。它找不到你刚刚添加的内容。它甚至可能崩溃或破坏内存。

如果你实现了 `isEqual:` 但没有实现 `hash`，就可能发生这种情况。许多 Cocoa 代码都要求，如果两个对象比较为相等，那么它们也必须具有相同的哈希值。如果你只重写了 `isEqual:`，你就违反了这一要求。任何时候你重写 `isEqual:`，_一定_要同时重写 `hash`。更多信息，请参阅我关于[实现相等性与哈希](https://www.mikeash.com/pyblog/friday-qa-2010-06-18-implementing-equality-and-hashing.html)的文章。

**宏**
想象一下你在编写一些单元测试。你有一个方法应该返回一个包含单个对象的数组，所以你编写了一个测试来验证这一点：

```
    STAssertEqualObjects([obj method], @[ @"expected" ], @"Didn't get the expected array");
```

这使用了新的字面量语法来保持代码简洁。不错吧？

现在我们有另一个返回*两个*对象的方法，所以我们为它编写了一个测试：

```
    STAssertEqualObjects([obj methodTwo], @[ @"expected1", @"expected2" ], @"Didn't get the expected array");
```

突然，代码编译失败，并产生了完全离奇的错误。发生了什么？

事情是这样的：`STAssertEqualObjects` 是一个宏。宏由预处理器展开，而预处理器是一个古老且相当愚蠢的程序，它对现代的 Objective-C 语法一无所知，对现代的 C 语法也是如此。预处理器在逗号处分割宏参数。它足够聪明，知道括号可以嵌套，所以这被认为是三个参数：

```
    Macro(a, (b, c), d)
```

其中第一个参数是 `a`，第二个是 `(b, c)`，第三个是 `d`。然而，预处理器完全不知道它应该对 `[]` 和 `{}` 做同样的事情。对于上面的宏，预处理器看到了*四个*参数：

- `[obj methodTwo]`
- `@[ @"expected1"`
- `@"expected2 ]`
- `@"Didn't get the expected array"`

这导致了完全混乱的代码，不仅无法编译，而且让编译器困惑到无法提供可理解的诊断信息。一旦你知道问题所在，解决方案就很简单了。只需将字面量用括号括起来，这样预处理器就会将其视为一个参数：

```
    STAssertEqualObjects([obj methodTwo], (@[ @"expected1", @"expected2" ]), @"Didn't get the expected array");
```

单元测试是我遇到这个问题最频繁的地方，但任何有宏的地方都可能出现这个问题。Objective-C 字面量和 C 复合字面量都会受此影响。如果你在 `block` 内部使用了逗号运算符（这种情况很少见，但合法），`block` 也可能出问题。你可以看到 Apple 在他们的 `Block_copy` 和 `Block_release` 宏中考虑到了这个问题，这些宏在 `/usr/include/Block.h` 中：

```
    #define Block_copy(...) ((__typeof(__VA_ARGS__))_Block_copy((const void *)(__VA_ARGS__)))
    #define Block_release(...) _Block_release((const void *)(__VA_ARGS__))
```

这些宏从概念上讲只接受一个参数，但它们被声明为接受可变参数来避免这个问题。通过接受 `...` 并使用 `__VA_ARGS__` 来指代“参数”，带有逗号的多个“参数”会在宏的输出中被重现。你也可以采用相同的方法来使你自己的宏免受此问题影响，尽管这只对多参数宏的最后一个参数有效。

**属性合成**
考虑以下类：

```
    @interface MyClass : NSObject {
        NSString *_myIvar;
    }

    @property (copy) NSString *myIvar;

    @end

    @implementation MyClass

    @synthesize myIvar;

    @end
```

这没什么问题，对吧？在这个时代，实例变量声明和 `@synthesize` 有点多余，但不会造成伤害。

不幸的是，这段代码会*静默地*忽略 `_myIvar`，并合成一个名为 `myIvar`（不带前导下划线）的*新*变量。如果你的代码直接使用了该实例变量，它将看到与使用该属性的代码不同的值。混乱！

`@synthesize` 的变量命名规则有点奇怪。如果你指定了一个变量名，如 `@synthesize myIvar = _myIvar;`，那么它当然会使用你指定的任何名称。如果你省略了变量名，那么它会合成一个与属性同名的变量。如果你完全省略了 `@synthesize`，那么它会合成一个与属性同名但*带有前导下划线*的变量。

除非你需要支持 32 位 Mac，否则你最好的选择是避免为属性显式声明后备实例变量。让 `@synthesize` 来创建变量，如果你弄错了变量名，你会得到一个漂亮的编译器错误，而不是神秘的行为。

**被中断的系统调用**
Cocoa 代码通常坚持使用高级构造，但有时也需要降级使用一些 `POSIX` 调用。例如，这段代码会将一些数据写入文件描述符：

```
    int fd;
    NSData *data = ...;

    const char *cursor = [data bytes];
    NSUInteger remaining = [data length];

    while(remaining > 0) {
        ssize_t result = write(fd, cursor, remaining);
        if(result < 0)
        {
            NSLog(@"Failed to write data: %s (%d)", strerror(errno), errno);
            return;
        }
        remaining -= result;
        cursor += result;
    }
```

然而，这段代码可能会失败，并且会以奇怪且间歇性的方式失败。像这样的 POSIX 调用可能会被信号中断。即使是 App 其他地方处理的无害信号，如 `SIGCHLD` 或 `SIGINFO`，也可能导致这种情况。如果你正在使用 `NSTask` 或处理子进程，就可能发生 `SIGCHLD`。当 `write` 被一个信号中断时，它会返回 `-1` 并将 `errno` 设置为 `EINTR` 以指示该调用被中断了。上面的代码将所有错误都视为致命的，会退出，即使这个调用只需要再次尝试即可。正确的代码会单独检查这种情况，然后重试该调用：

```
    while(remaining > 0) {
        ssize_t result = write(fd, cursor, remaining);
        if(result < 0 && errno == EINTR)
        {
            continue;
        }
        else if(result < 0)
        {
            NSLog(@"Failed to write data: %s (%d)", strerror(errno), errno);
            return;
        }
        remaining -= result;
        cursor += result;
    }
```

**字符串长度**
同一个字符串，以不同方式表示，可能具有不同的长度。这是一个相对常见但不正确的模式：

```
    write(fd, [string UTF8String], [string length]);
```

问题在于，`NSString` 以 UTF-16 代码单元为单位计算长度，而 `write` 需要的是字节数。当字符串只包含 ASCII 字符时（这就是为什么人们经常侥幸写出这段错误代码的原因），这两个数字是相等的，但一旦字符串包含非 ASCII 字符（如带重音符号的字符），它们就不再相等。始终计算你所操作的那同一表示形式的长度：

```
    const char *cStr = [string UTF8String];
    write(fd, cStr, strlen(cStr));
```

**转换为 `BOOL`**
看这段仅仅检查对象指针是否为 `nil` 的代码：

```
    - (BOOL)hasObject
    {
        return (BOOL)_object;
    }
```

这通常能工作……但大约 6% 的情况下，即使 `_object` 不是 `nil`，它也会返回 `NO`。这是怎么回事？

不幸的是，`BOOL` 类型并不是一个布尔值。它的定义如下：

```
    typedef signed char BOOL;
```

这是 C 语言还没有布尔类型时留下的另一个不幸的遗产。Cocoa 早于 C99 的 `_Bool`，所以它将“布尔”类型定义为一个 `signed char`，这只是一个 8 位整数。当你将指针强制转换为整数时，你只是得到了该指针的数值。当你将指针强制转换为一个较小的整数时，你只是得到了该指针低位的数值。当指针看起来像这样时：

```
    ....110011001110000
```

`BOOL` 得到的是：

```
               01110000
```

这不是 `0`，意味着它求值为 true，那么问题出在哪里？问题在于当指针看起来像这样时：

```
    ....110011000000000
```

那么 `BOOL` 得到的是：

```
               00000000
```

这是 `0`，也就是 `NO`，即使指针并非 `nil`。哎呀！

这种情况发生的频率有多高？`BOOL` 有 `256` 个可能的值，其中只有一个是 `NO`，所以我们天真地认为它大约会在 1/256 的情况下发生。然而，Objective-C 对象是经过对齐分配的，通常是 `16` 字节。这意味着指针的低四位始终为零（[标记指针（tagged pointer）](https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html)利用了这一点），因此产生的 `BOOL` 只有四个自由位。得到全零的概率大约是 1/16，也就是大约 6%。

要安全地实现这个方法，请执行显式的 `nil` 比较：

```
    - (BOOL)hasObject
    {
        return _object != nil;
    }
```

如果你想变得聪明但难以阅读，你也可以两次使用 `!` 运算符。这个 `!!` 结构有时被称为 C 的“转换为布尔”运算符，尽管它只是由部分组合而成：

```
    - (BOOL)hasObject
    {
        return !!_object;
    }
```

第一个 `!` 根据 `_object` 是否为 `nil` 产生 `1` 或 `0`，但结果是相反的。然后第二个 `!` 将其纠正，如果 `_object` 不是 `nil` 则结果为 `1`，如果是 `nil` 则为 `0`。

你可能应该坚持使用 `!= nil` 的版本。

**缺失的方法参数**
假设你正在实现一个表格视图（table view）的数据源。你将这个方法添加到了你的类中：

```
    - (id)tableView:(NSTableView *) objectValueForTableColumn:(NSTableColumn *)aTableColumn row:(NSInteger)rowIndex
    {
        return [dataArray objectAtIndex: rowIndex];
    }
```

然后你运行你的 App，`NSTableView` 抱怨你没有实现这个方法。但它明明就在那里！

像往常一样，计算机是正确的。计算机是你的朋友。

再仔细看看。第一个参数*缺失*了。为什么这甚至能*编译*？

事实证明，Objective-C 允许空的选择器片段。上述代码并没有声明一个名为 `tableView:objectValueForTableColumn:row:` 但缺少参数名的方法。它声明了一个名为 `tableView::row:` 的方法，而第一个参数名是 `objectValueForTableColumn`。这是一种特别容易导致方法名拼写错误的方式，如果你在编译器无法警告你方法缺失的上下文中这样做，你可能会花很长时间来调试它。

**结论**
Objective-C 和 Cocoa 有很多陷阱，随时准备捕获粗心的程序员。以上只是一些示例。不过，这是一个值得小心的好列表。

今天就到这里！下次再来获取更多疯狂的建议。Friday Q&A 是由用户的想法驱动的，如果你还不知道的话，那么下次，请[把你对文章的想法发给我](mailto:mike@mikeash.com)！

你喜欢这篇文章吗？我正在出售装满这些文章的整本书！第二卷和第三卷现已出版！它们有 ePub、PDF、印刷版，也可在 iBooks 和 Kindle 上购买。 [点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-12-14-objective-c-pitfalls.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会在我的全权决定下被公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
