---
title: 'SwiftUI 中的数据基础'
session_id: 10040
collection: wwdc2020
year: 2020
duration: '36:15'
topics: [Swift, System Services, 'SwiftUI & UI Frameworks']
group: H · 持久化与文件系统
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2020/10040/'
content_hash: 'sha256:c091885706511705'
translated: true
---

# SwiftUI 中的数据基础

<sub>WWDC2020 · 36:15 · Swift、System Services、SwiftUI & UI Frameworks</sub>

数据是任何 App 中复杂的一部分，但 SwiftUI 让从原型到产品都能确保顺畅、数据驱动的体验变得简单……

> [!note] 归档理由
> SwiftUI 数据流的所有权模型

## 相关资源

- [Model data](https://developer.apple.com/documentation/SwiftUI/Model-data)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10040/3/76E05CA6-5C92-45FC-8DB0-0009FC6D18F0/wwdc2020_10040_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2020/10040/3/76E05CA6-5C92-45FC-8DB0-0009FC6D18F0/wwdc2020_10040_sd.mp4?dl=1)
- [Use SwiftUI with UIKit](https://developer.apple.com/videos/play/wwdc2022/10072)
- [Demystify SwiftUI](https://developer.apple.com/videos/play/wwdc2021/10022)
- [Discover concurrency in SwiftUI](https://developer.apple.com/videos/play/wwdc2021/10019)
- [App essentials in SwiftUI](https://developer.apple.com/videos/play/wwdc2020/10037)
- [Introduction to SwiftUI](https://developer.apple.com/videos/play/wwdc2020/10119)
- [Stacks, Grids, and Outlines in SwiftUI](https://developer.apple.com/videos/play/wwdc2020/10031)
- [Structure your app for SwiftUI previews](https://developer.apple.com/videos/play/wwdc2020/10149)
- [What's new in SwiftUI](https://developer.apple.com/videos/play/wwdc2020/10041)
- [BookCard](https://developer.apple.com/videos/play/wwdc2020/10040/?time=129)
- [EditorConfig](https://developer.apple.com/videos/play/wwdc2020/10040/?time=215)
- [ProgressEditor](https://developer.apple.com/videos/play/wwdc2020/10040/?time=359)
- [CurrentlyReading](https://developer.apple.com/videos/play/wwdc2020/10040/?time=795)
- [BookView](https://developer.apple.com/videos/play/wwdc2020/10040/?time=936)
- [CurrentlyReading with isFinished](https://developer.apple.com/videos/play/wwdc2020/10040/?time=1070)
- [BookView with Toggle](https://developer.apple.com/videos/play/wwdc2020/10040/?time=1101)
- [CoverImageLoader](https://developer.apple.com/videos/play/wwdc2020/10040/?time=1198)
- [BookCoverView](https://developer.apple.com/videos/play/wwdc2020/10040/?time=1220)
- [ReadingListViewer (Bad)](https://developer.apple.com/videos/play/wwdc2020/10040/?time=1536)
- [ReadingListViewer (Good)](https://developer.apple.com/videos/play/wwdc2020/10040/?time=1599)
- [App-wide Source of Truth](https://developer.apple.com/videos/play/wwdc2020/10040/?time=1852)
- [SceneStorage](https://developer.apple.com/videos/play/wwdc2020/10040/?time=1963)
- [AppStorage](https://developer.apple.com/videos/play/wwdc2020/10040/?time=2029)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，欢迎来到 WWDC。

大家好，欢迎来到 SwiftUI 中的数据基础。我是 Curt Clifton，SwiftUI 团队的工程师。稍后我的朋友兼同事 Luca Bernardi 和 Raj Ramamurthy 也会加入。我们将在本次演讲中涵盖三个主要领域。我会先介绍 SwiftUI App 中数据流的入门，包括 State 和 Binding 等主题。然后 Luca 会讨论如何在这些想法的基础上设计 App 的数据模型。最后，Raj 会分享把数据模型集成到 App 中的技术。一路上，我们会讨论 SwiftUI 视图的生命周期，并分享几项让建模数据更容易的酷炫新功能。我们还会帮助你更深入地理解 Swift 中的值类型和引用类型如何与 SwiftUI 中的数据流交互。

我会演示 SwiftUI 中的一些基本数据流特性，以及每次创建新的 SwiftUI 视图时应该问自己的几个问题。Luca 非常喜欢读书俱乐部，他太投入了，以至于决定需要一个 App 来跟踪每个俱乐部正在读什么书，并为下次会议做笔记。我也喜欢阅读，觉得一起做这个 App 很有趣。

要开始，我想先为我正在读的一本书原型化一个视图。在 SwiftUI 中开始一个新视图时，我喜欢思考三个关键问题。

这个视图需要什么数据来完成它的工作？在这个例子中，视图需要书籍封面的缩略图、标题、作者名，以及我已读完的百分比。

视图将如何操作这些数据？这个视图只需显示数据，不改变它。

数据将从哪里来？这就是「真相来源（Source of Truth）」。在本次演讲的示例中，Luca、Raj 和我将使用这个徽章来标注真相来源。

最终，正如我们将看到的，真相来源的问题是你数据模型设计中最重要的问题。让我们构建这个视图，看看它的真相来源应该是什么。

那么这个视图需要什么数据来完成它的工作？book 值提供封面图片名、作者和标题。

progress 值提供完成百分比。

视图将如何操作这些数据？它只是显示数据，不改变它，所以这些可以是「let」属性。

数据将从哪里来？它将在 BookCard 被实例化时从父视图传入。

真相来源在视图层级更上方的某个地方。父视图在实例化 BookCard 时传入真正的数据。每次父视图的 body 执行时，都会实例化一个新的 BookCard。该实例只存在足够长的时间让 SwiftUI 渲染它，然后就消失了。

我们可以用图来可视化内部结构。左侧的方框表示构成这个 BookCard 的 SwiftUI 视图。

右侧的胶囊表示用于渲染视图的数据。我们会在整个演讲中回到类似的图。

接下来，我想看一个稍微有趣的视图。当我点按一本书时，App 会带我到这个屏幕，我可以在这里查看进度。我想添加一种更新进度的方式，并在点按「Update Progress」按钮时添加笔记。类似这样。

让我们看看父视图和这个表单（sheet）如何协同工作。

我们会聚焦于表单如何呈现。

当用户点按「Update Progress」按钮时，我们会调用 presentEditor 方法。它会改变某些状态，使表单出现。

这个视图需要什么数据来控制表单的呈现？我们需要一个布尔值来跟踪表单是否呈现，一个字符串来跟踪笔记，一个 Double 来跟踪进度。每当我有多个相关属性时，我喜欢把它们提取到自己的结构体中。

除了让 BookView 更可读之外，这种方法还有另外两个好处。我们获得了封装的所有好处。EditorConfig 可以维护其属性的不变式，并可独立测试。而且因为 EditorConfig 是值类型，EditorConfig 的任何属性（如 progress）的变化，都会表现为 EditorConfig 本身的变化。

我们的下一个问题是，视图将如何操作这些数据？当「Update」按钮被点按时，我们需要把 isEditorPresented 设为「True」，并把 progress 更新为当前进度。

因为我们把状态提取到了 EditorConfig 结构体中，可以让它负责这些更新，只需让 BookView 要求 EditorConfig 做这项工作。

然后，我们会给 EditorConfig 添加一个 mutating 方法，像这样。

数据将从哪里来？嗯，编辑器配置对这个视图是局部的。没有父视图可以把它传入，所以我们需要建立一个局部的真相来源。SwiftUI 中最简单的真相来源是 State。

当我们把这个属性标记为 State 时，SwiftUI 会接管管理其存储。让我们把它作为图来看。

我们再次有左侧这些方框表示的视图，以及右侧胶囊表示的数据。注意胶囊有粗边框。我用这个边框表示由 SwiftUI 为我们管理的数据。为什么这很重要？记住，我们的视图只短暂存在。SwiftUI 完成一次渲染通道后，结构体本身就会消失。

但因为我们把这个属性标记为 State，SwiftUI 会为我们维护它。下次框架需要渲染这个视图时，它会重新实例化结构体，并重新连接到现有存储。

接下来看看 ProgressEditor。

ProgressEditor 需要什么数据来完成它的工作？EditorConfig 中的所有数据。视图将如何操作这些数据？它需要改变它们，所以我们会使用 var。

数据将从哪里来？这是个有趣的问题。回到图。

让我们聚焦 BookView 和 ProgressEditor。假设我们只是把 EditorConfig 作为常规属性传给 ProgressEditor。

因为 EditorConfig 是值类型，Swift 会创建该值的新副本。ProgressEditor 对 note 或 progress 做的任何更改，只会改变这个新副本，而不是 SwiftUI 为我们管理的原始值。所以这不允许 ProgressEditor 与 BookView 通信。

接下来怎么办？啊！如果给 ProgressEditor 自己的 State 属性呢？这似乎可能是我们想要的。它告诉 SwiftUI 为我们管理一个新的数据片段。

可惜，这也不对。记住，State 会创建新的真相来源。ProgressEditor 做的任何更改都会作用于它自己的 state，而不是与 BookView 共享的那个。我们想要单一的真相来源。

我们需要一种方式，把 BookView 的真相来源的写访问权共享给 ProgressEditor。在 SwiftUI 中，共享对任何真相来源的写访问权的工具是 Binding。BookView 创建一个指向 EditorConfig 的 Binding——对现有数据的读写引用——并把这个引用共享给 ProgressEditor。

通过这个 Binding 更新 EditorConfig，ProgressEditor 就是在改变 BookView 正在使用的同一状态。SwiftUI 会注意到 EditorConfig 的变化。它知道 BookView 和 ProgressEditor 都依赖于这个值，因此知道在值变化时重新渲染这些视图。

ProgressEditor 需要把数据传回 BookView。

我们刚看到 Binding 是完成这项任务的正确工具。

调用中的美元符号从 State 创建一个 Binding，因为 State 属性包装器的投影值是一个 Binding。

Binding 属性包装器在 ProgressEditor 和 BookView 中的 EditorConfig state 之间创建数据依赖。许多内置的 SwiftUI 控件也接受 Binding。例如，我们笔记中使用的新 TextEditor 控件接受一个指向 String 值的 Binding。使用美元符号投影值访问器，我们可以获得 EditorConfig 中 note 的新 Binding。

SwiftUI 让我们可以从现有 Binding 构建新的 Binding。记住，Binding 不仅用于 State。

这就是 SwiftUI 数据流的入门。记住在添加 SwiftUI 视图时问自己三个问题：这个视图需要什么数据？它将如何使用这些数据？数据从哪里来？你可以对不变化的数据使用属性。对视图拥有的瞬态数据使用 State。对由另一个视图拥有的可变数据使用 Binding。

现在我想把话题交给 Luca，深入设计你的数据模型，因为 State 并不是全部。

谢谢你，Curt。大家好，我是 Luca。我的同事 Curt 刚刚描述了如何使用 State 和 Binding 驱动 UI 变化，以及这些工具是快速迭代视图代码的好方法。

但 State 设计用于视图局部的瞬态 UI 状态。在这一节中，我想把你的注意力转向设计模型，并解释 SwiftUI 提供的所有工具。

通常，在你的 App 中，你使用与 UI 分离的数据模型来存储和处理数据。

这时你到达一个关键点，需要管理数据的生命周期，包括持久化和同步、处理副作用，以及更普遍地与现有组件集成。这时你应该使用 ObservableObject。先看看 ObservableObject 是如何定义的。

它是一个类约束协议，意味着只能由引用类型采用。

它有一个单一要求：objectWillChange 属性。objectWillChange 是一个 Publisher，顾名思义，ObservableObject 协议的语义要求是：publisher 必须在任何变更应用到对象之前发出。默认情况下，你得到一个开箱即用的 publisher。但如果你需要，可以提供自定义 publisher。例如，你可以使用计时器的 publisher，或使用观察现有模型的 KVO publisher。

既然我们已经看过协议，让我们看看理解 ObservableObject 的心智模型。

当你的类型符合 ObservableObject 时，你正在创建新的真相来源，并教导 SwiftUI 如何对变化做出反应。

换句话说，你正在定义视图渲染 UI 和执行逻辑所需的数据。

SwiftUI 会在你的数据和视图之间建立依赖，这里用蓝色方框表示。

SwiftUI 使用这个依赖自动保持视图一致，并显示数据的正确表示。

我们喜欢把 ObservableObject 视为你的数据依赖表面。这是模型中向视图暴露数据的部分，但不一定是完整模型。

如果你这样看待 ObservableObject，它不必完全就是你的数据模型。你可以把数据与其存储和生命周期分离。你可以用值类型建模数据，并用引用类型管理其生命周期和副作用。例如，你可以有一个集中的 ObservableObject 管理整个数据模型，并由所有视图共享，如图所示。这给你一个所有逻辑的单一位置，便于推理 App 中所有可能的状态和变更。或者你可以专注于 App 的一部分，使用多个 ObservableObject，它们提供对数据模型的特定投影，并设计为只暴露所需的数据。当你有复杂数据模型，并想为 App 的一部分提供更紧致的失效时，这更好。让我们回到我们正在构建的 App，看看如何应用刚讨论的内容。让我们把 Curt 之前工作的视图带回来。这是允许我更新书中进度并添加一些在阅读过程中发现的有趣点的笔记的视图。

Curt 聚焦于进度表单的数据。让我们看看这个视图还需要的其余数据，以及如何使用 ObservableObject 添加丰富功能，如把数据存储到磁盘或与 iCloud 同步。

我们可以创建一个名为 CurrentlyReading 的新类，符合 ObservableObject，保存一本书及其阅读进度。这是我们暴露给视图以呈现数据并响应变化的模型部分。具体书籍不会改变，所以我们可以把这个属性设为 let。我们希望能够更新进度并让 UI 对其反应。只需用 @Published 属性包装器标注 progress 属性即可。让我们看看 @Published 如何工作。

@Published 是一个属性包装器，通过暴露 Publisher 使属性可观察。

对于大多数模型，你只需符合 ObservableObject，对可能变化的属性添加 @Published，就完成了。

就这么简单，再也不用担心让数据与视图保持同步。

当你将 @Published 与默认的 ObservableObject publisher 一起使用时，系统会在值变化之前自动发布以执行失效。

对于高级用例，@Published 的投影值是一个 Publisher，你可以用它构建响应式流。

让我们重新审视设计数据模型时应该问的三个问题。

使用 ObservableObject 时，回答第二个问题相当直接：我们总是假设可变性。

现在让我们看看如何回答 ObservableObject 的其他两个问题。我们已经看到如何定义模型，但现在需要在视图中使用它。

SwiftUI 提供三种属性包装器，你可以在视图中使用它们来创建对 ObservableObject 的依赖。

这些工具是 ObservedObject、今年新增的 StateObject，以及 EnvironmentObject。先看看 ObservedObject。ObservedObject 是一个属性包装器，你可以用它标注视图中持有符合 ObservableObject 类型的属性。使用它会通知 SwiftUI 开始跟踪该属性作为视图的依赖。

你正在定义这个视图完成工作所需的数据。

这是最简单、最灵活的工具。ObservedObject 不拥有你提供给它的实例的所有权，管理其生命周期是你的责任。让我们看看如何在 App 中使用它。这里我有 BookView，显示书籍以及我到目前为止记录的所有进度。从这个屏幕，我还可以更新这本书的进度。我们可以添加一个 currentlyReading 类型的属性，并用 @ObservedObject 属性包装器标注它。分配给这个属性的实例将成为这个视图的真相来源。

现在，我们可以在视图 body 中读取模型。SwiftUI 保证视图始终是最新的。你不必写任何代码，也不必管理任何事件来保持视图同步。你只需声明式地描述如何从数据构建视图，SwiftUI 会处理其余一切。我的同事 Raj 会更详细地介绍 SwiftUI 更新生命周期，但我想带你幕后看看 SwiftUI 为你做了什么。

每当你使用 ObservedObject 时，SwiftUI 会订阅该特定 ObservableObject 的 objectWillChange。现在，每当 ObservableObject 即将变化时，所有依赖它的视图都会更新。我们经常被问到的一个问题是「为什么是『will』变化？为什么不『did』变化？」原因是 SwiftUI 需要知道某事即将变化，以便把所有变化合并成单次更新。但我们如何产生变更呢？SwiftUI 提供的许多 UI 组件接受指向某块数据的 Binding，而更早的演讲中你已经看到如何设计组件来做到这一点。这是 SwiftUI 的基本设计原则之一。接受 Binding 允许组件对一块数据进行读写访问，同时保留单一的真相来源。

Curt 已经向你展示如何从 State 派生 Binding。对 ObservableObject 做同样的事同样容易。

你可以通过对 ObservableObject 上的任何值类型属性添加美元符号前缀并访问该属性，来获得 Binding。让我们在读书俱乐部 App 中看一个具体示例。

读书的一大满足感是读完最后一章，我想用一个盛大手势来标记这个事件。我想不出比点按 Toggle 说「我读完这本书了」更好的方式。第一件事是改变模型。我们只需添加新属性「isFinished」，并用 @Published 标注，这样每当它的值变化时，UI 就会反映变化。让我们看看如何改变 BookView 来添加这个功能。我可以添加一个带漂亮标签的 Toggle，允许我标记这本书为已完成。Toggle 期望一个 Binding，以便显示当前状态，并在用户点按它时改变值。我们只需在 currentlyReading 前加美元符号前缀并访问「isFinished」属性，就能提供 Binding。现在，每当用户与 Toggle 交互，currentlyReading 就会更新，SwiftUI 会更新所有依赖它的视图。例如，在这个视图中，当我们读完这本书时，更新进度的按钮会被禁用。在整个 App 中，我们展示这些精美的封面图，想在它们即将显示在屏幕上前从网络异步加载。

它们是昂贵的资源，所以我们只想在视图可见时保持它们存活。

更普遍地说，我们注意到你通常确实希望把 ObservableObject 的生命周期与视图绑定，就像 State 一样。

如果你还记得，ObservedObject 不拥有其 ObservableObject 的生命周期，所以我们想提供一个更符合人体工程学的工具。

这个工具是今年新增的 StateObject。

当你用 StateObject 标注属性时，你提供一个初始值，SwiftUI 会在首次运行 body 之前实例化该值。SwiftUI 会为视图的整个生命周期保持对象存活。

这是 SwiftUI 的很棒的新增功能，让我们看看如何在实践中使用它。让我们创建一个 CoverImageLoader 类，按名称加载特定图片。这里我只展示这个类的骨架，而不是如何让它成为 ObservableObject 并用 @Published 标注持有图片的属性。

一旦我们有了图片，SwiftUI 会自动更新视图。

现在在我们的视图中，我们可以使用 CoverImageLoader，只需用 StateObject 标注该属性。CoverImageLoader 不会在视图创建时实例化。相反，它会在 body 运行前实例化，并在视图的整个生命周期内保持存活。当视图不再需要时，SwiftUI 会按预期释放 CoverImageLoader。你不再需要摆弄 onDisappear。相反，你可以使用 ObservableObject 的生命周期来管理资源。在 SwiftUI 中，视图非常廉价。我们非常鼓励你把它们作为主要封装机制，并创建简单、可理解、可复用的小视图。

这意味着你可能会得到深而宽的视图层级，如图所示。从数据流的角度看，你可能需要在视图层级高处创建一个 ObservableObject，并把同一实例传给许多视图。

有时你需要在遥远的子视图中使用 ObservableObject，把它向下传给不需要数据的视图可能很麻烦，涉及大量样板代码。幸运的是，我们有 EnvironmentObject 来解决这个问题。EnvironmentObject 既是视图修饰器也是属性包装器。你在想要注入 ObservableObject 的父视图中使用视图修饰器。在所有想要读取该特定 ObservableObject 实例的视图中使用属性包装器。框架会负责把值传递到需要的地方，并且只在读取处跟踪它作为依赖。

在演讲的这一部分，我们已经看到如何使用 ObservableObject 设计模型，以及 SwiftUI 提供的所有基本原语，你可以用它们构建最适合你需求的架构。

我们已经看到如何在视图和一块数据之间创建依赖，如何用新的 StateObject 属性包装器把 ObservableObject 的生命周期绑定到视图，最后如何用 EnvironmentObject 方便地在视图层级中流动 ObservableObject。现在我把它交给 Raj。他会深入 SwiftUI 的生命周期及其与性能的关系、如何处理副作用，以及一些令人兴奋的新工具。谢谢大家，祝 WWDC 愉快。Raj？谢谢，Luca。你已经学会了 SwiftUI 中数据的入门，以及如何设计出色的模型。现在我想告诉你如何设计以获得最佳性能，以及选择真相来源时的进一步考虑。首先，让我们谈谈视图及其在 SwiftUI 系统中的角色。视图只是 UI 一块的定义。SwiftUI 使用这个定义来创建适当的渲染。

SwiftUI 管理视图的身份和生命周期。而且因为视图定义了一块 UI，它们应该轻量且廉价。在读书俱乐部 App 中，就像每个 App 一样，屏幕上的一切都是视图。

注意视图的生命周期与定义它的结构体的生命周期是分开的。

你创建的符合 View 协议的结构体实际上生命周期非常短。SwiftUI 用它来创建渲染，然后它就消失了。

让我们用图来说明让视图轻量的重要性。

这个图显示 SwiftUI 更新生命周期。从顶部开始，我们有你的 UI。逆时针移动，一个事件进来，导致某个闭包或动作运行。那然后导致真相来源的变更。

然后一旦我们改变了真相来源，我们会得到视图的新副本，用它来产生渲染。那个渲染就是你的 UI。

这只是基础。我们稍后会回到这个图。现在让我们简化它。再简化一点。

啊。好多了。

顾名思义，这个生命周期是一个循环。它在 App 运行期间会重复很多次。

这个循环对性能也非常重要……

理想情况下，循环像这样顺畅地进行。

但如果在这些点中有任何昂贵的阻塞工作，App 的性能就会受损。

我们称之为慢更新。它意味着你可能会掉帧，或者 App 可能挂起。

那么如何避免慢更新？嗯，避免慢更新的第一件事是确保视图初始化廉价。

视图的 body 应该是纯函数，没有副作用。这意味着你只需创建视图描述并返回。没有派发，没有其他工作。只需创建一些视图然后继续。

避免对 body 何时以及多频繁被调用做假设。记住，SwiftUI 有时相当智能，这意味着它可能不会按你的假设调用 body。

为了说明 body 廉价的重要性，让我们看一个例子。

这里是一个我们 Currently Reading 列表可能样子的简化示例。在 ReadingListViewer 中，我们会把 body 定义为带 ReadingList 的 NavigationView。然后在 ReadingList 中，我们会使用 ObservedObject 来生成数据。

这看起来相当合理，但其实隐藏着一个 bug。你能看到吗？事实证明，每当 ReadingListViewer 的 body 被创建时，你都会招致 ReadingListStore 的重复堆分配，这可能导致慢更新。

记住，你的视图结构体没有定义的生命周期，所以当你这样写时，你实际上每次都会创建对象的新副本。这样的重复堆分配可能昂贵且缓慢。它还会导致数据丢失，因为对象每次都会被重置。

好的，我们已经识别了问题，但如何修复？嗯，过去你必须在其他地方创建模型并传入。但直接内联做这件事不是很棒吗？我很高兴地告诉你，今年我们有一个工具来解决这个问题，叫做 StateObject，正如 Luca 早些时候解释的，StateObject 让 SwiftUI 在正确的时间实例化你的 ObservableObject，这样你就不会招致不必要的堆分配，也不会丢失数据。

这意味着你可以获得出色的性能和正确性。

有一点需要注意：我们在这里声明了新的真相来源，所以让我们把徽章贴上。

好的，让我们再次把图带回来。

并增强。

很好。有一点需要注意：左上角有多个事件来源。你的 App 可能对由用户交互生成的事件做出反应，例如点按按钮，也可能对 publisher 触发做出反应，如计时器或通知。无论触发事件的是什么，循环仍然是相同的。我们会改变真相来源，更新视图，然后产生新的渲染。这些触发器被称为事件来源。它们是视图变化的驱动者。如我提到的，一个好例子是用户交互或 publisher，如计时器。今年新增，我们有新的方式对环境和绑定的变化做出反应，以及处理 URL 和用户活动的新方式。

这些修饰器中的每一个都接受一个参数，如 publisher 或要比较的值，以及一个闭包。

SwiftUI 会在正确的时间运行闭包，帮助你避免慢更新并保持 body 廉价。不过注意，SwiftUI 会在主线程运行这些闭包，所以如果你需要做昂贵的工作，考虑派发到后台队列。

我们今天不会详细讨论这些，但我鼓励你查看文档以了解更多信息。

这就是关于如何避免慢更新以及如何设计以获得出色性能的内容。接下来，让我们把那三个问题带回来。

所以我们基本上已经涵盖了如何解决前两个问题，但第三个并不那么容易。

当你回答这个问题时，你是在做关于将要使用的真相来源的决定。这是一个难题。

这里没有唯一正确的答案，为了帮助你，我想介绍一些考虑因素。

一个重要的问题是，谁拥有数据？是使用数据的视图，还是该视图的祖先？也许甚至是 App 的另一个子系统。

这里有一些指导：如前所述，与共同祖先共享数据。另外，优先使用 StateObject 作为视图拥有的 ObservableObject 真相来源。最后，考虑把全局数据放在 App 中。我们接下来会介绍这个。

现在让我们谈谈数据生命周期。我们会介绍把数据生命周期绑定到视图、场景和 App。关于 SwiftUI 场景和 App 的更多信息，请参考「SwiftUI 中的 App 基础」session。

首先，从视图开始。

正如我们整个演讲向你展示的，视图是把数据生命周期绑定到的好工具，我们讨论的所有属性包装器都与视图配合。你可以使用 State 和 StateObject 属性包装器把数据生命周期绑定到视图生命周期。接下来，谈谈场景。

因为 SwiftUI 的每个场景都有独立的视图树，你可以把重要的数据挂载到树的根部。例如，你可以把真相来源放在窗口组内的视图上。

这样做时，窗口组创建的每个场景实例都可以拥有自己的、独立的真相来源，作为底层数据模型的窗口。这在多窗口时很好用。

如你所见，这两个场景有独立的 UI 状态，表示相同的基础数据。所以现在 Luca 可以同时参加两个在线读书俱乐部。接下来，谈谈 App。

App 是今年 SwiftUI 中强大的新工具，允许你只用 SwiftUI 编写整个 App。但 App 的好处是，你可以在 App 中使用 State 和其他真相来源，就像在视图中一样。让我给你看一个例子。

这里，我们将通过使用 StateObject 属性包装器为整个 App 创建全局书籍模型。每当模型变化时，App 的所有场景，以及它们的所有视图，都会更新，通过这样写，我们创建了 App 范围的真相来源。考虑在哪里放置真相来源时，如果它表示真正的全局数据，你可能想把它放在 App 中。

数据的生命周期很重要，但该生命周期绑定到其真相来源的生命周期，而在所有前面的示例中，我们使用了 State、StateObject 和常量等工具。

但这些有限制，即它们绑定到进程生命周期，这意味着如果你的 App 被终止或设备重启，State 不会回来。

为了帮助解决这个问题，今年新增，我们引入了 Storage。

它们有扩展的生命周期，并自动保存和恢复。注意，这些不是你的模型。相反，它们是轻量存储，你与模型一起使用。

让我们先看看 SceneStorage。

SceneStorage 是一个按场景作用域的属性包装器，读写完全由 SwiftUI 管理的数据。它只能从视图内部访问，这使它成为存储关于 App 当前状态的轻量信息的绝佳候选。让我们看一个例子。

这是前面的读书俱乐部 App，两个场景并排。使用 SceneStorage 时第一件事是思考你真正需要恢复什么。在这种情况下，我们只需要保存和恢复选择。书籍名、进度和笔记都存储在模型中，所以不需要保存和恢复它们。让我们跳到代码。

这里你可以看到我们如何使用 SceneStorage 保存和恢复选中状态。我们会传一个键，它必须对我们存储的数据类型唯一。然后我们可以像使用 State 一样使用它。SwiftUI 会自动为我们保存和恢复值。

而且因为这表现得像 State，我们实际上在这里声明了新的真相来源，这次是场景范围的真相来源。

现在，如果设备重启，或系统需要回收支持场景的资源，数据将在下次启动时可用，允许 Luca 从上次离开的地方继续他的读书俱乐部活动。既然你已经看到 SceneStorage 的实际使用，我想讨论 AppStorage。这是 App 作用域的全局存储，使用 UserDefaults 持久化。它可从任何地方使用，所以你可以从 App 内部或视图内部访问它。AppStorage 与 UserDefaults 一样，非常适合存储小块数据，如设置。

在我们的读书俱乐部 App 中，我们还决定引入一些设置。

让我们看看如何使用 AppStorage 来完成这件事。

在我们的设置视图中，我们只需添加 AppStorage 属性包装器并给它一个键。默认情况下，它使用标准 user defaults，但如果你需要可以自定义。

更多信息请参考文档。

在这种情况下，我们为这里的两个设置各设置一个 AppStorage。我们给它们各自的唯一键，因为它们是独立的数据片段。使用 SceneStorage 和 AppStorage 时，重要的是不同的数据片段要有不同的键。就像其他属性包装器一样，这也是真相来源，这意味着我们可以获得它的绑定，例如用于 Toggle。现在，每当数据变化，它都会自动保存和恢复到 user defaults。

今天我们已经看到各种用于进程生命周期和扩展生命周期的工具，你使用这些工具中的每一个来存储 UI 级别的状态。对于存储类型，请注意不要用它们存储所有东西，因为持久化不是免费的。我还想指出一个工具，那就是 ObservableObject。

我们把 ObservableObject 设计得非常灵活，所以你可以用它实现高度自定义的行为，例如把数据由服务器或其他服务支持。这些工具共同构成一个家族，给你高度的自由来选择最适合你需求的方案。

今天我们已经看到很多工具及其用法，但主要收获是没有放之四海而皆准的工具。每个都有自己的特性，所以典型 App 会使用多种工具。我们在读书俱乐部 App 中就是这样做的。我们用 State 处理按钮和进度视图，用 StateObject 处理 currentlyReading 模型，用 SceneStorage 处理选择，用 AppStorage 处理设置。思考数据的属性以及使用正确的真相来源很重要，你也应该尽量限制真相来源的数量以减少复杂性。最后，利用绑定作为构建可复用组件的方式。记住，绑定完全不知道其真相来源是什么，这使它们成为构建干净抽象的强大工具。既然你已经学会了基础，现在是时候构建出色的模型了。谢谢。

祝 WWDC 愉快。
EOF
echo done