---
title: 'objc_msgSend 的新原型'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/objc_msgsends-new-prototype.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2b3d5ad8166475f9'
translated: true
---

> 原文：[objc_msgSend's New Prototype](https://www.mikeash.com/pyblog/objc_msgsends-new-prototype.html)　·　mikeash.com Friday Q&A

发表于 2019-10-11 12:09 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
上一篇：[Friday Q&A 2018-06-29: Debugging with C-Reduce](https://www.mikeash.com/pyblog/friday-qa-2018-06-29-debugging-with-c-reduce.html)  
标签： [objc](https://www.mikeash.com/pyblog/?tag=objc)

objc_msgSend 的新原型

作者：[Mike Ash](https://www.mikeash.com/)

**真正的原型**  
这个问题背后隐藏着一个巨大且出乎意料的难点：`objc_msgSend` 的*真正*原型是什么？也就是说，它实际接受什么参数，又实际返回什么？这个问题没有一个直截了当的答案。

你可能听说过 `objc_msgSend` 是用汇编实现的，因为它的调用极其频繁，需要榨取每一点性能。这是事实，但并非全部。在*任何*速度下都不可能用 C 实现它。

`objc_msgSend` 的快速路径会执行几个关键操作：

1. 加载对象的类（class）。
2. 在该类的方法缓存（method cache）中查找选择器（selector）。
3. 跳转到缓存中找到的方法实现（method implementation）。

从方法实现的角度看，就像是调用者直接调用了它。因为 `objc_msgSend` 会直接跳转到方法实现，而不经过一次函数调用，所以它在完成工作后就有效地消失了。它的实现会小心地避免干扰任何可用于向函数传递参数的寄存器。调用者调用 `objc_msgSend` *就像*要直接调用方法实现一样，以与直接函数调用完全相同的方式传递所有参数。一旦 `objc_msgSend` 查找到实现并跳转过去，这些参数仍然正好位于实现所期望的位置。当实现返回时，它直接返回给调用者，返回值通过标准机制提供。

这回答了上面的问题：`objc_msgSend` 的原型就是它最终调用的方法实现的原型。

但等等，动态方法查找和消息发送的全部意义不就在于你并不知道会调用哪个方法实现吗？没错！然而，你确实知道该实现会有什么样的*类型签名*（type signature）。编译器可以从 `@interface` 或 `@protocol` 块中的方法声明获取这一信息，并利用它来生成适当的参数传递和返回值获取代码。如果你重写了一个方法，而类型签名不匹配，编译器会报错。通过隐藏声明或在运行时添加方法可以绕过这一点，在这种情况下，你最终可能会得到一个与调用点不匹配的方法实现类型签名。这种调用的行为就取决于这两个类型签名在 ABI 层面的匹配程度，结果可能从完全合理且正确的行为（如果 ABI 匹配，所有参数恰好对齐）到完全胡闹（如果不匹配）。

这间接回答了本文的问题：旧原型在某些情况下（当 ABI 匹配时）能正常工作，但在其他情况下（当 ABI 不匹配时）会以奇怪的方式失效。新原型除非你先将其转换为适当的类型，否则永远无法工作。只要你转换成了正确的类型，它就总能工作。因此，这种新的做法鼓励正确地行事，并使得出错变得更加困难。

**最小原型**  
尽管 `objc_msgSend` 的原型取决于将要被调用的方法实现，但所有方法实现都有两个共同点：第一个参数总是 `id self`，第二个参数总是 `SEL _cmd`。任何额外参数的数量和类型是未知的，返回类型也是未知的，但这两个参数是已知的。`objc_msgSend` 需要这两条信息来完成其消息派发（method dispatch）工作，因此它们必须始终位于相同的位置，以便它能够找到它们。

我们可以为 `objc_msgSend` 编写一个近似的泛化原型来表示这一点：

```
    ??? objc_msgSend(id self, SEL _cmd, ???)
```

这里的 `???` 表示我们不知道，它取决于将要被调用的具体方法实现。当然，C 语言没有办法表示这种通配符。

对于返回值，我们可以尝试选择一个常见的类型。由于 Objective-C 全是关于对象（object）的，假设返回类型是 `id` 是合理的：

```
    id objc_msgSend(id self, SEL _cmd, ???)
```

这不仅涵盖了返回值是对象的情况，也涵盖了返回值是 `void` 以及返回值是其他类型但未被使用的情况。

参数呢？C 语言实际上有一种方式来表示任意数量的任意类型的参数，即可变参数函数原型（variadic function prototype）。参数列表末尾的省略号表示后面跟着可变数量的任意类型值：

```
    id objc_msgSend(id self, SEL _cmd, ...)
```

这正是此次变更之前的原型。

**ABI 不匹配**  
运行时的一个关键问题是调用点处的 ABI 是否与方法实现的 ABI 匹配。也就是说，接收方会从相同位置、以相同格式获取参数吗？如果调用者将参数放入 `$rdx`，那么实现也需要从 `$rdx` 取回该参数，否则就会造成混乱。

最小原型可能能够表达传递任意数量任意类型参数的概念，但要在运行时实际工作，它必须使用与方法实现相同的 ABI。而该实现几乎肯定使用了不同的原型，并且通常具有固定数量的参数。

无法保证可变参数函数的 ABI 与固定数量参数的函数的 ABI 一致。在某些平台上，它们几乎完美匹配。在其他平台上，它们则完全不匹配。

**Intel ABI**  
让我们看一个具体的例子。macOS 使用标准的 [System V ABI for x86-64](https://www.uclibc.org/docs/psABI-x86_64.pdf)。ABI 中有大量细节，但我们只关注基础知识。

参数通过寄存器传递。整数参数按顺序通过寄存器 `rdi`、`rsi`、`rdx`、`rcx`、`r8` 和 `r9` 传递。浮点参数通过 SSE 寄存器 `xmm0` 到 `xmm7` 传递。调用可变参数函数时，寄存器 `al` 被设置为用于传递参数的 SSE 寄存器的数量。整数返回值放在 `rax` 和 `rdx` 中，浮点返回值放在 `xmm0` 和 `xmm1` 中。

可变参数函数的 ABI 与普通函数的 ABI 几乎完全相同。唯一的例外是在 `al` 中传递使用的 SSE 寄存器数量。然而，当使用可变参数 ABI 来调用普通函数时，这是无害的，因为普通函数会忽略 `al` 的内容。

C 语言把事情弄乱了一点。C 语言规定，某些类型在作为可变参数传递时会被提升为更宽的类型。小于 `int` 的整数（如 `char` 和 `short`）会被提升为 `int`，而 `float` 会被提升为 `double`。如果你的方法签名包含这些类型之一，那么调用者如果使用可变参数原型，就无法以该确切类型传递参数。

对于整数来说，这实际上无关紧要。整数被存储在相应寄存器的低位比特中，无论哪种方式，比特位最终都会出现在相同位置。然而，对于 `float` 来说，这是灾难性的。将较小的整数转换为 `int` 只需要用额外的比特位填充。而将 `float` 转换为 `double` 则涉及到将值完全转换为另一种结构。`float` 中的比特位与 `double` 中的相应比特位并不对齐。如果你试图使用可变参数原型来调用一个接受 `float` 参数的非可变参数函数，该函数将收到垃圾值。

为了说明这个问题，这里有一个快速示例：

```
    // 使用 objc_msgSend 的旧可变参数原型。
    #define OBJC_OLD_DISPATCH_PROTOTYPES 1

    #import <Foundation/Foundation.h>
    #import <objc/message.h>

    @interface Foo : NSObject @end
    @implementation Foo
    - (void)log: (float)x {
        printf("%f\n", x);
    }
    @end

    int main(int argc, char **argv) {
        id obj = [Foo new];
        [obj log: (float)M_PI];
        objc_msgSend(obj, @selector(log:), (float)M_PI);
    }
```

它产生以下输出：

```
    3.141593
    3370280550400.000000
```

如你所见，当写成消息发送时，值正确传递，但通过显式调用 `objc_msgSend` 传递时，值完全被破坏了。

这可以通过将 `objc_msgSend` 转换为具有正确的签名来补救。回想一下，`objc_msgSend` 的实际原型就是最终被调用的任何方法的原型，因此使用它的正确方式是将其转换为相应的函数指针类型。这个调用可以正确工作：

```
    ((void (*)(id, SEL, float))objc_msgSend)(obj, @selector(log:), M_PI);
```

**ARM64 ABI**  
让我们看另一个相关示例。iOS 使用 [标准 ARM64 ABI 的一个变体](https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/iPhoneOSABIReference/Articles/ARM64FunctionCallingConventions.html)。

整数参数通过寄存器 `x0` 到 `x7` 传递。浮点参数通过 `v0` 到 `v7` 传递。额外的参数通过栈传递。返回值放在与其作为参数传递时相同的寄存器中。

这只适用于普通参数。可变参数永远不会通过寄存器传递。它们总是通过栈传递，即使参数寄存器可用。

没有必要仔细分析这在实践中会如何表现。ABI 完全不匹配，通过未经转换的 `objc_msgSend` 调用的方法将在其参数中收到垃圾值。

**新原型**  
新原型简短而精炼：

```
    void objc_msgSend(void);
```

这完全不对。然而，旧原型也不对。这个新原型则更为*明显*地不正确，这是一件好事。旧原型使得人们容易在不进行类型转换的情况下使用它，并且它经常能正常工作，以至于你很容易认为一切都没问题。当你遇到有问题的情形时，bug 则非常不明确。

这个原型甚至不允许你传递 `self` 和 `_cmd` 这两个必需参数。你可以在不传递任何参数的情况下调用它，但它会立刻崩溃，并且出错的原因应该非常明显。如果你尝试在不进行类型转换的情况下使用它，编译器会报错，这比奇怪的参数值损坏要好得多。

因为它仍然是一个函数类型，你仍然可以将其转换为适当类型的函数指针，并通过这种方式调用它。只要你正确设置了类型，这就能正常工作。

喜欢这篇文章吗？我正出售包含全部文章的书籍！第二卷和第三卷现已上市！提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击此处获取更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/objc_msgsends-new-prototype.html)

发表你的想法，发布评论：

垃圾评论和离题评论将被删除，恕不另行通知。违规者可能会由我全权酌情公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
