---
title: block 代理
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-10-28-generic-block-proxying.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:617bb0aa557b7a9f'
translated: true
---

> 原文：[block proxying](https://www.mikeash.com/pyblog/friday-qa-2011-10-28-generic-block-proxying.html)　·　mikeash.com Friday Q&A

发表于 2011-10-28 13:57 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客目录](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2011-11-11：构建一个带有记忆功能的 block 代理](https://www.mikeash.com/pyblog/friday-qa-2011-11-11-building-a-memoizing-block-proxy.html)  
上一篇：[Friday Q&A 2011-10-14：GCD 新功能](https://www.mikeash.com/pyblog/friday-qa-2011-10-14-whats-new-in-gcd.html)  
标签：[blocks](https://www.mikeash.com/pyblog/?tag=blocks) [evil](https://www.mikeash.com/pyblog/?tag=evil) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hack](https://www.mikeash.com/pyblog/?tag=hack) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2011-10-28：通用 block 代理

作者：[Mike Ash](https://www.mikeash.com/)

**这是什么意思**  
在 Objective-C 中，你可以拦截消息。任何发送给对象但没有实现的消息，都会被构造为一个 `NSInvocation` 对象，然后发送给 `forwardInvocation:`。在那里，你可以对消息做任何想做的事，比如在把它传递给另一个对象之前修改其参数，或者通过网络发送它。

这个功能最常见的用途是编写一个几乎不实现任何方法的代理类。发送给它的几乎所有消息都会被转发机制捕获，然后代理就可以对任何消息进行巧妙处理，同时仍然表现得像是被代理的对象。这对于构建像[透明 futures](https://github.com/mikeash/MAFuture) 和[透明的零化弱引用](https://github.com/mikeash/MAZeroingWeakRef/blob/master/Source/MAZeroingWeakProxy.h)这类东西非常有用。

Block 代理的原理类似，但代理的是 `block` 而不是对象。你用一个能够拦截调用并根据需要干预的 `block` 去封装一个任意的 `block`。

我即将展示的技术工作得很好，但绝对**不受支持**，不应在实际代码中使用。它依赖于私有 API 和公共 API 的私有特性。这是一个有趣的实验，而不是一个稳定的库。

**代码**  
像往常一样，代码可在 GitHub 上获取。今天探索禁区的旅程在这里：

[https://github.com/mikeash/MABlockForwarding](https://github.com/mikeash/MABlockForwarding)

**理论**  
Objective-C 的消息分派过程是：获取选择器和类，然后在类中查找与该选择器对应的方法。更具体地说，它查找实际实现该方法的函数，即 `IMP`，然后调用该函数。

消息转发就挂接在这个系统上。当查找函数时，如果在该类中没有找到方法，就会返回一个特殊的转发 `IMP`。该函数会处理所有将函数调用转换为 `NSInvocation` 对象的繁琐且平台特定的细节。

如果我们能获取到这个特殊的转发 `IMP`，就可以围绕它构建一个假的 `block`，从而实现转发 `block` 的目标。事实证明，获取特殊的转发 `IMP` 非常容易。你只需要向系统请求一个未实现选择器的 `IMP` 即可。有几种方法可以做到，但最简单的是直接调用 `[self methodForSelector:...]`，并传入一个你知道在该类中不存在的选择器。

一个 `block` 就是一个在正确位置包含函数指针的 Objective-C 对象。要调用 `block`，编译器会调用该函数指针，并将该对象作为第一个参数传入。我们可以构造一个 Objective-C 对象，在正确的位置放上指向转发 `IMP` 的指针，这样转发机制就会被触发，构建一个 `NSInvocation`，然后调用我们的 `forwardInvocation:` 方法。

转发机制需要知道正在被调用的方法的方法签名（method signature），以便知道如何打包参数。幸运的是，在比较新的编译器中，`block` 以相同的格式嵌入了方法签名信息。

转发处理的是消息，消息有两个隐式参数：对象和选择器。`Block` 只有一个隐式参数：`block` 对象本身。`Block` 的第二个参数可以是任何东西，或者根本不存在（对于没有参数的 `block`）。幸运的是，只要第二个参数存在，转发函数似乎并不关心它的类型。对于那些没有第二个参数的 `block`，可以在方法签名中插入一个假的参数，而不会搞砸事情。

**实现**  
目标是构建这个函数：

```
    typedef void (^BlockInterposer)(NSInvocation *inv, void (^call)(void));

    id MAForwardingBlock(BlockInterposer interposer, id block);
```

`MAForwardingBlock` 接受两个参数。第一个是拦截 block，即被调用以处理调用的 `block`。第二个是要封装的原始 `block`。拦截器会接收到一个 `block` 作为参数，当调用该 `block` 时，它会使用 `NSInvocation` 作为参数来调用原始 `block`。该函数返回一个新的 `block`，它会将调用转发给传入的拦截 `block`。

首先要创建一个新的类，它将伪装成一个 `block`。这个类的实例会像 `block` 一样工作，并处理所有代理职责。这个类的内存布局需要与 `block` 的布局兼容。一个 `block` 包含五个字段，后面可以跟其他数据。它有一个 `isa` 字段（使其能够作为 Objective-C 对象工作），然后是标志位、一些保留空间、`block` 的函数指针，以及一个指向 `block` 描述符的指针，该描述符包含关于 `block` 的其他有用信息。

`isa` 字段已经处理好了，剩下的部分可以作为实例变量来布局。在 `block` 字段之后，可以跟随其他数据。在这个例子中，该类在 `block` 字段之后将拦截 `block` 和原始 `block` 存储为实例变量：

```
    @interface MAFakeBlock : NSObject
    {
        int _flags;
        int _reserved;
        IMP _invoke;
        struct BlockDescriptor *_descriptor;

        id _forwardingBlock;
        BlockInterposer _interposer;
    }
```

这个类在其接口中只有一个方法，即初始化方法：

```
    - (id)initWithBlock: (id)block interposer: (BlockInterposer)interposer;
```

其他所有事情都通过 `block` 调用约定和转发来完成，因此不需要做别的事情。这个方法的实现会复制并存储传入的两个 `block`，然后通过获取一个未实现的方法来将 `invoke` 字段设置为转发 `IMP`：

```
    - (id)initWithBlock: (id)block interposer: (BlockInterposer)interposer
    {
        if((self = [super init]))
        {
            _forwardingBlock = [block copy];
            _interposer = [interposer copy];
            _invoke = [self methodForSelector: @selector(thisDoesNotExistOrAtLeastItReallyShouldnt)];
        }
        return self;
    }
```

现在一切就绪，每当 `MAFakeBlock` 的实例像 `block` 一样被调用时，它最终会走常规的 Objective-C 转发机制。常规转发路径有两个步骤：首先，运行时使用 `methodSignatureForSelector:` 获取方法签名，然后构造一个 `NSInvocation` 并调用 `forwardInvocation:`。

为了找出提供给运行时的方法签名，我们首先需要获取被包装的 `block` 的方法签名。这通过深入 `BlockDescriptor` 结构体并提取签名来完成。细节有点枯燥，我将跳过它们，直接假设存在一个 `BlockSig` 函数，它接受一个 `block` 并返回其方法签名作为 C 字符串。好奇的话，代码在 [GitHub 上](https://github.com/mikeash/MABlockForwarding/blob/master/MABlockForwarding.m#L26)。

`NSMethodSignature` 提供了一个从 C 字符串获取签名对象的方法 `+signatureWithObjCTypes:`。唯一的小麻烦是，如果提供的签名没有至少两个参数，转发机制会崩溃。为了解决这个问题，我通过在签名中添加额外的假 `void *` 参数来伪造，使其至少有所需数量的参数。这些额外的参数是无害的，尽管它们会被来自寄存器或栈的随机垃圾数据填充。`methodSignatureForSelector:` 的实现如下所示：

```
    - (NSMethodSignature *)methodSignatureForSelector: (SEL)sel
    {
        const char *types = BlockSig(_forwardingBlock);
        NSMethodSignature *sig = [NSMethodSignature signatureWithObjCTypes: types];
        while([sig numberOfArguments] < 2)
        {
            types = [[NSString stringWithFormat: @"%s%s", types, @encode(void *)] UTF8String];
            sig = [NSMethodSignature signatureWithObjCTypes: types];
        }
        return sig;
    }
```

`-forwardInvocation:` 的实现就很简单了。将调用的 target 设置为原始 `block`，然后调用拦截器：

```
    - (void)forwardInvocation: (NSInvocation *)inv
    {
        [inv setTarget: _forwardingBlock];
        _interposer(inv, ^{
```

传递给拦截器的调用 `block` 有点棘手。在公共接口中，`NSInvocation` 只提供了用特定选择器来调用它的方法，该方法会走 `objc_msgSend`。这当然不适合调用 `block`。

幸运的是，有一个名为 `invokeUsingIMP:` 的私有方法。它绕过 `objc_msgSend`，直接调用提供的 `IMP`。在实践中，它可以调用任何任意的函数指针，只要它与所拥有的签名兼容。然后我们可以将内部 `block` 的函数指针传递给它，就大功告成了：

```
            [inv invokeUsingIMP: BlockImpl(_forwardingBlock)];
        });
    }
```

同样，我在这里使用了一个小的辅助函数来处理内部 `block` 结构。`BlockImpl` 从 `block` 中取出函数指针。这个函数非常简单：它只是将对象解释为 `block` 结构，并获取 `invoke` 字段。如果你想看，[代码在这里](https://github.com/mikeash/MABlockForwarding/blob/master/MABlockForwarding.m#L12)。

这个类剩下的就是为 `copyWithZone:` 提供一个伪实现，因为 `block` 经常被拷贝。这个实现不需要做任何特殊的事情，除了保留假的 `block`，因为在这个类中没有可变状态：

```
    - (id)copyWithZone: (NSZone *)zone
    {
        return [self retain];
    }
```

现在这个类完成了，剩下的就是实现 `MAForwardingBlock`。这个函数需要做的只是创建并返回一个经过正确初始化的假 block 类的新实例：

```
    id MAForwardingBlock(BlockInterposer interposer, id block)
    {
        return [[[MAFakeBlock alloc] initWithBlock: block interposer: interposer] autorelease];
    }
```

就是这样！现在我们可以代理 `block` 了。这里有一个简单的例子：

```
    void (^block)(int) = ForwardingBlock(^(NSInvocation *inv, void (^call)(void)) {
        [inv setArgument: &(int){ 4242 } atIndex: 1];
        call();
    }, ^(int testarg){
        NSLog(@"%d %d", argc, testarg);
    });
    block(42);
```

尽管 `block` 是以 `42` 调用的，但实际打印的是 `4242`，因为拦截 `block` 在调用原始 `block` 之前改变了参数。

由于这段代码利用了 Cocoa 的转发机制，它几乎适用于任何接受任意参数组合和返回值的 `block`，而不仅仅是简单的 `int` 类型的 `block`。当然，它也存在与 Cocoa 转发相同的局限性。特别是，它无法处理接受可变参数或联合体（unions）的 `block`。它也不能处理结构体返回的特殊情况。由于大多数架构上结构体返回的工作方式，实际上存在一个单独用于结构体返回的转发 `IMP`。为了处理结构体返回，这段代码需要检测 `block` 签名是否使用了结构体返回的调用约定，并获取那个单独的 `IMP`。

**结论**  
理解像消息转发这样的机制在底层是如何工作的，使得扭曲它们来做全新的事情成为可能。有时你会得到一些真正有用的东西。有时你只会得到一个有趣的玩具，无法在实际代码中使用。虽然这个只是一个玩具，但它仍然是对系统内部的一次有趣探索，而这种探索往往能在之后催生真正、扎实、有用的代码。

今天就到这里。两周后回来，我将讨论如何使用这个 `block` 代理代码来实现[记忆化](http://en.wikipedia.org/wiki/Memoization)。在那之前，请继续发送你们的主题想法。除偶尔例外，Friday Q&A 是由读者建议驱动的，所以如果你有一个想在这里看到的话题，[请发过来](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我正在出售包含它们的全套书籍！第二卷和第三卷现已出版！它们有 ePub、PDF、印刷版，以及在 iBooks 和 Kindle 上提供。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-10-28-generic-block-proxying.html)

添加你的想法，发表评论：

垃圾邮件和离题评论将被不经通知地删除。违规者可能会被我酌情公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
