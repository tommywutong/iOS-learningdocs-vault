---
title: 安全地混用 C、C++ 与 Swift
session_id: 311
collection: wwdc2025
year: 2025
duration: '32:11'
topics: [Swift]
group: A · ObjC/Swift runtime 与语言实现
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2025/311/'
content_hash: 'sha256:c48db88371eb3dad'
translated: true
---

# 安全地混用 C、C++ 与 Swift

<sub>WWDC2025 · 32:11 · Swift</sub>

学习如何混用 C、C++ 与 Swift，同时提升你的 App 的安全性。我们将向你展示如何找出 Swift 中不安全的 C 和 C++ API 调用位置……

> [!note] 归档理由
> C/C++/Swift 混编的 ABI 与内存安全边界

## 章节

- [引言](/videos/play/wwdc2025/311/?time=0)
- [在 Swift 中查找不安全调用](/videos/play/wwdc2025/311/?time=159)
- [安全地调用 C/C++](/videos/play/wwdc2025/311/?time=295)
- [接收指针的函数](/videos/play/wwdc2025/311/?time=445)
- [返回指针的函数](/videos/play/wwdc2025/311/?time=1033)
- [导入自定义类型](/videos/play/wwdc2025/311/?time=1216)
- [提升 C/C++ 的安全性](/videos/play/wwdc2025/311/?time=1617)
- [总结](/videos/play/wwdc2025/311/?time=1848)

## 相关资源

