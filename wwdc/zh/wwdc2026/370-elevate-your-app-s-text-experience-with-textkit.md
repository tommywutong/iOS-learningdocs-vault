---
title: 用 TextKit 提升 App 的文本体验
session_id: 370
collection: wwdc2026
year: 2026
duration: '23:46'
topics: [App Services, 'SwiftUI & UI Frameworks']
group: E · UIKit/SwiftUI 渲染与 UI 性能
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2026/370/'
content_hash: 'sha256:d9720df41ff5e54e'
translated: true
---

# 用 TextKit 提升 App 的文本体验

<sub>WWDC2026 · 23:46 · App Services、SwiftUI & UI Frameworks</sub>

了解如何将内置文本视图的便捷性与 TextKit 的控制力相结合。我们将展示新 API 如何让……变得简单。

> [!note] 归档理由
> TextKit 最新形态

## 章节

- [Introduction](/videos/play/wwdc2026/370/?time=0)
- [TextKit architecture](/videos/play/wwdc2026/370/?time=189)
- [What's new in TextKit](/videos/play/wwdc2026/370/?time=557)
- [Extending framework text views](/videos/play/wwdc2026/370/?time=687)
- [Example: Code editor with line numbers](/videos/play/wwdc2026/370/?time=778)
- [Example: Collapsible recipe sections](/videos/play/wwdc2026/370/?time=1072)
- [Text attachments and view provider reuse](/videos/play/wwdc2026/370/?time=1196)
- [Next steps](/videos/play/wwdc2026/370/?time=1380)

## 相关资源

- [Introduction](https://developer.apple.com/videos/play/wwdc2026/370/?time=0)
- [TextKit architecture](https://developer.apple.com/videos/play/wwdc2026/370/?time=189)
- [What's new in TextKit](https://developer.apple.com/videos/play/wwdc2026/370/?time=557)
- [Extending framework text views](https://developer.apple.com/videos/play/wwdc2026/370/?time=687)
- [Example: Code editor with line numbers](https://developer.apple.com/videos/play/wwdc2026/370/?time=778)
- [Example: Collapsible recipe sections](https://developer.apple.com/videos/play/wwdc2026/370/?time=1072)
- [Text attachments and view provider reuse](https://developer.apple.com/videos/play/wwdc2026/370/?time=1196)
- [Next steps](https://developer.apple.com/videos/play/wwdc2026/370/?time=1380)
- [Enriching your text in text views](https://developer.apple.com/documentation/UIKit/enriching-your-text-in-text-views)
- [TextKit](https://developer.apple.com/documentation/AppKit/textkit)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/370/5/f61dbe38-7302-451a-b3ab-9851d5746315/downloads/wwdc2026-370_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2026/370/5/f61dbe38-7302-451a-b3ab-9851d5746315/downloads/wwdc2026-370_sd.mp4?dl=1)
- [Enhance the accessibility of your reading app](https://developer.apple.com/videos/play/wwdc2026/219)
- [What's new in TextKit and text views](https://developer.apple.com/videos/play/wwdc2022/10090)
- [Meet TextKit 2](https://developer.apple.com/videos/play/wwdc2021/10061)
- [NSTextViewportRenderingSurface conformance](https://developer.apple.com/videos/play/wwdc2026/370/?time=587)
- [NSTextViewportRenderingSurfaceKey and NSMapTable](https://developer.apple.com/videos/play/wwdc2026/370/?time=625)
- [UITextView/NSTextView in SwiftUI via ViewRepresentable](https://developer.apple.com/videos/play/wwdc2026/370/?time=759)
- [ContainerView with TextView and line number view](https://developer.apple.com/videos/play/wwdc2026/370/?time=813)
- [Three NSTextViewportLayoutControllerDelegate overrides](https://developer.apple.com/videos/play/wwdc2026/370/?time=882)
- [startingLineNumber(for:) using enumerateTextElements](https://developer.apple.com/videos/play/wwdc2026/370/?time=959)
- [DidLayout: convert frames to viewport coordinates](https://developer.apple.com/videos/play/wwdc2026/370/?time=1022)
- [Draw line numbers in ContainerView closure](https://developer.apple.com/videos/play/wwdc2026/370/?time=1036)
- [Collapsible sections: full TextView class](https://developer.apple.com/videos/play/wwdc2026/370/?time=1162)
- [Text attachment view provider reuse policy](https://developer.apple.com/videos/play/wwdc2026/370/?time=1326)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好，欢迎观看"用 TextKit 提升 App 的文本体验"。我是 Tarun Uday，TextKit 团队的工程师。

TextKit 是 Apple 新一代文本引擎，也是所有 Apple 平台上文本布局与渲染的基础。

SwiftUI、UIKit 和 AppKit 中的文本控件都使用 TextKit 来布局和渲染文本内容。在这段视频里，我想讨论我们从开发者那里听到一段时间的问题：便捷性与控制力之间的张力，以及我们为解决它而构建的新 API。

如果你在 Apple 平台上构建文本编辑体验，有两条路可走。第一条是使用框架文本视图。也就是 AppKit 中的 NSTextView、UIKit 中的 UITextView，以及 SwiftUI 中的 TextEditor。

使用这些视图，你免费得到大量功能。

文本输入、选择、辅助功能、撤销与重做、听写、内联预测等等。这些文本视图内部使用 TextKit，但内部实现大多被隐藏。你对文本如何绘制、视口如何管理其视觉元素的自定义能力有限。

第二条路是把 TextKit 作为文本引擎，直接在视图或图层中渲染文本。我们把这种视图称为自定义文本视图，以区别于预封装的框架文本视图。你搭建一个 NSTextLayoutManager，在自己的视图或图层上实现视口布局，并自行处理所有渲染。

构建自定义文本视图时，你对存储、布局和视口布局过程拥有完全控制，但要放弃框架文本视图提供的所有功能。从零开始构建达到生产质量的文本编辑体验工作量很大。然而在某些场景下，在框架文本视图的便捷性与自定义文本视图的控制力之间做选择很困难。今天我们将看看如何兼得两者。

若想深入了解 TextKit 架构与自定义文本视图，请观看 WWDC21 的"认识 TextKit 2"。若想了解框架文本视图如何采用 TextKit，请观看 WWDC22 的"TextKit 与文本视图的新变化"。虽然本讲是自成一体的，但这两个场次能为你今天的内容打下更深的基础。

我将先回顾 TextKit 的架构。之后再谈我们为 TextKit 引入的一些新 API。

最后，我将用一些示例展示扩展文本视图的新方式。

理解 TextKit 架构对于打造出色的自定义文本体验至关重要。我们从这里开始。

TextKit 使用四层架构进行文本渲染。

最底层是文本存储层。它封装了所有要渲染的文本数据。

布局层位于文本存储之上。负责把文本拆分成用于渲染的块。

再上一层是视口层。它跟踪布局中哪些块可见。

最顶层是视图层。文本在你的 App 中就出现在这里。

存储、布局和视口层在所有 Apple 的 UI 框架间共享。你可以用这些共享层在 UI 框架提供的任何视图或视图状可绘制视觉元素上渲染文本。

接下来我会介绍每层如何工作。理解构成每层的各部分，你就能自定义 TextKit，在 App 中创造独特体验。

为此，我将以在自定义文本视图中渲染一段长 NSAttributedString 为例。文本内容存储负责把这段带属性字符串拆成段落。在本例中，文本内容存储为底层带属性字符串的每个段落创建 NSTextParagraph 对象。NSTextContentStorage 和 NSTextParagraph 是与 NSAttributedString 配合工作的具体类型。

如果你有不同类型的后备存储，可以编写对应抽象类 NSTextContentManager 和 NSTextElement 的子类。

好了，这就是文本存储层。继续这个例子，下一步看布局。

文本内容存储把带属性字符串拆成段落后，NSTextLayoutManager 负责准备段落以供渲染。文本布局管理器高效地测量组成所表示文本的字形度量，并动态创建存储该段落计算布局信息的 NSTextLayoutFragment。

这些对象是不可变的。这意味着如果段落被编辑，NSTextParagraph 和 NSTextLayoutFragment 会被重建。例如，我把单词 sandwich 替换为 slider，该段落会创建新的 NSTextParagraph，并创建带新布局信息的对应新 NSTextLayoutFragment。

接下来我将展示视口与视图这两个顶层如何协同高效渲染海量文本。

文本视图是动态大小的视图，文本布局和绘制进去时会增长，文本移除时会缩小。视口是文本视图中用户可见的部分。TextKit 的所有工作都围绕视口进行，只渲染用户能看到的文本。这意味着你使用 TextKit 时的核心任务之一，是基于视口提供的布局信息增强用户交互。为便于把布局片段渲染到文本视图上，TextKit 提供了一个专门的类：NSTextViewportLayoutController。

NSTextViewportLayoutController，我就叫它视口控制器。

视口控制器与文本布局管理器、文本视图协作，高效布局与渲染文本段落。让我展示一下。

文本视图了解视口相对于整个文档的滚动位置和大小，并把这一信息提供给视口控制器。

视口控制器随后请求文本布局管理器提供所有与视口相交的布局片段，并把它们发送给文本视图进行渲染。视口控制器协调的这一过程会在视口状态的任何变化时重复。也就是任何滚动、编辑或选择事件，这被称为视口布局过程。

视口布局过程是 TextKit 高性能布局与渲染的核心。就这样！要构建你自己的自定义文本视图，实例化 NSTextContentStorage 和 NSTextLayoutManager，并使用 NSTextViewportLayoutController 把文本渲染到 UI 框架提供的视图（其委托）上。

虽然我称文本视图为"视图"，但它可以是 UI 框架提供的任何可绘制视觉元素。例如在 UIKit 中，你可以选择 UIView 或 CALayer 把文本渲染到自定义文本视图中。UI 框架也会为你的便捷打包自带类型的文本视图，使用这些 TextKit 层。

在 UIKit 中，你可以用 UITextView 实现开箱即用的文本编辑体验。AppKit 和 SwiftUI 有类似视图。

有时框架文本视图可能无法满足你的 App 需求。也许你在构建一个对同一文本有多种呈现方式的 App。

把多个文本布局管理器连接到同一个文本内容存储，一个视图中的编辑会通过共享的内容存储传播到另一个视图。

这意味着你可以在两个不同视图中呈现同一文档，它们会自动保持同步。

借助 TextKit 提供的灵活性，你可以用适合自己场景的分层配置构建自定义文本视图。现在我们来看看 TextKit 中引入的一些新 API。上一节我们谈到了把布局片段中的文本渲染到视口——这就是视口布局过程。在 2027 年版本之前，我们无法引用 TextKit 中文本渲染到的目标视图。这意味着虽然 TextKit 帮你跟踪布局片段，但不会帮你跟踪它们被绘制到的视图。

首先认识 NSTextViewportRenderingSurface。

这是一个新协议，表示视口内可绘制的视觉元素。真正渲染布局片段文本的视图，提供一个通用抽象以便协作。你可以让 UIView、NSView 或 CALayer 遵循这个协议，并在视口控制器的委托方法中用它来跟踪视口中可见的视图。

渲染表面附带一个配套的键协议 NSTextViewportRenderingSurfaceKey。渲染表面键是任何能唯一标识渲染表面的类，跨越视口布局过程周期，例如 NSTextLayoutFragment。

这意味着你可以用 NSTextLayoutFragment 作为键，在映射表或字典中缓存渲染表面。

视口布局过程在内部大量使用渲染表面键到渲染表面的映射。

你可以在视口布局过程中通过 renderingSurfaceFor 委托方法把渲染表面赋给一个键。

这些在视口布局过程开始时被清空。

你可以在 didLayout 过程中使用视口控制器的 renderingSurfaceFor 方法查询特定键的渲染表面。

这些新 API 让你在使用 TextKit 构建自定义文本视图时能使用并自定义自己的渲染表面。

既然我们已经了解了 TextKit 在 2027 年版本中的工作方式，接下来看看支撑 Apple 默认文本体验的文本视图如何工作。UIKit 的 UITextView 和 AppKit 的 NSTextView 支撑着 Apple 平台上成千上万的长文本体验，包括"信息"、TextEdit、"备忘录"和 Journal。

如果你有 SwiftUI App，实现长文本体验最便捷的方式是使用 TextEditor。但你也可以通过 ViewRepresentable 在 App 中包含 UITextView 或 NSTextView。

让我展示一下。

首先我创建一个名为 MyTextView 的视图。

我用 ViewRepresentable 填充 MyTextView 的 body，命名为 TextViewRepresentable。

TextViewRepresentable 在 macOS 上是有条件地成为 NSViewRepresentable，否则是 UIViewRepresentable。

在 NSViewRepresentable 内部，你只需在 makeNSView 方法中调用 NSTextView 或其子类的初始化器。

在 UIViewRepresentable 中对 UITextView 做同样的事。你可以在随附的示例 App 中看到具体例子。

为了展示如何使用 UITextView 的 TextKit 钩子扩展它，我将创建几个不同的示例 App。

第一个示例中，我想为 iPad 构建一个代码编辑器，以便离开 Mac 时也能快速写代码。

我从 UITextView 的子类开始，初始化它并把字体设为等宽系统字体。

不错，开始有了！但如果看不到行号，这并不是很好的代码编辑体验。我们开始构建它。

首先创建一个能容纳 TextView 和 lineNumberView 的视图，命名为 ContainerView。

ContainerView 持有 UITextView 子类和用于显示行号的 UIView。

我有了基本设置，现在想要在视口变化时重新计算并显示视口中布局片段的 NSTextParagraph 索引。为此，文本视图需要在视口控制器完成一次视口布局过程时收到通知。

现在这成为可能！从 2027 年版本开始，UITextView 和 NSTextView 现在遵循 NSTextViewportLayoutControllerDelegate。

这意味着你可以子类化 UITextView 或 NSTextView 并重写委托方法来添加自己的行为。接下来我就这么做！在我的 TextView 子类中，我将重写委托方法。

首先重写 WillLayout 方法做一些设置工作。细节稍后展示。重写 configureRenderingSurface 方法捕获要渲染的段落边界。最后重写 DidLayout 方法把累积的信息共享回 ContainerView，以便它渲染行号。

在展示这些方法之前，我先给子类添加一些状态。一个数组累积文本视图布局的每个段落的边界，一个整数跟踪起始行号，以及一个闭包把累积信息发送给 ContainerView 渲染行号。

视口控制器的委托方法帮助文本视图知道滚动或编辑何时发生，以便重绘行号。

接下来实现这些方法，从 WillLayout 开始。先调用 super。记住所有这些委托方法都要这样做。

清空 lines 变量，以便准备存储布局片段的边界。我们还需要起始行号，它基本上是视口开始前所有段落的计数。

让我把这个放在自己的函数里，并从 WillLayout 中调用它。

先做一些简单的 nil 检查和变量命名。我用文本位置的 enumerateTextElements 方法枚举元素，递增计数直到到达 viewportRange。就这样！示例代码通过缓存改进了这一点，这样每次布局过程都不用付出这个代价。回到委托方法，看看如何获取每个段落的边界。

我们用下一个委托方法 configureRenderingSurfaceFor: textLayoutFragment 来做。

再次先调用 super，以获得默认的文本视图行为，然后把布局片段的 layoutFragmentFrame 变量追加到 lines 数组。这就是 configureRenderingSurfaceFor textLayoutFragment 方法的全部。该方法会在视口中的每个段落触发。

看看 DidLayout 方法。此时我拥有了视口中每个段落的边界信息，想把它传给 ContainerView。

在触发闭包之前，需要把片段帧从文本容器坐标转换为视口坐标。

我通过减去视口原点来做到。然后把起始行号和调整后的帧传给 ContainerView。回到 ContainerView，我设置闭包。对每个帧，把索引加到起始行号计算出行号，并在 LineNumber 视图的正确位置绘制。就这样。我们设置变量，收集文本视图中每个段落的边界，并传给 ContainerView 显示。运行 App 看看效果。

完美，我们用几行代码给 UITextView 加上了行号。

我还有更多工作要做，但这构建代码编辑器是很好的第一步。

使用框架文本视图的视口布局过程是访问和显示单个段落信息的强大方式。

再给你展示一个例子。这次涉及修改多个段落的布局。

这里我设置了一个 UITextView 显示一些最喜欢的食谱。但我想一次只看一个食谱。也就是把每个多段落食谱折叠成只显示标题。

为此，我从上例的三个视口委托方法开始。在此之上，如果段落被折叠，我想避免对其做布局。

为此，我让 TextView 遵循 NSTextContentStorageDelegate。

通过这个遵循，我获得 textContentManager: shouldEnumerate 的访问，帮我标记 textElements 为折叠或未折叠。记住，NSTextContentManager 只是 NSTextContentStorage 的抽象版本，NSTextElement 是 NSTextParagraph 的抽象版本。

我们想要一些状态来记录哪些章节被折叠。

我们用一组整数跟踪段落偏移来唯一标识每个段落。

另外添加一个方法处理用户点击切换按钮时的情况。

这就是你需要的全部！用文本内容存储委托方法跳过布局，用视口控制器委托方法处理视口中做布局的每个段落，并处理用户点击章节披露按钮的交互。

细节请看示例代码。看看我们实现了什么。

我可以把任何食谱折叠成只显示标题，点击它旁边的三角形即可，而且直接在 UITextView 中完成。好吧，退一步。

到目前为止，我们的例子都围绕文本、段落、行号和章节标题。但文本视图显示的远不止文本。想想"信息"里的内联照片和贴纸，或"备忘录"里的绘图和文档扫描。

所有这些非文本内容都住在文本视图里，由 TextKit 管理。它们被称为文本附件。文本附件遵循与常规文本相同的架构。我聚焦一个段落，用回形针符号代表附件以简化。文本附件与任何其他字符一样存储在文本存储中，通过 NSTextAttachment 对象完成。

当布局管理器遇到文本附件时，它请求 NSTextAttachmentViewProvider，这是布局层对应的对象。视图提供者提供把附件渲染到文本视图所需的信息。这带来一个挑战。由于这些对象是不可变的，如果编辑段落中的文本，所有实例都必须被丢弃并重建。让我展示一个具体例子。

假设我在构建一个带内联动画的即时通讯 App。仔细看我编辑时的情况。每次编辑对应段落的动画都会重新开始。我的视图提供者在每次编辑时被重建，从而重启动画。

为了解决这个问题，我们为 UITextView 添加了新 API。

初始化文本视图后，我用 register forTextAttachmentViewProviderType 方法为 NSTextAttachmentViewProvider 的某个子类注册视图提供者复用策略。第一个参数，我添加 onEditingInlineParagraphs 复用策略。

这在段落编辑间保留视图提供者，因此按键不会拆毁我的视图提供者。

第二个参数，我提供视图提供者子类类型，文本视图会处理该特定类的所有对象。在示例代码中，你可以看到第二种复用策略：onScrollingOutOfViewport。它在附件滚动出视口时缓存附件的渲染表面，回来时恢复。你可以根据场景组合两种复用策略。

现在编辑时，UITextView 复用视图提供者，保持状态，避免任何动画故障。

就是这样！三个在 UITextView 中使用 TextKit 的例子：代码编辑器的行号、食谱 App 中的可折叠章节，以及简单文本视图中的内联文本附件复用。你可以下载示例 App 查看细节。

总结一下，要创建便捷但强大的富文本编辑体验，在 UIKit 上用 UITextView、AppKit 上用 NSTextView 启动你的 App。如果你有 SwiftUI App，用 ViewRepresentable 把这些文本视图包含进来。如果你想要对文本渲染有更多控制，用 TextKit 创建自定义文本视图并使用新的渲染表面 API。

查看示例代码，看看可折叠章节、行号和内联附件复用的实际效果。感谢观看！
