---
title: 使用 Swift 改善内存使用与性能
session_id: 312
collection: wwdc2025
year: 2025
duration: '31:31'
topics: [Swift]
group: A · ObjC/Swift runtime 与语言实现
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2025/312/'
content_hash: 'sha256:41c4eb2ef205523b'
translated: true
---

# 使用 Swift 改善内存使用与性能

<sub>WWDC2025 · 31:31 · Swift</sub>

探索提升 Swift 代码性能与内存管理的方法。我们将探讨从优化代码开始的多种途径——包括……

> [!note] 归档理由
> InlineArray/Span、去分配与去引用计数，语言级性能新范式

## 章节

- [引言与议程](/videos/play/wwdc2025/312/?time=0)
- [QOI 格式与解析器 App](/videos/play/wwdc2025/312/?time=79)
- [算法](/videos/play/wwdc2025/312/?time=145)
- [分配](/videos/play/wwdc2025/312/?time=497)
- [独占访问](/videos/play/wwdc2025/312/?time=990)
- [栈与堆](/videos/play/wwdc2025/312/?time=1152)
- [引用计数](/videos/play/wwdc2025/312/?time=1268)
- [Swift 二进制解析库](/videos/play/wwdc2025/312/?time=1792)
- [后续步骤](/videos/play/wwdc2025/312/?time=1863)

## 相关资源

