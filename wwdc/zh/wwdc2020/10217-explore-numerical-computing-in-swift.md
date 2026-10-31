---
title: 探索 Swift 中的数值计算
session_id: 10217
collection: wwdc2020
year: 2020
duration: '15:24'
topics: [Swift]
group: I · 系统服务、进程与安全底层
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2020/10217/'
content_hash: 'sha256:9f611db4f6ce8858'
translated: true
---

# 探索 Swift 中的数值计算

<sub>WWDC2020 · 15:24 · Swift</sub>

认识 Swift Numerics：一个用于计算数学的全新 Swift 包。纵览包中提供的协议和类型……

> [!note] 归档理由
> Swift 数值计算

## 相关资源

- [Float16](https://developer.apple.com/documentation/Swift/Float16)
- [GitHub 上的 Swift Numerics](https://github.com/apple/swift-numerics)
- [数值协议](https://developer.apple.com/documentation/Swift/numeric-protocols)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10217/6/608C3CB1-C8BD-4B19-B5F3-5ADA44E200E3/wwdc2020_10217_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10217/6/608C3CB1-C8BD-4B19-B5F3-5ADA44E200E3/wwdc2020_10217_sd.mp4?dl=1)
- [认识 Swift Algorithms 与 Collections 包](https://developer.apple.com/videos/play/wwdc2021/10256)
- [Swift 的新变化](https://developer.apple.com/videos/play/wwdc2021/10192)
- [Swift 的新变化](https://developer.apple.com/videos/play/wwdc2020/10170)
- [对数几率函数（Double）](https://developer.apple.com/videos/play/wwdc2020/10217/?time=65)
- [对数几率函数（Real）](https://developer.apple.com/videos/play/wwdc2020/10217/?time=153)
- [Complex 类型](https://developer.apple.com/videos/play/wwdc2020/10217/?time=430)
- [Complex 类型：基本定义](https://developer.apple.com/videos/play/wwdc2020/10217/?time=458)
- [Complex 类型：标准算术运算](https://developer.apple.com/videos/play/wwdc2020/10217/?time=484)
- [Complex 类型：极坐标](https://developer.apple.com/videos/play/wwdc2020/10217/?time=499)
- [使用 Accelerate 的基本线性代数子程序](https://developer.apple.com/videos/play/wwdc2020/10217/?time=556)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，欢迎来到 WWDC。欢迎收看“探索 Swift 中的数值计算”。我叫 Tim Kientzle，来自 Swift 运行时团队。我想和大家聊聊 Swift 中浮点数值支持的最新改进。我会先介绍 Swift Numerics 包。除其他特性外，这个包包含一个名为 Real 的协议和一个功能完备的复数（Complex）类型。然后我会介绍我们加入 Swift 核心语言和标准库的全新高性能 Float16 类型。我们先整体看一下 Numerics 包。Swift Numerics 包是托管在 github.com 上的开源 Swift 开发项目。它的设计目标是让实现数值算法变得容易，而且这些算法能与任何标准浮点类型协作。它通过让标准浮点类型可以使用 Swift 的泛型编程设施来做到这一点。

要看看这是如何运作的，假设你在做某个项目时发现需要用到概率论中常见的 logit（对数几率）函数。你先定义一个接受并返回 Double 的 logit 函数。为实现这个函数，你从 Darwin 模块导入 log 和 log1p 函数。这段代码能工作，但有一个小问题。

它被写成只支持 Double。将来某天你可能想把它用于 Float，或者 Float80。对于这样一行代码来说，再复制一份没什么大不了。但是，如果将来新增了一种浮点类型怎么办？你该如何处理 Float80 这种只在特定平台可用的类型？当然，如果这个函数有几百行，那么复制就会带来问题：有人可能修好了其中一份的 bug，却忘了正确修改另一份。

这可能变得一团糟。所以我们换个方式，试着把 logit 定义为一个可用于任何浮点类型的泛型函数。这是一个合理的第一次尝试。可惜，这无法编译。问题在于我们告诉编译器这个函数适用于任何类型。

但当然，log 和 log1p 函数并非对每种类型都有定义。它们只对少数浮点类型才有意义。所以我们需要某种方式把类型 T 约束为那些真正拥有 log 函数的浮点类型。换个方式，我们导入 Numerics 模块。通过导入 Numerics 模块，我们获得了 Real 协议，它为这类编程提供了所有必要的支持。利用它，我们可以把 logit 函数定义成适用于任何功能完备的浮点类型。我们还需要使用 Numerics 模块暴露的 log 和 log(onePlus:) 的泛型形式。

这个版本的 logit 适用于每个标准浮点类型。如果将来新增浮点类型，这些代码无需任何改动就能支持它们。在支持 Float80 的平台上，它甚至可以直接用于 Float80，而你不必去琢磨那些神奇的条件编译。

关键在于 Real 协议。我们仔细看看它。

遵循 Real 协议的类型支持所有标准浮点能力。Real 是通过组合其他若干协议实现的，正如你在这里的定义中所见。顺便说一句，这个定义与你在 Numerics 源代码中看到的完全一致。

标准库的 FloatingPoint 协议是其中的一个关键组件。

另外两个协议 AlgebraicField 和 RealFunctions 是 Numerics 包定义的新协议。但在深入它们的细节之前，我想重申：你实际应该使用的是 Real 协议。我之所以要描述这些协议如何拼装在一起，是因为我认为这有助于更好地理解 Real 所带来的能力范围。当然，如果你某天需要定义一个新的数值类型，你大概率也会按这样的思路分解你的实现。但对你们大多数人来说，Real 是你日常唯一会用到的协议。记住这一点后，我们来回顾一下 Swift 标准库中已有的协议。Swift 标准库定义了许多适用于标准浮点类型的协议。这张图只列出了其中比较重要的几个。本次演讲我只关心其中的三个：AdditiveArithmetic、SignedNumeric 和 FloatingPoint。AdditiveArithmetic 适用于支持加法和减法的类型。它几乎涵盖了所有能合理自称某种“数”的东西，并且与数学家所说的“代数群”（Algebraic Group）很好地对应。SignedNumeric 在此基础上引入乘法的概念。最后，FloatingPoint 加入了任何实际的计算机浮点数实现所需的各种概念，包括比较函数、把数分解为指数和尾数的方式，以及有用的常量，比如最大最小值、无穷、pi 等等。Numerics 包正是构建在这些核心概念之上的。这里的第一个协议为 SignedNumeric 增加了除法的概念。数学家把支持全部四种基本运算的数系称为“代数域”（algebraic field），这个名字由此而来。

ElementaryFunctions 协议指定了庞大的常用浮点函数集合，包括核心三角函数以及对数、指数、根和幂。

RealFunctions 协议在这之上进一步扩展，加入了许多较少使用的函数，例如伽马函数和误差函数，以及常见三角函数的各种变体。

Real 协议把这一切合并成一个统一的概念，干净利落地定义了标准浮点类型的公共能力。

任何遵循 Real 协议的类型都是一个支持全部标准算术运算、并拥有完整常用数学函数库的浮点类型。这就是 Numerics 包让标准浮点类型比以往任何时候都更好用的方式。从根本上说，Real 协议是一个在实践中非常强大的简单概念。它让你可以用泛型编程技术来编写浮点代码，并自动支持每一种标准浮点类型。它构建在一组环环相扣的协议之上，这些协议应当能让定义新的数值类型变得容易。现在，我们转向 Numerics 包提供的复数支持。Swift Numerics 包中的 Complex 类型是标准复数类型的一个功能齐备的实现。要使用它，只需把 Numerics 包导入你的程序。

由于 Complex 类型以 Real 协议为泛型约束，它可以用于任何浮点类型。在这个例子中，常量 1.0 和 2.0 默认为 Double，所以这里的 'z' 是一个 Complex。一如既往，Swift 会为你推断类型，所以你通常可以直接省略类型标注。复数类型本身就很有用，但它同时也是展示 Real 协议如何支持泛型数值编程的一个绝佳范例。基本类型的定义大致像这样。

复数同时拥有实部和虚部，以及一种从这两个分量创建新复数的方式。这些分量可以是任何遵循 Real 协议的 NumberType。当然，要让复数功能齐备，我们还需要定义标准的算术运算。

这里是我们刚才讨论的 SignedNumeric 协议所要求的基本加法、减法和乘法运算。复数常用极坐标表示，也就是用长度和相位角来表示。由于实部和虚部都是遵循 Real 协议的浮点类型，我们自动获得了暴露长度和相位属性所需的一切。长度用标准的斜边（hypotenuse）函数定义，相位用标准的反正切函数定义。其他常见的三角函数让我们能够以指定的长度和相位创建新的复数。这个 Complex 类型是一个保存两个浮点值的普通结构体。因此，它的内存布局与 C 和 C++ 的复数类型精确一致。所以复数在内存中的样子在三种语言里完全相同。你可以在 Swift 中创建一个装满复数的缓冲，并把指向该缓冲的指针传给期望相应 C 或 C++ 复数类型的 C 或 C++ 库。要看看这是如何工作的，我们来看一个使用 Accelerate 的基本线性代数子程序（BLAS）实现的例子。这个例子的第一部分只是用一个常见的 Swift 惯用法创建了 100 个 Complex 值的数组。现在我们可以用 & 运算符把指向这个数组的指针直接传进 Accelerate API。

这个特定的函数接受一个 Complex 数组，计算欧几里得 2-范数并返回一个 Double。特别是在从 C 或 C++ 移植代码时，处理无穷大或 NaN 值时你可能需要小心。关于这些值应当如何运作，多年来存在不同的风格。C 和 C++ 彼此使用相同的风格并不奇怪，毕竟它们的复数支持大约在同一时间被标准化。

然而，Swift 使用一个略不同的约定，它更简单，而且性能显著更好。要看看差别，这里有一个基本的基准测试程序，它只是执行一大堆复数乘法和除法。

用这个程序，乘法在 Swift 中比在 C 中快约 1.3 倍，除法快接近 4 倍。而且，如果你能把工作安排成除以一个常量，你会发现 Swift 中的除法可以快 10 倍以上。我希望前面几节已经让你初步了解了我们想用 Swift Numerics 包实现的目标。这仍是一项进行中的工作。这个包作为社区项目在 GitHub 上开发，关于它未来的走向有活跃的讨论。新功能定期加入，最近就包括对整数幂的改进处理，以及一些处理近似相等的新工具。目前还有活跃的讨论，探讨如何扩展这个库以支持任意精度整数、带形状的数组（shaped arrays）和十进制浮点数。如果你想参与，请到 github.com 上查看该项目，或加入 Swift 论坛的讨论。现在，让我们转向 Swift 核心语言和标准库，以及新的 Float16 数据类型。Float16 是一种 IEEE 754 标准浮点格式，对 Swift 而言是新的。它已经在基于 ARM 的平台上随 Swift 提供，我们正在与 Intel 合作确定正确的调用约定，之后才会在 x86 上落地。Float16 在各方面都是一个标准的、获得完全支持的浮点类型。它遵循标准库的核心协议，包括 SIMDScalar 之类的东西。它遵循我在本演讲前面讨论过的 Real 协议。你记得的话，这意味着它支持所有标准的浮点运算和函数。所以我们之前那张展示遵循 Real 的类型的图，现在有了第四个类型。在 Swift Numerics 发布后的几个月里，已经有一些项目在使用 Real 协议编写跨所有标准浮点类型工作的算法。这些项目无需任何源代码改动，就已经能配合 Float16 工作。与任何实际的数值格式一样，用 Float16 替代其他类型存在取舍。这些取舍大多只与它的大小有关。由于它是更小的数据类型，你能在同一个 SIMD 寄存器或同一页内存里塞下更多值，这直接转化为性能提升。然而，作为更小的数据类型，它的精度和范围也更有限。我们来仔细看看。顾名思义，Float16 只占 16 位即 2 字节，而单精度 Float 是 4 字节，双精度值是 8 字节。

它能表示的最小值约为 10 的负 8 次方，这一般不成问题。然而，Float16 能表示的最大值只比 65,000 略多一点。这对许多应用来说可能是个问题，在把原本为 Double 或 Float 编写的代码移植到 Float16 时，你应当小心这一点。

在硬件方面，Float16 已经得到良好支持。Apple GPU 使用它已有很长时间，Apple CPU 从 A11 Bionic 开始提供直接支持。在较老的 CPU 上，我们通过用 Float 模拟运算来支持 Float16。结果完全相同，只是稍微慢一点。

正如我之前提到的，在完全支持 Float16 的硬件上，同一个 SIMD 寄存器可以塞进两倍的值，这通常转化为性能翻倍。看看这在实践中的表现：我们来比较一个用单精度 Float 计算的 BNNS 卷积——大约 49 giga-flops——与一个用 Float16 计算的卷积——达到 119 giga-flops，性能超过两倍。

本次演讲讨论了 Swift Numerics 包，并展示了 Real 协议如何提供一种泛型编写浮点算法的方式，让它们适用于所有浮点类型。我还谈到了一个新的复数类型，它与 C 和 C++ 完全互操作。最后，我介绍了提升我们高性能数值支持的新 Float16 类型。想要参与的话，你可以访问 GitHub 上的 Swift Numerics 项目，看看现有的 issue 和 Pull Request 以了解正在进行的工作，并向社区贡献你自己的想法。

你也可以访问 forums.swift.org 的 Swift 论坛，在“Related Projects”分类中找到专门讨论 Swift Numerics 的内容。

感谢你与我一起了解 Swift Numerics，祝你享受这次大会！
