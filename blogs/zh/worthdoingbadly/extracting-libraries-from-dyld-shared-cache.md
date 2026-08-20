---
title: 从 dyld 共享缓存中提取库
source: worthdoingbadly (Zhuowei Zhang)
source_key: worthdoingbadly
source_url: 'https://worthdoingbadly.com/dscextract/'
original_language: en
published: 2018-06-24
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c86d58d42ba6fada'
translated: true
---

> 原文：[Extracting libraries from dyld_shared_cache](https://worthdoingbadly.com/dscextract/)　·　worthdoingbadly (Zhuowei Zhang)

# 从 dyld 共享缓存中提取库

2018 年 6 月 24 日

我学会了从 macOS 的 dyld 共享缓存中提取可用的共享库，并在这个过程中学到了一些关于 Mach-O 可执行文件、Objective-C 以及问题解决的知识。

## 引言

计算机程序会用到很多**库**，这些库包含不同程序共享的代码。当程序启动时，它需要加载所有需要的库，并链接它们，使它们能够互相调用函数。此外，Objective-C 运行时必须在每次加载库时对其进行初始化。这些任务会拖慢程序的启动速度。

macOS 和 iOS 通过将所有系统库合并到 [**dyld 共享缓存**](http://iphonedevwiki.net/index.php/Dyld_shared_cache) 中，来改善启动时间和内存使用：这个文件包含了操作系统内置的所有库，它们被链接在一起，并且 Objective-C 运行时已经完成了初始化。这样，程序启动时只需加载一个已经预处理好的文件，而不是加载和处理数百个文件。

在 iOS 上，由于所有系统库都在共享缓存中，因此会移除单独的库文件以节省空间。我正在进行一个项目，需要单独加载一个 iOS 系统库，所以为了得到这个库，我必须从共享缓存中把它提取出来。这意味着要撤销构建共享缓存时所做的所有预处理。

## 当前可用的工具

[iPhone Dev wiki](http://iphonedevwiki.net/index.php/Dyld_shared_cache#Cache_extraction) 列出了多种提取 dyld_shared_cache 的工具：然而，每种都有其缺点。

- [jtool](http://www.newosxbook.com/tools/jtool.html)：由 NewOSXBook 的 Jonathan Levin 编写，更新频繁，但不修复 Objective-C 选择器（selector）。
- Phoenix3200 的 [decache](https://github.com/phoenix3200/decache) 在 iOS 9 之后就无法使用了。
- Apple 自己的 [dsc_extractor](https://opensource.apple.com/source/dyld/dyld-519.2.2/launch-cache/dsc_extractor.cpp.auto.html)，当你第一次连接设备进行调试时，Xcode 会用到它（这就是“Preparing debugger support”做的事情）。提取出的库仅能用于向调试器提供符号。
- @comex 的 [imaon2](https://github.com/comex/imaon2)。Wiki 说它产生的输出质量最高，但很难编译。

最后两个看起来最有希望，因为它们都支持 iOS 11。听起来 imaon2 是唯一能生成可用库的工具，但我选择改进 Apple 的 dsc_extractor，因为我无法编译 imaon2，而且我也不需要 imaon2 的复杂性。

那么，imaon2 修复了哪些 dsc_extractor 没有修复的问题呢？要理解这一点，我们需要了解 macOS 可执行文件是如何工作的。

## Mach-O 入门

[**Mach-O**](https://en.wikipedia.org/wiki/Mach-O) 是 macOS 和 iOS 上使用的可执行文件格式。

有很多关于 Mach-O 文件的指南；例如，[@qwertyoruiopz 的演讲](https://news.ycombinator.com/item?id=17378829)，在撰写本文时，它就在 HN 的首页上。你可能应该读一读其中一篇来了解全貌，但这里对 Mach-O 文件做一个非常简短的总结。

一个 Mach-O 文件包含一个由一系列**加载命令（load command）**组成的头部——这些命令告诉 macOS 的动态库加载器 **dyld** 关于该文件的信息。一些加载命令指定了文件的元数据，例如它编译目标 macOS 版本或文件的入口点。

最重要的加载命令定义了**段（segment）**，它们是 Mach-O 文件中被加载到指定地址内存的部分。

大多数库中有三个段：

- __TEXT：包含不会变化的代码和数据
- __DATA：包含会变化的数据
- __LINKEDIT：包含供动态链接器执行的指令，用于：

    - 将库重定位到正确的内存地址
    - 导入它需要的函数
    - 导出它包含的函数

每个段还可以定义**节（section）**，它将段进一步细分为命名部分。例如，__DATA 段包含像 __objc_cfstring（包含 NSString）和 __objc_classlist（包含指向文件中定义的 ObjC 类的指针）这样的节。

（段和节的概念也存在于 [ELF](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format) 中，这是 Linux 和其他现代 Unix 系统使用的可执行文件格式。）

## imaon2：我真的需要它吗？

我花了太多时间试图编译 Comex 的 imaon2。结果发现 Comex 没有将 [Cargo.lock](https://doc.rust-lang.org/cargo/guide/cargo-toml-vs-cargo-lock.html) 文件添加到仓库中。这个文件指定了程序所需的所有 Rust 依赖项，类似于 CocoaPods 的 Podfile.lock 或 Yarn 的 Yarnfile。没有这个文件，根本无法编译这个程序。

所以，我转而研究了 imaon2 的源代码，想弄明白它为什么这么复杂。那 11448 行代码到底在做什么？

我发现 imaon2 在提取库时，确实会[修复 dyld 的所有优化](https://github.com/comex/imaon2/blob/master/src/fmt-macho_dsc_extraction/macho_dsc_extraction.rs#L319)。这对于找出我必须在 dsc_extractor 中实现什么很有帮助。

然而，这只是 imaon2 代码的一小部分。它的主要工作是将 __TEXT 和 __DATA 节重新拼接在一起。

在一个独立的库中，各个段会被加载到内存中相邻的位置：

| 0x000000000000 | BusinessChat __TEXT |
|---|---|
| 0x000000008000 | BusinessChat __DATA |
| 0x00000000B000 | BusinessChat __LINKEDIT |

但是，当库被添加到 dyld 缓存中时，这些段会被拆分，相同类型的段会被放在一起，以简化加载过程：

| 0x7FFF2002D000 | ClientFlowService __TEXT |
|---|---|
| ... | ... |
| 0x7FFF26A9C000 | BusinessChat __TEXT |
| ... | ... |
| 0x7FFF80000000 | ClientFlowService __DATA |
| ... | ... |
| 0x7FFF818EF000 | BusinessChat __DATA |
| ... | ... |
| 0x7FFFC0336000 | __LINKEDIT |

不幸的是，dyld 缓存还移除了重新排列段所需的信息，使得撤销这一更改变得非常困难。imaon2 尽力使用先进的静态分析将库恢复到原始状态。

但我真的需要那样做吗？我想要解决的问题实际上并不是重现原始库：我只是想运行提取出来的代码。

Apple 的 dsc_extractor 无法将段移回原处，因此提取出来的库在内存中会有很大的空隙：

| 0x7FFF2002D000 | BusinessChat __TEXT |
|---|---|
| 0x7FFF20035000 | 1.5 GB 的空闲空间 |
| 0x7FFF818EF000 | BusinessChat __DATA |
| 0x7FFF818FA000 | BusinessChat __LINKEDIT |

在 32 位系统上，这会浪费总共仅 2GB 地址空间中的 1.5GB，并且该库很可能无法在设备上加载。然而，目前所有的 macOS 和 iOS 设备都是 64 位的。在 64 位设备上，与可用的 [64GB（iOS）](https://www.mikeash.com/pyblog/friday-qa-2013-09-27-arm64-and-you.html) 或数 TB（macOS）地址空间相比，1.5GB 的地址空间是微不足道的。

（注意：上述实际上是一种简化：dyld 使用的 `mmap`，似乎[在 64 位 iOS 上限制为 2GB](https://github.com/apple/darwin-xnu/blob/0a798f6738bc1db01281fc08ae024145e84df927/osfmk/mach/arm/vm_param.h#L153)，正如[这里报告的那样](https://github.com/pixelglow/zipzap/issues/72)，但 Mach 虚拟内存 API 可以[映射到更高的内存地址](https://github.com/apple/darwin-xnu/blob/0a798f6738bc1db01281fc08ae024145e84df927/osfmk/mach/arm/vm_param.h#L157)。允许内存量的计算[相当复杂](https://github.com/apple/darwin-xnu/blob/0a798f6738bc1db01281fc08ae024145e84df927/osfmk/arm/pmap.c#L8983)，需要考虑设备的物理内存以及 App 是否可以执行 JIT。总之，我们有足够的地址空间。）

因此，我们的程序可以比 imaon2 更简单。

## Apple 自己的 dyld 缓存提取器

我决定基于 Apple 自己的 dyld 缓存提取器来开发，该提取器可以从 [Apple 的开源门户](https://opensource.apple.com/tarballs/dyld/) 获取。正如我之前提到的，它旨在为 iOS 调试提取库，而不是生成可用的库，所以它只进行了足够让调试器加载它的修复。然而，它是个很好的基础，因为它能很好地处理 macOS 10.13 和 iOS 11 的缓存，并且还附带一个不错的 Xcode 项目。（我只需要调整 Xcode 项目，将提取器库添加到可执行文件的依赖项中，然后才能构建它。）

## 读取未 rebase 的 dyld 缓存

我做的第一个更改是读取未经内核修改的 dyld 缓存。根据 [iPhoneDevWiki](http://iphonedevwiki.net/index.php/Dyld_shared_cache#Cache_retrieval) 的描述，在运行的系统上直接从磁盘读取缓存会得到一个修改过的版本，其中缺少必要的重定位信息。

即使是按照 Wiki 文章的建议，mmap 空内存然后用 F_NOCACHE 读取，似乎也不起作用。幸运的是，[一个旧版本的 dyld 本身](https://opensource.apple.com/source/dyld/dyld-195.5/launch-cache/update_dyld_shared_cache.cpp.auto.html)展示了正确的方法：分配非缓存（uncached）的 Mach 内存，然后从文件中读取非缓存的数据。

## 比较原始库和提取出的库

接下来，我开始比较原始库和 dsc_extract 提取出的版本。我需要一个足够小但功能齐全的库来进行测试。macOS 上的 BusinessChat 框架被证明是一个很好的候选。

为了比较这两个文件，Peter Saghelyi 的 [MachOView](https://sourceforge.net/projects/machoview/files/?source=navbar) 至关重要。它描述了每个段和节，解释了所有数据结构，并具有出色的十六进制视图。如果你在进行高级的 macOS/iOS 开发，你绝对需要它。

我还使用了 IDA Free——它能够解释文件中的 Objective-C 数据，并提供了更好的代码反汇编。

## 撤销 Objective-C 选择器的唯一化

我从 imaon2 的源代码和 [Twitter](https://twitter.com/theninjaprawn/status/905932038372458496) 上得知，我需要修复提取出的库中的 Objective-C 选择器。在此之前，这些选择器指向不存在的内存（在 IDA 中用红色文字表示）：

![来自 IDA 的反汇编，显示了 Objective-C 代码中的一个无效选择器](https://worthdoingbadly.com/assets/blog/dscextract/selector_unfixed1.png)

要理解为什么必须撤销这种 dyld_shared_cache 优化，我们需要看看 Objective-C 是如何工作的。

在 Objective-C 中，调用方法涉及[向对象传递一个对象和一个选择器（selector）](https://developer.apple.com/documentation/objectivec/1456712-objc_msgsend)以在该对象上调用。

Objective-C 运行时使用[这段代码](https://github.com/opensource-apple/objc4/blob/cd5e62a5597ea7a31dccef089317abb3a661c154/runtime/objc-runtime-new.mm#L4498)来查找与选择器匹配的正确方法，它非常简单，我甚至不需要用伪代码来表示：

```
//// zhuowei：mlist 包含对象的方法，sel 是要调用的方法的选择器
static method_t *search_method_list(const method_list_t *mlist, SEL sel)
{
    int methodListIsFixedUp = mlist->isFixedUp();
    int methodListHasExpectedSize = mlist->entsize() == sizeof(method_t);
    
    if (__builtin_expect(methodListIsFixedUp && methodListHasExpectedSize, 1)) {
        return findMethodInSortedMethodList(sel, mlist);
    } else {
        // 对未排序的方法列表进行线性搜索
        for (auto& meth : *mlist) {
            //// zhuowei：注意，选择器是通过其地址进行比较的
            if (meth.name == sel) return &meth;
        }
    }

    return nil;
}
```

注意（通过我的注释）选择器是通过它们的内存地址而不是通过字符串比较来比较的。这节省了时间，但意味着程序中只能有一个选择器的唯一实例。这需要编译器和 Objective-C 运行时的共同协助。

像 `[NSObject new]` 这样的 Objective-C 代码会被编译器翻译成类似下面的内容：

```
// 库 1
SEL mySelector = "new";
SEL* pointerToUniqueSelector = &mySelector;

objc_msgSend(NSObject, *myPointerToUniqueSelector);
```

如果我们有另一个库也调用了“new”：

```
// 库 2
SEL yourSelector = "new";
SEL* yourPointerToUniqueSelector = &yourSelector;

objc_msgSend(NSObject, *yourPointerToUniqueSelector);
```

如果没有 Objective-C 运行时的干预，`yourSelector != mySelector`，第二个库将找不到正确的方法。因此，当一个库被加载时，Objective-C 运行时会更改变量引用来匹配：

```
// 库 2，加载后
SEL yourSelector = "new"; // unused
SEL* yourPointerToUniqueSelector = &mySelector; // modified to point to Library 1's copy

objc_msgSend(NSObject, *yourPointerToUniqueSelector);
```

现在两个调用都将使用相同的地址来表示这个选择器。

为了避免在启动时执行此操作，在构建 dyld 缓存时，这种选择器唯一化（selector uniquing）是预先完成的。根据 [Greg Parker](http://sealiesoftware.com/blog/archive/2009/09/01/objc_explain_Selector_uniquing_in_the_dyld_shared_cache.html) 的说法，这曾将 Mac OS X Snow Leopard 上加载 App 所需的时间减少了一半。

然而，这阻止了库的提取，因为从缓存中提取库时，我们得到的是：

```
// 库 2，提取后
SEL yourSelector = "new"; // unused
SEL* yourPointerToUniqueSelector = /* invalid address! since mySelector isn't in this file */

objc_msgSend(NSObject, *yourPointerToUniqueSelector);
```

选择器的唯一副本在另一个我们未提取的库中，所以在加载时，该指针指向一个无效地址。

我们可以通过遍历所有指向选择器的指针，找出它们在缓存中指向哪些选择器，然后在我们要提取的文件中找到等效的选择器来撤销这一点：伪代码如下：

```
for each pointerToSelector in pointer to selectors:
  selectorString = readFromCache(pointerToSelector);
  pointerToSelector = findStringInLocalLibrary(selectorString)
```

这修复了函数的反汇编：

![来自 IDA 的反汇编，显示了 Objective-C 代码中的一个有效选择器](https://worthdoingbadly.com/assets/blog/dscextract/selector_fixed1.png)

## 修复 rebase

下一个任务是重新生成 **rebase 信息（rebase info）**，它指定了将库从其原始链接地址移动到加载后内存地址所需的更改。

在构建 dyld 缓存时，原始库的 rebase 信息会被一个压缩版本取代。其格式在 [dyld 中有 Apple 的文档](https://github.com/zhuowei/dsc_extractor_badly/blob/master/launch-cache/dyld_cache_format.h#L150)，而且非常巧妙：它使用这些指针未使用的最高位作为链表来存储需要更改的指针列表，从而几乎免费地存储了重定位信息。

（它效果非常好，以至于 Apple 在 iOS 12 beta 中也采用了它来[压缩内核](https://bazad.github.io/2018/06/ios-12-kernelcache-tagged-pointers/)。）

不幸的是，普通的库不能使用这种压缩格式，因此必须将其转换回原始格式。

为此，我借用了 dyld 的代码来解释这种压缩格式，记录了它所做的每一项更改，并将这些更改写回提取出的库的 rebase 信息表中。

## 修复 Objective-C 信息

做了这两项更改之后，并且使用 [dyld 的调试变量](https://github.com/zhuowei/dsc_extractor_badly/blob/master/src/dyld.cpp#L199) 解决了其他一些问题后，我实际上可以通过 `dlopen` 调用来加载这个库了：

```
// 注意：我必须将库重命名为 "DusinessChat"，否则它会加载已在缓存中的 BusinessChat 版本
void* handle = dlopen("/private/tmp/System/Library/Frameworks/BusinessChat.framework/Versions/A/DusinessChat", RTLD_LOCAL | RTLD_LAZY);
Class clsBCChatButton = NSClassFromString(@"BCChatButton");
id anObj = [[clsBCChatButton alloc] initWithStyle:0];
```

然而，对 `initWithStyle` 的调用因“方法未找到”错误而崩溃。[使用 Stack Overflow 上的一个代码段](https://stackoverflow.com/questions/2094702/get-all-methods-of-an-objective-c-class-or-instance)来列出该对象上的所有方法也同样因为段错误而崩溃。为什么？

还记得查找与选择器匹配的正确方法的代码吗？它将所需的选择器与 `const method_list_t *mlist`（该类定义的方法列表）进行比较。当然，方法列表中的选择器也必须是唯一的。

与选择器引用列表一样，dyld 缓存也会预处理方法信息以引用唯一的选择器。同样，在提取库之后，方法列表包含指向无效选择器的指针，在 IDA 反汇编中以红色显示：

__objc_const:00007FFF818EFB40 _OBJC_INSTANCE_METHODS_BCChatButton __objc2_meth_list \<1Bh, 2Eh\> __objc_const:00007FFF818EFB40 ; DATA XREF: __objc_const:BCChatButton_$classData↓o __objc_const:00007FFF818EFB48 __objc2_meth \<7FFF250C68BCh, offset aV2408q16, \\ ; -[BCChatButton _setStyle:] ... __objc_const:00007FFF818EFB48 offset __BCChatButton__setStyle__\> __objc_const:00007FFF818EFB60 __objc2_meth \<7FFF25DC90B2h, offset aV1608, \\ ; -[BCChatButton .cxx_destruct] ... __objc_const:00007FFF818EFB60 offset __BCChatButton__cxx_destruct_\> __objc_const:00007FFF818EFB78 __objc2_meth \<7FFF25DC928Ah, offset a240816, \\ ; -[BCChatButton initWithCoder:] ... __objc_const:00007FFF818EFB78 offset __BCChatButton_initWithCoder__\>

因此，在提取时，也必须使用与之前完全相同的过程来撤销这一更改：只是这次我们遍历类列表以找到方法列表，而不是遍历选择器列表，并修复其中引用的每个选择器。修复后的方法列表如下所示，所有选择器都与预期方法匹配：

__objc_const:00007FFF818EFB40 _OBJC_INSTANCE_METHODS_BCChatButton __objc2_meth_list \<18h, 2Eh\> __objc_const:00007FFF818EFB40 ; DATA XREF: __objc_const:BCChatButton_$classData↓o __objc_const:00007FFF818EFB48 __objc2_meth \<offset sel__setStyle_, offset aV2408q16, \\ ; -[BCChatButton _setStyle:] ... __objc_const:00007FFF818EFB48 offset __BCChatButton__setStyle__\> __objc_const:00007FFF818EFB60 __objc2_meth \<offset sel__cxx_destruct, offset aV1608, \\ ; -[BCChatButton .cxx_destruct] ... __objc_const:00007FFF818EFB60 offset __BCChatButton__cxx_destruct_\> __objc_const:00007FFF818EFB78 __objc2_meth \<offset sel_initWithCoder_, offset a240816, \\ ; -[BCChatButton initWithCoder:] ... __objc_const:00007FFF818EFB78 offset __BCChatButton_initWithCoder__\>

## 修复延迟绑定指针

现在 Objective-C 方法可以找到了…… 然后在第一次调用 `objc_msgSendSuper` 时立刻发生段错误，跳转到了一个未映射的内存区域。要理解原因，我必须了解方法调用在 Mach-O 中是如何工作的。

为了加速库的加载，Mach-O 使用了**延迟绑定（lazy binding）**，它仅在第一次使用外部方法时才进行查找。为此，对外部方法的调用实际上会跳转到**桩（stub）**——一小段代码，它从 Mach-O 文件的 `__la_symbol_ptr` 节加载一个指针，然后跳转到该指针指向的地址。

当程序启动时，`__la_symbol_ptr` 中的每个指针都指向一个匹配的**解析函数（resolver function）**，其工作是查找与该桩对应的真正外部方法。

第一次调用外部方法时：

- 代码调用桩
- 桩从其 `la_symbol_ptr` 加载地址（最初指向其解析函数），并跳转到它
- 解析函数：

    - 实际找到要调用的函数
    - 将真正函数的地址写入 `la_symbol_ptr` 变量中
    - 跳转到真正函数

此后，将来的调用将：

- 调用桩
- 桩从 `la_symbol_ptr` 加载地址（现在包含解析函数存储的真正函数地址），并跳转到它

这意味着解析函数只在第一次被调用，后续调用的开销可以忽略不计。

（顺便提一下，Linux 上的 ELF 有完全相同的系统：它被称为[过程链接表（Procedure Linkage Table）](https://www.iecc.com/linker/linker10.html)。）

在构建 dyld 缓存时，它会尝试移除这种延迟加载：通过预先执行解析，它避免了在桩中进行初始查找。因此，当我们提取库时，桩的地址不是指向正确的解析函数，而是指向缓存中其他库中不存在的函数。

我们通过恢复 `__la_symbol_ptr` 中每个条目的解析函数来修复这个问题。为此：

对于每个解析函数：

- 获取解析函数的数据
- 找到解析函数必须写入最终地址的位置（即 dyld 缓存本应更改的内容）
- 将该位置的值更改为指向当前的解析函数

修复了这最后一个问题后，我就可以顺利运行测试程序了，这证明我们已经成功地从 dyld 共享缓存中提取了一个库。

## 遗留问题

我对 dsc_extractor 所做的所有更改都已[发布在 GitHub 上](https://github.com/zhuowei/dsc_extractor_badly/compare/original...master)。

所以现在我可以从 x86_64 架构中提取一个简单的库了：这当然没什么意义，因为我可以直接从磁盘上获取这个库。我真正想要的是从 arm64 iOS 中提取，因为那里没有单独的库文件。不幸的是，arm64 要复杂一些。

arm64 在每个库中还有两个段，__DATA_CONST 和 __DATA_DIRTY，我的 dyld 缓存重定位代码没有正确地重定位这些新段。由于所有其他修复都依赖于此，我目前还无法提取任何 arm64 架构的库。

此外，我还需要修复 Objective-C 协议（protocol）的选择器，就像我修复方法选择器那样。

我目前正在研究如何解决这些问题，以实现我的目标：从一个 iOS 固件中提取库并将其移植到另一个不同的固件。（敬请期待下周的第二部分！）

## 后记：但，我真的需要它吗？

所以我完成了所有这些复杂的工作，意图将一些代码从一个 iOS 固件移植到另一个。但我需要再次问自己，“我真的需要这个吗”？

我知道一个类似的 iOS 代码移植项目：[@stroughtonsmith](https://twitter.com/stroughtonsmith) 和 [@chpwn](https://twitter.com/chpwn) [将 Siri 移植到了 iPhone 4 上](https://www.theiphonewiki.com/wiki/Siri)。

Stroughtonsmith 和 Chpwn 没有经历所有这些麻烦来提取单个库，他们只是简单地[替换了某些进程的整个共享缓存](https://www.theiphonewiki.com/wiki/Siri#Shared_Cache_Injection)。据 Stroughtonsmith 说，这花了“[午饭时间的 15 分钟](https://twitter.com/stroughtonsmith/status/1010423049466851328)”，而我却花了一个月——而且还在继续——来学习提取一个库。我猜它可能也比我尝试的方法效果更好。

我想这其中的教训是：始终要设法找出你真正需要的是什么。我是否需要像 imaon2 试图生成的那样，一个与原始库完全相同的库？我是否需要像我所尝试的那样，一个能加载的独立库？还是我只需要将某些功能从一个设备移植到另一个设备？

## 我学到了什么

- 编程就像创业：首先找出你要解决的问题，这样你才能问“你真的需要它吗？”并为自己节省时间
- Mach-O 的工作原理，以及它的概念与 ELF 的相似之处
- Objective-C 运行时如何通过将选择器与唯一地址进行比较来解析方法
- 不起作用的开源代码仍然可以成为灵感，就像 imaon2 的 ObjC 修复模块帮助我意识到我需要做什么

## 备注

抱歉延迟了！由于时间不够，我不得不搁置我原定于 6 月 14 日的计划（我最终会回来的），所以我决定花尽可能多的时间来研究和撰写本周的文章。下周将恢复正常日程。

[https://worthdoingbadly.com/dscextract/](https://worthdoingbadly.com/dscextract/)
