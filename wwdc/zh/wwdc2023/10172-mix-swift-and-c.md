---
title: 混合使用 Swift 与 C++
session_id: 10172
collection: wwdc2023
year: 2023
duration: '17:45'
topics: [Developer Tools, Swift]
group: A · ObjC/Swift runtime 与语言实现
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2023/10172/'
content_hash: 'sha256:364b169079867905'
translated: true
---

# 混合使用 Swift 与 C++

<sub>WWDC2023 · 17:45 · Developer Tools、Swift</sub>

了解如何在 C++ 和 Objective-C++ 项目中使用 Swift，使代码更安全、更快速、更易于开发。我们将向你展示……

> [!note] 归档理由
> Swift 与 C++ 互操作模型

## 章节

- [互操作性基础](/videos/play/wwdc2023/10172/?time=40)
- [将 Swift 添加到 C++ 代码库](/videos/play/wwdc2023/10172/?time=142)
- [在 Swift 中调用 C++ 方法](/videos/play/wwdc2023/10172/?time=250)
- [在 C++ 中调用 Swift 方法](/videos/play/wwdc2023/10172/?time=290)
- [改进 C++ API 的导入方式](/videos/play/wwdc2023/10172/?time=452)
- [外部引用类型](/videos/play/wwdc2023/10172/?time=735)

## 相关资源

