---
title: 'TextKit 与文本视图有什么新功能'
session_id: 10090
collection: wwdc2022
year: 2022
duration: '24:04'
topics: [Essentials, 'SwiftUI & UI Frameworks']
group: E · UIKit/SwiftUI 渲染与 UI 性能
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2022/10090/'
content_hash: 'sha256:624a5e2e853adecf'
translated: true
---

# TextKit 与文本视图有什么新功能

<sub>WWDC2022 · 24:04 · Essentials、SwiftUI & UI Frameworks</sub>

了解 TextKit 和 UI 框架中文本视图的最新更新。探索布局改进和 API 增强，了解如何……

> [!note] 归档理由
> TextKit 与文本视图更新

## 相关资源

- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/10090/4/5A0AE4B4-BE39-434E-8B9E-0910F2FD152D/downloads/wwdc2022-10090_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2022/10090/4/5A0AE4B4-BE39-434E-8B9E-0910F2FD152D/downloads/wwdc2022-10090_sd.mp4?dl=1)
- [Q&A: UI Frameworks](https://developer.apple.com/videos/play/wwdc2022/110829)
- [Q&A: UI Frameworks](https://developer.apple.com/videos/play/wwdc2022/110830)
- [What's new in UIKit](https://developer.apple.com/videos/play/wwdc2022/10068)
- [Meet TextKit 2](https://developer.apple.com/videos/play/wwdc2021/10061)
- [Check for NSTextLayoutManager first](https://developer.apple.com/videos/play/wwdc2022/10090/?time=801)
- [Counting number of lines of wrapped text in a text view with TextKit 2](https://developer.apple.com/videos/play/wwdc2022/10090/?time=1061)
- [Convert NSRange to NSTextRange](https://developer.apple.com/videos/play/wwdc2022/10090/?time=1270)
- [Convert NSTextRange to NSRange](https://developer.apple.com/videos/play/wwdc2022/10090/?time=1300)
- [Convert UITextRange to NSTextRange](https://developer.apple.com/videos/play/wwdc2022/10090/?time=1322)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

- 大家好，欢迎来到《TextKit 与文本视图有什么新功能》！我是 Donna Tom，一名 TextKit 工程师。

在 iOS 15 和 macOS Monterey 中，我们引入了 TextKit 2，一个强大的新文本引擎，具有改进的性能、正确性和安全性。

TextKit 2 基于视口的布局架构提供了高性能的文本布局，特别是对于大内容的文档。

TextKit 2 通过移除与字形打交道的不必要复杂性，为国际受众提供更好的文本体验，并完全支持 OpenType 和 Variable Fonts 等现代字体技术。

TextKit 2 专注于使用更高层的对象来控制文本布局，使你更容易自定义文本的布局，以便用更少的代码构建更酷的东西。

展望未来，TextKit 2 引擎构成所有 Apple 平台上文本布局和渲染的基础。

未来的性能增强、更新和改进都将专注于 TextKit 2 引擎。

通过更新到 TextKit 2，你的 App 可以在我们推出这些改进时获得它们的好处。

有关 TextKit2 的深入介绍，请观看 Meet TextKit2 视频。该视频涵盖基础知识以及如何使用 TextKit 2 构建自己的文本布局组件。

相比之下，本视频涵盖 TextKit 2 的最新进展以及如何从基于 TextKit 2 的文本视图中获得最大收益。没错，我说的是文本视图，复数，因为现在，从 iOS 16 和 macOS Ventura 开始，UIKit 和 AppKit 中的所有文本控件都在使用 TextKit 2，包括 UITextView。所以我们在整个系统中都使用 TextKit 2 进行布局和渲染。所有 App 尽快过渡到 TextKit 2 非常重要，我们添加了一些工具使过渡对你更容易。对于许多 App，这可以是零代码过渡。我们期望不对其文本视图做任何特殊修改的 App 能做到这一点。我稍后会告诉你更多关于这一点。

但首先，我将从 TextKit 2 的新功能开始，包括我刚提到的那些工具。

之后，我将深入 TextKit 1 文本视图的兼容模式的细节。

然后我将以讨论你可以用来准备把代码过渡到 TextKit 2 的现代化策略结束。

所以首先是 TextKit 2 的新功能。

TextKit 2 最先在 iOS 15 来到 UIKit，其中 UITextField 被升级为使用它。在 iOS 16 中，UIKit 向 TextKit 2 的过渡完成，所有文本控件默认使用 TextKit 2，包括 UITextView。大多数文本视图会自动选择使用 TextKit 2，不需要你做任何采用。只有几种情况文本视图可能不会被选择，我将在本视频的兼容性部分介绍。

AppKit 的故事类似。TextKit 2 最先在 macOS Big Sur 来到 AppKit。在 macOS Monterey 中，NSTextField 被升级为默认使用它，NSTextView 可以通过选择加入使用。

在 macOS Ventura 中，所有文本控件默认使用 TextKit 2。就像 UITextView 一样，大多数 NSTextView 会自动选择使用 TextKit 2，不需要你做任何采用。

TextEdit，它是 NSTextView 的薄封装，在 macOS Ventura 中处处使用 TextKit 2。TextEdit 从 macOS Big Sur 起在纯文本模式下就使用 TextKit 2。在 macOS Ventura 中，富文本模式也使用 TextKit 2。

由于 TextKit 2 是新标准，我们为 UITextView 和 NSTextView 添加了一些便利构造器。使用这些新构造器在初始化时选择使用哪个文本引擎。

要创建一个使用 TextKit 2 的文本视图，使用新构造器并为"UsingTextLayoutManager"参数传 true。如果文本视图需要为兼容性使用 TextKit 1，改为传"false"。

并且文本视图在 Interface Builder 中创建时有一个新的 Text Layout 选项。这个新选项让你可以按实例控制使用哪个布局系统。默认设置是系统默认，即 TextKit 2。

你也可以选择显式使用 TextKit 2 或 TextKit 1。

TextKit 2 现在支持非简单文本容器。非简单文本容器可能有孔洞或间隙。这允许文本围绕图像或其他内联内容换行。

要创建非简单文本容器，使用 NSTextContainer 上的 exclusionPaths 属性来定义文本不应布局的区域。有关如何做到这一点的示例，请查看本视频相关资源中的 TextKitAndTextView 示例代码。你可以在"exclusion path"标签页找到相关示例。

我们增强了 TextKit 2 中的断行引擎，为两端对齐的段落选择更均匀的断行。这是微妙的改变，更容易在更长的文本段落上注意到。

这里我们有相同文本的两个版本，布局在相同区域。

注意传统断行下的拉伸行和大的词间间距。

使用新的均匀断行，这种情况少得多。这使文本更容易阅读，你免费获得它与 TextKit 2。不需要采用。

最后，我们在所有平台上为 TextKit 2 添加了文本列表支持。使用文本列表，你可以编程创建编号或项目符号列表以在文本视图中显示。TextKit 2 使用 NSTextList 来表示文本列表，就像 TextKit 1 一样。NSTextList 过去只在 AppKit 中可用，但在 iOS 16 中，它也在 UIKit 中可用。

使用 NSTextList 与 NSmutableParagraphStyle 一起，指定文本存储中的某个段落应格式化为列表以供显示。文本视图负责从文本存储拾取这些属性，并重新格式化段落内容使其看起来像列表。

虽然 NSTextList 本身并不新，但有一些新的 TextKit 2 增加。由于列表可以有嵌套项，自然地把它们表示为树结构。在 TextKit 2 中，我们增强了 NSTextElement 以支持把它们作为树结构，提供访问子元素和父元素的属性。

我们还添加了一个新的元素子类 NSTextListElement。当内容管理器遇到文本内容中的 NSTextList 时，它将生成 NSTextListElements 来表示列表中的项。

要更深入地了解如何创建文本列表和添加项，请参考 TextKitAndTextView 示例代码。你可以在"list"标签页找到相关示例。

在探索示例代码时，不要错过文本附件示例，它展示了如何在 TextKit 2 中使用文本附件视图提供者 API。

这些 API 让你使用 UI 或 NSView 作为文本附件，并且事件可以直接由附件视图处理。这使文本附件的事件处理容易得多，并且只在 TextKit 2 中可能。好了，这就是 TextKit 2 的新功能。接下来，我将进入 TextKit 1 兼容模式的细节。由于 TextKit 2 与 TextKit 1 的设计相比是彻底的背离，我们理解对于大量投资于 TextKit 1 架构的 App，完全采用 TextKit 2 可能需要一些时间。我们希望这些 App 在过渡完成之前继续良好工作，这就是为什么我们为 UITextView 和 NSTextView 添加了特殊的 TextKit 1 兼容模式。当你显式调用 NSLayoutManager API 时，文本视图会用 NSLayoutManager 替换其 NSTextLayoutManager，并重新配置自己以使用 TextKit 1。当文本视图遇到 TextKit 2 尚不支持的属性，如表格，或在打印时，这也会发生。

如果你在 UITextView 中遇到意外的运行时回退到 TextKit 1，请检查日志中关于切换的警告消息。在符号 underscore UITextViewEnablingCompatibilityMode 上设置断点，以捕获堆栈跟踪和其他有用的调试信息。

对于 NSTextView，你可以通过订阅 willSwitch 或 didSwitchToNSLayoutManager 通知，获得更多关于意外运行时回退的信息。

如果你必须退回到 TextKit 1，最好在初始化时选择退出，使用编程初始化的文本视图。通过使用你自己的文本容器和 TextKit 1 布局管理器来做到这一点。

另一个选项是使用新的便利构造器来初始化 TextKit 1 文本视图，并把 false 作为参数。这将使你的文本视图使用 TextKit 1。

第三个选项是使用 Interface Builder，并在你的文本视图上把新的 Text Layout 选项设置为 TextKit 1。

这里有一些要注意的。如果你在初始化期间或之后交换文本容器的布局管理器，那么你的文本视图将按设计回退到 TextKit 1。在初始化时创建所有 TextKit 2 对象只是为了稍后丢弃它们，这是低效的。根据时机，还可能有用户端副作用。如果它在输入时发生，文本视图可能失去焦点并中断输入，需要重新选择文本视图以恢复。通过在初始化时选择退出文本视图来避免这种情况。现在你已经了解了兼容模式的所有知识，是时候讨论如何通过现代化你的 App 和采用 TextKit 2 来完全避免它了。我真想让你记住一件非常重要的事。

每个文本视图只能有一个布局管理器。文本视图不能同时拥有 NSTextLayoutManager 和 NSLayoutManager。

一旦文本视图切换到 TextKit 1，就没有自动回到的方式。切换布局系统的进程是昂贵的，你会丢失切换时存在的任何 UI 状态。所以为了最佳性能和可用性，系统永远不会把文本视图从 TextKit 1 切回 TextKit 2。这是一次性操作。

这意味着避免兼容模式真的很重要。文本视图进入兼容模式有几个不同的原因。文本视图进入兼容模式的头号原因是访问文本视图的 layoutManager 属性。其他原因要少见得多。

所以一个重要策略是避免访问文本视图的 layoutManager 属性。也避免通过文本视图的文本容器访问布局管理器。审计你的代码中这些属性的使用，并移除它们或用 TextKit 2 等价物替换。

如果你把 App 部署到没有 TextKit 2 的旧 OS 版本，你可能无法完全移除你的 layoutManager 代码。

在这种情况下，你应该首先检查文本视图的 NSTextLayoutManager。

把你的 TextKit 2 代码放在 if 子句中，把 TextKit 1 代码放在 else 子句中，包括 layoutManager 访问。这样，TextKit 1 代码只在 TextKit 2 不可用时运行，你的 layoutManager 查询不会导致意外回退到 TextKit 1。

如果你遵循了所有这些建议，但仍然遇到来自系统的意外回退到 TextKit 1，那是我们的问题，所以请使用 Feedback Assistant 报告问题。包括回退发生时的堆栈跟踪捕获，你可以从在 UIKit 中对 underscore UITextViewEnablingCompatibilityMode 断点，或在 AppKit 中对 willSwitchToNSLayoutManagerNotification 断点获得。

好了，现在我将进入更新与 TextKit 1 类型相关的代码的具体内容，从 NSLayoutManager 开始。一旦你审计了代码中的 NSLayoutManager 查询，你将需要找出 NSTextLayoutManager 中的 TextKit 2 等价物。

一些布局管理器 API 在 TextKit 1 和 2 之间有相似的名称，替换是直接的。这里有几个例子。在 TextKit 1 中，你调用 NSLayoutManager 上的 usedRect(for: textContainer) 来获取文本容器内文本的边界矩形。在 TextKit 2 中，你从 NSTextLayoutManager 上的 usageBoundsForTextContainer 属性获取这个。

在 TextKit 1 中，我们使用名称"temporary attributes"来指仅影响渲染而不影响布局的属性。在 TextKit 2 中，我们更准确地称那些为"rendering attributes"。但有些 TextKit 1 API 在 TextKit 2 中没有直接等价物。要理解为什么，你需要了解对于 Kannada 等 Indic 脚本中的许多单词，没有正确的字符到字形映射。

在这些脚本中，字形可以被拆分、重新排序、重组，甚至删除。

NSLayoutManager 上基于字形的 API 假设你可以直接把连续的字符范围与连续的字形范围关联起来，但这对所有脚本都不成立。使用这些 API 可能导致用 Kannada 等脚本编写的文本布局和渲染损坏。这就是 TextKit 2 中没有字形 API 的原因。你不能只是用一个 TextKit 2 API 替换一个 TextKit 1 字形 API。替换这些 API 需要不同的方法。

所以这里是更新基于字形的代码的方法。第一步是识别你使用的字形 API。接下来，查看你如何使用这些 API，并在高层定义你试图做什么。基于字形的代码非常底层，有许多与你的高层任务无关的细节。

一旦你定义了高层任务，然后检查 TextKit 2 中可用的结构，如布局片段、行片段和文本选择。这些可以帮助你完成任务。例如，考虑这个 TextKit 1 代码。这里使用了两个字形 API：numberOfGlyphs 和 lineFragmentRect(forGlyphAt: index)。这个 TextKit 1 代码正在遍历文档中的所有字形并计数行片段矩形。高层任务是计数文本视图中换行文本的行数。由于这个代码在处理行片段矩形，要使用的 TextKit 2 结构是 NSTextLineFragment 和 NSTextLayoutFragment。

这里是重写为使用 TextKit 2 的代码。它不再遍历字形，而是枚举文档中的文本布局片段，并提供一个闭包，计数每个布局片段内的所有文本行片段。

更新你自己的代码为 TextKit 2 时请记住那个例子。现在我将转到讨论基于 NSRange 的代码更新。

TextKit 1 使用 NSRange 来索引文本内容，NSRange 是字符串的线性索引。对于文本"Hello TextKit 2!"感叹号，表示"TextKit 2 感叹号"的 NSRange 是位置 6 长度 10，因为它从第 6 个字符开始，长度为 10 个字符。这个线性模型易于理解，用于索引字符串时工作得很好。

但线性模型不适用于索引任何比字符串有更多结构的内容。这里有一个例子。HTML 文档被表示为树结构，每个标签是树中的一个节点。如果我们的 Hello TextKit 2! 文本是 HTML 文档的一部分，我们的 NSRange 无法告诉我们文本在 span 标签内，嵌套 3 层深。线性模型不够表达力来存储该信息，所以我们不能用它来索引这样的嵌套结构。这就是为什么 TextKit 2 添加了新的类型来表示文本内容中的范围。NSTextLocation 是表示文本内容中单个位置的对象。NSTextRange 由开始和结束位置组成。结束位置被排除在范围之外。这些新类型可以通过把位置定义为 DOM 节点加字符偏移来表示这个 HTML 文档的嵌套结构。

由于 NSTextLocation 是协议，任何自定义对象都可以是位置，只要它实现了 NSTextLocation 协议方法。这对于与支持其模型中结构化数据的不同类型的后备存储一起工作至关重要。

但文本视图构建在不具有这种结构的 NSAttributedString 后备存储之上，我们不能在不破坏许多 App（包括你的）的情况下改变这一点。所以使用文本视图 API 如 selectedRange 或 scrollRangeToVisible 时，你将继续使用 NSRange。在与 TextKit 2 布局管理器或内容管理器通信时，你将需要在 NSRange 和 NSTextRange 之间转换。

要转换文本视图的 NSRange 到 NSTextRange，把位置定义为 attributed string 中的整数索引。

使用 NSRange 的 location 作为 NSTextRange 的开始位置。

使用 NSRange 的 location 加上 length 作为 NSTextRange 的结束位置。概念上，这就是从 NSRange 映射到 NSTextRange 的方式。

在实践中，代码看起来有点不同，因为 NSTextLocations 必须是对象。

你需要通过内容管理器来计算位置。

对于开始位置，向内容管理器询问文档开头的位置，然后按 NSRange 的 location 偏移它。然后把开始位置按 NSRange 的 length 偏移以获得结束位置。

要反向进行，使用文本内容管理器获取两个不同的偏移。

NSRange 的 location 是文档开头与 NSTextRange 的 location 之间的偏移。NSRange 的 length 是 NSTextRange 的开始和结束位置之间的偏移。

UITextView 和 UITextField 遵循 UITextInput 协议，它使用 UITextPosition 和 range。大多数时候，使用 UITextView 或 UITextField 时你不需要直接把 UITextRange 转换为 NSTextRange。但如果你需要，使用整数偏移作为两种范围类型之间的中介。

另一方面，如果你使用带有 UITextInput 的自定义视图，你对与视图一起使用的 UITextPosition 和 UITextRange 子类有直接控制。你可以让你的 UITextPosition 子类符合 NSTextLocation，实现所需方法，并用你的子类直接创建 NSTextRanges。

最后，这里提醒不要在不同视图之间重用 UITextPosition 对象，即使两个视图中的内容相似。UITextPosition 只对用于创建它的视图有效。

好了，现在你有了大量可用于现代化代码的策略。应用这些策略，你的 App 将准备好收获 TextKit 2 的好处。

这就是 TextKit 与文本视图有什么新功能。我涵盖了许多 TextKit 2 的很棒改进，并分享了更新你的 App 同时为旧 OS 版本保持兼容性的策略。今天就在你的 App 中使用 TextKit 2，以充分利用新的改进。检查你的文本视图，确保它们没有意外回退到 TextKit 1。最后，采用现代化策略把你的 App 放到 TextKit 2 上。我们迫不及待想读你用 TextKit 2 和文本视图创造的内容。感谢观看！
