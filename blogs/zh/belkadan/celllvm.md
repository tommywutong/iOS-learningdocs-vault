---
title: CellLVM
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2023/12/CellLVM/'
original_language: en
published: 2023-12-28
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:292c1de0094be558'
translated: true
---

> 原文：[CellLVM](https://belkadan.com/blog/2023/12/CellLVM/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Protobuf 几乎可以流式处理](https://belkadan.com/blog/2023/12/Protobuf-Is-Almost-Streamable/)

[最大的最小 PNG](https://belkadan.com/blog/2024/01/The-Biggest-Smallest-PNG/) »

« [没有所谓的「隐式原子」](https://belkadan.com/blog/2023/10/Implicity-Atomic/?tag=compilers)

« [「FIXME」不总是意味着「修复我」](https://belkadan.com/blog/2018/04/FIXME/?tag=llvm)

« [GitMounter](https://belkadan.com/blog/2023/11/GitMounter/?tag=source-code)

## [CellLVM](#)

几周前我发了这个：

[（屏幕录像）](https://belkadan.com/blog/2023/12/CellLVM/CellLVM.mp4)

如果你现在没兴趣看视频的话，这其实是一个把 LLVM 编译成 Excel 电子表格的概念验证编译器。

### 是什么。

前一天晚上，我和朋友们聊起了 [CSV](https://en.wikipedia.org/wiki/Comma-separated_values)，尤其是拿对齐图表（alignment chart）开玩笑，讨论什么样的东西才算得上「真正的」CSV。有人指出，按照惯常的打印方式，汇编代码其实也可以算一种 CSV，我当时回了一句

> 哦，在 Excel 里搞 asm 差点就要绕回成一个好主意了  
>  你的标签就是行引用

我躺在床上的时候意识到，这个类比其实比我一开始想的更贴切。别管 CSV 那部分了，真正让 Excel 能做*计算*的是行引用。虽然理论上也能拿汇编凑出这个效果，但有一个更合适的替代品：LLVM。

### SSA 格式

[LLVM](https://llvm.org) 是一个用来构建编译器及相关工具的库——实际上 Swift 和 Rust 用的就是它。^[1](#fn:gcc) 它的核心是一门被精简过的语言，也叫 LLVM，或者也可以叫「[LLVM 指令集](https://llvm.org/docs/LangRef.html)」。这门语言的独特之处，除了它是被设计成用来编译更高级语言的中间阶段之外，还在于每个局部变量都只会被赋值恰好一次，赋的是一个只能依赖于它之前变量的简单表达式。这就叫做[静态单赋值形式（SSA）](https://en.wikipedia.org/wiki/Static_single-assignment_form)。

我的这个洞见——我觉得应该不算新——是 Excel 公式的工作方式其实是一样的。任何一个带公式的单元格，公式都是预先定义好的，数值则根据公式里设定的引用关系在表格里流动——这和 SSA 一模一样。所以理论上，对于 LLVM 和 Excel 都支持的操作，应该可以把一个 LLVM 函数改写成一张执行同样计算的 Excel 表格！

我带着这个兴奋的想法睡着了。醒来后我意识到了这个方案的主要问题：那循环怎么办？

### Phi Nodes

为了让 SSA 能表示分支控制流（比如条件递增），必须有某种方式记录分支重新汇合时的「历史」。惯常做法是引入一种特殊的表达式，叫 phi node，它基本上是在说「如果我们是从 true 分支过来的，就用 x~1 作为值；如果是从 else 分支过来的，就用 x~2 作为值」。「phi」这个名字不是任何词的缩写；据说它只是刻意取得接近「fi」——也就是倒过来写的「if」。^[2](#fn:args) 这种形式对 switch 语句同样适用（只是可能的前驱更多），甚至对循环也适用：一个循环体的前驱可能是循环的入口，也可能是上一次经过循环时的最后一个基本块。

但电子表格没有循环啊，对吧？我查了一下，发现自己错了：Excel 电子表格确实支持循环，形式是「迭代计算」。只要公式能在一定步数内收敛到一个不动点，Excel 就能找到它。所以现在我需要弄清楚，怎样编码循环才能让它们真正收敛。

于是我从床上爬起来，开始在 Google Sheets 里捣鼓。（那天是周末，不用上班。）然后我想到了一个办法：真实 CPU 里那种经典「程序计数器」的一个变体。如果你记录下自己访问过的基本块数量（重复访问也算），你就总能知道「当前」的基本块是哪个，更重要的是知道「上一个」基本块是哪个。这样一来，你就能实现 phi node 了。

下面是一个 phi 表达式在 Excel 里长什么样：

| `=CHOOSE(` | phi 是一个选择… |
|---|---|
| ` XMATCH(` | 基于某个来源，在多个值之间选… |
| ` MAX(` | 这个来源就是最近的（也就是最大的）PC… |
| ` IF(B5=ROW(),C5,0),` | 来自第 5 行的分支，如果它是从这里过来的话… |
| ` IF(B10=ROW(),C10,0),` | 来自第 10 行的分支，如果它是从这里过来的话… |
| ` C7-0.5),` | 以及当前这一行（第 7 行），作为兜底… |
| ` {C5,C10,C7-0.5}),` | 把这些值当作一个数组，用 `XMATCH` 求出索引… |
| ` B4,B8,B7)` | 再用 `CHOOSE` 选出正确的值 |

不算好看，但能干活。有了这个之后，我就知道这事是可行的，于是着手去写这个编译器。

### 编译器

实际的编译器代码少得可怜，只有 150 行，一部分原因是它几乎没实现什么功能，但也因为它本身确实没做多少工作。所有困难的部分都在 LLVM 里（以及它的封装库 [LLVMSwift](https://github.com/llvm-swift/LLVMSwift)，这个库我还[不得不 fork 了一份](https://belkadan.com/source/LLVMSwift/)）和 [xslxwriter](https://libxlsxwriter.github.io/) 里（以及[它自己的封装库](https://github.com/damuellen/xlsxwriter.swift)）。没有这些现成的库，一天之内做出这个东西是不可能的。

这个编译器对单个 LLVM 函数做两趟遍历：一趟给各条指令和基本块分配行号，另一趟把每条指令 1:1 翻译成一个公式。真正相关的列只有三列：一个标注指令类型的标签、每条指令的值，以及上面说的那个「程序计数器」。[如果你想看，可以读读全部代码。](https://belkadan.com/source/CellLVM/)

最终成果是一个命令行工具，输入 LLVM bitcode，输出一个 xlsx 文件。如果输入里有一个以上的函数，或者出现了它不支持的操作（比如说，减法），它就会报错。但我确实认为这是一个站得住脚的概念验证！当然，这也是个成功的项目——这一点很重要，毕竟[我现在下班之后没法在电脑上花太多时间了。](https://belkadan.com/blog/2021/07/Keyboard-Pants/)

[上面那段视频的输出结果放在 Google Sheets 上](https://docs.google.com/spreadsheets/d/1_K4gMtS0GGviPAIFkhGZmXXFXvuaAatxcx2ulM1XZXk/edit)，不过如果你想「运行」它，得先自己复制一份。它把两个输入相加，然后不断翻倍，直到结果大于 50。（目前这个实现大概就只会处理这些。）

### 未来方向：alloca

这个概念验证里*没有*实现的一件事是 alloca，也就是局部变量。这既不方便——因为这是非优化构建的默认选项——也确实是把 LLVM*真正*编译成电子表格这件事里缺失的一块。问题在于，LLVM 的 load 和 store 指令在某种意义上*确实*是命令式的，这一点电子表格做不到。所以要真正表示一个内存位置，我们大概需要把一次 load 表达成「与该位置匹配的最近一次 store 的值」，就像我们把 phi 表示成「基于最近一个基本块的若干个值之一」那样。循环那边大概也有些棘手之处——也许「程序计数器」实际上应该按指令计数，而不是只按基本块计数，这样「最近」才能包含「但不能是我未来的那次」这种情况。

走到这一步，距离*任意*内存分配依然还有一跳，但也许没有想象中那么大。只要把 store 拆分成一个个独立的字段，我们就可以说 H 列代表堆内存，I 列代表它最后一次被修改的时刻。这会是一个*涉及程序里每一条 store 指令*的公式，但也许能行得通。不过我还没试着把细节想清楚。

### 未来方向：调用栈

另一个重要的缺失是函数调用。对于非递归函数来说，这基本上就是一种奇怪的分支/phi 组合，但对递归函数来说就有问题了：我们所有的局部 SSA 变量都得身兼两职！除了用*列*来表示栈帧之外，我目前没有什么好办法来做这件事。（这样一来，栈溢出就变成了「用完了带有正确公式的列」。）这样做还有个好处，就是你能*看到调用栈*，但我还没想清楚它到底能不能真的行得通。

1. 也有一个 [Rust 的 GCC 后端](https://rust-gcc.github.io)！不过还在开发中。[↩︎](#fnref:gcc)
2. Swift 在它的 IR 里对这个概念用了另一种表示方式：[基本块参数](https://github.com/apple/swift/blob/main/docs/SIL.rst#basic-blocks)。基本块不再通过 phi node 指定如何取得它要用的值，而是改成跳转到该基本块的分支必须把该基本块可能需要的所有值都传过去。我觉得这种模型更容易理解，但如果要翻译成 Excel 就会麻烦得多，所以今天我很庆幸 LLVM 用的是 phi node！[↩︎](#fnref:args)

本文发表于 [十二月](https://belkadan.com/blog/2023/12) 28 日, [2023](https://belkadan.com/blog/2023)，归类于 [技术](https://belkadan.com/blog/technical)。标签：[编译器](https://belkadan.com/blog/tags/compilers)、[LLVM](https://belkadan.com/blog/tags/llvm)、[电子表格](https://belkadan.com/blog/tags/spreadsheets)、[源代码](https://belkadan.com/blog/tags/source-code)