- [引言与议程](https://developer.apple.com/videos/play/wwdc2025/312/?time=0)
- [QOI 格式与解析器 App](https://developer.apple.com/videos/play/wwdc2025/312/?time=79)
- [算法](https://developer.apple.com/videos/play/wwdc2025/312/?time=145)
- [分配](https://developer.apple.com/videos/play/wwdc2025/312/?time=497)
- [独占访问](https://developer.apple.com/videos/play/wwdc2025/312/?time=990)
- [栈与堆](https://developer.apple.com/videos/play/wwdc2025/312/?time=1152)
- [引用计数](https://developer.apple.com/videos/play/wwdc2025/312/?time=1268)
- [Swift 二进制解析库](https://developer.apple.com/videos/play/wwdc2025/312/?time=1792)
- [后续步骤](https://developer.apple.com/videos/play/wwdc2025/312/?time=1863)
- [Swift Binary Parsing](https://github.com/apple/swift-binary-parsing)
- [性能与指标](https://developer.apple.com/documentation/Xcode/performance-and-metrics)
- [Swift 官方网站](https://www.swift.org)
- [The Swift Programming Language](https://docs.swift.org/swift-book/)
- [HD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2025/312/4/ae42066d-6af2-4371-bf68-81a81ddef963/downloads/wwdc2025-312_hd.mp4?dl=1)
- [SD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2025/312/4/ae42066d-6af2-4371-bf68-81a81ddef963/downloads/wwdc2025-312_sd.mp4?dl=1)
- [使用 Instruments 优化 CPU 性能](https://developer.apple.com/videos/play/wwdc2025/308)
- [分析与优化 App 中的电源使用](https://developer.apple.com/videos/play/wwdc2025/226)
- [Swift 新变化](https://developer.apple.com/videos/play/wwdc2025/245)
- [探索 Swift 性能](https://developer.apple.com/videos/play/wwdc2024/10217)
- [修正后的 Data.readByte() 方法](https://developer.apple.com/videos/play/wwdc2025/312/?time=421)
- [RGBAPixel.data(channels:) 方法](https://developer.apple.com/videos/play/wwdc2025/312/?time=596)
- [原始的 QOIParser.parseQOI(from:) 方法](https://developer.apple.com/videos/play/wwdc2025/312/?time=621)
- [修改后的 QOIParser.parseQOI(from:) 方法](https://developer.apple.com/videos/play/wwdc2025/312/?time=773)
- [Array 行为](https://developer.apple.com/videos/play/wwdc2025/312/?time=907)
- [InlineArray 行为（第 1 部分）](https://developer.apple.com/videos/play/wwdc2025/312/?time=1187)
- [InlineArray 行为（第 2 部分）](https://developer.apple.com/videos/play/wwdc2025/312/?time=1223)
- [processUsingBuffer() 函数](https://developer.apple.com/videos/play/wwdc2025/312/?time=1393)
- [危险的 getPointerToBytes() 函数](https://developer.apple.com/videos/play/wwdc2025/312/?time=1414)
- [processUsingSpan() 函数](https://developer.apple.com/videos/play/wwdc2025/312/?time=1486)
- [getHiddenSpanOfBytes() 函数（尝试 1）](https://developer.apple.com/videos/play/wwdc2025/312/?time=1507)
- [getHiddenSpanOfBytes() 函数（尝试 2）](https://developer.apple.com/videos/play/wwdc2025/312/?time=1528)
- [RawSpan.readByte() 方法](https://developer.apple.com/videos/play/wwdc2025/312/?time=1587)
- [最终的 QOIParser.parseQOI(from:) 方法](https://developer.apple.com/videos/play/wwdc2025/312/?time=1682)
- [RGBAPixel.write(to:channels:) 方法](https://developer.apple.com/videos/play/wwdc2025/312/?time=1711)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好！我是 Nate Cook，在 Swift 标准库团队工作。今天我们要探讨如何理解并改进代码的性能，其中一部分将借助 Swift 6.2 语言和标准库中的一些新增功能。我们将使用新的 InlineArray 和 Span 类型，体验值泛型（value generics），并了解非逃逸类型（non-escapable types）。我们将利用这些新工具来消除 retain 和 release 操作、独占访问检查（exclusivity checks）和唯一性检查（uniqueness checks），以及其他额外工作。我还将首次展示一个使用了所有这些工具的开源新库，用于快速安全地编写二进制解析器。它叫做 Swift Binary Parsing。该库专注于速度，并提供了管理多种不同安全性问题的工具。我们都希望代码运行迅速，Swift 也给出了实现这一目标的工具。但有时，事情并不像我们预期的那样快。在本节中，我们将练习找出代码的时间消耗点，然后尝试几种性能优化方法……选择正确的算法。消除多余分配。消除独占访问检查。将堆分配转移到栈分配。以及减少引用计数。在探索过程中，我们将看看我构建的一个小 App。它是一个名为 QOI 的图像格式查看器，包含一个手写的格式解析器。QOI 是一种无损图像格式，其规范简单到只有一页，非常适合用来尝试不同的方法并观察它们的性能。QOI 格式使用了二进制格式的标准惯用方法，包含一个固定大小的头部，后跟一个数据部分，数据部分包含动态数量的、大小各异的编码像素。编码像素有几种形式。一个像素可以是 RGB 或 RGBA 值、与前一个像素的差值、对先前见过像素的缓存查找，或者……只是前一个像素的重复次数。好了——让我们试试我的 QOI 解析器 App！我可以打开这个只有几千字节的图标文件，它会立即加载。

这张鸟的照片稍微大一点。加载可能需要几秒钟……好了。是什么花了这么长时间？当你处理真实世界的数据时遇到明显的减速，通常是算法或数据结构使用不当的信号。让我们使用 Instruments 来查找并解决这个问题的根源。在我的解析库中，我写了一个测试来解析那张加载缓慢的鸟的图片。我可以点击运行按钮来执行测试……

几秒钟后测试通过了。除了用这个测试来检查正确性，我还可以分析这个测试，在 Instruments 中查看它的性能。这次，我辅助点击运行按钮。菜单中有一个分析测试的选项。

我喜欢这个功能。分析测试时，我可以专注于我感兴趣的代码特定部分。我现在选择该选项来启动 Instruments。

Instruments 打开了模板选择器，展示了它可以帮助你理解代码性能的各种方式。我们今天要使用两种不同的 instruments 工具，所以我会从空白模板开始。

我可以点击添加 instrument 按钮来添加工具。我将添加 Allocations instrument 来帮助理解我的解析器是如何分配内存的。由于我真的很想知道我的 App 的时间花在了哪里，我还会添加“Time Profiler”工具。

Time Profiler 是解决性能问题的绝佳起点。

让我们隐藏侧边栏，为结果腾出更多空间。然后使用录制按钮启动测试。

我们可以在结果窗口中看到一些东西。

配置文件中包含的 instruments 工具列在窗口顶部。我们会先使用“Time Profiler”，所以我保持选中它。底部是所选工具的详细视图。左边是捕获调用的列表……

右边是当前选中调用的最重堆栈跟踪。

我想先看捕获频率最高的调用，不管它们是如何被调用的，所以我点击 Call Tree（调用树）按钮，然后勾选“Invert Call Tree”（反转调用树）复选框。我可以使用详细视图顶部的这个按钮切换到图形视图。点击后，视图切换为以火焰图形式显示分析结果。

火焰图中的每个条块都表示该调用在分析期间被捕获的时间比例。在这种情况下，有一个巨大的条块主导了整个过程，标为“platform_memmove”。同样的符号也出现在堆栈跟踪中，memmove 是一个用于复制数据的系统调用，所以这个巨大的条块表明解析器大部分时间都在四处复制数据，而不是仅仅读取数据。但这本不该发生。让我们找出代码中导致所有这些复制的部分。我想查看堆栈跟踪中的所有帧，所以点击视图顶部的“show all frames”（显示所有帧）按钮。

跟踪的顶部是系统调用，包括 platform_memmove，然后是 Foundation 的 Data 类型提供的一些专门化方法。你可能在堆栈跟踪中或调试时见过像这样的专门化方法。这些专门化方法是 Swift 编译器为你生成的泛型代码的类型特定版本。

最后，我们来到了我定义的一个方法——readByte。

由于这是我代码中离问题最近的函数，因此是合适的起点。要直接跳转到这个方法，我可以辅助点击，然后选择“Reveal in Xcode”（在 Xcode 中显示）。这就是 Xcode 中 readByte 方法的声明。Instruments 直接把我带到了这一行，这里我丢弃了第一个字节，然后调用了 Data 的初始化方法。借助 Instruments，我能够找出所有那些 memmove 调用是库性能缓慢的潜在来源，然后直接跳转到导致所有这些复制的具体代码行。

这个辅助方法非常重要……因为我的解析代码在消费原始二进制数据时，会反复调用 readByte。

我原以为这只会缩小数据量，每次调用 readByte 方法时返回第一个字节并将数据的起始位置前移。但实际上，每次我读取一个字节，它都会将数据的全部内容复制到一个新的分配中。这比我预期的要多得多的工作量。让我们修复这个错误。我现在回到 Xcode 中，编辑 readByte 方法。

由于 Data 类型设计为可以从两端收缩，我们实际上有一个名为 `popFirst()` 的集合方法可用。popFirst() 返回 `data` 中的第一个字节，然后将集合的前端向后滑动，使其大小减少一个字节。正是我们想要的。

修复之后，我可以切换回我的测试，再次运行分析。

Instruments 自动打开，测试已经在相同的分析配置下运行。太棒了！火焰图中那个巨大的 platform_memmove 条块消失了。

当我基准测试我的代码时，我也看到了这个改变带来的巨大加速！这非常棒，但对于这样的算法变更，绝对变化量并不一定是全部故事。在我最初的版本中，图像大小与解析所需时间之间的关系是二次的。随着我解析的图像变大，解析所需的时间急剧增加。有了复制修复之后，现在这种关系是线性的。图像大小和解析时间之间有了更直接的匹配。接下来我们还会进行更多的改进，以提升线性性能，并且我们将能够更直接地比较这些改进。

解决了那个问题，让我们看看另一个常见的性能陷阱：多余的分配。

让我们看看现在最重的堆栈跟踪是什么。这些调用显示我们看到了大量对分配和释放 Swift 数组的方法的访问。分配和释放内存可能代价高昂。如果我能找出这些多余分配来自哪里并消除它们，我的解析器会更快。要查看解析器所做的分配，我可以使用我们之前添加的 Allocations instrument。有几个不同的指标表明我的代码可能导致了不必要的分配。

首先是数量：在解析一张图片的过程中有近一百万次分配？我认为我们可以做得更好。其次，我们可以看到几乎所有这些分配都是瞬态分配（transient allocations），由 Allocations instrument 标记为短生命周期。为了找到问题的根源，我将详细面板切换到调用树视图。首先，我点击标为“Statistics”（统计）的弹出式按钮。然后我选择“Call Trees”（调用树）。

选中顶部线程后，我将查看堆栈跟踪以找到离问题最近的代码部分。由于这个堆栈跟踪没有反转，我需要从跟踪的底部开始查看。来自我解析器的第一个符号是这个 RGBAPixel.data 方法。

当我点击那个方法时，它在调用树详细信息窗口中显示出来。当我在那里辅助点击该方法时，我可以选择 Reveal in Xcode 来跳转到源代码。

这个方法似乎是多余分配的来源。我可以看到每次调用它时，它都会返回一个包含像素 RGB 值或 RGBA 值的数组。这意味着它每次调用都会创建一个数组并为至少三个元素分配空间。

为了找出它在哪里被使用，我将辅助点击函数名并选择“Show callers”（显示调用者）。调用者是我们主解析函数中的这个闭包，它只是这个大的 flatMap 和 prefix 链的一部分。为了理解为什么这段代码会产生这么多独立的分配，让我们一步步看看分配是如何堆积起来的。

首先，readEncodedPixels 方法将二进制数据解析为编码像素——这些是我之前提到的不同像素类型——并且它需要分配足够的空间来存储它们。

接下来，为每个编码像素调用 decodePixels，以产生一个或多个 RGBA 像素。大多数编码只变成一个像素，但有一种编码表示我们需要将前一个像素重复一定次数。为了支持这一点，decodePixels 总是返回一个数组。这些数组中的每一个都需要被分配。

flatMap 的“展平”部分把我们刚刚创建的所有小数组合并成一个更大的数组。这是一个新的分配，所有我们刚刚创建的小数组都被释放了。

这个 prefix 方法限制了我们能产生的像素数量。

第二个 flatMap 首先调用 RGBAPixel.data，即我们使用 Allocations instrument 时标记的那个方法。我们之前看到它返回一个包含三个或四个元素的数组。我们现在看到的情况意味着，最终图像中的每一个像素都会创建这些 3 或 4 元素数组中的一个。有时编译器能够优化掉其中一些多余的分配，但正如我们在跟踪中看到的，这并不总是发生。

接下来，这些小数组再次被展平成一个大的新数组。

最后，那个大的 RGB 或 RGBA 像素数据数组被复制到一个新的 Data 实例中，以便它可以被返回。

这几行代码有其优雅之处。它们将强大的功能浓缩在简短、链式的方法调用中。但更短并不意味着更快。与其经历所有这些不同的步骤，最终得到一个 Data 实例再返回，不如我们首先分配数据，然后在从二进制源数据解码时直接写入每个像素。这样，我们可以在不需要任何中间分配的情况下完成所有相同的处理。我回到了我的解析函数中。让我们重写这个方法以消除所有这些多余的分配。

我们要做的第一件事是计算“totalBytes”：结果数据的最终大小。然后我们将分配“pixelData”，只分配恰好足够的存储空间。“offset”变量跟踪我们已经写入了多少数据。这种预先分配意味着我们在处理二进制数据的过程中不必进行额外的分配。

接下来，我们将解析每一段数据并立即处理它。我们可以使用 switch 语句来处理解析后的像素。

对于指示运行（run）的编码像素，我们将循环所需的次数，每次写入像素数据。

对于任何其他类型的像素，我们将直接解码并写入数据中。这就是完整的重写，除了我们需要返回的数据之外，没有其他分配。让我们通过再次分析我们的测试来验证我们已经解决了这个问题。

我们可以立即看到分配数量大大减少了。要查看代码中实际分配的数量，我可以使用过滤器。我点击窗口底部的过滤器字段。然后输入“QOI.init”。这将过滤掉任何在堆栈跟踪中不包含 QOI.init 的调用树。

剩下的行显示现在我们的解析器代码只进行了少量分配，总共不到两兆字节。当我按住 option 键并点击展开三角形时，调用树展开了。

展开的树显示了我们想要的结果。

我们真正分配的唯一东西就是存储结果图像的 Data。

看看基准测试，这又是一个巨大的改进！通过削减那些多余的分配，我们将执行时间减少了一半以上。

到目前为止，我们对解析器进行了两项算法更改，消除了大量意外的复制，然后减少了分配数量。在接下来的几个改进中，我们将使用一些更高级的技术，让 Swift 编译器能够消除运行时发生的许多自动内存管理工作。

首先，让我们谈谈数组和其他集合类型是如何工作的。Swift 的 Array 类型是我们工具箱中最常用的工具之一，因为它快速、安全且易于使用。数组可以根据需要增长或缩小，所以你无需预先知道将要处理多少项。Swift 在后台为你处理内存。数组也是值类型，这意味着对一个数组副本的更改不会影响其他副本。如果你通过赋值给不同的变量或将其传递给函数来复制一个数组，Swift 不会立即复制元素。相反，它使用了一种称为写时复制（copy-on-write，COW）的优化技术，将复制推迟到你实际更改其中一个数组时。

这些特性使数组成为出色的通用集合，但它们也有一些权衡。为了支持其动态大小和多个引用，Array 将其内容存储在一个单独的分配中，通常在堆上。Swift 运行时使用引用计数来跟踪每个数组的副本数量，当你进行更改时，数组会进行唯一性检查（uniqueness check）以确定是否需要复制其元素。最后，为了确保代码安全，Swift 强制执行独占访问（exclusivity），这意味着两个不同的事物不能同时修改相同的数据。虽然这个规则通常在编译时强制执行，但有时只能在运行时强制执行。现在我们已经了解了这些底层概念，让我们看看它们如何出现在我们的分析中。我们将首先查找运行时的独占访问检查，它们会给程序增加工作并妨碍优化。在我们开始查找独占访问检查之前，我们实际上有一个好问题。我们的性能已经提升得足够好，以至于 Instruments 没有足够的时间来检查解析器的进程。我们可以通过循环解析代码来给它多一点东西来观察——循环 50 次应该就够了。

让我们看看这个更丰富的分析结果。

独占访问检查在跟踪中显示为‘swift_beginAccess’和‘swift_endAccess’符号。我再次点击窗口底部的过滤器框。然后输入符号名。

在火焰图的顶部，swift_beginAccess 出现了几次，需要进行此检查的符号就在下面。这些符号是前一个像素（previous pixel）和像素缓存（pixel cache）的访问器，它们存储在我的解析器的 State 类中。我切换回 Xcode 并找到那个声明。就是这里……State 是一个包含我们在火焰图中看到的这两个属性的类。修改类实例是 Swift 必须在运行时检查独占访问的情况之一，所以这个声明就是我们看到上述现象的原因。我们可以通过将这些属性从类中移出，直接放在解析器类型中来消除这种检查。

接下来，我们将进行查找替换，移除 previousPixel 和 pixelCache 的 `state.` 访问。

当我构建时，编译器告诉我还有一些工作需要做。

由于 state 属性不再嵌套在类中，我无法在非 mutating 方法中修改它们。

我将接受这个修复，使该方法变为 mutating。

还有一个需要修复……

我们完成了。完成这个更改后，让我们回到测试。

并重新录制一个分析来看看变化。

我再次过滤 swift_beginAccess。

什么都没有了！我们已经完全移除了运行时独占访问检查。让我们再看看那些状态变量。这是一个很好的地方，可以使用 Swift 的新特性将数据从堆内存移动到栈内存，并确保那些独占访问检查不会卷土重来。我们解析器中的像素缓存是一个 RGBAPixel 数组——它被初始化为 64 个元素，并且大小从不改变。这个缓存是使用新的 InlineArray 类型的绝佳位置。InlineArray 是 Swift 6.2 中新增的标准库类型。像常规数组一样，它在连续内存中存储相同类型的多个元素，但它有一些重要的区别。首先，内联数组具有在编译时设置的固定大小。与可以追加或删除的常规数组不同，InlineArray 使用新的值泛型特性，将其大小作为类型的一部分。这意味着虽然你可以更改内联数组的元素，但不能追加或删除，也不能将一个大小不同的内联数组赋值给它。

其次，顾名思义，当你使用 InlineArray 时，元素总是内联存储，而不是在单独的分配中。内联数组在副本之间不共享存储，也不使用写时复制。相反，每当你复制时，它们都会被复制。这消除了常规数组所需的所有引用计数、唯一性和独占性检查。InlineArray 这种不同的复制行为有点像一把双刃剑——如果你对 Array 的使用需要制作副本或在不同的变量或类之间共享引用，那么 InlineArray 可能不是正确的选择。然而，在这种情况下，像素缓存是一个固定大小的数组，它在原地被修改，但从不被复制。使用 `InlineArray` 的绝佳场所。

对于我们的最终优化，我们将使用标准库新的 span 类型来消除解析过程中的大部分引用计数。回到 Time Profiler 火焰图，让我们再次使用过滤，只查看我们的 QOI 解析器。我在过滤器框中添加 QOI.init。

视图会改变，只关注那些包含我们的解析初始化器的堆栈跟踪。让我们寻找 retain 和 release 符号。swift_retain 是这个粉色的条块，出现在 7% 的样本中，而 swift_release 是这个，出现在另外 7% 的样本中。我们之前谈到的唯一性检查也出现在这里，在另外 3% 的样本中。

为了找出这些来自哪里，我点击回 swift_release，就像我们之前做的那样，向下扫描最重的堆栈跟踪，找到第一个用户定义的方法。看起来这和我们开始时使用的 readByte 方法是同一个。

这次，我们处理的不是算法问题，而是 `Data` 本身的使用。就像 `Array` 一样，`Data` 通常将其内存存储在堆上，并且需要被引用计数。

这些引用计数操作——retain 和 release——非常高效，但当它们发生在像这个方法一样的紧密循环中时，加起来可能会占用大量时间。为了解决这个问题，我们希望从使用像 `Data` 或 `Array` 这样的高级集合类型，转向一种不会导致这种引用计数暴增的类型。在 Swift 6.2 之前，你可能使用过像 `withUnsafeBufferPointer` 这样的方法来访问集合的底层存储。这些方法让你手动管理内存，没有引用计数，但它们会将不安全引入你的代码。

值得一问——为什么指针是不安全的？Swift 之所以称它们为不安全，是因为它们绕过了语言的许多安全保障。它们可以指向已初始化和未初始化的内存，它们放弃了一些类型保证，并且它们可以逃逸出它们的上下文，导致访问不再分配的内存的风险。当你使用不安全指针时，你完全负责保持代码的安全。编译器无法帮助你。这个 processUsingBuffer 函数确实正确地使用了不安全指针。使用完全保留在不安全缓冲区指针闭包内，只有计算结果在最后返回。另一方面，这个 `getPointerToBytes()` 函数是危险的。它包含两个主要的编程错误。该函数创建了一个字节数组并调用了 withUnsafeBufferPointer 方法，但不是将指针的使用限制在闭包内，而是将指针返回到外部作用域。错误 1。更糟糕的是，代码随后从函数本身返回了那个不再有效的指针。错误 2！这两个错误都将指针的生命周期延长到了它所指向的对象生命周期之外，创建了一个危险的、指向已被移动或释放的内存的残留引用。

为了帮助解决这个问题，Swift 6.2 引入了一组新的类型，称为 Spans。Spans 是一种使用属于集合的连续内存的新方法。重要的是，span 使用了新的“非逃逸”（non-escapable）语言特性，它允许编译器将它们生命周期与提供它们的集合绑定在一起。span 提供访问权限的内存在 span 的整个生命周期内保证有效，不存在残留引用的机会。因为每个 span 类型都声明为 Non-Escapable，编译器会阻止你将 span 逃逸或返回到你获取它的上下文之外。

这个“processUsingSpan”方法展示了如何使用 span 来编写比指针更简单、更安全的代码。要获取数组元素的 Span，只需使用 span 属性。无需使用闭包，我们就能访问数组的存储，其效率与不安全指针相同，而且没有任何不安全性。如果我们尝试重写之前那个危险的函数，就能看到非逃逸语言特性的作用。我们首先会遇到的问题是无法用 `Span` 写出相同的函数签名。因为 span 的生命周期与提供它的集合绑定，没有传入任何集合或 span，就无法为传出的 span 获取生命周期。

如果我们尝试通过将 span 捕获到闭包中来隐藏它呢？在这个函数中，我会创建一个数组，访问它的 span，然后尝试返回一个捕获了该 span 的闭包。但即使这样也不行。编译器识别出捕获 span 会让它逃逸，并指出它的生命周期依赖于局部数组。

这种由编译器检查的、要求 span 不逃逸出其作用域的约束意味着 retain 和 release 不再是必需的。我们获得了使用不安全缓冲区的性能，没有任何不安全性。`Span` 系列包括只读和可变 span 的类型化版本和原始版本，用于操作现有集合，以及一个输出 span（OutputSpan），你可以用它来初始化新的集合。该系列还包括 UTF8Span，这是一种旨在进行安全高效 Unicode 处理的新类型。

回到我们的代码，让我们为 RawSpan 实现同样的 readByte 方法。

我们首先添加一个 RawSpan 扩展……

并定义 readByte 方法。

RawSpan 的 API 与 Data 稍有不同，但它做的事情与上面实现相同。它加载第一个字节，缩小 RawSpan，然后返回加载的值。请注意，这个 unsafeLoad 方法之所以如此命名，只是因为加载某些类型的类型可能不安全。像我们这里所做的那样加载一个内置整数类型始终是安全的。

接下来，我们将更新我们的解析方法。

这两个解析方法应该使用 RawSpan 而不是 Data 作为参数。

我还需要在调用处做一个更改。

我们不传递数据本身，而是获取数据的 RawSpan 并将其传递给解析方法。我将使用 `bytes` 属性访问 Data 的 RawSpan。这个 rawBytes 值是非逃逸的。我不能从这个函数返回它，但我可以毫无问题地将其传递给解析方法。

完成这个更改后，我完成了使用 RawSpan 的更新。为了节省更多的底层工作，我们还可以在我们的解析方法中采用新的 OutputSpan。

我们不创建零初始化的 Data，而是使用新的 rawCapacity 初始化器，它提供一个 OutputSpan 来逐步填充未初始化的数据。

OutputSpan 会跟踪你已经写入了多少数据，所以我们可以使用它的 count 属性来代替这个单独的 offset 变量。

我们将使用我们写入方法的一个不同变体，该变体写入 outputSpan 而不是 Data 实例。

让我们看看那个方法的实现。

write(to:) 方法能够为像素中的每个通道调用 OutputSpan 的 append 方法。由于 OutputSpan 是一种专为这类用途设计的非逃逸类型，这比写入 `Data` 实例更简单、更高效，也比下降到不安全缓冲区指针更安全。完成这些更改后，我跳回我的测试。并录制一个新的分析。

我过滤 QOI.init。

在火焰图中我们可以看到那些 swift_retain 和 swift_release 块消失了！这看起来真棒。让我们停在这里，看看采用 InlineArray 和 RawSpan 的结果。

通过这些最新的更改，我们的内存管理工作使解析速度提高了六倍，而且没有使用任何不安全代码。这比我们摆脱二次算法后快了 16 倍，比我们开始时快了 700 多倍！我们在本节中涵盖了很多内容。在修改这个图像解析库的过程中，我们做了两项算法更改，以提高效率并减少分配。我们使用了新的标准库类型 InlineArray 和 RawSpan 来消除运行时内存管理，并学习了新的非逃逸语言特性。新的 Swift Binary Parsing 库就是建立在同样的这些特性之上的。该库旨在为二进制格式构建安全、高效的解析器，并支持开发者处理多种不同的安全性问题。该库提供了一整套解析初始化器和其他工具，指导你安全地从原始二进制数据中消费值。

这是一个使用新库编写的 QOI 头部解析器的例子。这展示了它的几个特性，包括 ParserSpan，一种用于解析二进制数据的自定义原始 span 类型。以及防止整数溢出并允许你指定符号、位宽和字节序的解析初始化器。该库还为你自己的自定义原始可表示类型提供验证解析器，以及产生可选值的运算符，用于安全地使用不可信的、新解析的值进行计算。

我们已经在 Apple 内部使用 Binary Parsing 库了，并且它今天已经公开可用！我们鼓励你去看看并尝试一下。你可以通过在 Swift 论坛发帖或在 GitHub 上提出 issue 或 pull request 来加入社区。

非常感谢你与我一同踏上这段优化我们 Swift 代码的旅程！尝试使用 Xcode 和 Instruments 来分析你自己 App 中对性能关键的部分进行测试。你可以在文档中探索新的 InlineArray 和 Span 类型，或者下载新版本的 Xcode。祝你在 WWDC 玩得开心！
