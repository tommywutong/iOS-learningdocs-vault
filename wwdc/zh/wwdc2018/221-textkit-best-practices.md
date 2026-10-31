---
title: 'TextKit 最佳实践'
session_id: 221
collection: wwdc2018
year: 2018
duration: '37:55'
topics: ['SwiftUI & UI Frameworks']
group: E · UIKit/SwiftUI 渲染与 UI 性能
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2018/221/'
content_hash: 'sha256:560afa477a465361'
translated: true
---

# TextKit 最佳实践

<sub>WWDC2018 · 37:55 · SwiftUI & UI Frameworks</sub>

利用 TextKit 的能力，提供显示和编辑文本的最佳体验。从 TextKit 中获取最佳性能……

> [!note] 归档理由
> TextKit 1 的排版流水线

## 相关资源

- [TextEdit Sample Code](https://developer.apple.com/library/archive/samplecode/TextEdit/)
- [Attributed String Programming Guide](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/AttributedStrings/AttributedStrings.html)
- [Ruler and Paragraph Style Programming Topics](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/Rulers/Rulers.html)
- [Text Attribute Programming Topics](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/TextAttributes/TextAttributes.html)
- [Text System User Interface Layer Programming Guide](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/TextUILayer/TextUILayer.html)
- [Text Layout Programming Guide](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/TextLayout/TextLayout.html)
- [Text System Storage Layer Overview](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/TextStorageLayer/TextStorageLayer.html)
- [Cocoa Text Architecture Guide](https://developer.apple.com/library/content/documentation/TextFonts/Conceptual/CocoaTextArchitecture/Introduction/Introduction.html)
- [Text Programming Guide for iOS](https://developer.apple.com/library/content/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/Introduction/Introduction.html)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2018/221dm4k4kaqjqapkxt/221/221_hd_textkit_best_practices.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2018/221dm4k4kaqjqapkxt/221/221_sd_textkit_best_practices.mp4?dl=1)
- [Presentation Slides (PDF)](https://devstreaming-cdn.apple.com/videos/wwdc/2018/221dm4k4kaqjqapkxt/221/221_textkit_best_practices.pdf?dl=1)
- [Meet Scribble for iPad](https://developer.apple.com/videos/play/wwdc2020/10106)
- [What's New in Cocoa for macOS](https://developer.apple.com/videos/play/wwdc2018/209)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

大家好。

欢迎来到 session 221，TextKit 最佳实践。我是 Donna Tom。我是 TextKit 工程师。我的同事 Emily Van Haren 来自 authoring tools，今天会和我一起。我们俩都对与各位分享使用 TextKit 的最佳实践感到非常兴奋。那么让我们开始吧。首先，我们将回顾使用 TextKit 的一些关键概念。

然后，我们将深入一些例子，来说明如何在你的 App 中应用这些关键概念。

最后，我们将在正确性、性能和安全方面，总结一些最佳实践。

那么让我们从关键概念开始。现在为了确保我们在同一页面上，我们将从最开始说起。

什么是 TextKit？你的第一反应可能是打开 Xcode 里闪亮的新 playground 并输入 import TextKit，只不过如果你真的试过，你会发现它并不工作。那是因为 TextKit 和你可能用过的其他框架有点不同。

你不必导入任何特殊的东西就能使用它。

UIKit 和 AppKit 中的文本控件都是构建在 TextKit 之上的。所以如果你曾经用过 label、text field 或 text view，你其实已经用过 TextKit 了。

TextKit 把强大的底层技术（如 Core Text、Core Graphics 和 Foundation）整合起来，让你的 App 显示文本变得简单而无缝。

每次你使用这些内置控件之一时，你都在使用 TextKit 的力量，以完全国际化、可本地化的方式显示或编辑文本，而无需直接使用这些底层技术，或理解复杂脚本的细节。并且你还能免费获得很多东西，比如你在这里看到的所有这些显示特性。对于编辑，你还会得到 OS 支持的所有文本服务，如辅助功能、拼写检查等。

而且你可以利用所有这些很棒的特性，而无需写一行代码，这相当棒。

那么在所有这些功能触手可及的情况下，你如何决定使用哪个控件呢？所以让我们谈谈，为你的场景选择合适的控件。选项会根据你使用的是 UIKit 还是 AppKit 而有所不同。所以让我们分别回顾。好的。我们从 UIKit 开始。首先你要考虑是否需要文本输入。如果你不需要文本输入，那么考虑是否需要选择或滚动。如果你不需要这些，那么你应该使用 UILabel。

UILabels 适用于少量文本，比如几个词或几行。

所以如果你有比那更多的文本，或者如果你需要这些选择或滚动能力，那么你应该使用编辑禁用的 UITextView。现在回到顶部。如果你确实需要文本输入，那么考虑是否需要安全文本输入。这会像密码字段，文本被遮掩并且复制被禁用。所以如果你需要那个，那么使用 UITextField，因为这是唯一支持安全文本输入的控件。否则，想想你期望输入多少文本。

如果你想要的是像表单字段输入那样只需一行的东西，那么使用 UITextField。UITextField 只支持一行文本输入。否则，如果你需要更多，你可以使用 UITextView。现在，这是 AppKit 的相同决策过程。它与 UIKit 的过程相似，但有几处小差异。

所以，同样，你将从考虑是否需要文本输入开始。AppKit 没有 label 控件。所以如果你需要显示文本，使用 NSTextField，你可以禁用编辑和选择来获得 label 行为。现在回到顶部这里。如果你确实需要文本输入，再次问是否需要安全文本输入。如果需要，你可以使用 NSSecureTextField。否则，我们要问我们最喜欢的问题，你期望多少文本？所以 NSTextView 对大量文本的性能进行了优化。所以如果你期望很多文本，你应该使用 NSTextView，否则你可以使用 NSTextField。

现在，与它的 UIKit 对应物不同，NSTextField 支持多行文本，但它仍然为较短的字符串优化，所以如果你有很多文本，你仍然应该使用 NSTextView。现在那些在 TextKit 上摸爬滚打过几次的人可能会注意到流程图缺少一个选项，那就是字符串绘制。

你通过直接调用 NSString 或 NSAttributedString 下的 draw in point 或 draw in rect 方法来使用字符串绘制。

你们中的许多人可能正在为了性能好处而使用它，以避免 kit 层级 view 对象的开销。

所以如果你要走这条路，请记住以下提示。

你想把它用于少量静态文本。并且你想限制调用 draw 方法的频率。

现在如果你经常调用字符串绘制方法，你实际上可能从 label 或 text field 获得更好的性能，因为这些控件提供更好的缓存，尤其是如果你使用 auto layout。如果你用很多自定义属性绘制 attributed string，这也可能减慢你的字符串绘制，因为文本系统需要在渲染前验证所有属性，所以为了最佳性能，你应该在绘制前剥离额外的属性，只传入那些需要决定视觉外观的属性，比如 font 或 color。最后，记住通过使用字符串绘制，你将错过文本控件提供的所有这些免费功能，所以应该尽可能使用文本控件。现在你知道了你能用 TextKit 做什么，只通过使用内置控件。

但如果你想超越这些控件提供的功能，你需要在文本栈中找到合适的定制点。

像很多 Cocoa 一样，TextKit 基于 model view controller 设计模式。文本系统可以被划分为三个阶段，直接对应 MVC，那就是 storage、display 和 layout。

所以现在让我们更仔细地看看构成每个阶段的 TextKit 对象。我们将从对应于 model 的 storage 开始。现在 NSTextStorage 持有你的字符串数据和属性。

它是 mutable attributed string 的子类，所以你可以用你已经知道的处理 attributed string 的同样方式来处理它。

我的同事 Emily 将在稍后向你展示一些非常强大的定制文本存储的方式，所以请继续关注。

现在 NSTextContainer 模型化你的文本将被布局的区域的几何形状。

默认情况下它是矩形，但你可以自定义文本布局的流动或形状，如这里所示。欲了解处理 storage 对象的更详细信息，请查看这些很棒的过去 WWDC 会议和文档。它们将可以从会话末尾的 more information 链接获得。

接下来是对应于 view 的 display 阶段。我们已经在谈论选择合适的控件时谈了很多 display 阶段。所以欲了解更多信息，你可以再次查看这些文档资源。它们也将可以从会话末尾的 more information 链接访问。最后，我们有对应于 controller 的 layout 阶段。NSLayoutManager 是这个阶段中唯一的组件。让我告诉你，它是一个 beast。

我的意思是好的方面，因为它在它所做的事情上太棒了。所以它是整个操作的大脑。它协调所有阶段之间的变化，并控制布局过程本身。所以这里是对布局过程如何工作的快速概述。

文本布局发生在系统修复文本存储中的属性以消除不一致之后，比如确保字符串中的所有字符都被支持显示这些字符的字体覆盖。所以在这个例子中，Times New Roman 字体被指定给整个字符串，但这个字体不支持显示日语 kanji 或 emoji。

所以在 attribute fixing 之后，你的文本存储看起来会像这样，日语字符分配了合适的日语字体，emoji 字符分配了 emoji 字体。好的。

所以一旦属性被修复，布局过程就可以开始。我们可以把布局分为两步：glyph generation 后面跟着 glyph layout。

一旦它们被布局，它们就准备好显示了。但等一下。什么是 glyph？让我们退一步回顾一下。

glyph 是一个或多个字符的视觉表示。如你这里所见，字符和 glyph 之间的映射并不总是一对一。

所以这里这个字符串 ffi 有三个字符，但它可以由 ligature 的单个 glyph 表示。你也可以反方向走。

这里我们有 n，它是一个可以由多个 glyph 表示的单个字符：一个用于 n，一个用于 tilde。

所以回到我们的图这里，我们有 NSLayoutManager 执行 glyph generation 和 glyph layout。

glyph generation 是 layout manager 取字符并弄清楚需要绘制哪些 glyph 的地方。

glyph layout 是 layout manager 为你的 view 中的显示定位这些 glyph 的地方。从这些过去的 WWDC 会议和文档中有更多要了解 layout manager 的内容。你可以从，你猜对了，会话末尾的 more information 链接访问它们。好的。所以现在你理解了文本系统的阶段。并且你知道构成每个阶段的 TextKit 组件。

所以现在让我们探索选择这些组件的正确配置来创建不同效果。这是你的标准配置。当你从 Interface Builder 拖放一个 text view 时，你将自动得到如这里所示的每个组件各一个。

大多数时候这就是你所需要的。如果你想要多页或多列布局，你可以使用成对的 text containers 和 text views，每页或每列一对。

你可以把所有这些 hook 到同一个 layout manager 和同一个 text storage 上，这样它们共享 backing store 中的布局信息。如果你想要每个 view 中有不同的布局，你也可以这样做，只需使用多个 layout manager。并且，再次，因为文本共享相同的 backing store，更新文本将更新所有 view。

我们没有深入这些配置的太多细节，因为有一个很棒的过去 session 已经做过了，所以查看 WWDC 2010 session Advanced Cocoa Text Tips and Tricks。这将可以从会话末尾的 more information 链接访问。好的。

所以，我们已经看了内置文本控件。

我们看了 TextKit 中的组件。我们看了如何配置这些组件来实现不同效果。用这些知识你已经可以做很多事，但如果你需要更多，你需要自己扩展和定制 TextKit 的部分。

所以现在我们将谈一点关于选择正确的方法来做这件事。

选择正确的方法就像充实你的文本工具箱。就像去商店因为你需要一个锤子。然后当你到达时，你遇到这个巨大的锤子墙要选。

你想要选择能完成工作的锤子，理想情况下是能做你需要的最便宜的那个。所以这些是我们可用的锤子。

delegation 就像你标准的带 claw 的锤子，它用于执行多个任务。

所以 delegate 有很多不同的定制 hooks，大多数时候它们会为你完成工作。Notifications 就像 ball-peen hammer。这个一端有 ball 而不是 claw，所以它更专业化，更适合某些任务，但不如 delegation 的标准锤子通用。最后，subclassing 是你的 sledgehammer。

sledgehammer 非常强大，你可以用它做几乎任何你需要锤子做的事情，但它对很多东西来说可能过度。有了这些，我想邀请 Emily 上来向我们展示如何使用这些不同种类的锤子。Emily。

谢谢，Donna。

所以，作为开发者，我们有一系列控件可选，各种配置，以及广泛的定制选项来实现我们需要的东西。

所以我们的工具箱装满了，但我们怎么知道选哪些工具呢？所以我们将通过一起构建 journal app 的步骤，查看一些利用 TextKit 力量的 App 示例。

我们不必看得太远，因为几乎我们使用的每个 App 都显示或编辑文本。

我们将从我们都很熟悉的两个 App 开始，然后经历构建我们自己的步骤。所以我们要看的第一个 App 是 iOS 上的 Apple News，它是一个美丽的 App，在个性化、策划的文章中显示文本。

这是 spotlight tab 中 featured 的一篇文章的例子。

现在 App 顶部显示了一些关于这篇文章的细节。

我们如何使用 TextKit 来重新创建这种外观和感觉？所以让我们考虑 Donna 早些时候向我们展示的流程图，来挑选最适合这个例子的控件。所以我们要从 handful of text controls 中选，但因为我们想在单行上显示少量文本，我们将使用 label。现在我们可以在 inspector panel 中看到大量的定制选项。所以我们将继续把文本改为 spotlight。我们将把 font 改为使用 body style。我们将启用 dynamic type，允许那些启用辅助功能设置的人以适合他们需求的字体大小和样式查看文本。

现在可以在 Interface Builder 中定制这个 label 很棒，但我们也可以在 Swift 中看到所有这些属性。

所以我们可以动态地在运行时设置文本和 formatting 属性。现在回到 Interface Builder，我们将添加两个更多的 label。

现在所有东西都相当合适，但我们还有一件事要做。

所以回顾 Apple News，我们可以看到右边的文本实际上是用两种不同的颜色显示的。一部分是黑色，一部分是白色。

现在我们可以用两个 separate labels 来实现这个，但如果我们想只用一个 label，我们就不能在 Interface Builder 中做这个。我们怎么能做到？嗯，我们可以利用 attributed strings 的力量和灵活性。

现在 attributed string 是一段可以对字符范围应用属性的字符。

现在你免费得到一些属性，比如默认 font 和 text color，但我们可以用我们自己的值覆盖这些属性。

在这种情况下，我们将把我们字符串的一部分 text color 设置为白色。现在为了看到 attributed string 的实际效果，我们将使用 NSMutableAttributedString 上的 add attribute 方法，只为我们要的范围把 text color 设置为白色。

这次我们将把 attributed text 属性设置在我们的 label 上。在运行时，这看起来相当 spiffy。

现在 UILabels 对这种文本是很好的选择。现在如果我们看屏幕底部，我们将看到一个 headline。现在这也是文本，但它有点大并且跨越多行。让这个文本不同的另一件事是它是 selectable 的。所以这次我们应该用哪个控件？现在 text field 和 text view 都支持 selection，但 text field 通常只是一行。所以在这种情况下，因为我们的 headline 可以跨越多行，我们将使用 text view。现在当我们把 text view 放到我们的 storyboard 上时，我们可以看到默认我们得到很多 lorem ipsum 文本。

所以我们将继续在 inspector panel 中改变文本。

我们还将改变 font 以看起来更像 Apple News。我们想禁用 editing 功能，因为 headline 实际上不可编辑。现在 UITextView 默认会滚动，因为它们是 UIScrollView 的子类。

但如果我们想让我们的 text view 与 auto layout 配合良好，我们想禁用 scrolling。

这将允许 text view 的 bounds 调整以适应文本。最后但同样重要的是，这个白色背景真的需要去掉，所以我们将把它设置为透明。

现在 Interface Builder 使定制这个 text view 变得非常容易，但就像我们之前的 label 一样，我们可以在代码中设置所有这些。

所以这里在 Swift 中，我们可以在运行时动态设置文本和 formatting 属性。

所以我们在 Apple News 中看了如何选择合适的控件，但现在我们将看一个我们都很熟悉的不同的 App 来选择正确的配置，那就是 TextEdit。

现在 TextEdit 是 macOS 上一个处理 rich text 内容显示和编辑的 App。

大多数人不知道的是，TextEdit 实际上是 NSTextView 的一个非常 thin 的 wrapper。

所以我想花一点时间惊叹于我们从 TextKit 免费获得的力量。这是 inspector bar，我们只需在 Interface Builder 中勾选一个 checkbox 就免费得到它。它正下方是一个 ruler view，我们只需启用它也免费得到。所有下面的东西只是一个 text view。实际上，它是一个 text view、text container、layout manager 和 text storage。

现在这是 NSTextView 和 UITextView 的标准配置，但相似性大多到此为止。所以，例如，tables 只在 NSTextView 中支持。

再次惊叹于我们免费得到的力量，TextKit 提供了一个 table editor，为我们做了所有繁重的工作。

现在当我们使用 TextEdit 时，我们经常编辑大量文本。

有时我们粘贴大量 lorem ipsum 来看我们还免费得到一个 spell-checker。

但我们真正想看的是，当我们使用 format menu 选择 wrap to page 时，它最终看起来更像一页。我们可以看到 text container 已被调整大小以匹配一页纸的尺寸。现在如果我们向下滚动，我们可以看到文本从第一页跳到第二页。

现在标准配置并不真正支持这样的布局。

当然，这个布局使用了两个 text views 和 text containers。

现在它们仍然由同一个 layout manager 和 text storage 管理，允许文本自由地从一页跳到下一页。如果你想知道更多关于 TextEdit 如何工作，你实际上可以在 guides and sample codes library 中找到它的 source。所以，我们选了合适的控件，我们选了合适的配置，但有时我们实际上需要 hammer 这些来实现我们想要的。

但我们如何决定使用哪个 hammer 呢？所以我们将通过一起构建 journal app 的步骤，为 job 选择合适的 hammer。我们将从把今天的日期放到 window 上开始。

现在 AppKit 中我们没有 UILabels，但我们可以让 text field 行为像 label。

我们所需要做的就是禁用 editing。现在对于 window 的 journal entry 部分，我们将使用 text view。

所以 in the inspector，我们可以确保 text view 是 editable 和 selectable 并支持 rich text 和 undo。我们还将在 window 底部添加几个 text fields，这样我们可以显示写了多少 words。现在当我们运行 App 时，我们希望底部的 word count 改变，所以让我们为这个 job 找到合适的 hammer。现在我们可以 conform to 一个 delegate，处理一个 notification 或 subclass。但这种情况下，我们将使用一个小锤子。我们将监听来自 text storage 的 notification。

我们可以从 text storage 获取 word 数量。

当我们听到 notification 时，我们可以更新 text field 的 string value 属性。当我们开始输入时，我们可以看到 word count 改变。现在如果我们想强调我们文本的一部分，我们可以使用 keyboard shortcuts 或 menu 来应用 formatting like bold。但如果能支持现代文本 formatting like Markdown，它使用 control characters 来指定 formatting，那会很棒。

所以如果我们开始在前后插入 asterisks，我们希望它变成 bold。

但我们应该为这个使用哪个 hammer？嗯，我们想知道 change 何时发生，并想知道 change 发生在哪里。但 notifications 并不真正给我们提供关于这个 change 的很多信息。

所以我们将使用一个更大的 hammer 并实现 text storage delegate，具体是 didProcessEditing 方法。

现在我们可以从我们现有的 font 创建一个新的 bold font。

我们可以直接把那个 font 添加到我们想要 bold 的 range 的 text storage 上。现在当我们插入那个最后的 asterisk 时，我们可以使它 bold。现在我们对这个 Markdown 事情感觉相当好，那如果我们试试插入一个 code snippet 呢？现在在 Markdown 中它看起来像这样。

如果我们添加这个最后的 back-tick，我们希望它看起来像一个 code block。

它应该有一个 background 和一个说 Swift Code 的 header。

现在这实际上是一个 complex task，所以我们将需要两个 sledgehammers。

第一个是 subclass NSTextStorage。

当我们 subclass NSTextStorage 时，我们需要实现四个 required methods。我们可以通过在一个 private instance of a mutable string 上操作来做到这一点。现在让我们关注 replaceCharacters 方法。

现在我们可以把一个 NSTextBlock 添加到我们的 paragraph style 上。然后我们可以把那个 paragraph style 添加到我们的 text storage 上，跨越那个 code block 的 range。

现在 NSTextBlock 本身不做任何 custom drawing。

所以我们也需要 subclass 它。我们的 NSTextBlock subclass 需要有带顶部额外 padding 的 padding 和 light gray background。我们将 override drawBackground 并使用 string drawing 来绘制 header Swift Code。

现在这实际上就是我们需要做的全部，来让一个 text block 看起来像 code snippet。现在回到我们 custom text storage 中，我们可以创建我们新 code block 的 instance，而不是使用 plain text block。现在，最后但同样重要的是，我们需要告诉我们的 text view 使用我们的 custom text storages 之一，所以我们将替换 layout manager 上的 text storage。现在这正在变成一个真正的 WYSIWYG Markdown editor。

现在大多数 Markdown editor 的一个流行功能是 side-by-side view，左边是 editing version，右边是 rendering。

现在我们可以用两个 text views side-by-side 来做这个。

我们将禁用右边那个的 editing。

现在我们有两个 text views，但我们希望它们显示相同的内容，但在右边看起来有点不同。

所以我们想要像这样的 configuration，我们有一个 text storage，但其他东西都有两个。

为了做到这一点，我们将把右边的 text storage 替换为左边的那个。

现在让我们看看这看起来像什么。现在这实际上真的很 cool。如果我们向左边添加任何字符，它们会立即显示在右边。

现在通常右边并不真正显示 Markdown characters，但由于这是 shared text storage，这意味着我们必须在 layout process 期间隐藏 characters。现在既然我们不得不这样做，我们真的只有一个选项，那就是在 NSLayoutManager delegate 上实现 shouldGenerateGlyphs 方法。

这将允许我们介入 glyph generation process。所以我们可以取那些即将被 layout 的 glyphs，如果它们代表一个 Markdown control character，我们可以把 null property 应用到那个 glyph 上。

这将在 layout process 期间完全消除 glyph，而不会改变 underlying text storage。然后，我们将使用新的 glyphs 并告诉 layout manager 我们想用我们的新 properties 来呈现这些 glyphs。

现在这实际上真的很 cool。所以左边显示一个包含所有 Markdown characters 的 editable version。右边显示没有 Markdown characters at all，全部使用相同的 text storage。现在构建一个 side-by-side Markdown editor 不是我们每天都会做的事，但看到 TextKit 用真实世界的例子有多么可定制，真的很棒。

如果你想了解更多关于如何使用和定制 TextKit，请查看我们 amazing 的 programming guides。

有了这些，我将把它交还给 Donna。

谢谢，Emily。

那些是非常 cool 的例子。我真的希望你能把其中一些她展示的技术拿走，并在你自己的 App 中使用它们。

但现在让我们稍微转一下话题，谈谈使用文本的一些最佳实践。

所以在 correctness 话题上，如果你的文本没有按你期望的方式渲染，它可能与 attributed string 上不完整或不正确的属性有关。

所以让我们看一个例子来实践一下。

假设我们有一个 UITextView，有一些 attributed text 说 don't hate。它说这个用 Comic Sans 24 point 字体。我们想以编程方式把 bold typeface 应用到单词 don't 上，因为如果有任何字体比 Comic Sans 更普遍被讨厌，那就是 Comic Sans bold。所以乍一看，写这样的代码似乎合理。

现在这里我们有我们原来的 font。我们将使用 font descriptor 来创建这个 original font 的 bold 版本。

然后我们将使用原始文本初始化我们的 mutable attributed string。我们将把我们的 new font 或 new bold font 应用到单词 don't 上，那就是前五个字符。然后我们将把 UITextView 的 attributed text 属性设置为使用这个新的 attributed string，除了当我们这样做时我们将看到我们的 new bold font 应用到单词 don't 上，正如我们期望的，但字符串的其余部分不知怎么丢失了 original font。现在那些鄙视 Comic Sans 的人可能对此感到高兴，但结果是 wrong，所以这值得一个 sad face。

所以为什么会发生这个？要回答这个，让我们更仔细地看看我们如何初始化 attributed string。

所以注意我们使用 plain text string 来初始化它，并且我们使用 no attribute information 的 initializer。当你创建一个新的 attributed string 并且你不提供任何 attribute information 时，那个新的 attributed string，我们使用 default attributes。

默认 font 是 Helvetica 12 point。所以 recap 发生了什么，我们从这个 original attributed string 开始，font Comic Sans 24 应用到整个 range。然后我们创建了这个新的 attributed string，它用 default attributes 初始化。

我们在 new string 上把 bold font 应用到单词 don't 上，我们得到了这个 incorrect result，单词 don't 是 Comic Sans bold 24，字符串的其余部分是 default font Helvetica 12。所以有两种不同的方式我们可以正确地做这件事，一种是避免 altogether 混合 plain 和 attributed text。

所以通过使用 original one 初始化我们的新 attributed string，我们将保留那些 original attributes。然后我们可以应用我们的新 attributes，而不会得到这个与 default ones 的 reset effect。但并不总是 feasible 只避免混合 plain 和 attributed text。所以如果你必须 mix it up，你可以在从 plain text string 创建那个 new attributed string 时显式提供 attributes。如果我们确保从 original text 应用相同的 attributes，我们将得到 correct result。但你应该意识到这个 reset effect 可以发生在任何有 default values 的 attributes 上，而不仅仅是 fonts。

如你所见，有很多 attributes 有 default values。所以我想特别指出 paragraph style 作为 sneaky reset point。

为了看到为什么，我们将 revisit 我们早先的例子。但这次不是改变 font，我们将把 paragraph style 改为 truncate 单词 hate，因为没人喜欢 hate。所以我们希望我们的文本看起来像这样，但当我们运行这段代码时，我们将得到像这样的 result，所有文本都是 Helvetica 12 并使用 default paragraph style，default line break mode 为 word wrapping。

并且，再次，这对那些讨厌 Comic Sans 的人真的很棒，因为它已从 string 中完全消除，但它是 wrong 的。并且它以与上次不同的方式 wrong。为了理解差异，让我们 recall attribute fixing 发生在 layout 之前，这是系统修复 inconsistent attributes 的地方。

所以这里在我们的 attributed string 中，我们有一个 single paragraph 有 multiple paragraph styles，那是相当 inconsistent 的。

所以当系统修复这个 string 的 attributes 时，它将取它找到的第一个 paragraph style 并把它应用到整个 paragraph。

那就是我们如何 ended up with 我们的 attributed string 显示 default paragraph style。关键 takeaway 是对你的 attributes 要 explicit，尤其是当你混合 plain 和 attributed text 时。

通过这样做，你将避免这个与 default attributes 的 reset effect。对于 AppKit 开发者，如果你为 dark mode 更新你的 App，这实际上超级重要。所以通过使用 explicit attributes with dynamic colors like NSColor.textColor，你将确保你的文本以适合 context 的 correct colors 绘制。所以继续。下一个话题是 performance。

如果你在处理大量文本，改善你的 App 性能的一个好方法是使用 noncontinuous layout。为了理解这意味着什么，让我们 revisit 我们的老朋友 layout process。

我们说 layout process 由 glyph generation 后面跟着 glyph layout 组成。

所以 with continuous layout，layout manager 将从 text storage 的 beginning 执行 glyph generation 和 glyph layout。

它按顺序从 beginning 到 end。

所以如果你 App 的某人滚动到你的 text view 中间某处，layout manager 必须为所有在那个 point 之前的 glyph 生成和 layout glyph，如红色矩形所示。注意这也包括你无法看到的文本，它从屏幕顶部滚动出去，一直到 text storage 的 beginning。

所以如果你有很多文本，那个可怜的人可能要等一会儿，让你的 App 完成 layout，但幸运的是，我们可以通过使用 noncontinuous layout 来避免这种情况。

所以正如名字所暗示的，with noncontinuous layout，layout manager 不必从 text storage 的 beginning 按顺序做 glyph generation 和 layout。

所以现在当那个人，使用你的 App，滚动到 text view 的中间时，layout manager 可以 right away 为中间那个 section 执行 glyph generation 和 layout。所以如果你的 text storage 有很多文本，使用 noncontinuous layout 是巨大的 performance win。棒。那你如何 turn this on？嗯，noncontinuous layout 是 NSLayoutManager 的一个 property。所以对于 NSTextView，你可以访问 text to use layout manager，然后你可以在那里设置那个 property。对于 UITextView，你通常不必做任何事情，因为这默认 turned on，但有一个重要的事情要记住。

因为 UITextView 是 UIScrollView 的子类，noncontinuous layout 将要求 scrolling 被启用。

这是因为当你禁用 scrolling 时，询问 text view 的 intrinsic content size 将要求 layout 所有文本，然后你首先得不到 noncontinuous layout 的性能好处。这引出一个非常重要的 point。

你应该避免在使用 noncontinuous layout 时一次请求 all or most of text 的 layout，因为那 kind of defeats 使用它的 purpose。所以如果你只有一个 text container，不要请求整个东西的 layout。

并且不要请求包含文本末尾的 large ranges of characters or glyphs 的 layout。我们这里没有太深入文本性能话题，因为我去年在 WWDC 2017 给了一个很棒的 talk，Efficient unteractions with Frameworks。你可以从会话末尾的 more information 链接访问视频。好的。

现在是时候谈谈每个人最喜欢的话题，security。

所以你可能注意到在 recent past 中，互联网上的一些人利用我们软件中的 bugs 来给使用我们产品的人造成问题。

作为回应，我们继续 devise 技术来 mitigate 这类 attacks，但今天我想谈谈我们如何合作来对这些 attacks 提供更强的 defense。

所以你可能听说过 defense in depth 的概念。万一你不熟悉这些术语，defense in depth 指的是创建 multiple layers of protection 来防御 threats。这个概念已经存在了几个世纪。你可以在 medieval castles 的设计中看到它。外部周围的土地清除了树木，这样你就可以看到 attackers 来临。还有 moat 来使接近 castle 更困难并防止在它下面 tunneling。walls 是另一个 defense。它们被建得 tall，这样就难爬。

walls 里有 arrow slits，顶部有 crenellations，允许 defenders 从 protected locations 向 attackers 开火。

现在这些 individual protections 中的任何一个可能都不足以 fend off 一个 attack，但 collectively 它们提供 strong defense。

像 castle 一样，我们这里在 Apple 提供 multiple layers of defense against attacks，但没有什么能阻止你在你的 App 或 framework 中也采取自己的 defensive measures。通过这样做，你添加了 another layer of protection 并改善了你的 product security。Everyone wins。所以让我们谈谈你能在这里做什么。我想让你考虑的一件事是在你的 App 或 framework 中对文本输入设置 limits。

现在我想强调，这可能并不总是 make sense。所以，例如，如果你的 App 是一个 authoring tool，像 Emily 早先展示的 journal app 那样，设置文本长度 limit 真的没有任何 sense。所以如果它 doesn't make sense，你不应该做它。

但相比之下，如果你的 phone app 有一个 text field 用于给 account 分配 nickname，你可能对 reasonable limit 有什么想法。设置这些 limits 是个好主意，因为所有文本输入都是 potentially untrusted 的。

当你允许文本输入时，你允许 copy and paste。你不知道那里可以 paste 什么 kind 的文本。

它可能是一切。它可能是带有 malicious character combinations 的 string，或者它可能只是 really, really, really long 的 string。

并且即使像那样的 long strings 本身可能不是 malicious 的，也可能导致你的 App freeze 或 hang。

所以如果你有一个 text field 旨在 one line of input，有人把 "War and Peace" 的全部内容 paste 进去，这在 English 中大约是 3.1 million characters，那是 reasonable 的吗？Probably not。

所以这是一个 make sense 对这种情况 impose 你自己的 limits 的 great example。

这里是我们设置这类 limits 的 recommended approaches。

你想在文本被设置到 text field 之前 validate 输入 string。所以对于 UITextFields，你可以通过使用 UITextFieldDelegate 来做到这一点。

对于 NSTextFields，你应该使用 custom NSFormatter 来实现你的 validation logic。哦，我们还有 some additional security enhancements 即将到来。所以请在 release notes 中留意它们，并且如果你有任何问题，本周来实验室 see us。好的。我们几乎没时间了，所以让我们 recap。

你知道如何选择合适的 control、customization point 和 customization approach，并且你知道在 correctness、performance 和 security 领域要遵循的最佳实践。

所以用这些 knowledge 去 forth 并用 TextKit 创建 great things。

哦，在你走之前，这是那个超级重要的 more information link，你可以在这里找到我们今天 reference 的所有 great past sessions 和 documentation。并且周四和周五来实验室 visit us。谢谢你，enjoy the rest of the conference。[ Applause ]
