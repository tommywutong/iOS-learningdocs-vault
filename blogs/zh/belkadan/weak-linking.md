---
title: 弱链接
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2011/07/Weak-Linking/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ca1ade5d229a1faf'
translated: true
---

> 原文：[Weak Linking](https://belkadan.com/blog/2011/07/Weak-Linking/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [在 Xcode 里用 SVN 版本的 Clang](https://belkadan.com/blog/2011/07/Using-Clang-from-SVN-in-Xcode/)

["「小细节，大讲究」"](https://belkadan.com/blog/2011/08/Little-Big-Details/) »

« [自动引用计数](https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/?tag=compilers)

["跳过 FFI"](https://belkadan.com/blog/2015/01/Skip-the-FFI/?tag=compilers) »

[动态链接对 App 不好，静态链接对 App 同样不好](https://belkadan.com/blog/2022/02/Dynamic-Linking-and-Static-Linking/?tag=linking) »

## [弱链接](#)

当你编译一个用到外部库或框架的程序时，最后一步（至少是接近最后的一步）是把你程序里用到的所有函数等等，跟它们在库里的实现对接起来。这个过程叫做"链接（linking）"。^[1](#fn:simplified)

一段时间之前，Apple 意识到，当他们给框架添加新功能时（通常伴随每个新系统版本的发布），大家可能想用上这些新功能，同时又想保持对旧系统的向后兼容。于是他们加入了一个叫[弱链接](http://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPFrameworks/Concepts/WeakLinking.html#//apple_ref/doc/uid/20002378-106633-CJBGFCAC)的特性。Apple 并不是第一个意识到这可能是个问题的公司，我也不知道他们是不是第一个想出弱链接这个办法的。（其实这甚至都不是他们第一次这么干了；据说 Mac OS Classic 的 Code Fragment Manager 里就有类似的能力。）不过我第一次听说这东西，就是从 Apple 这儿。

这是它的用法（摘自上面链接里 Apple 的指南）：

> 如果一个弱链接的符号在框架里不可用，链接器会把这个符号的地址设为 `NULL`。你可以在代码里用类似下面这样的代码来检查这个地址：

```
extern int MyWeakLinkedFunction() __attribute__((weak_import));
int main() {
    int result = 0;
    if (MyWeakLinkedFunction != NULL) {
        result = MyWeakLinkedFunction();
    }
    return result;
}
```

> **注意：** 检查一个符号是否存在时，你必须在代码里显式地把它和 `NULL` 或 `nil` 做比较。你不能用取反运算符（ `!` ）对这个符号的地址取反。

我不太确定为什么会有这条注意事项；我很确定就算不这么做，用现代的 GCC 或 Clang 也照样能正常工作。不过我没有实际测试过。

总之，挺酷的，对吧？如果你想用上只在 10.6 才有的东西（比如说，[关联对象](http://developer.apple.com/library/mac/documentation/cocoa/conceptual/ObjectiveC/Chapters/ocAssociativeReferences.html#//apple_ref/doc/uid/TP30001163-CH24-SW1)），你可以在不牺牲向后兼容性的前提下做到这一点。

函数当然挺好用，但其他符号呢？Webmailer 用 [`NSImageNameStatusAvailable`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSImage_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSImageNameStatusAvailable) 这个常量来显示 iChat 里那个标准的"在线"图标，用它来表示哪个目的地是活跃的。我当时是这么用的：

```
NSImage *activeImage;
// No need to redeclare it as weak-linked: AvailabilityMacros.h takes care of it.
if (NSImageNameStatusAvailable != NULL) {
    activeImage = [[NSImage imageNamed:NSImageNameStatusAvailable] copy];
} else {
    // Fall back to an image in our bundle.
    activeImage = [[NSImage alloc] initWithContentsOfFile:[bundle pathForImageResource:@"active"]];
}
```

结果它没有正常工作。尽管我检查了这个图片名是不是 `NULL`，它看起来还是无条件地在加载这张图片。

看出问题了吗？

我们再看一遍说明：

> 如果一个弱链接的符号在框架里不可用，链接器会把这个符号的**地址**设为 `NULL`。

啊哈！对啊。你得能区分开"值是 `NULL` 的变量"和"根本不存在的变量"。对函数指针来说，这没关系：当你写下像 `objc_getAssociatedObject` 这样的函数名时，编译器会把它当成 `&objc_getAssociatedObject` 来处理。但对 `NSImageNameStatusAvailable` 来说就不是这样了，它只是一个全局常量，一个指向 NSString 的指针。

我本该这样写才对：

```
if (&NSImageNameStatusAvailable != NULL)
```

这样确实管用。以后可得小心点！

顺便说一句，Greg Parker 写过一篇关于[弱链接_类_](http://www.sealiesoftware.com/blog/archive/2009/09/09/objc_explain_Weak-import_classes.html)的好文章，不过因为这只在框架第一个_编译时_就支持弱链接类的版本之后才有效，你只能在 Mac OS X v10.7+ 或 iOS 3.1+ 上使用它们。*唉* 在那之前，你只能用老办法，靠 `NSClassFromString` 在运行时看看某个类是否可用。

### 附言：这是怎么实现的？

在普通代码里，你知道一个变量的地址不可能是 `NULL`。显然，只要这个变量存在，它就活在内存里的某个地方，而 C 标准_保证_这个地址不会是 `0`。^[2](#fn:null) 但对于弱链接的符号来说，_这个变量可能根本不存在，_所以它的"地址"有可能是 `NULL`，其实是相当合理的。

这是怎么实现的呢？基本上就像 C++ 的引用：一个弱链接的符号 `X`，实际上还有一个名字类似 `X$non_lazy_ptr` 的"影子"符号。每次你引用 `X`，编译器内部都会把它替换成 `*X$non_lazy_ptr`。

那 `X$non_lazy_ptr` 是怎么拿到它的值的呢？当你加载 bundle 时，有两个秘密函数，分别叫 `dyld_stub_binding_helper` 和 `__dyld_func_lookup`。我（不太靠谱的）理解是：前者会遍历你所有动态链接的符号，然后用后者去找到正确的地址，"填进"这些"影子指针"里。

这基本上就是一种规模很小的自修改代码，但正是它让弱链接得以实现。挺酷的，对吧？

1. 当然，这是对链接器实际工作原理的极度简化。如果你是计算机专业的，大概多少学过一点链接器的知识；如果没学过，那也没关系，反正你多半短期内也用不着自己写一个。如果你还想找个解释来看看，[这里有一篇](http://thecoffeedesk.com/news/index.php/2009/06/01/how-linker-works/)，是我在 Google 搜"什么是链接器"时第一页结果里找到的。 [↩︎](#fnref:simplified)
2. 呃，其实吧，这可能并不对。真正能保证的是：如果你把整数 `0` 转换成指针值，你会得到空指针；空指针不会指向任何有效对象；空指针的条件值是 `false`。但我不认为标准规定空指针的_表示_必须是 `0`，这意味着对 `0` 做 C++ 的 `reinterpret_cast`，理论上是有可能得到一个有效指针的。我觉得是这样。

  实际中，几乎所有人都用 `0` 来表示空指针。 [↩︎](#fnref:null)

本文发表于 [七月](https://belkadan.com/blog/2011/07) 29 日, [2011](https://belkadan.com/blog/2011)，归类于 [技术](https://belkadan.com/blog/technical)。标签：[编译器](https://belkadan.com/blog/tags/compilers)、[链接](https://belkadan.com/blog/tags/linking)
