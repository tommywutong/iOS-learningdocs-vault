---
title: block 的实现方式（及其后果）| Cocoa with Love
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/10/how-blocks-are-implemented-and.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:52b6ca8ffa2c3970'
translated: true
---

> 原文：[How blocks are implemented (and the consequences) | Cocoa with Love](https://www.cocoawithlove.com/2009/10/how-blocks-are-implemented-and.html)　·　Cocoa with Love (Matt Gallagher)

本文探讨 clang 如何实现 block，以及这种实现如何引发一系列奇怪行为，包括最终变成全局变量的局部变量、分配在栈上而非堆上的 Objective-C 对象、表现出类似 C++ 引用行为的 C 变量、非 Objective-C 语言中的 Objective-C 对象、不真正拷贝的 copy 方法以及不真正 retain 的 retain 方法。

## 编译器如何看待 block

block 是以内联（inline）方式（在其他函数内部）实现的可寻址代码段。内嵌写法固然方便，但 block 与普通函数和函数指针的真正区别在于：block 可以引用实现它的那个函数作用域中的局部变量，而 block 的调用者无需知晓那些作用域变量的存在。

block 内部由两部分实现：

1. 位于可执行文件 `.text` 段中的编译代码
2. 一个数据结构，主要包含 block 从其所在作用域中使用的变量的值

编译代码位于自己独立的位置，实际上并不存在于其所在作用域的代码内部。在实现上，block 的代码和其他任何函数别无二致。如果你运行：

```objc
otool -tV MyCompiledExecutable
```

你就会看到各个 block 紧挨在其所在函数之后出现，命名类似 `___surroundingFunction_block_invoke_21`。

所以，让 block 与众不同的不是代码，而是那个独立的数据结构。本文剩余部分将聚焦于这个数据结构。

## block 的数据结构

[Clang 关于 block 实现的基础文档](http://clang.llvm.org/docs/BlockImplementation.txt)指明，描述 block 的数据结构大致如下：

```objc
struct Block_literal {
    void *isa;

    int flags;
    int reserved; // 实际上是堆分配 block 的 retain 计数

    void (*invoke)(void *, ...); // 指向 block 编译代码的函数指针

    struct Block_descriptor {
        unsigned long int reserved; // 始终为 nil
        unsigned long int size; // 整个 Block_literal 的大小

        // 用于拷贝与销毁 block 的函数（如果需要）
        void (*copy_helper)(void *dst, void *src);
        void (*dispose_helper)(void *src);
    } *descriptor;

    // 从这里开始，结构体为每一个来自所在作用域的变量包含一个条目。
    // 对于非指针，这些条目是变量实际的常量值。
    // 对于指针，则存在一系列可能（__block 指针、
    // 对象指针、弱引用指针、普通指针）
};
```

当然，实际情况是 clang 从不会像这样显式声明此结构体。clang 是一个编译器——一个代码生成器——此结构的格式是通过 [CodeGenFunction::BuildBlockLiteralTmp](http://clang.llvm.org/doxygen/CGBlocks_8cpp-source.html#l00103) 方法以编程方式*生成*的。

## 栈 block 与全局 block

既然函数指针与 block 最大的区别在于能否使用所在作用域的变量，那么看看当 block 不引用所在作用域的任何内容时会发生什么，就很有意思。

通常情况下，`Block_literal` 数据会出现在栈上（就像普通的 `struct` 在它所在函数中那样）。但当没有对所在作用域的引用时，clang 会把 `Block_literal` 配置为*全局* block。这会让 block 出现在固定的全局位置，而非栈上（对应标记位中的 `BLOCK_IS_GLOBAL` 会在运行时表明这一点，不过我暂时还不清楚这个标记是否真的会被用到）。

这带来的后果是，全局 block 永远不会真正被拷贝或销毁，即便你调用相应函数也是如此。这种优化之所以可行，是因为一旦没有任何对所在作用域的引用，block 的任何部分（无论是其代码还是其 `Block_literal`）都不会再改变——它变成了一个共享的常量值。

## block 始终是对象

如果你熟悉 Objective-C 对象的声明方式，上面 `Block_literal` 中的 `isa` 字段应该不陌生——block 就是 Objective-C 对象。这在 Objective-C 中或许并不奇怪，但事实是，即使在纯 C 或 C++ 中，block 也依然是 Objective-C 对象，而且 block 的运行时（runtime）支持会以 Objective-C 消息传递（messaging）方式处理 block 的 `retain`/`release`/`copy` 行为。

Clang 使用 `_NSConcreteStackBlock` 和 `_NSConcreteGlobalBlock` 作为 block 字面量（literal）的类名，但在 CoreFoundation 项目中，它们会被映射为 `NSStackBlock` 和 `NSGlobalBlock`。如果你拷贝一个 `NSStackBlock`，它会返回一个 `NSMallocBlock`（表明其分配位置已改变）。

## block 是有些奇怪的对象

关于 `NSStackBlock`，值得关注的一点是：它是一个分配在栈上的 Objective-C 对象。如果你曾试图在栈上分配一个 Objective-C 对象（非指针，而是静态分配），你就知道编译器通常会禁止这样做。

block 默认放在栈上的原因是速度。在 block 的生命周期短于包含它的栈函数的常见情况下，这是一项很不错的优化。

栈 block 分配在栈上所带来的后果是，你不能简单地对一个栈 block 执行 `retain` ——一旦包含它的函数从栈中弹出，它就会失效。如果你对栈 block 调用 `retain`，将不会产生任何效果（该 block 的 retain 计数会保持为 1）。

因此，当你需要从函数或方法中返回一个 block 时，必须对它执行 `[[block copy] autorelease]`，而非简单地 `[[block retain] autorelease]`。

## __block 变量可以神奇地移动

block 中使用的作用域变量通常以 `const` 值方式传入（编译器不允许你修改该值，即使你改了，也不会影响 block 外那个变量的值）。

为了改变这一行为，引入了类型说明符 `__block`。任何声明为 `__block` 的变量都会以引用方式传入 block（也就是说，block 外部的值可以在 block 被调用后发生改变）。

在实现层面，`__block` 变量最初分配在栈上，但如果任何引用它的 block 被拷贝，这些变量就会被移到堆上（通过 `malloc` 分配）。这就导致了下面这种奇怪的局面……

```objc
int (^function())()
{
    __block int x = 0;

    int (^block)() = ^{
        x += 1;
        return x;
    };

    NSLog(@"x's location is on the stack: %p", &x);
    block = [[block copy] autorelease];
    NSLog(@"x's location is now on the heap: %p", &x);

    return block;
}
```

在这个例子中，当 `copy` 被调用时，x 的地址发生了变化。这是因为我们声明一个 `__block` 变量时，实际上是创建了一个指向实际变量的指针，任何对该变量的使用都会解引用（dereference）这个指针。当 `copy` 被调用时，指针所指向的位置变成了堆上的新位置，因此任何对 `x` 的访问都会被解引用到这个新位置。

这让 `__block` 与 C++ 中的引用参数有几分相似，因为 C++ 引用本质上也是透明地解引用的指针。

## NSMallocBlock 实际从不真正拷贝

拷贝一个 block 并不会真的给你一份 block 的副本——如果 block 已经是 `NSMallocBlock`，那么 `copy` 只是增加该 block 的 retain 计数（这个 retain 计数就是内部的 `reserved` 字段——从该对象返回的 `retainCount` 则始终为 1）。这完全合理，因为 block 的作用域一经创建便不可改变（因此 block 是常量的），但这也意味着，对 block 调用 `copy` 和重新创建它并不是一回事。

假设以下代码与上一个示例在同一个程序中。

```objc
int (^someBlock)() = counterBlock();
int (^someBlockCopy)() = [[someBlock copy] autorelease];
int (^anotherBlock)() = counterBlock();
```

从 `counterBlock()` 返回的 block 会将计数保存在 `__block` 变量 `x` 中，以此统计自己被调用的次数。

但在本例中，`someBlock` 与 `someBlockCopy` 共享同一个 `x` 变量——它们并非真正独立的副本。然而，`anotherBlock` 则确实有自己的独立 `x` 值。

如果你需要一份真正独立的副本，请重新创建 block，而不是拷贝它。

## block 会 retain 它们所使用的 NSObject 类型作用域变量

当 block 被拷贝时，它会 `retain` 从所在作用域中使用的任何 `NSObject`。

这带来的最大影响是：如果 block 的生命周期超过单纯的栈生命周期，你就必须记住[避免循环 retain](https://www.cocoawithlove.com/2009/07/rules-to-avoid-retain-cycles.html)。

正如[其他文章](http://www.mikeash.com/?page=pyblog/friday-qa-2009-08-14-practical-blocks.html)所指出的，要抑制 block 对 `NSObject` 的 retain，可以在 block 外部将该对象赋给一个 `__block` 变量，然后在 block 内部只使用这个 `__block` 变量即可。

你也可以反其道而行之，强制一个并非继承自 `NSObject` 的指针在拷贝时被 retain。方法是使用 `__attribute__((NSObject))` 声明该指针。当然，需要这么做的场景极为罕见。

## 结论

当你内联声明一个 block 并立即传入另一个函数的场景下，block 非常简单易用；但一旦你需要拷贝 block 或者将它持有一段时间，就会出现许多古怪行为，我在本文中已经介绍了其中一部分。

遗憾的是，目前 [Apple 关于 block 的文档](http://developer.apple.com/mac/library/documentation/Cocoa/Conceptual/Blocks/Articles/00_Introduction.html)还相当基础，缺乏细节。这也正是促使我开始研究 clang 源代码的原因。

当然，你并不需要盯着别人的 C++ 代码才能学习 block。关于这个主题，还有其他更轻松、更平易近人的文档。除了我已在文中链接的资料外，还有：

- Mike Ash 那篇标题俏皮的 "[Friday Q&A 2008-12-26](http://www.mikeash.com/?page=pyblog/friday-qa-2008-12-26.html)"——对 block 在 Objective-C 中的潜在用例做了出色的梳理。
- Joachim Bengtsson 的 [Programming with C Blocks](http://thirdcog.eu/pwcblocks/)——对 block 的大多数方面做了很好的概述。
- Jim Dovey 的 Blocks [Episode 2: Life Cycles](http://alanquatermain.net/post/138827791/blocks-episode-2-life-cycles)——结合图示探讨了 block 的栈与堆分配。
- clang 的 [BlockLanguageSpec](http://clang.llvm.org/docs/BlockLanguageSpec.txt)
