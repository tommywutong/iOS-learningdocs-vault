---
title: 面向 Swift 的 Accelerate 介绍
session_id: 718
collection: wwdc2019
year: 2019
duration: '20:59'
topics: [System Services, Swift]
group: I · 系统服务、进程与安全底层
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2019/718/'
content_hash: 'sha256:92065057c6da1a06'
translated: true
---

# 面向 Swift 的 Accelerate 介绍

<sub>WWDC2019 · 20:59 · System Services、Swift</sub>

Accelerate 框架提供数百个针对设备系统架构高度优化的计算函数……

> [!note] 归档理由
> Swift 版 Accelerate

## 相关资源

- [从噪声中提取信号](https://developer.apple.com/documentation/Accelerate/signal-extraction-from-noise)
- [Accelerate](https://developer.apple.com/documentation/Accelerate)
- [Accelerate Sparse](https://developer.apple.com/sample-code/wwdc/2017/AccelerateSparse.zip)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2019/718sn5zybluwhbuq/718/718_hd_introducing_accelerate_for_swift.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2019/718sn5zybluwhbuq/718/718_sd_introducing_accelerate_for_swift.mp4?dl=1)
- [演示文稿 (PDF)](https://devstreaming-cdn.apple.com/videos/wwdc/2019/718sn5zybluwhbuq/718/718_introducing_accelerate_for_swift.pdf?dl=1)
- [使用 Accelerate 提升性能并处理加密归档](https://developer.apple.com/videos/play/wwdc2021/10233)
- [使用 Accelerate 和 SIMD](https://developer.apple.com/videos/play/wwdc2018/701)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，我是 Simon Gladman，来自向量与数值计算组。在本次演示中，我会讲两个主题。第一，我们为 Accelerate 新推出的 Swift 覆盖层（Swift Overlay）。第二，使用 Linpack 基准测试来衡量 Accelerate 的性能。在深入 Swift 覆盖层之前，我们先回顾一下 Accelerate 框架到底是什么。Accelerate 的首要目的是提供数千个运行在 CPU 上的底层数学原语，支持图像和信号处理、向量运算、线性代数和机器学习。这些原语大多针对处理器的微架构手工调优。这意味着我们能获得出色的性能，而这些性能直接转化为能耗节省。所以，如果你是一名 App 开发者并且使用 Accelerate 框架，你的应用不仅会跑得更快，还会更省电。

我们在 Apple 的所有平台上都提供这些原语。这不仅包括 macOS 和 iOS，还包括 watchOS 和 tvOS。

这意味着你的用户会获得整体上更好的体验。

Accelerate 的库功能极其强大，但到目前为止，它们的接口对 Swift 开发者来说并不算友好。我们挑选了四个库，创建了新的 Swift 友好 API，让在 Swift 项目里使用 Accelerate 变得非常容易。我们关注的四个库是：vDSP，提供数字信号处理例程，包括大型向量上的算术运算、傅里叶变换、双二次滤波和强大的类型转换；vForce，提供算术和超越函数，包括三角函数和对数例程；Quadrature，专门用于函数的数值积分；还有 vImage，提供海量的图像处理函数，并能与 Core Graphics 和 Core Video 轻松集成。Accelerate 的性能优势来自向量化。要理解向量化，先来看一个用标量代码对数组元素做简单计算的例子。

举例来说，如果你编写的代码是把一个数组的每个元素与另一个数组的对应元素相乘，而你用的是 for 循环，那么每一对元素都会被单独加载、相乘，然后存储结果。

所以，在 A 和 B 的第一个元素相乘算出 C 的第一个元素之后，处理第二对，然后第三对，最后第四对。然而，如果你使用 Accelerate 处理数组的元素，你的计算是在单指令多数据（SIMD）寄存器上执行的。这些寄存器可以把多个数据项打包进单个寄存器，从而对多个数据项执行同一条指令。例如，一个 128 位寄存器实际上可以存储四个 32 位浮点值。因此，一次向量化的乘法操作可以同时相乘四对元素。

这意味着不仅任务更快，能耗效率也会显著提高。

我们刚看的乘法函数是 Accelerate 的数字信号处理库 vDSP 的一部分。那么，先来看看新的 Swift API 如何简化 vDSP 的使用。

vDSP 提供向量化的数字信号处理函数，包括傅里叶变换、双二次滤波、卷积和相关性。

此外，vDSP 还提供一些强大的更通用的函数，包括逐元素算术和类型转换。

所以，即使你眼下并不需要计算两个信号之间的相干性之类的东西，你也可能发现 vDSP 的通用计算例程能提供提升应用性能的方案。

来看一些基本算术。一个例子是：给定四个单精度值数组，你需要计算其中两个数组的逐元素和、另外两个数组的逐元素差，然后把这些结果相乘。用 for 循环解决这个问题完全合理，能算出预期结果。下面是用 vDSP 经典 API 执行该计算的方式。

使用 vDP 比用 for 循环大约快三倍。

这是用我们为 vDSP 新写的 Swift API 完成的同样计算。我们通过 vDSP 命名空间暴露新的 Swift 友好函数，你可以看到函数名和参数名本身就解释了操作。因为新函数处理的是熟悉的类型——包括数组和数组切片——而不是指针，你不再需要显式传入数量。整个函数调用因此更清晰、更简洁。

传入一个已初始化的结果数组能带来最佳性能，而且你显然可以在其他操作中复用该数组，获得进一步的性能收益。不过，我们也提供自分配版本的函数。它们利用了 Swift 访问数组未初始化缓冲区的新能力来返回计算结果。虽然比不上传入现有存储那么快，但仍比标量方式快，而且在某些情况下能简化你的代码。

vDSP 可以向量化的另一项常见任务是类型转换。这个例子把一个包含双精度值的数组转换为 16 位无符号整数，向零取整。

标量版本使用带显式取整的 map。同样，这是完全合理的技术，但 vDSP 可以向量化这个任务来提升性能。在这个例子里，vDSP 比之前的标量实现大约快四倍。

vDSP 函数的新 Swift 版本提供了清晰的接口。该函数接受一个源数组、你要把每个元素转换成的整数类型，以及一个指定取整方式的枚举。

vDSP 提供傅里叶变换，用于在一维和二维数据的时间域与频率域之间转换。对信号做正向傅里叶变换，会把它分解成组成它的正弦波，也就是频域表示。

反过来，对该频域表示做逆变换会重建原始信号，也就是时域表示。傅里叶变换在信号和图像处理中用途广泛。例如，对音频信号做正向变换之后，你可以轻松地减少或增加某些频率来均衡音频。

如果你熟悉经典 API，它还算容易读懂。你先创建一个 setup 对象，指定要变换的元素数量和方向；然后，在创建两个接收结果的数组之后，调用 execute 函数。完成后，你还得记得销毁 setup 以释放分配给它的资源。新 API 简化了 setup 对象的实例化，而变换本身成为 DFT 实例上一个带参数名的方法。而且你现在不必操心释放资源，我们替你做了。

与我们看过的 vDSP 函数非常相似，变换函数也有一个自分配版本，会为你创建并返回结果数组。

如果你处理音频数据，你可能熟悉双二次（biquad）滤波。双二次滤波器可用于均衡音频、塑造频率响应，例如让你去除低频或高频。

vDSP 的 biquad 功能作用于单通道和多通道信号，使用一组称为“节”（section）的独立滤波器对象。这些滤波器是级联的：它们按顺序排布，整个信号依次通过每个滤波器。

这些滤波器由一系列系数定义，代入这里展示的方程。在这个例子中，这些值构成一个低通滤波器，也就是衰减高频的滤波器。这是使用 vDSP 经典 API、用上一页幻灯片的系数创建 biquad setup 的代码。这是把该双二次滤波器应用于名为 signal 的数组、把结果返回到名为 output 的数组的代码。我们来看看用新 API 实现的相同功能。

如你所见，新 API 极大地简化了 biquad 结构的创建。你只需把系数传给 biquad 初始化方法，并指定通道数和节数。

把双二次滤波器应用到信号上只需一次函数调用。

现在来看我们为 Accelerate 的大型数组快速数学运算库 vForce 创建的新 API。

vForce 提供 vDSP 未包含的超越函数，包括指数、对数和三角运算。

vForce 的一个典型例子是计算大型数组中每个元素的平方根。这段代码的标量版本可以用 map。

vForce 提供计算平方根的向量化函数，某些情况下可比标量实现快达 10 倍。

新的 Swift 覆盖层提供了与新的 vDSP 函数一致的 API，并带来向量化的性能与能耗效率优势。与我们之前看到的类似，这里也有一个自分配版本，返回一个包含所给数组中每个元素平方根的数组。

接下来看看我们为 Quadrature 创建的新 API。Quadrature（求积）是“确定曲线下面积”的历史术语。它提供函数在有限或无限区间上定积分的近似。在这个例子里，我们将用 Quadrature 对所示的函数求积分，近似这里以绿色显示的半圆面积。

与 vDSP 的 Biquad 代码很像，使用现有的 Quadrature API 需要相当多的代码。第一步是定义一个结构体来描述要积分的函数。

第二步是定义积分选项，包括积分算法。最后，在定义好函数和选项之后，你就可以用 Quadrature 的 integrate 函数执行积分。

新 API 简化了代码。一大优势是：你可以把被积函数（integrand）——也就是要积分的函数——指定为一个普通闭包，而不是 C 函数指针。这意味着你可以轻松地向被积函数传值。

还要注意，积分器现在是带关联值的枚举。所以不需要在这里提供不必要的区间分点数或最大区间数。例如，你可以传入全局自适应积分器的枚举，指定区间分点数和最大区间数。

现在来看看我们为 Accelerate 的图像处理库 vImage 创建的新 API。

vImage 是一个包含丰富图像处理工具集合的库。它设计为与 Core Graphics 和 Core Video 无缝协作。它包括诸如 alpha 混合、格式转换、直方图操作、卷积、几何和形态学等操作。

我们的新 Swift API 引入了许多新特性，让在 Swift 中使用 vImage 更容易、更简洁。我们把标志实现为 option set。vImage 会抛出 Swift 错误。我们还隐藏了一些与可变性和处理非托管类型相关的要求。

如果你在处理 Core Graphics 图像，把图像数据放进 vImage 缓冲有一个常见工作流程。

首先，你需要创建 CG 图像格式的描述。

然后实例化一个 vImage 缓冲。从图像初始化该缓冲。最后，以非 Swift 的方式检查错误。对于一个常见操作来说，这实在是太多的样板代码。

新 API 把所有这些代码包进了一个单独的可抛出初始化方法。

不过，因为我们稍后还要使用 CG 图像的格式，这里用新 API 分两步实现类似功能。我们为 CGImageFormat 添加了一个接受 CG 图像的新初始化方法，以及一个接受 CG 图像和显式格式描述的备用缓冲初始化方法。缓冲用完之后，这是经典的 vImage 函数，用于从缓冲内容创建 CG 图像。

我们的新 API 同样简化了这个操作，提供了一个新的 create CGImage 方法，它使用我们刚从图像生成的格式。

vImage 的一个重要用例是在不同域和不同格式之间转换。vImage 的任意转换器（any-to-any converter）可以在 Core Video 与 Core Graphics 之间转换，也可以在不同的 Core Graphics 格式之间转换。

例如，你可能想把一幅 CMYK 的 Core Graphics 图像转换为 RGB。

创建转换器的现有 API 接受转换的源格式和目标格式，返回一个非托管（unmanaged）转换器。

你取该转换器的托管引用，把它传给执行转换的函数。

我们的新 API 在现有转换器类型上添加了一个新的静态 make 函数，返回一个转换器实例。转换通过转换器实例上的 convert 方法完成。

最后看看 Core Video 图像格式的处理。在一个典型的例子中，你可能想从 Core Video 像素缓冲创建图像格式描述，并计算它的通道数。

这是经典 vImage API 从像素缓冲创建图像格式描述并获取其通道数所需的代码。新 API 用两行代码提供同样的功能。你用一个新的静态 make 函数从像素缓冲创建 Core Video 图像格式实例，然后直接以属性形式访问它的通道数。

以上只是新 API 中一小部分的快速浏览。现在我们来看 Linpack 基准测试，看看 Accelerate 到底能快多少、省多少电。

Linpack 基准测试源自 Linpack 库，后者起初是一组提供快速计算线性代数的例程。它后来被一个叫 LAPACK 的库吸收，LAPACK 代表“线性代数包”。LAPACK 的开发利用了当时被称为缓存的新事物。LAPACK 由许多分块算法组成。这些算法构建在另一个叫 BLAS 的库之上，BLAS 代表“基本线性代数子程序”。我们会在本演示的稍后部分更多地谈到 BLAS。现在请记住：Linpack 基准测试运行在 LAPACK 之上，而 LAPACK 运行在 BLAS 之上。

Linpack 基准测试衡量一个平台求解一般线性方程组的速度。它由两步组成：先是矩阵分解步骤，然后是回代（back substitution）步骤。通过固定算法，我们能看到不同平台运行该算法的表现。这为我们提供了一种比较不同平台的方法。Linpack 基准测试随时间演化。最初它求解 100 x 100 的方程组，后来是 1000 x 1000。如今最常用的变体是不设限制（no holds barred）的变体，问题规模可以任意大。这就是我们今天要运行的变体。我们现在要比较 iPhone XS 上的 Linpack 性能。顶部橙色的是未优化的 Linpack。这个 Linpack 基准测试不使用 Accelerate 框架，它依赖的软件没有针对其运行所在的处理器进行调优。让我们看看它的表现。现在我们要与使用 Accelerate 框架的版本做比较：也就是说，我们在同一平台上运行同一个基准测试，但使用针对该平台调优过的 Accelerate 框架。

可以看到，使用 Accelerate 框架后，我们快了 24 倍以上。这不仅节省时间，也节省能量，从而延长电池续航。现在我们换个话题，看看 Linpack 基准测试的主力例程，叫做 GEMM。

正如我之前提到的，运行在 LAPACK 之上的 Linpack 构建在 BLAS 之上。BLAS 内部有一个叫 GEMM 的例程，代表“通用矩阵乘法”。这个例程被用来实现 BLAS 中的其他若干分块例程，而后者又用于 LAPACK 的分块算法中，最著名的是矩阵分解和求解例程。

因此，GEMM 有时被用作性能的代名词。在本演示中，我们专门看 GEMM 的单精度变体。

这里我们将比较 Eigen 库与 Accelerate 的性能。Eigen 库和 Accelerate 框架都运行在一台 iPhone XS 上，都在执行单精度矩阵乘法。看看 Eigen 的表现。Eigen 的峰值大约是 51 gigaflops。再看看 Accelerate 的表现。可以看到，在同一平台上，Accelerate 框架比 Eigen 快接近两倍半。

这是因为 Accelerate 框架针对平台手工调优，让我们能充分发挥平台的能力。所以，如果你是开发者，在你的 App 中使用 Accelerate 会带来更好的性能。这些性能转化为更少的能耗，意味着更长的电池续航和用户整体上更好的体验。

总结一下：Accelerate 提供执行大规模数学计算和图像计算的函数，快速且节能。而现在我们添加了 Swift 友好的 API，让 Accelerate 的库非常容易上手，你的用户将从中受益于这种性能与能效。

请访问我们的网站，那里有覆盖整个 Accelerate 框架的示例、文章和大量的参考材料。非常感谢。
