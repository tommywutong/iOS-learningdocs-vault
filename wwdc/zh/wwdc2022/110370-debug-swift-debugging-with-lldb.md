---
title: 使用 LLDB 调试 Swift 调试
session_id: 110370
collection: wwdc2022
year: 2022
duration: '20:04'
topics: [Developer Tools, Swift]
group: G · 调试、崩溃与 Instruments
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2022/110370/'
content_hash: 'sha256:4c0c5191c04bad25'
translated: true
---

# 使用 LLDB 调试 Swift 调试

<sub>WWDC2022 · 20:04 · Developer Tools、Swift</sub>

了解如何为复杂的 Swift 项目做好调试准备。我们将深入探讨 LLDB 的内部机制和调试信息……

> [!note] 归档理由
> Swift 调试信息如何生成与丢失，反射与类型元数据

## 相关资源

- [HD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/110370/7/31CCC67C-D5AC-4493-AFB4-7B833E2B8162/downloads/wwdc2022-110370_hd.mp4?dl=1)
- [SD 视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/110370/7/31CCC67C-D5AC-4493-AFB4-7B833E2B8162/downloads/wwdc2022-110370_sd.mp4?dl=1)
- [问答：使用 LLDB 调试 Swift 调试](https://developer.apple.com/videos/play/wwdc2022/110505)
- [探索断点改进](https://developer.apple.com/videos/play/wwdc2021/10209)
- [符号化：超越基础](https://developer.apple.com/videos/play/wwdc2021/10211)
- [LLDB：超越 "po"](https://developer.apple.com/videos/play/wwdc2019/429)
- [使用 Xcode 和 LLDB 的高级调试](https://developer.apple.com/videos/play/wwdc2018/412)
- [显示所有已加载动态库的信息](https://developer.apple.com/videos/play/wwdc2022/110370/?time=304)
- [显示代码地址的调试信息](https://developer.apple.com/videos/play/wwdc2022/110370/?time=324)
- [显示 target.source-map 的帮助信息](https://developer.apple.com/videos/play/wwdc2022/110370/?time=358)
- [在 LLDB 中重映射源路径](https://developer.apple.com/videos/play/wwdc2022/110370/?time=397)
- [源路径重映射](https://developer.apple.com/videos/play/wwdc2022/110370/?time=422)
- [调试前缀映射](https://developer.apple.com/videos/play/wwdc2022/110370/?time=493)
- [打印 "words" 的对象描述](https://developer.apple.com/videos/play/wwdc2022/110370/?time=512)
- [计算表达式 "words"](https://developer.apple.com/videos/play/wwdc2022/110370/?time=520)
- [显示变量 "words"](https://developer.apple.com/videos/play/wwdc2022/110370/?time=538)
- [Swift 变量的原始内存](https://developer.apple.com/videos/play/wwdc2022/110370/?time=610)
- [查看 LLDB 内嵌 Swift 编译器的诊断信息](https://developer.apple.com/videos/play/wwdc2022/110370/?time=719)
- [向链接器注册 Swift 模块](https://developer.apple.com/videos/play/wwdc2022/110370/?time=947)
- [验证二进制文件中已注册的 Swift 模块](https://developer.apple.com/videos/play/wwdc2022/110370/?time=965)
- [在 Linux 上将 Swift 模块包装到目标文件中](https://developer.apple.com/videos/play/wwdc2022/110370/?time=972)
- [计算表达式 "self"](https://developer.apple.com/videos/play/wwdc2022/110370/?time=1012)
- [打印 "words" 的对象描述](https://developer.apple.com/videos/play/wwdc2022/110370/?time=1018)
- [步入函数调用](https://developer.apple.com/videos/play/wwdc2022/110370/?time=1028)
- [单步执行指令](https://developer.apple.com/videos/play/wwdc2022/110370/?time=1030)
- [避免 Swift 模块中的序列化搜索路径（命令行）](https://developer.apple.com/videos/play/wwdc2022/110370/?time=1103)
- [避免 Swift 模块中的序列化搜索路径（Xcode）](https://developer.apple.com/videos/play/wwdc2022/110370/?time=1104)
- [在 LLDB 中重新引入搜索路径](https://developer.apple.com/videos/play/wwdc2022/110370/?time=1112)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ 大家好。我叫 Adrian，今天我将与大家讨论如何为使用 LLDB 获得出色的调试体验来设置项目。LLDB 是与 Xcode 一起提供的底层调试技术。LLDB 允许你在 App 中设置断点、暂停执行、检查变量和对象的状态、探索代码等等。LLDB 可以帮助你理解代码正在做什么，并让你能够找到代码行为偏离预期的地方。它是理解和探索代码的强大工具。如果你想了解有关 LLDB 的更多信息，请查看之前的视频，例如 WWDC21 的“探索断点改进”。今天，我们将探讨一些对调试 Swift 代码有独特影响的高级工作流程。也许你正在将第三方 framework 集成到你的 App 中。也许你的 App 和团队已经发展到大部分代码由持续集成系统构建的地步。也许你正在使用自定义构建系统来集成到你公司的基础架构中。也许你正在为其他软件开发人员构建软件。或者你只是想更多地了解 LLDB。我的目标是让你更好地理解 LLDB 的工作原理，以及它需要从构建系统中获取哪些信息才能正常运行。我这里有一个小项目，我们将把它作为我们的运行示例。我是一名编译器工程师，喜欢游戏，所以我在业余时间用纯 Swift 为文字冒险游戏编写解析器。这是我最近开始的一个。让我给你看看我目前所做的工作。游戏使用文本界面，所以我在终端中运行它。就像每一个优秀的冒险游戏一样，我们将从检查我们的背包开始。

游戏设定在当代。我看到我有一部 iPhone。接下来，让我们看看周围的环境。

嗯，这个传感器看起来很有趣。也许我们可以在传感器上使用 iPhone？我扔掉了 iPhone？呃，这不是我想展示给你的。我想我的游戏有一个 bug。好在这是一场关于调试器的演讲。让我们在解析器中设置一个断点，然后再次运行我们的命令。

我们应该首先确认命令被正确读取了。"words" 变量包含分词后的命令。

啊，这并没有按预期进行。我不知道这里发生了什么。昨天我使用调试器还没有问题，然后昨晚我集成了这个用于在终端上设置文本样式的 UI framework。该 framework 的开发者有一个持续集成系统，可以每天生成该 framework 的构建版本，而我正在直接链接最新的版本。我想知道这个 framework 是否与我的调试问题有关。比如说，我已经注意到我无法步入该 framework 的源代码，即使我明确下载了调试构建版本。你看那个。

我只能看到汇编代码。

让我们试着理解那里发生了什么，首先弄清楚为什么我看不到任何源代码。LLDB 需要什么才能显示源代码？当编译器编译一个函数时，它会生成机器码。

它会为调试器留下线索，以便可执行文件中的地址可以映射到源文件和行号，反之亦然。这些线索称为调试信息。在 Apple 平台上，调试信息存储在目标文件中。为了归档和分发，调试信息可以链接到 .dSYM bundle 中。调试信息链接器称为 dsymutil。LLDB 使用“聚焦”来定位 .dSYM bundle，因此它在磁盘上的位置非常灵活。既然我们知道了调试信息的工作原理，让我们回到示例。首先，让我们验证 LLDB 是否确实找到了该 framework 的 dSYM。我们可以使用 `image list` 命令来做到这一点。这个 UI framework 叫做 "TerminalInterface"。

是的，LLDB 确实找到了该 framework 的 dSYM。这意味着它可以访问调试信息。我们可以使用 `image lookup` 来获取有关当前地址的更多信息。

顺便说一下，如果你想了解有关各种选项的更多信息，LLDB 有一个出色的内置帮助。

啊，我想我明白为什么没有源代码了：这个源路径指向构建服务器上源代码的位置，而不是我本地机器上的位置。我们可以解决这个问题。LLDB 有一个内置的源映射，我们可以用它来重定向这些路径。

我们现在就可以输入命令，但我更希望让这个更改更持久。在 Scheme 编辑器中（你可以通过“Product” > “Scheme” > “Edit scheme”来打开，或者只是按住 Option 键单击播放按钮），你可以定义每个项目的 LLDB 初始化文件。我已经为这个项目添加了一个。

现在我们已经设置好了 LLDB，让我们再次运行我们的项目。

我们有了源代码。

LLDB 可以使用 `settings set target.source-map` 来重映射源路径。你可以将此命令放入项目的 `.lldbinit` 文件中，以便自动运行。或者，每个 .dSYM bundle 都包含一个 XML .plist 文件，你可以在其中放置一个路径前缀重映射字典。如果你有一个从服务器获取最新构建版本的下载脚本，你可以修改该脚本，以自动将适当的重映射字典注入到下载的 .dSYM 中。你可以在 LLDB 网站上了解有关此过程的更多信息。

源路径完全与语言无关，因此此方法适用于 Swift、C++ 和 Objective-C 项目。要了解有关 Apple 平台上符号的更多信息，请查看 WWDC21 的“符号化：超越基础”。当源代码在构建服务器群上编译时，源文件的远程路径可能因机器而异。为了避免为每台机器定义一个重映射前缀，我们可以指示编译器在将源路径放入调试信息之前对其进行规范化。这是使用 `-debug-prefix-map` 选项完成的。这样，机器特定的路径前缀就可以被一个唯一的、规范的占位符名称替换，然后可以在 LLDB 中重映射到本地路径。在我们深入探讨源路径问题之前，我正试图打印 "words" 的对象描述。

那没有成功。实际上，就连计算表达式 "words" 也没有成功。

至少我们可以在变量视图中看到变量。

Xcode 变量视图的控制台等效命令是 `frame variable` 或 `v` 命令。

如果你想了解这些命令之间的细微差别，请查看 WWDC19 的“LLDB：超越 'po'”。那么 po 是什么，为什么它仍然不工作？要理解这意味着什么，我们需要更多地了解 LLDB。提醒一下，LLDB 是一个调试器。但 LLDB 不仅仅是一个调试器。它还是一个编译器！除了调试器的功能外，LLDB 还包含一份功能完整的 Swift 和 Clang 编译器副本。这些编译器为 LLDB 的表达式求值器提供动力，你可能通过 `p` 和 `po` 命令别名了解它。使用表达式求值器，我们可以超越查看变量，执行计算、调用函数，甚至更改程序的状态。查看 WWDC18 的“使用 Xcode 和 LLDB 的高级调试”，了解这些命令可能的应用。调试器如何格式化局部变量？编译器提供的调试信息告诉调试器变量在内存中的存储位置。但仅凭这些信息，LLDB 只能向我们显示一串随机排列的原始字节。那么 LLDB 是如何将其转变为格式良好的输出的呢？答案是类型。类型信息使 LLDB 能够理解源变量的结构和内存布局。有了类型信息，LLDB 就知道一个聚合类型有哪些字段，并且类型允许 LLDB 使用适当的数据格式化器来美化打印它们。现在让我们看看类型信息来自哪里。在调试器端，`frame variable` 和 `v` 命令所在的位置，LLDB 从调试信息中获取类型信息。同时，LLDB 也从 Swift 反射元数据中获取类型。在编译器端，表达式求值器和 `po` 所在的位置，LLDB 从模块中获取类型信息。这种清晰的分离是 Xcode 14 中的新特性，并解释了为什么即使表达式求值器无法工作，变量视图也可以完全功能正常。模块是编译器组织类型声明的方式。Swift 编译器知道很多导入模块的方法，但在我们深入探讨之前，我想向你展示一个方便的新功能。

我们如何开始诊断发生在编译器端的问题？今年，LLDB 新增了一个 `swift-healthcheck` 命令。这是你查明模块导入是否失败的第一站。让我展示一下它的工作原理。通过在问题发生后运行 `swift-healthcheck`，我们可以访问 Swift 表达式求值器配置的日志。

在日志的末尾，我们看到 LLDB 导入 "TerminalUI" Swift 模块时遇到了问题。根据名称，我假设这是 TerminalInterface framework 的一个实现细节。缺少这个模块是个问题，因为 `self` 的类型在 UI 实现上是泛型的，没有包含该类型的模块，表达式求值器就无法实现 "self" 的动态类型。我正在向 framework 的开发者发送消息，并请他们调查。根据我的经验，他们总是非常响应迅速。谁知道呢，也许我们甚至可以在本视频结束前找到解决方案。在此期间，让我们看看 LLDB 的编译器是如何找到 Swift 模块的。

我的 App 有自己的 Swift 模块。它可能会导入一个系统 framework，例如 Foundation。系统 framework 是位于 SDK 中的文本稳定 Swift 接口文件。任何 Swift 模块都可能导入一个 Clang 模块，这是一个花哨的名称，指的是在模块映射文件的帮助下分组在一起的一个或多个头文件。Clang 模块可以依赖其他 Clang 模块。

我的 App 也可能导入一个属于本地构建的 framework 的 Swift 模块。它也可以导入不属于 SDK 的文本 Swift 接口文件。如果你想了解如何操作，请查看 WWDC19 的“Swift 中的二进制 Framework”。我的 App 还可能链接一个包含 Swift 代码的静态库，然后它也会附带一个 Swift 模块。嗯，不过我们还没说完。我应该提一下还有桥接头文件，它也可以导入 Clang 模块。最后，作为 LLDB 特有的一个特性，一些模块内容可以仅从调试信息中重建。来源真多！LLDB 如何找到它们全部？打包这些模块以便 LLDB 能找到它们是构建系统的工作。来自系统 framework 的模块留在 SDK 中。LLDB 会在附加到你的程序时找到一个匹配的 SDK 来读取它们。当直接从目标文件调试时，LLDB 会在构建时所在的位置找到所有非 SDK 模块。Dsymutil 可以为每个动态库、framework 或 dylib 以及可执行文件打包一个名为 .dSYM bundle 的调试信息存档。

每个 .dSYM bundle 都可以包含二进制 Swift 模块，这些模块可能包含桥接头文件、文本 Swift 接口文件，以及最重要的调试信息。这涵盖了所有内容。所有内容？除了属于静态归档文件的 Swift 模块之外的所有内容。

为了使 Swift 模块能被 dsymutil 拾取，它需要向链接器注册。对于动态库和可执行文件，构建系统会自动为你完成此操作。但是静态归档文件不是由链接器生成的，它们只是目标文件的集合，就像 zip 文件一样。这意味着将任何 Swift 模块注册到链接器的责任落在了链接该静态归档文件的每个可执行文件或动态库上。在许多情况下，Xcode 的构建系统会为你执行此操作。但是如果你正在维护自己的自定义构建系统，或者你定义了自定义构建规则，则需要注意这一点。

在使用 Apple 链接器时，需要使用 `-add-ast-path` 选项注册 Swift 模块。检查你的构建日志以确认情况如此。你也可以使用 dsymutil 转储你的可执行文件的符号表，并 grep 查找 "swiftmodule" 来验证它是否有效。

在像 Linux 这样的其他平台上，swift 驱动程序支持一个 `-modulewrap` 操作，该操作将二进制 Swift 模块文件转换为目标文件，你可以将其与其余调试信息一起链接到你的二进制文件中。LLDB 会在那里找到它。framework 的开发者们非常响应迅速。正如我们怀疑的那样，结果是作为 framework 构建系统的一部分，使用了一个静态归档文件。而属于该静态归档文件的 Swift 模块缺失在 dSYM bundle 中。我现在已经安装了修复版本的 framework。它已将缺失的静态模块注册到链接器，因此 dsymutil 能够收集到它。

现在 `self` 可以被解析了。

并且我们可以打印 "words" 的对象描述。

既然我们已经在使用控制台，我使用 `s` 别名步入 `parseFrom` 函数。

现在我们也可以轻松地找到 bug，这里只是一个复制粘贴的错误。

这样，我们不仅解决了缺失 Swift 模块的难题，也解决了游戏中的第一个谜题。

在我们结束之前，我还有一个细节需要注意。Swift 编译器会将 Clang 头文件搜索路径和其他相关选项序列化到二进制 .swiftmodule 文件中。这很好，因为它使得在构建期间导入它们的 Clang 模块依赖项能够正常工作。但是当在不同的机器上构建时，这些本地路径可能会造成不利影响。因此，在将二进制 .swiftmodule 分发到另一台机器之前，请考虑使用 `-no-serialize-debugging-options` 编译器标志进行构建。在 Xcode 中，这通过 `SWIFT_SERIALIZE_DEBUGGING_OPTIONS` 设置进行控制。

你可以使用以下设置之一在 LLDB 中重新引入这些搜索路径。让我们回顾一下我们学到的内容。如果你想将代码从一台机器分发到另一台机器，你应该问问自己期望进行何种程度的调试。例如，如果你将一个二进制 framework 分发给另一个开发者，并且你不希望他们步入你的代码进行调试，那么最好只将 Swift 模块作为文本 .swiftinterface 文件分发。但是如果你正在设置一个构建服务器或持续集成系统，并且期望开发者调试下载的构建产物，那么你将希望确保构建一个二进制 Swift 模块，并考虑关闭搜索路径序列化。你还可以使用 `-debug-prefix-map` 选项规范化服务器上调试信息中的源路径。这就是我要分享的全部内容。今天我们了解了 LLDB 作为调试器和编译器的双重性质。调试器需要调试信息和反射元数据才能工作，并提供 Xcode 变量视图和 `v` 命令。编译器需要模块，并且对搜索路径很敏感。它位于 `expr`、`p` 和 `po` 命令之后。获取编译器诊断信息的一个好方法是 LLDB 中新增的 `swift-healthcheck` 命令。感谢观看！♪ ♪