- [引言](https://developer.apple.com/videos/play/wwdc2025/311/?time=0)
- [在 Swift 中查找不安全调用](https://developer.apple.com/videos/play/wwdc2025/311/?time=159)
- [安全地调用 C/C++](https://developer.apple.com/videos/play/wwdc2025/311/?time=295)
- [接收指针的函数](https://developer.apple.com/videos/play/wwdc2025/311/?time=445)
- [返回指针的函数](https://developer.apple.com/videos/play/wwdc2025/311/?time=1033)
- [导入自定义类型](https://developer.apple.com/videos/play/wwdc2025/311/?time=1216)
- [提升 C/C++ 的安全性](https://developer.apple.com/videos/play/wwdc2025/311/?time=1617)
- [总结](https://developer.apple.com/videos/play/wwdc2025/311/?time=1848)
- [安全地混用 Swift 与 C++](https://www.swift.org/documentation/cxx-interop/safe-interop/)
- [-fbounds-safety：为 C 强制执行边界安全](https://clang.llvm.org/docs/BoundsSafety.html)
- [HD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2025/311/4/10e5709a-8f4f-488a-92f6-f551b4ce97c5/downloads/wwdc2025-311_hd.mp4?dl=1)
- [SD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2025/311/4/10e5709a-8f4f-488a-92f6-f551b4ce97c5/downloads/wwdc2025-311_sd.mp4?dl=1)
- [使用 Swift 改善内存使用与性能](https://developer.apple.com/videos/play/wwdc2025/312)
- [不安全性可能很微妙](https://developer.apple.com/videos/play/wwdc2025/311/?time=199)
- [严格内存安全](https://developer.apple.com/videos/play/wwdc2025/311/?time=241)
- [原始指针无法防止越界错误](https://developer.apple.com/videos/play/wwdc2025/311/?time=480)
- [原始指针无法防止越界错误](https://developer.apple.com/videos/play/wwdc2025/311/?time=501)
- [原始指针无法防止越界错误](https://developer.apple.com/videos/play/wwdc2025/311/?time=510)
- [越界错误的解决方案](https://developer.apple.com/videos/play/wwdc2025/311/?time=528)
- [越界错误的解决方案](https://developer.apple.com/videos/play/wwdc2025/311/?time=534)
- [使用 __counted_by 表达边界信息](https://developer.apple.com/videos/play/wwdc2025/311/?time=598)
- [接收 C++ span 的不安全函数声明](https://developer.apple.com/videos/play/wwdc2025/311/?time=730)
- [缓存 C++ span 的不安全 C++ 函数](https://developer.apple.com/videos/play/wwdc2025/311/?time=801)
- [Swift Span 防止逃逸出作用域](https://developer.apple.com/videos/play/wwdc2025/311/?time=848)
- [使用 __noescape 表达生命周期信息](https://developer.apple.com/videos/play/wwdc2025/311/?time=918)
- [安全地将 C++ Span 用作 Swift Span](https://developer.apple.com/videos/play/wwdc2025/311/?time=956)
- [返回的 C++ Span 是不安全的](https://developer.apple.com/videos/play/wwdc2025/311/?time=1041)
- [Swift Span 通过设计防止 use-after-free](https://developer.apple.com/videos/play/wwdc2025/311/?time=1086)
- [使用 __lifetimebound 表达生命周期依赖](https://developer.apple.com/videos/play/wwdc2025/311/?time=1127)
- [安全地返回 C++ Span 作为 Swift Span](https://developer.apple.com/videos/play/wwdc2025/311/?time=1130)
- [将 C++ 视图类型导入为 SWIFT_NONESCAPABLE](https://developer.apple.com/videos/play/wwdc2025/311/?time=1349)
- [导入 C++ 引用计数类型](https://developer.apple.com/videos/play/wwdc2025/311/?time=1411)
- [安全地返回引用计数类型](https://developer.apple.com/videos/play/wwdc2025/311/?time=1437)
- [C++ 标准库强化](https://developer.apple.com/videos/play/wwdc2025/311/?time=1671)
- [C++ 不安全缓冲区使用错误](https://developer.apple.com/videos/play/wwdc2025/311/?time=1739)
- [C 的边界安全扩展](https://developer.apple.com/videos/play/wwdc2025/311/?time=1811)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，我叫 Yeoul，是 Apple 安全语言扩展团队的经理。在创建 App 时，优先考虑安全性至关重要。这意味着要保护用户私密信息免受潜在攻击者的侵害。这些不法分子常常利用用 C 和 C++ 编写的代码中的漏洞，因为这两种语言本身是不安全的。好消息是，如果你的 App 已经使用 Swift，这门语言默认就是安全的。这真是个好消息。

但即使你所有新代码都用 Swift 编写，App 的旧部分可能仍包含一些 C 和 C++ 代码。或者，它可能依赖外部库。当混用这些语言时，重要的是确保 Swift 的安全保证不会被破坏。从高层次来看，问题在于接受或返回原始指针的 C 和 C++ 函数很难被安全地调用。调用不当可能会导致安全与稳定性 bug，例如缓冲区溢出和 use-after-free。

因此，来自 C 和 C++ 的指针在 Swift 中被导入为不安全类型。例如，一个 C 整数指针会被导入为 `UnsafeMutablePointer`。Swift 故意在类型名中加入 "unsafe"，好让我知道调用该函数时不能依赖其正常的安全保证。然而，我知道有些函数是可以从 Swift 安全调用的。但直到现在，C 和 C++ 都没有方式来传达应如何安全地调用它们。而这正是本次演讲的主题。首先，我将描述一项名为严格内存安全（strict memory safety）的新功能，它有助于识别 Swift 中的不安全调用；其次，我将介绍如何注解 C 和 C++ 函数，以传达缺失的信息，从而使 Swift 能安全地调用它们；然后，我将解释如何注解自定义 C++ 类型以实现安全导入；最后，虽然永远不可能让基于 C 的语言像 Swift 一样安全，但我会介绍一些让 C 和 C++ 代码更安全一点的工具。Swift 6.2 提供了一项酷炫的新功能，帮助捕获对不安全 C 和 C++ 函数的调用。我将在一个我编写的 App 上演示，该 App 允许用户分享可爱的宠物资料照片。这个 App 能访问用户极其敏感的私密信息，比如狗狗的中间名，因此我想让它保持安全。它用 Swift 编写。不过，它也会调用 C 和 C++ 代码来应用自定义图像滤镜。我想找出 App 中所有对 C 和 C++ 的不安全调用，以便把它们变得安全。棘手的是，有时找出这些调用并不容易。Swift 默认是安全的，但它允许使用不安全构造，尤其在与 C 和 C++ 互操作时。例如，在幕后，`imageData` 会创建一个 `UnsafeMutablePointer`，从名字就能看出它是不安全的。但在阅读代码时并不容易注意到。现在我可以使用 Swift 6.2 中名为严格内存安全的新编译器模式，来发现所有对不安全函数的调用。开启严格内存安全后，编译器会警告所有不安全代码，并附带解释原因的注释。

严格内存安全默认未开启，但因为我的 App 对安全敏感，我一定会开启它。我们来看看 Xcode 中的表现。

我将在项目的构建设置中把严格内存安全设为 yes 以选择启用。

重新构建后，编译器会提供警告，帮助我发现不安全构造。

现在我看到一些新警告。大部分不安全代码都涉及 C 和 C++ 指针。

我将向你展示如何从 Swift 安全地调用使用这些指针的函数。

但首先，我们来谈谈为什么 C 和 C++ 指针如此难以安全使用。

指针是强大且有用的工具。它们让我能高效地查看内存而无需复制。但要安全使用它们非常困难。问题的根源在于 C 和 C++ 不会帮助程序员避免犯错。例如，没有任何东西阻止我意外地在内存被释放后使用它，或访问超出缓冲区边界的内存。这里有个好消息：Swift 6.2 引入了一种新的安全指针类型 `Span`，它提供指针的好处，同时自动防止这类错误。`Span` 的行为类似指针，但内置了安全性。Swift 确保你不能用它做不安全的事。如果需要修改内存，还有 `MutableSpan`。要了解更多关于 `Span` 的信息，请查看 "Improve memory usage and performance with Swift"。如果 Swift 能把 C 和 C++ 指针导入为 `Span` 而不是不安全指针，那就太好了。不幸的是，编译器缺少两块关键信息，无法安全地做到这一点。没有 C++ 提供的指针边界信息，Swift 无法防止越界访问；没有 C++ 提供的指针生命周期信息，Swift 无法防止内存被释放后继续使用。关键思想是：如果程序员提供这些缺失信息，Swift 就能把不安全指针当作 Swift `Span` 处理。

在 Swift 6.2 中，我可以给 C 和 C++ 代码添加注解，把缺失信息提供给编译器。这不会改变代码的工作方式，只是让它的假设显式化。这使得 Swift 能安全地调用使用指针的 C 和 C++ 代码。我们来谈谈如何注解接收和返回指针的函数。为此，我们回到我的 App。

第一个警告是在 `invertImage` 函数的使用上，它接收一个原始指针。我将向你展示如何安全地调用这类接收指针参数的函数。

如我所提，原始指针缺少边界信息，因此无法验证访问是否在边界内。如果不小心使用，它们可能造成越界内存错误。这里有个例子。`InvertImage` 从 Swift 调用。该函数接收一个 image 指针，即指向图像的原始指针，而大小是单独的参数。

但由于 image 指针只是原始指针，没有什么能阻止我意外传入过大的 size。如果我这么做了，函数就会读写超出缓冲区边界。这正是 `Span` 解决的问题之一。想象一下，如果 `invertImage` 被导入为接收 `Span` 的 Swift 函数。那么我可以直接传入 `Span`，而不是分别传入原始指针和大小。这会自动保护我免于传错大小之类的错误，因为 `Span` 总是携带其指向内存的正确边界信息。然后，在幕后，编译器会负责解包 `Span`，提取正确的指针和大小，并把它们传给 C 函数。这样就不会有犯错的空间。

编译器能做这件事，但它缺少原始指针与大小之间的联系。`invertImage` 函数假设指针指向一个包含 imageSize 个元素的缓冲区，但这只是一个隐含假设。我需要显式表达这种关系，以便人类和编译器都理解。这可以用 `counted_by` 注解表达。该注解告诉编译器指针所指向内存中的元素数量。然后指针还需要另一个名为 `noescape` 的注解来提供缺失的生命周期信息。但你可以暂时忽略它，我稍后会讲到。一旦提供这些额外信息，我就可以通过直接传入 `Span` 从 Swift 安全地调用该函数。然后编译器会自动处理其余部分。这样错误就不可能发生。我将回到我的 `invertImage` 函数。

我将在 `invertImage` 函数上添加 `counted_by` 和 `noescape` 注解。

我将跳到声明处并添加相同的注解。

然后我将跳回 Swift 的调用点。

我现在将直接传入 imageData 的 `Span` 来从 Swift 调用该函数。

现在没有不安全指针参与，所以警告消失了。

下一个警告是在 `applyGrayScale` 函数的使用上。它说该函数使用了不安全的 C++ 类型。

我们来看看该函数的 C++ 定义。顾名思义，`applyGrayScale` 是对输入图像应用灰度效果的函数。该函数接收图像的视图，可以看到其类型是 C++ `Span`。到目前为止，我们谈的是 Swift 的 `Span`。但 C++ 也有 `Span` 的概念。我们看到警告，是因为 Swift 认为 C++ `Span` 是不安全的，尽管它们试图解决同一个问题。与 Swift `Span` 类似，C++ `Span` 是用于访问他人拥有的连续内存的标准类型。它包含指向该内存的指针及其大小。因为 C++ `Span` 知道自己的大小，它可以像 Swift `Span` 一样安全地检查越界访问。然而，与 Swift `Span` 不同，C++ `Span` 没有生命周期信息，因此不能防止访问已分配的内存。所以使用 C++ `Span` 可能导致 use-after-free bug。

这里有个例子。想象一下，`ApplyGrayScale` 接收一个名为 `ImageView` 的 C++ `Span`，它指向由 Swift 创建的数组。

在 `applyGrayscale` 内部，我可能会存储这个指针，比如放在像 `cachedView` 这样的全局变量中，以便其他 C++ 代码稍后使用。但问题在于：一旦函数返回，Swift 可能会释放数组，认为没有其他代码在使用它。现在 C++ 代码持有一个不再指向有效内存的指针。这是悬空指针，访问它就是经典的 use-after-free bug。

另一方面，Swift `Span` 是安全的。它不允许超出其指向内存的生命周期。如果函数接收 Swift `Span`，它只能在函数内使用它。它不允许保留它，比如保存到 `cachedView` 供稍后使用。这种指针在函数结束后仍被保留的行为称为逃逸（escaping）。每当 `Span` 试图逃逸其作用域时，编译器就会报告类似这样的错误。

这样，悬空指针在 Swift `Span` 中根本不可能出现，use-after-free bug 也从设计上被避免。C++ `Span` 不提供同等保证。要安全使用它，我需要手动审计函数，确保它不会保留 `imageView` 参数以避免悬空指针。一旦验证参数不会逃逸 C++ 函数，我需要在函数定义中记录这一信息。这将让人类和编译器都理解函数行为。添加 `noescape` 注解有助于做到这一点。`noescape` 注解也可以应用于原始指针和引用。

从 Swift 6.2 开始，带 `noescape` 注解的 C++ `Span` 参数可以被视为 Swift `Span`。这意味着我现在可以直接把 Swift `Span` 传给 `applyGrayscale`，非常方便，也消除了不安全样板代码。能让 C++ 函数调用如此安全、如此简单，真是太棒了。

我将跳到 `applyGrayscale` 的定义处，在参数 `imageView` 上添加 `noescape`，并在声明处也添加。

现在我将跳回 Swift 的调用点。

现在我可以移除对不安全可变缓冲区指针的临时访问，直接传入从 imageData 获取的 Swift `Span`。

现在警告消失了，因为我安全地调用了 `applyGrayscale`。

下一个警告是在 `scanImageRow` 的使用上，它接收一个 C++ `Span` 并返回另一个 C++ `Span`。

那么，如何安全地调用返回指针（如 C++ `Span`）的函数呢？返回 C++ `Span` 可能很危险，因为它不跟踪其指向的内存是否仍然有效。这里有个例子。`ScanImageRow` 接收 `imageView` 作为 C++ `Span`，并返回另一个指向 imageData 中选定行的 C++ `Span`。一旦函数返回，数据就会被释放。但返回的 C++ `Span` 仍指向那块内存，这是悬空指针。访问它将是 use-after-free。如果返回值能像 Swift `Span` 而不是 C++ `Span` 那样处理，这个 bug 就不可能发生。那是因为编译器只有在知道返回的内存仍然有效、使用它是安全的时，才会允许你返回 Swift `Span`。那么返回的 `Span` 什么时候实际上可以安全使用呢？它指向与 `imageView` 参数相同的内存的一部分。这意味着它只在 `imageView` 存活时才有效。这种关系称为生命周期依赖（lifetimebound）。

这正是 Swift 需要的信息，以便把返回的 C++ `Span` 导入为 Swift `Span`。我可以用 `lifetimebound` 注解来表达。这使编译器能够确保它被安全使用。

我将跳到 `scanImageRow` 的定义处。

我将在 `scanImageRow` 函数的 `imageView` 参数上添加 `lifetimebound` 注解。

我也会在声明处做同样的事。

有了 `lifetimebound` 注解，该函数现在可以接收 Swift `Span` 并返回另一个 Swift `Span`。我将移动到 Swift 的调用点。

这里，我现在可以移除不安全指针访问，直接传入 Swift `Span`。

该函数现在返回 Swift `Span` 而不是不安全指针。重新构建后，警告就会消失。

现在我已经解决了调用 C 和 C++ 代码中的不安全性，所有警告都消失了。到目前为止，我谈到了如何把 C 和 C++ 指针当作 Swift `Span`。但 C++ 中还有一些其他惯用类型，可以通过注解直接安全地导入到 Swift 中使用。这些是自定义视图类型和引用计数类型。首先，我们看看如何安全地导入自定义 C++ 视图类型。视图类型是包含指向其不拥有的内存的指针或引用的结构体。Swift `Span` 也是视图类型。

因此，让我们更仔细地看看是什么真正让 Swift `Span` 安全。在幕后，`Span` 被标记为一种特殊的 Swift 类型：非逃逸（nonescapable）。非逃逸类型常用于实现提供对另一种类型内存的视图而不复制它的类型。就像 `Span` 一样，Swift 确保所有非逃逸类型都不会逃逸其当前上下文。这确保它们不会超出其指向内存的生命周期，因此受到 use-after-free bug 的保护。C++ 视图类型可以作为非逃逸类型安全地导入到 Swift。我只需添加一个注解。这里有个例子。我的 App 有一个自定义 C++ 结构体 `ImageView`，它存储图像的宽度、高度，以及指向图像像素数据的指针。`ImageView` 不拥有那些像素数据。它属于另一个对象，该对象负责在不再需要时释放内存。这意味着 `ImageView` 逃逸是不安全的。如果它逃逸了，视图就可能在底层内存被释放后使用它。

因此，我想确保该类型永远不逃逸。为此，我可以添加 `SWIFT_NONESCAPABLE` 注解。这样编译器就会把 C++ 类型导入为非逃逸类型。一个好的经验法则是：如果你有一个结构体包含指向其不拥有的内存的视图或指针，就应该使用这个注解。

不仅是视图类型，C++ 和许多其他语言中还有一种常见惯用法：类型拥有它所引用的内存，并通过引用计数跟踪引用。Swift 提供了一项功能，可通过注解安全地导入这些类型。例如，我的 C++ `image buffer` 结构体拥有其底层的 `imageData`。当结构体被释放时，`imageData` 也随之释放。我希望 `image buffer` 被导入为引用计数类型到 Swift，以便编译器自动管理其生命周期。为此，我将使用 `SWIFT_SHARED_REFERENCE` 注解告诉编译器 Swift 应调用哪些函数来增加和减少引用计数。现在 Swift 把 `image buffer` 视作引用计数类型。但编译器还需要从我这里获得更多信息，才能安全地返回 `image buffer`。

当 C++ 函数返回 `image buffer` 时，可能有两种情况。第一，如果函数返回一个新创建的图像，调用方有责任在使用完毕后释放图像。这种情况下，我将方法注解为 `SWIFT_RETURNS_RETAINED`。这告诉 Swift 编译器在调用方不再使用时释放图像。第二，如果函数返回对已存在图像的引用，调用方如果想保留它，就有责任 retain 该图像。这种情况下，我将方法注解为 `SWIFT_RETURNS_UNRETAINED`。这告诉 Swift 编译器，如果想保留图像，它应该 retain 它。添加这些注解使所有权预期显式化，因此 Swift 能安全地管理内存。

通过注解提供缺失信息，使 Swift 能安全地使用 C 和 C++ 函数与类型。这些注解不会改变代码的工作方式，只是让代码中的假设显式化。

我们来回顾一下我们涵盖的注解以及如何使用它们。

如果函数参数或返回值是指针或数组类型，并且它指向包含多个元素的内存，使用 `counted_by` 注解来指明元素数量。如果参数引用他人拥有的内存且参数不会逃逸函数，使用 `noescape`。如果函数返回值引用的内存其生命周期依赖于某个参数的生命周期，添加 `lifetimebound` 注解。通过添加这些信息，你就能让 Swift 把指针导入为安全的 Swift `Span` 类型，调用点无需 ceremonies 即可使用。

你还可以添加注解来帮助 Swift 安全地管理你的自定义 C++ 类型。如果你的 C++ 类型存储了指向其不拥有的内存的视图、指针或引用，使用 `SWIFT_NONESCAPABLE`。这告诉编译器把你的类型导入为非逃逸类型。如果你的类型是引用计数的，你应该使用 `SWIFT_SHARED_REFERENCE`。然后编译器会自动管理其内存。

是的，内容很多。如果你想现在暂停视频去吃点零食或喝口水，现在是个好时机。只要你答应我你会回来，因为接下来我将展示一些让 C 和 C++ 代码安全得多的、真正令人兴奋的新工具。

好的，我将转换话题，讲讲 C 和 C++ 代码实际上如何变得更安全。在我的 App 中，我添加了注解，以确保 Swift 能安全地调用 C 和 C++。然而，纯 C 和 C++ 代码仍然不安全。我离安全 bug 只差一步之遥。理想情况下，我会把那段代码用 Swift 重写以获得完全的安全。但有时这不切实际。永远不可能让 C 和 C++ 像 Swift 一样安全，但这里有一些为 C 和 C++ 提供部分安全的工具。首先，我将谈谈我们开发的一个增强 C++ 边界安全的工具。

有些人可能想知道，既然 `Span` 已经存储了边界信息，为什么 C++ 还不是边界安全的。然而，问题在于，默认情况下 C++ 中对 `Span` 的数组下标并不是边界检查的。其他标准容器如 vector 也是如此。Xcode 有一个名为 C++ 标准库强化（C++ Standard Library Hardening）的功能。它确保标准 C++ 视图和容器上的数组下标进行边界检查。它还会向标准库添加其他一些安全检查。

即使启用 C++ 标准库强化，仍有另一个问题。你仍可使用原始指针，它们因为没有边界信息而无法进行边界检查。因此使用 C++ 的最佳方式是避免原始指针，使用标准类型如 C++ `Span`。为此，Xcode 让你可以开启对 C++ 中使用不安全指针时的错误。这样你就能检查代码，并按需把原始指针替换为 C++ `Span` 或标准容器。

只是提醒一下，这些错误是关于边界安全的，不是生命周期安全的。

要让你的 C++ 项目边界安全，可以在项目构建设置中把 enforce bounds safe buffer usage in C++ 设为 yes。这将同时启用 C++ 标准库强化和不安全缓冲区使用错误。

那 C 呢？与 C++ 不同，C 没有像 `Span` 这样的标准类型来让指针携带边界信息。因此，针对 C，我们开发了一种新的语言扩展，保证边界安全。现在可以在 Xcode 中使用它。启用这个语言扩展后，编译器会告诉你在整个 C 代码中哪里缺少边界信息。然后你可以添加边界注解来表达缺失信息。在这个例子中，你可以对 buffer 添加 `counted_by` 注解，与前面用于 Swift 和 C 互操作的安全性相同的注解。然后编译器会在运行时插入边界检查，在越界内存访问时安全地 trap。

我可以在 Xcode 项目设置中为所有 C 文件启用边界安全扩展。要了解更多信息，请查看 llvm.org 网站上的边界安全文档。

在本次演讲中，我描述了如何确保 Swift 的安全性，以及如何安全地调用 C 和 C++ 代码。永远不可能让 C 和 C++ 像 Swift 一样安全，但它们可以变得更安全。

这里有一些混用 C、C++ 与 Swift 时获得最佳安全性的建议。

开启 Swift 的严格内存安全。这会在你使用不安全构造时提醒你，并帮助你找出 C 和 C++ API 的任何不安全使用。确保 Swift 能安全地与不安全的 C 和 C++ API 交互，方法是给它们添加注解。

让 C 和 C++ 默认更安全。你可以通过为 C 和 C++ 开启新的边界安全功能来做到这一点。

我们正与开源社区协作，让 C、C++ 与 Swift 无缝且安全地协同工作。因此你的反馈和参与对我们非常重要。请试用并告诉我们你的想法。感谢观看。
