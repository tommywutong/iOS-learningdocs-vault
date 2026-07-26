---
title: 诊断工程系的 Gregory Parker 博士
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2010/09/01/Dr_Gregory_Parker_Department_of_Diagnostic_Engineering.html'
original_language: en
published: 2010-09-01
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b2e9d15da102f884'
translated: true
---

> 原文：[诊断工程系的 Gregory Parker 博士](http://sealiesoftware.com/blog/archive/2010/09/01/Dr_Gregory_Parker_Department_of_Diagnostic_Engineering.html)　·　Hamster Emporium (Greg Parker)

[![](http://sealiesoftware.com/hamster.jpg)](http://sealiesoftware.com/blog/index.html)  
  
 **博客**  
 [最近](http://sealiesoftware.com/blog/index.html)  
 [归档](http://sealiesoftware.com/blog/archive/index.html)  
 [twitter](http://twitter.com/gparker)  
   
 **项目**  
 [Mac OS X](http://www.apple.com/macosx/)  
 [Keyboard](http://sealiesoftware.com/keyboard/index.html)  
 [backlight](http://sealiesoftware.com/keyboard/index.html)  
 [CSC Menu](http://sealiesoftware.com/cscmenu/index.html)  
 [Valgrind](http://sealiesoftware.com/valgrind/index.html)  
 [Fringe Player](http://sealiesoftware.com/fringe/index.html)  
 [pssh](http://sealiesoftware.com/pssh/index.html)  
 [Peal](http://sealiesoftware.com/peal/index.html)  
 [Frankenmouse](http://sealiesoftware.com/frankenmouse/index.html)

## Hamster Emporium 归档

\<\< [[objc explain]：objc_msgSend_vtable](http://sealiesoftware.com/blog/archive/2011/06/17/objc_explain_objc_msgSend_vtable.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [TargetConditionals.h 速查表](http://sealiesoftware.com/blog/archive/2010/8/16/TargetConditionalsh.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2010/09/01/Dr_Gregory_Parker_Department_of_Diagnostic_Engineering.html)

**诊断工程系的 Gregory Parker 博士** ([2010-09-01 3:15 AM](http://sealiesoftware.com/blog/archive/2010/09/01/Dr_Gregory_Parker_Department_of_Diagnostic_Engineering.html))

上周，[Rick Ballard](http://twitter.com/rballard) 到我办公室来做了一次会诊。他抓到 Xcode 在 `objc_msgSend()` 里崩溃了。这个崩溃看起来像是一个困扰了 Xcode 好几个月的间歇性问题。于是他找来了调试 `objc_msgSend()` 方面的本地专家：诊断工程系的 Gregory Parker 博士。

好消息是，Rick 的这个崩溃能够稳定复现。在活着的病人身上做测试，总比在死者身上做尸检要强。坏消息是，那些常规的调试工具都没能帮上忙。`NSZombieEnabled` 和 `guardmalloc` 一无所获，而 `AUTO_USE_GUARDS=YES`（GC 版本的 `guardmalloc`）在耗尽地址空间之前，硬是把这台机器折腾了两个小时。

[你在 `objc_msgSend()` 里崩溃了](http://sealiesoftware.com/blog/archive/2008/09/22/objc_explain_So_you_crashed_in_objc_msgSend.html)。选择器是 `-isAbsolutePath`，这本身很合理，但意味着调试器的调用栈回溯里少了一帧。`objc_msgSend()` 从对象里读取了类，从类里读取了方法缓存，从方法缓存里读取了一个方法，然后在试图从这个方法里读取 `IMP` 时崩溃了。理论：要么这些数据结构中的某一个被某个内存破坏者撞坏了，要么原本那个对象本身就是伪造的，只是碰巧在正确的位置上有可以解引用的指针，才撑到了那一步。方法缓存的掩码是无效的——它本该是 2^n-1 这种形式——所以问题一定出在这条链路上、这一点之前或者正是这一点。

对象指针本身看起来是合理的。理论：这个对象是有效的，但同一位置上之前的某个对象，在被释放之后又被使用了。我们很幸运地拥有一个可复现的崩溃，于是我们打开了 `MallocStackLoggingNoCompact`，又跑了一遍。那块内存只被用于过一个对象，而且它并没有被释放。所以证据并不支持"释放后使用"这个理论。但历史记录显示，这个对象是作为一个 `NSPathStore2` 被分配的——这是 `NSString` 内部用来处理文件路径名的一个私有子类——这和选择器 `-isAbsolutePath`、以及调用点的预期都是吻合的。"对象指针是有效的"这个理论看起来站得住脚。

对象指针是好的，而方法缓存不是：问题就出在两者之间的链路上。对象的内容看起来是好的。这些字节看起来是交替出现的零和 ASCII 字符，这正是 `NSString` 内部所用 UTF-16 编码的明显特征。这个字符串值解码出来是 `@"/Xcode4/usr/bin/llvm-gcc"`，这在调用点的上下文里是说得通的。

这个对象的 `isa` 指针就不太妙了。它的值是 `0xa0050000`。这既不是 `NSPathStore2` 类，也不是任何其他类。`vmmap` 显示它位于 Foundation 的数据段里，而 `otool` 进一步显示，它具体位于 Foundation 的常量 CF 字符串里。但它指向的不是某个字符串的起始位置，而是某个字符串对象的中间位置。那个字符串对象是 `@"tzm-Latn"`：某种本地化相关的东西？理论：某个 bug 把这个对象的 isa 指针替换成了一个指向某个不相关的本地化字符串对象中间位置的指针。这听起来不像是个好理论。

回到白板前。症状：这个对象是作为 `NSPathStore2` 分配的。症状：这个对象的 `isa` 指针现在是 `0xa0050000`，而这不是 `NSPathStore2`。那 `isa` 指针本该是什么值？`otool` 和 `objc_getClass()` 的结果一致：正确的 `isa` 指针本该是 `0xa005f198`。`0xa0050000` 和它可疑地相似。理论：某个东西清空了这个对象的两个字节，留下了一个胡乱的 `isa` 指针。`@"tzm-Latn"` 只是个障眼法。

啊哈！这是 32 位的 i386。小端序。指针 `0xa005f198` 在内存里是反着存的：`0x98 0xf1 0x05 0xa0`。清空 `isa` 指针里最低有效字节，意味着清空的是这个对象的第 0 和第 1 字节，而不是第 2 和第 3 字节。第 0 和第 1 字节受损，正是内存中该对象前一个对象发生两字节溢出时会出现的典型症状。理论：这个 bug 出在前一个对象里，而这个 `NSPathStore2` 对象只是无辜的受害者。

`malloc_history` 也能处理指向某块分配内存中间位置的指针。我们把 `object-1` 这个地址代进去，得到的结果是一个 `DVTSourceModelItem` 的实例，并没有被释放。Rick 认出这是 Xcode 索引器的一部分，而它在崩溃发生时一直在另一个线程里运行着。来自 `DVTSourceModelItem` 对象的一次缓冲区溢出，和这些症状是吻合的。

但溢出到底发生在哪里？我原本预期溢出会出现在某个堆分配的 C 数组里，而不是一个普通对象上。而且 `DVTSourceModelItem` 的实例变量里也根本没有任何 C 数组。

理论：编译器或 runtime 为 `DVTSourceModelItem` 类的实例分配的内存太小了，而普通的 ivar 访问超出了这块分配的范围。这个想法有点碰运气，但很容易测试。`malloc_size()`、`class_getInstanceSize()`，以及肉眼数一遍 ivar 的数量，三者的结果都一致：这个对象是 32 字节。理论被推翻了。

我们又测试了一遍溢出理论。在 `DVTSourceModelItem` 末尾加一个没用到的 ivar，重新编译，运行。没有崩溃。去掉这个 ivar。崩溃。这个多出来的 ivar"修好"了这个 bug。缓冲区溢出理论依然和证据吻合，但我们就是找不到它。

没有别的想法了。我们需要数据。调试器的观察点（watchpoint）行不通：`DVTSourceModelItem` 有成千上万个实例，我们没法在每一个实例后面都盯着两个字节。我们还没有绝望到要去做暴力的代码审查。`AUTO_USE_GUARDS=YES` 或许能抓到它，如果它没先自己先垮掉的话。既然我们心里已经有了嫌疑对象，我们就可以自己动手，用一个更窄的目标玩一次 `guardmalloc` 的把戏。重写 `+[DVTSourceModelItem alloc]`，`mprotect()` 分配区之后的那一页，然后使劲交叉手指，祈祷在把时序改动这么大之后它还能复现。

砰！它崩溃了（好事），而且崩在了一个新地方（同样是好事）。`DVTSourceModelItem` 的 `-init` 正在写入自己的某个实例变量。这个 ivar 是位域（bitfield）里的一个位，而这个位域正好在 ivar 列表的末尾。

反汇编。生成的代码把这个位周围的 4 个字节读进一个寄存器，改变寄存器里的那一位，再把这 4 个字节写回内存。这对位域来说是很典型的写法。出乎意料的地方在于，这 4 个字节跨越了对象的最后两个字节，以及对象之后的头两个字节。这是个 bug。大多数时候这种越界访问是无效但无害的——它读取了两个不该读的字节，又把同样的值写了回去。但如果有另一个线程存在，它就可能崩溃：

| 线程 1 | 线程 2 |
|---|---|
| 读取四个字节，其中包括对象外的两个字节 |  |
|  | 分配一个新对象 |
|  | 写入一个 isa 指针 |
| 写入四个字节，把线程 2 刚写入的新值给覆盖掉了 |  |
|  | 崩溃 |

理论：一个编译器 bug 为 `DVTSourceModelItem` 的位域 ivar 生成了错误的代码，导致一次越界两字节的读-改-写，破坏了其他线程里的内存。测试：换一个编译器试试。`DVTSourceModelItem.m` 是用 `clang` 构建的，于是我们改用 `llvm-gcc` 重新编译。没有崩溃，反汇编看起来也是对的。再用 `clang` 编译一遍，又崩溃了。

诊断结果：`clang` 编译器在位域 ivar 上的一个 bug。在能做编译器移植手术之前，先给 `DVTSourceModelItem` 加一个多余的 ivar，暂时治好病人的症状。

耗时：大约三个小时。对于一集电视连续剧的破案戏码来说，可惜是长了点。

[Sealie Software](http://sealiesoftware.com/index.html)
