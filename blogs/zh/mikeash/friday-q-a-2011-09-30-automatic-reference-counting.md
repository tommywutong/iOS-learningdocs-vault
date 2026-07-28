---
title: 'Friday Q&A 2011-09-30: 自动引用计数（Automatic Reference Counting）'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-09-30-automatic-reference-counting.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ffaae452d0e13d07'
translated: true
---

> 原文：[Friday Q&A 2011-09-30: Automatic Reference Counting](https://www.mikeash.com/pyblog/friday-qa-2011-09-30-automatic-reference-counting.html)　·　mikeash.com Friday Q&A

发布于 2011-09-30 15:02 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2011-10-14: What's New in GCD](https://www.mikeash.com/pyblog/friday-qa-2011-10-14-whats-new-in-gcd.html)  
上一篇文章：[Friday Q&A 2011-09-16: Let's Build Reference Counting](https://www.mikeash.com/pyblog/friday-qa-2011-09-16-lets-build-reference-counting.html)  
标签：[arc](https://www.mikeash.com/pyblog/?tag=arc) [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [memory](https://www.mikeash.com/pyblog/?tag=memory) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2011-09-30: 自动引用计数（Automatic Reference Counting）

作者：[Mike Ash](https://www.mikeash.com/)

本文亦有[匈牙利语译本（Szabolcs Csintalan 翻译）](http://fertlond.com/automatikus-referencia-szamlalas/)。

**概念**  
[Clang 静态分析器](https://www.mikeash.com/pyblog/friday-qa-2009-03-06-using-the-clang-static-analyzer.html)是用于查找代码中内存管理错误的实用工具。如果你像我一样，你会看着分析器的输出想：“如果你能发现错误，那为什么不能直接帮我*修复*它呢？”

本质上，这就是 ARC 所做的。内存管理规则被编译进编译器，但编译器不再用它们来帮助程序员发现错误，而是直接自行插入必要的调用。

ARC 处于垃圾回收（garbage collection）和手动内存管理（manual memory management）之间。与垃圾回收类似，ARC 使程序员免于编写 `retain`/`release`/`autorelease` 调用。然而，与垃圾回收不同，ARC 不处理[保留环](https://www.mikeash.com/pyblog/friday-qa-2010-04-30-dealing-with-retain-cycles.html)。相互具有强引用的两个对象在 ARC 下永远不会被回收，即使没有其他对象引用它们。因此，虽然 ARC 使程序员免于处理*大部分*内存管理问题，但程序员仍然需要避免或手动打破对象图中的强引用循环。

在实现细节方面，ARC 和 Apple 的垃圾回收实现之间还有另一个关键区别：ARC 不是非此即彼的选择。使用 Apple 的垃圾回收器，要么整个应用程序在 GC 下运行，要么都不运行。这意味着应用程序中的所有 Objective-C 代码，包括所有 Apple 框架和你可能包含的所有第三方库，都必须兼容 GC 才能利用 GC。相比之下，ARC 与同一应用程序中非 ARC 的手动内存管理代码和平共存。这使得逐步转换项目成为可能，而不会遇到垃圾回收最初引入时遇到的兼容性和可靠性问题。

**Xcode**  
ARC 在 Xcode 4.2（目前处于 beta 阶段）中可用，并且仅在使用 Clang（即“Apple LLVM 编译器”）编译时可用。该设置名为“Objective-C Automatic Reference Counting”。打开它，然后一切就绪。

如果你在现有代码上工作，更改此设置会产生大量错误。ARC 不仅为你管理内存，还禁止你尝试自己管理。使用 ARC 时，手动发送 `retain`/`release`/`autorelease` 是非法的。由于普通的非 ARC Cocoa 代码中充斥着这些东西，你会遇到很多错误。

幸运的是，Xcode 提供了转换现有代码的工具。选择 Edit -> Refactor... -> Convert to Objective-C ARC...，Xcode 将引导你完成代码转换。尽管在某些情况下它可能需要帮助来确定该做什么，但该过程基本上应该是自动的。

**基本功能**  
Cocoa 内存管理规则相当简单。简而言之：

1. 如果你 `alloc`、`new`、`copy` 或 `retain` 了一个对象，你必须用 `release` 或 `autorelease` 来平衡它。
2. 如果你通过上述方式以外的方式获得一个对象，并且你需要它长期存活，你必须 `retain` 或 `copy` 它。当然，这必须在之后被平衡。

这些非常适合自动化。如果你编写以下代码：

```
    Foo *foo = [[Foo alloc] init];
    [foo something];
    return;
```

编译器可以看到未平衡的 `alloc`。因此，代码被转换为：

```
    Foo *foo = [[Foo alloc] init];
    [foo something];
    [foo release];
    return;
```

实际上，编译器不会插入对 `release` 的消息发送。相反，它会插入对特殊运行时函数的调用：

```
    Foo *foo = [[Foo alloc] init];
    [foo something];
    objc_release(foo);
    return;
```

这允许进行一些优化。在未重写 `-release` 的常见情况下，`objc_release` 函数可以绕过 Objective-C 消息发送，从而获得一定程度的速度提升。

这种自动化可以使代码更安全。大多数 Cocoa 程序员将规则 #2 中的“长期”解释为存储在实例变量（instance variables）及类似位置的对象。我们通常不会保留和释放本地的临时对象：

```
    Foo *foo = [self foo];
    [foo bar];
    [foo baz];
    [foo quux];
```

然而，这可能很危险：

```
    Foo *foo = [self foo];
    [foo bar];
    [foo baz];
    [self setFoo: newFoo];
    [foo quux]; // 崩溃
```

解决此问题的标准方法是让 `-foo` 获取器（getter）在返回值之前执行 `retain`/`autorelease`。这可行，但可能会累积大量临时对象，导致内存使用过多。然而，ARC 会非常谨慎，并在此处插入额外的调用：

```
    Foo *foo = objc_retainAutoreleasedReturnValue([self foo]);
    [foo bar];
    [foo baz];
    [self setFoo: newFoo];
    [foo quux]; // 没问题
    objc_release(foo);
```

同样，即使你编写了一个普通的获取器，ARC 也会使其安全：

```
    - (Foo *)foo
    {
        return objc_retainAutoreleaseReturnValue(_foo);
    }
```

但是等等，这根本没有解决临时对象过多的问题！我们仍在获取器中执行 `retain`/`autorelease` 序列，*并且*在调用代码中执行 `retain`/`release` 组合。这效率低得多！

别担心。正如我上面提到的，ARC 会发出这些特殊调用而不是普通的消息发送，以便进行优化。除了简单地使 `retain` 和 `release` 更快之外，这些调用还能够完全消除某些操作。

当 `objc_retainAutoreleaseReturnValue` 运行时，它会查看堆栈并获取其调用者的返回地址。这使它能够准确看到完成后会发生什么。当启用编译器优化时，对 `objc_retainAutoreleaseReturnValue` 的调用将受到尾调用优化（tail-call optimization）的影响，返回地址将指向对 `objc_retainAutoreleasedReturnValue` 的调用。

通过这种疯狂的返回地址检查，运行时能够看到它即将执行一些冗余工作。因此，它消除了 `autorelease`，并设置了一个标志，告诉调用者消除其 `retain`。整个序列最终在获取器中执行一次 `retain`，在调用代码中执行一次 `release`，这既完全安全又高效。

请注意，此优化与不采用 ARC 的代码完全兼容。如果获取器不使用 ARC，则该标志不会被设置，调用者将执行完整的 `retain`/`release` 组合。如果获取器使用 ARC 但调用者不使用，则获取器会看到它不会返回到立即调用特殊运行时函数的代码，并将执行完整的 `retain`/`autorelease` 组合。这会损失一些效率，但保持了正确性。

除此之外，ARC 还会自动为所有类创建或填写 `-dealloc` 方法以释放其实例变量。仍然可以手动实现 `-dealloc`，并且对于管理外部资源的类是必要的，但不再需要（也不可能）手动释放实例变量。ARC 甚至会为你添加最后的 `[super dealloc]`，因此你也无需这样做。以前，你可能会这样写：

```
    - (void)dealloc
    {
        [ivar1 release];
        [ivar2 release];
        free(buffer);

        [super dealloc];
    }
```

现在你只需这样写：

```
    - (void)dealloc
    {
        free(buffer);
    }
```

如果你的 `-dealloc` 方法只是释放实例变量，那么它完全可以被完全省略。

**循环与弱引用**  
ARC 仍然需要程序员手动解决引用循环，而解决引用循环的最佳方法通常是使用弱引用。

ARC 提供清零弱引用（zeroing weak references）。这些弱引用不仅不会保持被引用对象存活，而且当被引用对象被销毁时，它们还会自动变为 `nil`。清零弱引用避免了悬垂指针（dangling pointers）以及相关的崩溃和神秘行为的可能性。

要创建清零弱变量，只需在其声明前加上 `__weak`。例如，这是一个弱实例变量：

```
    @interface Foo : NSObject
    {
        __weak Bar *_weakBar;
    }
```

本地变量也是如此：

```
    __weak Foo *_weakFoo = [object foo];
```

然后你可以像使用任何其他变量一样使用它，其值会在适当时自动变为 `nil`：

```
    [_weakBar doSomethingIfStillAlive];
```

但请注意，`__weak` 变量几乎可以在任何时候变为 `nil`。内存管理本质上是一个多线程活动，弱引用的对象可能在一个线程上被销毁，而另一个线程正在访问它。因此，像这样的代码是无效的：

```
    if(_weakBar)
        [self mustNotBeNil: _weakBar];
```

相反，应将对象存储到本地强引用中并进行测试：

```
    Bar *bar = _weakBar;
    if(bar)
        [self mustNotBeNil: bar];
```

因为 `bar` 在这里是一个强引用，所以该对象在此代码执行期间保证存活（并且变量保证非 `nil`）。

ARC 对清零弱引用的实现需要 Objective-C 引用计数系统和清零弱引用系统之间的紧密协调。这意味着任何重写 `retain` 和 `release` 的类都不能成为清零弱引用的目标。虽然这种情况并不常见，但某些 Cocoa 类（如 `NSWindow`）存在此限制。幸运的是，如果你碰到这些情况之一，你会立即知道，因为你的程序会崩溃并显示如下消息：

```
    objc[2478]: cannot form weak reference to instance (0x10360f000) of class NSWindow
```

如果你确实需要对诸如上述类建立弱引用，你可以使用 `__unsafe_unretained` 限定符代替 `__weak`。这将创建一个*非*清零的弱引用。你必须确保在指针指向的对象被销毁后绝不使用该指针（最好通过手动将其置零）。请小心，因为非清零弱引用如同玩火。

虽然可以使用 ARC 构建在 Mac OS X 10.6 和 iOS 4 上运行的程序，但清零弱引用在这些操作系统上不可用。所有弱引用在这里必须是 `__unsafe_unretained`。由于非清零弱引用非常危险，在我看来，这一限制显著降低了 ARC 在这些操作系统上的吸引力。

**属性**  
由于属性（properties）与内存管理紧密耦合，因此 ARC 引入一些新行为是有道理的。

ARC 引入了一些新的所有权（ownership）修饰符。将属性声明为 `strong` 会使该属性成为强引用。将其声明为 `weak` 会使用清零弱引用。`unsafe_unretained` 修饰符使用非清零弱引用。当使用 `@synthesize` 时，编译器会创建一个相同存储类型的实例变量。

现有的修饰符 `assign`、`copy` 和 `retain` 仍然存在，并且工作方式与以前相同。值得注意的是，`assign` 会创建一个*非*清零的弱引用，因此应尽可能避免使用。

除了新的修饰符之外，属性的工作方式与以往相同。

**Block**  
Block 是 Objective-C 对象，因此也由 ARC 管理。Block 有特殊的内存管理要求，ARC 会相应地进行处理。block 字面量必须被复制（copy），而不是被保留（retain），这实际上意味着最好复制 block 而不是保留它们。ARC 遵循这一做法。

此外，ARC 知道，如果在当前作用域返回后使用 block 字面量，则必须复制它。非 ARC 代码需要显式复制和自动释放返回的 block：

```
    return [[^{
        DoSomethingMagical();
    } copy] autorelease];
```

使用 ARC，这简单地变为：

```
    return ^{ DoSomethingMagical(); };
```

但是，请注意！ARC 目前不会自动复制转换为 `id` 的 block 字面量。因此，虽然这段代码没问题：

```
    dispatch_block_t function(void)
    {
        return ^{ DoSomethingMagical(); };
    }
```

但这段代码不行：

```
    id function(void)
    {
        return ^{ DoSomethingMagical(); };
    }
```

通过简单地复制 block 可以轻松解决这个问题，但需要小心：

```
    return [^{ DoSomethingMagical(); } copy];
```

同样，你需要显式复制作为 `id` 参数传递的 block：

```
    [myArray addObject: [^{ DoSomethingMagical(); } copy]];
```

幸运的是，这似乎只是一个漏网的特例，并且很可能很快会被修复。如果你不确定，额外手动复制一下是没有问题的。

ARC 的另一个重要变化是 `__block` 限定变量的行为。`__block` 限定符允许 block 修改捕获的变量：

```
    id x;
    __block id y;
    void (^block)(void) = ^{
        x = [NSString string]; // 错误
        y = [NSString string]; // 有效
    };
```

在没有 ARC 的情况下，`__block` 还有一个副作用，即当它被 block 捕获时，不会保留其内容。Block 会自动保留和释放它们捕获的任何对象指针，但 `__block` 指针是特殊情况，充当弱指针。利用此行为以避免保留环已成为一种常见模式。

在 ARC 下，`__block` 现在会像其他被捕获的对象指针一样保留其内容。使用 `__block` 避免保留环的代码将不再有效。相反，应使用上面描述的 `__weak`。

**无缝桥接（Toll-Free Bridging）**  
ARC 仅适用于 Objective-C 类型。CoreFoundation 类型仍然必须由程序员手动管理。由于所有权存在歧义，ARC 禁止在指向 Objective-C 对象的指针和其他类型的指针（包括指向 CoreFoundation 对象的指针）之间进行标准转换。以下代码在手動内存管理下相当典型，但在 ARC 下无法编译：

```
    id obj = (id)CFDictionaryGetValue(cfDict, key);
```

为了使其再次编译，你必须通过使用特殊的转换标注（casting annotations）告诉 ARC 涉及的所有权语义。这些标注是 `__bridge`、`__bridge_retained` 和 `__bridge_transfer`。

最容易理解的是 `__bridge`。这是一个直接转换，没有所有权影响。ARC 接收该值，然后正常管理它。这就是我们对上述代码想要的：

```
    id obj = (__bridge id)CFDictionaryGetValue(cfDict, key);
```

其他的转换标注会将所有权传入或传出 ARC 系统。这些可以帮助减轻来回桥接时的痛苦。

以下是在需要释放返回对象的情况下使用桥接的示例：

```
    NSString *value = (NSString *)CFPreferencesCopyAppValue(CFSTR("someKey"), CFSTR("com.company.someapp"));
    [self useValue: value];
    [value release];
```

如果我们通过使用 `__bridge` 将其迁移到 ARC，删除 `release`，并且不进行任何其他更改，我们最终会泄漏：

```
    NSString *value = (__bridge NSString *)CFPreferencesCopyAppValue(CFSTR("someKey"), CFSTR("com.company.someapp"));
    [self useValue: value];
```

这段代码中的 `Copy` 需要用 `release` 来平衡。ARC 会在初始化 `value` 时发出一个 `retain`，然后在 `value` 不再使用时用一个 `release` 来平衡它。由于没有任何东西平衡原来的 `Copy`，该对象就泄漏了。

我们可以通过一些额外的代码来解决这个问题：

```
    CFStringRef valueCF = CFPreferencesCopyAppValue(CFSTR("someKey"), CFSTR("com.company.someapp"));
    NSString *value = (__bridge NSString *)valueCF;
    CFRelease(valueCF);

    [self useValue: value];
```

然而，这变得相当冗长。既然无缝桥接的要点在于尽可能无痛，而 ARC 的要点是消除编写内存管理代码的需要，那么如果能把这个过程变得更直接，那就太好了。

`__bridge_transfer` 标注解决了这个问题。它不是简单地将指针值移入 ARC，而是移动值*并转移所有权*。当在转换中使用 `__bridge_transfer` 时，它告诉 ARC 这个对象*已经*被保留了，并且 ARC 不需要再次保留它。由于 ARC 获得了所有权，它会在完成时释放它。最终结果是所有事情都按预期工作：

```
    NSString *value = (__bridge_transfer NSString *)CFPreferencesCopyAppValue(CFSTR("someKey"), CFSTR("com.company.someapp"));
    [self useValue: value];
```

无缝桥接是双向的。和之前一样，ARC 不允许标准转换将 Objective-C 对象指针转换为 CoreFoundation 对象指针。以下代码在 ARC 下无法编译：

```
    CFStringRef value = (CFStringRef)[self someString];
    UseCFStringValue(value);
```

在转换中添加 `__bridge` 使其编译通过，但生成的代码很危险：

```
    CFStringRef value = (__bridge CFStringRef)[self someString];
    UseCFStringValue(value);
```

由于 ARC 不管理 `value` 的生命周期，它会在 `value` 被传递给 `UseCFStringValue` 之前立即释放对该对象的所有权，可能导致崩溃或其他异常行为。通过使用 `__bridge_retained`，我们可以告诉 ARC 将所有权从系统中转移出来，交到我们手中。由于所有权被转移，我们现在有责任在使用完对象后释放它，就像处理任何其他 CF 代码一样：

```
    CFStringRef value = (__bridge_retained CFStringRef)[self someString];
    UseCFStringValue(value);
    CFRelease(value);
```

这些转换标注在无缝桥接之外也很有用。任何时候你需要在非 Objective-C 对象管理的存储中存储对象指针，它们都能使过程顺畅进行。Cocoa 中的许多地方都有 `void *` 上下文指针，一个突出的例子是表单（sheet）。在没有 ARC 的情况下：

```
    NSDictionary *contextDict = [NSDictionary dictionary...];
    [NSApp beginSheet: sheetWindow
       modalForWindow: mainWindow
        modalDelegate: self
       didEndSelector: @selector(sheetDidEnd:returnCode:contextInfo:)
          contextInfo: [contextDict retain]];

    - (void)sheetDidEnd: (NSWindow *)sheet returnCode: (NSInteger)code contextInfo: (void *)contextInfo
    {
        NSDictionary *contextDict = [(id)contextInfo autorelease];
        if(code == NSRunStoppedResponse)
            ...
    }
```

和之前一样，这在 ARC 下会失败，因为不允许在对象指针和非对象指针之间进行正常转换。然而，使用转换修饰符，我们不仅能让 ARC 允许它，还能让 ARC 为我们执行必要的内存管理：

```
    NSDictionary *contextDict = [NSDictionary dictionary...];
    [NSApp beginSheet: sheetWindow
       modalForWindow: mainWindow
        modalDelegate: self
       didEndSelector: @selector(sheetDidEnd:returnCode:contextInfo:)
          contextInfo: (__bridge_retained void *)contextDict];

    - (void)sheetDidEnd: (NSWindow *)sheet returnCode: (NSInteger)code contextInfo: (void *)contextInfo
    {
        NSDictionary *contextDict = (__bridge_transfer NSDictionary *)contextInfo;
        if(code == NSRunStoppedResponse)
            ...
    }
```

总结：

- `__bridge` 仅在 ARC 和非 ARC 之间传递指针，不转移所有权。
- `__bridge_transfer` 将非 Objective-C 指针移动到 Objective-C，并同时转移所有权，使得 ARC 会为你释放该值。
- `__bridge_retained` 将 Objective-C 指针移动到非 Objective-C 指针，并同时转移所有权，使得你（程序员）负责随后调用 `CFRelease` 或以其他方式释放该对象的所有权。

**结构体（Structs）**  
在 ARC 下，结构体和 Objective-C 对象指针几乎不能混合使用。问题在于编译器没有好的方法知道特定结构体何时被销毁或复制，因此也没有好的位置来插入必要的 `retain` 和 `release` 调用。由于这是一个非常困难的问题，并且由于将对象指针放在结构体中也很不寻常，ARC 干脆放弃了整个方案。如果你想把 Objective-C 对象指针放在结构体中，你*必须*用 `__unsafe_unretained` 限定它，并处理由此带来的所有问题和风险。

由于将 Objective-C 指针放入结构体非常罕见，这很可能不会对你的代码造成问题。如果确实有问题，你最好的选择是将该结构体改为一个轻量级的 Objective-C 类。ARC 将开始为你管理内存，问题就会消失。

**延伸阅读**  
虽然 Apple 关于 ARC 的官方文档在 Xcode 4.2 beta 期间仍未公开，但在 Clang 网站上可以找到大量关于该系统的信息：[http://clang.llvm.org/docs/AutomaticReferenceCounting.html](http://clang.llvm.org/docs/AutomaticReferenceCounting.html)

**结论**  
自动引用计数大大减轻了程序员处理内存管理的负担。ARC 不是完整的垃圾回收器。它无法检测保留环，这些必须由程序员处理并打破。尽管如此，它仍然承担了编写 Cocoa 代码中的大量繁重工作，并且它提供的清零弱引用是处理循环的强大工具。

在涉及 CoreFoundation 对象和无缝桥接时，事情会变得棘手。ARC 将自己限制在处理 Objective-C 上，因此程序员仍然需要手动管理 CoreFoundation 方面。在 Objective-C 和 CoreFoundation 指针之间进行转换时，需要使用特殊的 `__bridge` 转换修饰符来告知 ARC 转换的内存管理语义。

这就结束了今天对 Apple 最新编程语言技术的探索。两周后回来，迎接另一场精彩的文字盛宴。在那之前，继续仰望天空并[向我发送你的主题建议](mailto:mike@mikeash.com)。

你喜欢这篇文章吗？我在销售收录了这些文章的全套书籍！第二卷和第三卷现已出版！提供 ePub、PDF、印刷版，以及在 iBooks 和 Kindle 上购买。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-09-30-automatic-reference-counting.html)

添加你的想法，发表评论：

灌水和跑题帖子将被不经通知地删除。违规者可能会根据我的自由裁量权被公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