- [互操作性基础](https://developer.apple.com/videos/play/wwdc2023/10172/?time=40)
- [将 Swift 添加到 C++ 代码库](https://developer.apple.com/videos/play/wwdc2023/10172/?time=142)
- [在 Swift 中调用 C++ 方法](https://developer.apple.com/videos/play/wwdc2023/10172/?time=250)
- [在 C++ 中调用 Swift 方法](https://developer.apple.com/videos/play/wwdc2023/10172/?time=290)
- [改进 C++ API 的导入方式](https://developer.apple.com/videos/play/wwdc2023/10172/?time=452)
- [外部引用类型](https://developer.apple.com/videos/play/wwdc2023/10172/?time=735)
- [混合使用 Swift 与 C++](https://swift.org/documentation/cxx-interop)
- [跨语言边界调用 API](https://developer.apple.com/documentation/Swift/CallingAPIsAcrossLanguageBoundaries)
- [在 Xcode 项目中混合使用多种语言](https://developer.apple.com/documentation/Swift/MixingLanguagesInAnXcodeProject)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10172/4/58243B95-F51E-4E6A-96C8-B85E8102E450/downloads/wwdc2023-10172_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10172/4/58243B95-F51E-4E6A-96C8-B85E8102E450/downloads/wwdc2023-10172_sd.mp4?dl=1)
- [认识演讲者：混合使用 Swift 与 C++](https://developer.apple.com/videos/play/wwdc2023/111588)
- [Swift 的新功能](https://developer.apple.com/videos/play/wwdc2023/10164)
- [导入 C++ 框架](https://developer.apple.com/videos/play/wwdc2023/10172/?time=260)
- [导入生成的头文件](https://developer.apple.com/videos/play/wwdc2023/10172/?time=285)
- [在 C++ 中调用 Swift 方法](https://developer.apple.com/videos/play/wwdc2023/10172/?time=297)
- [使用 SWIFT_COMPUTED_PROPERTY 特性](https://developer.apple.com/videos/play/wwdc2023/10172/?time=502)
- [使用 SWIFT_SHARED_REFERENCE 特性](https://developer.apple.com/videos/play/wwdc2023/10172/?time=522)
- [使用 SWIFT_RETURNS_INDEPENDENT_VALUE 特性](https://developer.apple.com/videos/play/wwdc2023/10172/?time=532)
- [使用 for 循环在 Swift 中遍历 C++ std::vector](https://developer.apple.com/videos/play/wwdc2023/10172/?time=645)
- [导入 swift/bridging](https://developer.apple.com/videos/play/wwdc2023/10172/?time=834)
- [将 SWIFT_SHARED_REFERENCE 特性应用于 CxxImageEngine](https://developer.apple.com/videos/play/wwdc2023/10172/?time=841)
- [将 SWIFT_COMPUTED_PROPERTY 特性应用于 getImages](https://developer.apple.com/videos/play/wwdc2023/10172/?time=893)
- [使用“images”计算属性更新 for 循环](https://developer.apple.com/videos/play/wwdc2023/10172/?time=906)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ Zoe: 大家好，我是 Zoe，Apple 编译团队的一名工程师。今天，我将向大家介绍 Swift 与 C++ 互操作性（interoperability），这是 Xcode 15 的一项新功能，它允许你将 Swift 和 C++ 结合使用。本次演讲将分为两部分。首先，我将解释互操作性的基础概念。然后，我将向你展示如何让 C++ API 在 Swift 中显得自然且安全。Swift 诞生时，世界上已经有许多用 Objective-C 编写的大型 App 和代码库。Swift 必须能够利用这些现有的代码，并逐步被采用到这些代码库中。如今，Swift 将这种互操作性提升到了一个新的水平，允许你在更多地方采用 Swift。

如果你有一个大型的 C++ 代码库，现在你可以利用双向互操作性逐步采用 Swift。如果你需要为 App 访问某个 C++ 库，你不再需要编写一个 Objective-C 桥接层。让我们通过一个示例 App 来看看在 C++ 代码库中采用 Swift 有多么简单。

我正在开发一个照片编辑 App。它可以让我从相机胶卷中选择一张图片，反转颜色，调整亮度等等。

在我深入代码之前，先看看我的 App 的结构。

该 App 可以分为两部分：图像处理框架（framework）和用户界面（user interface）代码。我的 App 所依赖的图像处理框架是用 C++ 编写的。我希望我的用户界面层能够轻松地与我的 C++ 框架通信，所以我使用 Objective-C++ 来实现大部分用户界面，例如 ViewController。现在，我希望我的 App 用户能够从他们的相机胶卷中选择几张照片进行编辑。我听说 SwiftUI 有一个新的 PhotoPicker 视图（view）可以轻松实现这一点，所以我想开始在 App 中采用 Swift。幸运的是，从 Xcode 15 开始，我可以轻松地在我的 Objective-C++ 代码库中采用 Swift，同时仍然可以访问我所有的 C++ API。那么，让我们开始向项目中添加一个 Swift 文件吧。由于我使用的是 C++ 框架，Xcode 会自动导入我的 C++ API，因此我不需要桥接头文件（bridging header）。

然后，我需要在我的项目构建设置中启用 C++ 互操作性。如你所知，Swift 已经可以调用 C 和 Objective-C 的 API，因此构建设置当前设置为 C and Objective-C 模式。但我可以将其更改为 C++。

现在设置显示为 C++ and Objective-C++，我可以直接从我 C++ 的 ImageKit 框架中调用 API。回到我的 Swift 文件，我可以像导入任何其他 Swift 模块一样导入该框架，并且我可以按住 Command 键点击模块名称来查看其内容。现在，这些可能看起来像 Swift API，但它们实际上来自我的 C++ ImageKit 库；这只是 Swift 编译器看到它们的方式。让我们看看我今天将要用到的一些 API。

从底部开始，你可以看到一个类型为 CxxImageEngine 的静态成员。

它当前被作为一个不安全的指针（unsafe pointer）导入，但我们稍后会深入讨论这个问题。CxxImageEngine 还有其他几个成员，即 loadImage 和 getImages，我稍后将使用它们。现在，我将继续放入我的照片选择器的所有用户界面，以便我可以专注于与 C++ 通信的两个方法。

我可以获取共享的 CxxImageEngine，并在每个选中的图像上调用 loadImage 来将它们加载到引擎中。哇，在 Swift 中调用 C++ 方法超级简单。现在我的 SwiftUI 视图已经完成，我想在 Objective-C++ 的 ViewController 中使用它。

为此，我需要将我的 struct 设为 public，以便可以从 Objective-C++ 代码访问它。

太棒了！我所有的 Swift 代码都构建成功了。现在，我可以转到 ViewController 文件并导入 Swift 生成的头文件（header）。

这个头文件包含了我所有公开的 Swift API。现在我已经导入了生成的头文件，我可以开始在 C++ 中调用我的 Swift 代码了。首先，我将构造 SwiftUI 视图。然后，我可以调用 present 方法。

Xcode 会通过代码补全来帮助我。

让我们在设备上测试一下。

在我构建并运行 App 之后，你可以看到我们新的 SwiftUI 视图直接导入到了我的 Objective-C++ App 中。

这是一个真正的双向互操作性的例子。我能够无缝地在 Swift 中使用 C++ 类型和函数，反之亦然。在 C++ 中，我能够构造并使用一个 SwiftUI 视图，而该视图的 body 又回调到我的 C++ 框架中。所有的集成工作都是由 Swift 编译器自动完成的，所以我无需编写桥接层。而且所有的 API 都是直接且原生的，因此与大多数其他支持互操作的语言不同，在 Swift 中调用 C++ API（或反之）没有额外开销。今天我一直在处理一个很小的 App，但 Swift 编译器可以支持大型和复杂代码库的互操作性。

Swift 可以导入大多数 C++ 集合（collection），无论是来自标准库还是其他地方。Swift 可以处理函数模板（function template）和类模板特化（class template specialization）。它还支持使用共享指针（shared pointer）和类似的用户定义类型来管理内存。Swift 可以在高层次上理解这些导入的 API。例如，它知道共享指针的保留（retain）和释放（release）操作，并且可以利用这种高层次知识应用一系列强大的优化。

在另一个方向上，你可以向 C++ 公开大多数 Swift API，例如结构体、类及其方法和其他成员。你甚至可以公开泛型类型（generic type）（如 Array）以及随时间演变的弹性类型（resilient type）。并且 C++ 互操作性完全由 Xcode 支持，因此你将获得跨语言的代码补全、跳转到定义和调试器支持。这些只是 C++ 互操作性所支持的 API 中的一部分。Swift 编译器支持在使用所有这些 API 及其他功能的大型代码库之间实现互操作性，促进跨语言的一致体验，并允许你在更多地方采用 Swift。现在我们已经了解了互操作性的基础知识，让我们更深入地探讨这个特性，探索一些让 C++ API 在 Swift 中感觉自然且安全的方法。Swift 编译器能够自动导入大多数 C++ API，并将它们表示为安全的 Swift API。例如，默认情况下，C++ 类型将作为 Swift 结构体（struct）导入，C++ 运算符将被映射到类似的 Swift 运算符，容器（container）将自动作为集合（collection）导入。但编译器也允许你精细调整 API 的导入方式，并公开感觉更原生的 API。你可以通过使用注解（annotation）向编译器提供更多关于你 API 的信息来实现这一点。

例如，某个函数或方法可能使用了在 Swift 中感觉不自然的 C++ 命名约定。在这些情况下，你可以使用注解来重命名导入的函数、添加参数标签（argument label），或将 getter 和 setter 作为计算属性（computed property）导入。

注解还可以帮助解释高层次模式，例如引用语义（reference semantics），并允许你将某些类型作为 Swift 类（class）导入。

或者当 Swift 认为某个 API 不安全但实际上没问题时，纠正 Swift。

这些注解是一种强大的方式，可以向 Swift 正在导入的 API 传达信息。让我们找出示例 App 中使用的一些不同 API，并探索如何使用这些注解来帮助 Swift 以安全直观的方式导入我的 API。

现在我已经完成了照片选择器，我还想添加一个保存按钮，将编辑后的照片保存回我的照片库。

回到 Swift，我可以再查看一下我导入的所有 API。

首先，我需要收集要保存的照片。我可以使用 getImages 函数来实现。

getImages 函数返回一个 C++ vector（向量）。在调用这个方法之前，让我们了解一下 vector 在 Swift 中的运作细节。Swift 类型分为两类：值类型（value type）和引用类型（reference type）。在 Swift 中，结构体代表值类型，类代表引用类型。

默认情况下，C++ 类型在 Swift 中会作为值类型导入。

因此，Swift 会将 vector 作为一个行为类似于 Swift 结构体的值类型导入。vector 与任何其他 Swift 结构体之间的唯一区别在于，Swift 会使用类型的特殊成员（例如拷贝构造函数）来管理生命周期。这些拷贝构造函数通常执行深拷贝。因此，与仅在修改时才被拷贝的 Swift Array 不同，当 Swift 拷贝一个 vector 时，它会拷贝所有元素。

现在我有了一个图像的 vector，我可以在一个 for 循环中遍历这个 vector 来获取每个图像，将图像转换回 uiImage，并将图像保存到我的照片库。

这个 for 循环之所以有效，是因为 vector 有 begin 和 end 方法，所以 Swift 会自动将其作为集合（collection）导入。这种对 collection 的自动一致性使得 vector 可以轻松转换为 Swift Array，并提供了对 map 和 filter 等方法的访问。为了安全起见，使用这些 Swift 集合 API 非常重要，而不是使用不适合 Swift 安全模型的 C++ 迭代器 API。

使用这些 C++ 迭代器，很容易引入诸如生命周期问题或无效内存访问之类的 bug。另一方面，即使操作的是 C++ 集合，Swift 集合 API 也完全安全。

Swift 编译器会通过将不安全的 C++ API 标记为不可用（unavailable）并建议更安全的替代方案，来引导你使用这些更安全的 API。让我们回到我的 Swift App。有件事一直困扰着我。每次我使用 C++ImageEngine 时，它都提醒我这只是一个不安全的指针。实际上，在 Swift 和 C++ 中，这个类型总是以指针的形式使用。这是因为该类型具有所谓的“引用语义”。这意味着该类型旨在具有对象标识（object identity），拷贝不会生成独立的值，而是指向同一内存的共享引用。正如我之前提到的，Swift 类型分为两类：值类型和引用类型。Objective-C 也对值类型和引用类型有明确的区分，这使得将 Objective-C 类型映射到结构体和类变得容易。对于 C++ 来说，哪些类型属于哪一类并不那么明确，因为与 Swift 和 Objective-C 不同，C++ 在值类型和引用类型之间没有强区分。

因此，默认情况下，编译器会将所有内容作为值类型导入。但 Swift 也允许你通过在 C++ 代码中添加注解来选择将某些内容作为引用或类类型导入。

因此，我可以使用 SWIFT_SHARED_REFERENCE 特性（attribute）将 CxxImageEngine 映射到 Swift 类。这个特性意味着 Swift 将强制该类型始终以指针或引用的方式传递，并在 Swift 中简单地以该类型来表示这种间接性，而不是使用不安全的指针。

为了确保代码安全，Swift 会根据需要通过保留和释放引用来自动管理引用的生命周期。要启用这种引用计数（reference counting），你需要为 Swift 提供这两个保留和释放函数。让我们进入 C++ 的 ImageKit 头文件。

我可以导入 swift/bridging 来访问诸如 SWIFT_SHARED_REFERENCE 之类的注解。现在，我可以将此注解应用于该类型，并指定一个 Swift 可以调用的 retain 和 release 函数。太棒了！现在有一些 Swift 编译器错误，告诉我不再需要解引用指针了。

最后，还有一件事可以让这个 C++ API 在 Swift 中感觉更自然。在这里的 for 循环中，我调用了 getImages。像这样定义 getter 和 setter 在 C++ 中是一种相当常见的模式，但在 Swift 中感觉不太自然。为了让它在 Swift 中感觉更原生一点，我可以使用 swift/bridging 中的另一个注解。SWIFT_COMPUTED_PROPERTY 特性可以应用于 getter 和 setter，将这对方法映射到 Swift 的计算属性。让我们再次进入 C++ 头文件来应用这个注解。

现在，我可以通过在定义上执行辅助点击并选择我的 Swift 调用方来查找 getImages 方法的调用者，然后我可以将其重命名为简单的“images”。太棒了！现在让我们最后一次测试我们的 App。

我可以选择几张照片并将它们保存回我的相机胶卷。

太棒了！在这次演讲中，我只使用了两个注解来改善 API 的导入方式。但你可以在 C++ 头文件中使用许多其他注解。你只需导入 swift/bridging 即可访问它们。

要在 Xcode 15 中启用 C++ 互操作性，将 C++ and Objective-C Interoperability 模式从 C and Objective-C 更改为 C++ and Objective-C++。Swift 和 C++ 互操作性在所有 Apple 平台以及 Linux 和 Windows 上都受支持。C++ 是一种庞大而复杂的语言，我们希望根据你的反馈来改进我们导入 C++ API 和公开 Swift API 的方式。当我们改变 C++ API 的导入方式时，我们将创建新版本的互操作性。这意味着你可以选择何时采用这些新特性，从而让你有信心立即开始在开发中使用 C++ API。

如果你注意到任何问题或有任何建议，我们很乐意听取你的意见。请通过 Feedback Assistant 告诉我们。C++ 互操作性由一个 Swift 编译器工作组完全在开源社区中设计。该工作组由来自十多家公司和学校的工程师和学生组成。工作组编写了两份文档，定义了 Swift 和 C++ 互操作性的未来愿景，并将指导该功能随着时间的推移而演变。

你可以加入工作组并在论坛上参与讨论。只需前往 swift.org。

在 Swift 5.9 中，你可以自动、安全地使用你的 C++ API，且没有额外开销。你可以通过将新的 Swift 代码公开回 C++ 来逐步采用 Swift。你可以通过向编译器提供更多信息来改进和微调导入的 API。

感谢观看，祝你在所有 C++ 代码库中愉快地采用 Swift。
