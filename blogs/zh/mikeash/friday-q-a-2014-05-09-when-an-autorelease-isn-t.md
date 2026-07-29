---
title: 'Friday Q&A 2014-05-09：当 Autorelease 不是 Autorelease'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-05-09-when-an-autorelease-isnt.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:66f8dcdbd3b8420e'
translated: true
---

> 原文：[Friday Q&A 2014-05-09: When an Autorelease Isn't](https://www.mikeash.com/pyblog/friday-qa-2014-05-09-when-an-autorelease-isnt.html)　·　mikeash.com Friday Q&A

发布于 2014-05-09 13:59 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)）| [博客索引](https://www.mikeash.com/pyblog/)  
下一篇： [Friday Q&A 2014-05-23: A Heartbleed-Inspired Paranoid Memory Allocator](https://www.mikeash.com/pyblog/friday-qa-2014-05-23-a-heartbleed-inspired-paranoid-memory-allocator.html)  
上一篇： [Friday Q&A 2014-03-14: Introduction to the Sockets API](https://www.mikeash.com/pyblog/friday-qa-2014-03-14-introduction-to-the-sockets-api.html)  
标签： [arc](https://www.mikeash.com/pyblog/?tag=arc) [assembly](https://www.mikeash.com/pyblog/?tag=assembly) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [memory](https://www.mikeash.com/pyblog/?tag=memory)

Friday Q&A 2014-05-09：当 Autorelease 不是 Autorelease

作者： [Mike Ash](https://www.mikeash.com/)

**场景**  
[ARC](https://www.mikeash.com/pyblog/friday-qa-2011-09-30-automatic-reference-counting.html) 是一项很棒的技术，但它并不能覆盖所有情况。有时你需要使用 CoreFoundation 对象，然后就回到了手动内存管理的世界。

通常来说，这不是问题。我手动管理内存很多年了，虽然我很享受 _不用_ 在 ARC 下做这件事，但我仍然记得怎么做。然而，ARC 让一些事情比以前更难了。特别是，有时你想给一个 CoreFoundation 对象发送 `autorelease` 消息。没有 ARC 时，你可能会这样写：

```
    CFDictionaryRef MakeDictionary(void) {
        CFMutableDictionaryRef dict = CFDictionaryCreateMutable(NULL, 0, NULL, NULL);
        // 这里也许可以在字典里放一些内容

        [(id)dict autorelease];
        return dict;
    }
```

这提供了良好的内存管理语义——调用者不需要负责释放返回值，就像我们习惯的大多数 Cocoa 方法那样。它利用了这样一个事实：所有 CoreFoundation 对象也都是 Objective-C 对象，而 `autorelease` 是一种平衡 CoreFoundation 的 `Create` 调用的方式。

这段代码在 ARC 下不再有效，因为不允许调用 `autorelease`。为了解决这个问题，Apple 贴心地提供了 `CFAutorelease` 函数，它做同样的事情，并且可以在 ARC 下使用。不幸的是，它只在 iOS 7 和 Mac OS X 10.9 及更高版本中可用。对于需要支持更老系统版本的人来说，我们得自己想办法了。

我的解决办法是使用 `sel_getUid` 运行时调用来获取 `autorelease` 的选择器（selector），这可以绕过 ARC 的规则。然后将该选择器发送给 CoreFoundation 对象，从而达到与 `[(id)dict autorelease]` 相同的效果。我的代码如下：

```
    CFDictionaryRef MakeDictionary(void) {
        CFMutableDictionaryRef dict = CFDictionaryCreateMutable(NULL, 0, NULL, NULL);
        // 这里也许可以在字典里放一些内容

        SEL autorelease = sel_getUid("autorelease");
        IMP imp = class_getMethodImplementation(object_getClass((__bridge id)dict), autorelease);
        ((id (*)(CFTypeRef, SEL))imp)(dict, autorelease);

        return dict;
    }
```

注意：如果你是因为需要这样的代码而来到这里，_不要使用这段代码_。我们很快就会发现，它是有问题的。如果你想要能用的代码，请查看文末。

我测试了这段代码，一切正常。不久之后，项目中的另一个程序员报告说它在他那里总是崩溃。幸运的是，我没费太大力气就复现了他的崩溃。然而，弄清楚到底发生了什么却花了一些时间。

**崩溃**  
这段代码本身不会崩溃。但是，它_会_导致后续代码崩溃。例如：

```
    CFDictionaryRef dict = MakeDictionary();
    NSLog(@"Testing.");
    NSLog(@"%@", dict);
```

它在第二行 `NSLog` 处崩溃。堆栈跟踪看起来像典型的内存管理崩溃：

```
    frame #0: 0x00007fff917980a3 libobjc.A.dylib`objc_msgSend + 35
    frame #1: 0x00007fff97175184 Foundation`_NSDescriptionWithLocaleFunc + 41
    frame #2: 0x00007fff9077bd94 CoreFoundation`__CFStringAppendFormatCore + 7332
    frame #3: 0x00007fff907aa313 CoreFoundation`_CFStringCreateWithFormatAndArgumentsAux + 115
    frame #4: 0x00007fff907e1b9b CoreFoundation`_CFLogvEx + 123
    frame #5: 0x00007fff9719ed0c Foundation`NSLogv + 79
    frame #6: 0x00007fff9719ec98 Foundation`NSLog + 148
```

看起来字典在 `NSLog` 调用之前就被销毁了。但这怎么可能？我们在函数中调用了 `autorelease`，并且自动释放池（autorelease pool）还没有被清空。用于平衡 CoreFoundation 的 `Create` 调用的 `release` 还没有发生，所以这个对象应该仍然存在。

**汇编代码**  
在尝试了各种方式探查代码之后，我决定阅读编译器生成的汇编代码。我写的代码本身没什么东西，所以不管是什么问题，肯定隐藏得更深。

这是有问题的 `MakeDictionary` 函数的 x86-64 汇编输出：

```
    _MakeDictionary:                        ## @MakeDictionary
        .cfi_startproc
    Lfunc_begin0:
        .loc    1 11 0                  ## test.m:11:0
    ## BB#0:
        pushq   %rbp
    Ltmp2:
        .cfi_def_cfa_offset 16
    Ltmp3:
        .cfi_offset %rbp, -16
        movq    %rsp, %rbp
    Ltmp4:
        .cfi_def_cfa_register %rbp
        subq    $32, %rsp
        movabsq $0, %rax
        .loc    1 12 0 prologue_end     ## test.m:12:0
    Ltmp5:
        movq    %rax, %rdi
        movq    %rax, %rsi
        movq    %rax, %rdx
        movq    %rax, %rcx
        callq   _CFDictionaryCreateMutable
        leaq    L_.str(%rip), %rdi
        movq    %rax, -8(%rbp)
        .loc    1 15 0                  ## test.m:15:0
        callq   _sel_getUid
        movq    %rax, -16(%rbp)
        .loc    1 16 0                  ## test.m:16:0
        movq    -8(%rbp), %rax
        movq    %rax, %rdi
        callq   _object_getClass
        movq    -16(%rbp), %rsi
        movq    %rax, %rdi
        callq   _class_getMethodImplementation
        movq    %rax, -24(%rbp)
        .loc    1 17 0                  ## test.m:17:0
        movq    -24(%rbp), %rax
        movq    -8(%rbp), %rcx
        movq    -16(%rbp), %rsi
        movq    %rcx, %rdi
        callq   *%rax
        movq    %rax, %rdi
        callq   _objc_retainAutoreleasedReturnValue
        movq    %rax, %rdi
        callq   _objc_release
        .loc    1 19 0                  ## test.m:19:0
        movq    -8(%rbp), %rax
        addq    $32, %rsp
        popq    %rbp
        ret
```

这里相当直接。由于没有真正的计算，我们只需要看 `callq` 指令序列就能知道调用了哪些函数。它调用了 `CFDictionaryCreateMutable`、`sel_getUid`、`object_getClass`、`class_getMethodImplementation`，然后是一个通过函数指针的间接调用，这就是实际进行 `autorelease` 调用的地方。然后 ARC 介入，对调用的返回值进行了一些无意义但无害的操作——先 retain 它，然后立即 release。函数然后将字典返回给调用者。

**看似无害**  
我花了一小会儿才意识到发生了什么，但之后就一目了然了。我说过插入的 ARC 调用是“无意义但无害的”。事实上，它们_绝非_如此！

ARC 带来的一个有趣的特性是对自动释放返回值（autoreleased return value）的快速处理。这种模式在 ARC 下非常常见：

```
    // 被调用方
    obj = [[SomeClass alloc] init];
    [obj setup];
    return [obj autorelease];

    // 调用方
    obj = [[self method] retain];
    [obj doStuff];
    [obj release];
```

人类程序员通常会省略调用方中的 `retain` 和 `release` 调用，但 ARC 更加谨慎。这会使在使用 ARC 时速度变慢，而这正是快速自动释放处理发挥作用的地方。

在 Objective-C 运行时对 `autorelease` 的实现中，有一些非常巧妙且令人费解的代码。在真正发送 `autorelease` 消息之前，它首先检查调用者的代码。如果它发现调用者将立即调用 `objc_retainAutoreleasedReturnValue`，它就_完全跳过消息发送_。它实际上根本不会执行 `autorelease`。相反，它只是把对象藏在一个已知的位置，这表示它根本没发送过 `autorelease`。

`objc_retainAutoreleasedReturnValue` 与此方案协作。在调用 `retain` 之前，它首先检查那个已知的位置。如果那里包含正确的对象，它就跳过 retain。最终结果就是，上述代码被有效地转换成了这样：

```
    // 被调用方
    obj = [[SomeClass alloc] init];
    [obj setup];
    return obj;

    // 调用方
    obj = [self method];
    [obj doStuff];
    [obj release];
```

这样做更快，因为它完全跳过了自动释放池，节省了三次消息发送及相关工作：`autorelease`、调用方的 `retain`，以及自动释放池最终发送的 `release`。它还允许对象更早地被销毁，从而减少内存和缓存压力。

这项技术的美妙之处在于，由于运行时在进行此优化之前会检查调用者的代码，因此它与不参与此方案的代码完全兼容。如果调用者对返回值做了其他事情，那么运行时只是简单地调用 `autorelease`，一切正常工作。

我说过，这段代码_并非_无意义。那么，在上面的汇编代码中，紧随其后的 `retain` 和 `release` 的意义何在？它允许调用方参与此方案，即使它不使用返回值。简单地省略它们本来是正确的，但那样的话，快速自动释放路径就丢失了。结果是，至少在常见情况下，多进行这两个额外的调用反而更快。

我也说过这段代码并非无害。这里的危害正是那个快速自动释放路径。对于 ARC 来说，函数或方法中的 `autorelease` 后面跟着调用方中的 `retain`，只是一种传递所有权（ownership）的方式。然而，这段代码中的情况并非如此。这段代码试图_真正地_将对象放入自动释放池，无论何种情况。ARC 巧妙的优化最终绕过了这个尝试，结果是字典被立即销毁，而不是被放入自动释放池待稍后销毁。

**根本原因**  
这一切都归结于进行 `autorelease` 调用时使用的函数指针转换：

```
    ((id (*)(CFTypeRef, SEL))imp)(dict, autorelease);
```

我这样写是因为类型就是如此。`autorelease` 方法返回 `id` 并接受两个（通常是隐式的）参数：`self` 和要发送的选择器。为了方便，我将 `self` 参数改成了 `CFTypeRef` 而非 `id`，但保留了返回类型 `id`，因为那才是底层 `autorelease` 方法真正的返回类型。这应该无关紧要，因为返回值无论如何都被忽略了。

正是这个返回类型导致了这段代码的失败。我大多时候小心地避免了 ARC 的干预，但这个 `id` 让 ARC 介入并开始插入调用，从而导致字典被立即销毁。

**修复方法**  
一旦知道了所有这些，修复就很容易了。通过让调用返回 `CFTypeRef` 而不是 `id`，将 ARC 排除在外。这里是修复后的完整函数：

```
    CFDictionaryRef MakeDictionary(void) {
        CFMutableDictionaryRef dict = CFDictionaryCreateMutable(NULL, 0, NULL, NULL);
        // 这里也许可以在字典里放一些内容

        SEL autorelease = sel_getUid("autorelease");
        IMP imp = class_getMethodImplementation(object_getClass((__bridge id)dict), autorelease);
        ((CFTypeRef (*)(CFTypeRef, SEL))imp)(dict, autorelease);

        return dict;
    }
```

转储汇编显示 ARC 现在被排除在外了：

```
    _MakeDictionary:                        ## @MakeDictionary
        .cfi_startproc
    Lfunc_begin0:
        .loc    1 11 0                  ## test.m:11:0
    ## BB#0:
        pushq   %rbp
    Ltmp2:
        .cfi_def_cfa_offset 16
    Ltmp3:
        .cfi_offset %rbp, -16
        movq    %rsp, %rbp
    Ltmp4:
        .cfi_def_cfa_register %rbp
        subq    $32, %rsp
        movabsq $0, %rax
        .loc    1 12 0 prologue_end     ## test.m:12:0
    Ltmp5:
        movq    %rax, %rdi
        movq    %rax, %rsi
        movq    %rax, %rdx
        movq    %rax, %rcx
        callq   _CFDictionaryCreateMutable
        leaq    L_.str(%rip), %rdi
        movq    %rax, -8(%rbp)
        .loc    1 15 0                  ## test.m:15:0
        callq   _sel_getUid
        movq    %rax, -16(%rbp)
        .loc    1 16 0                  ## test.m:16:0
        movq    -8(%rbp), %rax
        movq    %rax, %rdi
        callq   _object_getClass
        movq    -16(%rbp), %rsi
        movq    %rax, %rdi
        callq   _class_getMethodImplementation
        movq    %rax, -24(%rbp)
        .loc    1 17 0                  ## test.m:17:0
        movq    -24(%rbp), %rax
        movq    -8(%rbp), %rcx
        movq    -16(%rbp), %rsi
        movq    %rcx, %rdi
        callq   *%rax
        .loc    1 19 0                  ## test.m:19:0
        movq    -8(%rbp), %rcx
        movq    %rax, -32(%rbp)         ## 8-byte Spill
        movq    %rcx, %rax
        addq    $32, %rsp
        popq    %rbp
        ret
```

**架构**  
还有一个问题：为什么这段代码最初对我有效，而我的同事后来才发现崩溃？

答案其实很简单，当其他一切都知道之后。这是一个 iOS 项目。我在模拟器中测试了代码，而他在真实的 iPhone 上测试。执行快速自动释放检查的运行时函数叫做 `callerAcceptsFastAutorelease`。它是架构相关的，因为它要检查机器码。如果你看一下 32 位 iOS 模拟器中的版本，问题就显而易见了：

```
    # elif __i386__  &&  TARGET_IPHONE_SIMULATOR

    static bool callerAcceptsFastAutorelease(const void *ra)
    {
        return false;
    }
```

简而言之，快速自动释放处理没有在 32 位 iOS 模拟器中实现。这很有道理。实现和修复它需要相当可观的工作量。同时，ARC 在 Mac 程序的 `i386` 上也不被支持，所以要在 `i386` 上命中这个路径，唯一的方法是在模拟器中运行。没有必要费力气去实现一个只适用于模拟器 App 的极端优化。

**题外话**  
在写这篇文章之前，我先写了一个小的测试用例，以便能够轻松地实验和孤立地检查这个问题。然而，有一个大问题：测试用例没起作用！更确切地说，它_确实_工作得很好，拒绝崩溃。代码非常简单，大致如下：

```
    int main(int argc, char **argv)
    {
        @autoreleasepool {
            CFDictionaryRef dict = MakeDictionary();
            NSLog(@"Testing.");
            NSLog(@"%@", dict);
        } 
        return 0;
    }
```

这里几乎不可能出错，所以它为什么不崩溃让我很困惑。

在调试器中单步执行汇编代码多次之后，我意识到这和 `dyld` 的延迟绑定（lazy binding）有关。对外部函数的引用在程序最初加载时并不会完全绑定。相反，会生成一个存根（stub），其中包含足够的信息，可以在第一次调用时完成绑定。在第一次调用外部函数时，会查找该函数的地址，重写存根使其指向该地址，然后进行函数调用。后续调用将直接跳转到该函数。通过延迟绑定，程序的启动时间得以改善，并且不会浪费时间查找从未被调用的函数。

这意味着，在这段代码的第一次运行时，对 `objc_retainAutoreleasedReturnValue` 的调用并没有被完全绑定。由于它没有被完全绑定，`callerAcceptsFastAutorelease` 不会意识到该调用是去往 `objc_retainAutoreleasedReturnValue`。由于它没有看到对 `objc_retainAutoreleasedReturnValue` 的调用，快速自动释放路径就不会被使用。字典按照最初的意图进入了自动释放池，代码工作正常……仅仅一次。

一旦我弄清楚了_这一点_，通过插入一个循环来强制崩溃就很简单了：

```
    int main(int argc, char **argv)
    {
        while(1) @autoreleasepool {
            CFDictionaryRef dict = MakeDictionary();
            NSLog(@"Testing.");
            NSLog(@"%@", dict);
        } 
        return 0;
    }
```

这个循环在第二次迭代时可靠地崩溃。第一次迭代触发了 `objc_retainAutoreleasedReturnValue` 的延迟绑定，这随后允许下一次调用走快速自动释放路径并触发这个 bug。

这对于正常的程序没什么影响，因为它们会很早就对这类函数进行延迟绑定。然而，对于一个小的测试程序来说，这却成为了一个严重的复杂因素。

**结论**  
ARC 是一项很棒的技术，但有时还是需要绕过它。当绕过它的时候，你必须确保_真正地_绕过了它，不给它任何介入的机会。如果你给了它机会，它可能会决定消除一个看起来无用的 `autorelease` 调用，从而导致你的对象被即时销毁，而不是被平稳地返回给调用者。

人们有时会问我是否真的使用我在这个博客上讨论的那些疯狂而深奥的东西。这是一个很好的例子：追踪这个 bug 需要基本的汇编代码阅读能力、Objective-C 运行时内部知识，以及对特定 ARC 调用的理解。构建崩溃示例还需要理解 `dyld` 如何在运行时绑定外部函数引用。这些都是很棒的知识，即使你从不使用它们，它们本身就很有趣。

今天就到这里。我希望回到正轨，所以请稍后回来查看另一篇文章。与此同时，一如既往，Friday Q&A 由读者建议驱动，所以如果你有希望看到的主题，请[发过来](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我在卖整本的书！第二卷和第三卷已经出版了！它们提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2014-05-09-when-an-autorelease-isnt.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会在我单方面的酌情下被公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
