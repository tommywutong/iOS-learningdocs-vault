---
title: TextKit
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/textkit
source_url: 'https://developer.apple.com/documentation/uikit/textkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/textkit.json'
content_hash: 'sha256:776792db3f01a426'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md)

# TextKit

<sub>API 集合</sub>

管理文本存储，并在你 App 的视图中对基于文本的内容执行自定义布局。

## 概述

TextKit 是 UIKit 和 AppKit 中提供的一个功能强大且用途广泛的文本布局与渲染引擎。它提供了多个用于控制文本布局的类，包括 [NSTextLayoutManager](nstextlayoutmanager.md)、[NSTextContentStorage](nstextcontentstorage.md)、[NSTextViewportLayoutController](nstextviewportlayoutcontroller.md) 和 [NSTextContainer](nstextcontainer.md)。

在 UIKit 中，你可以使用 [UITextView](uitextview.md)，它将 TextKit 的能力打包起来，提供了便捷的文本渲染与编辑体验。[UITextView](uitextview.md) 使用 [NSTextContentStorage](nstextcontentstorage.md) 作为文本支撑存储的管理器。[NSTextContentStorage](nstextcontentstorage.md) 使用 [NSTextStorage](nstextstorage.md) 的一个实例作为支撑存储，它是 [NSMutableAttributedString](../foundation/nsmutableattributedstring.md) 的子类。相关示例请参阅 [Enriching your text in text views](enriching-your-text-in-text-views.md)。

此外，你也可以使用自己的 `UIView` 或 `CALayer`，通过渲染 TextKit 文本引擎提供的文本来构建自定义文本视图。如果你想要一种与 [NSAttributedString](../foundation/nsattributedstring.md) 相关的存储类型，请使用 [NSTextContentStorage](nstextcontentstorage.md)；如果想使用自己的存储类型，请对 [NSTextContentManager](nstextcontentmanager.md) 进行子类化。相关示例请参阅 [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md)。

使用 [UITextView](uitextview.md) 时，可以通过该视图的 [textLayoutManager](uitextview/textlayoutmanager.md)、[textContainer](uitextview/textcontainer.md) 和 [textStorage](uitextview/textstorage.md) 属性来访问 TextKit 引擎。[UITextView](uitextview.md) 提供了对两种布局引擎的访问：使用 [NSTextLayoutManager](nstextlayoutmanager.md) 的现代版 [textLayoutManager](uitextview/textlayoutmanager.md)，以及使用 [NSLayoutManager](nslayoutmanager.md) 的旧版 [layoutManager](uitextview/layoutmanager.md)。使用 [textLayoutManager](uitextview/textlayoutmanager.md) 可以获得更好的性能，以及对国际化语言的支持。由于 TextKit 的类在 UIKit 和 AppKit 中都可用，同样的技术适用于 iOS、iPadOS、macOS、tvOS 和 visionOS。

## 主题

### Text management

- [NSTextContentStorage](nstextcontentstorage.md) — 一个具体对象，用于管理你视图的文本内容，并生成布局所需的文本元素。
- [NSTextContentManager](nstextcontentmanager.md) — 一个抽象类，定义了管理文本文稿内容的接口和默认实现。
- [NSAttributedString](../foundation/nsattributedstring.md) — 一段文本字符串，为字符范围管理数据、布局和样式信息，以支持渲染。
- [NSMutableAttributedString](../foundation/nsmutableattributedstring.md) — 一个可变字符串，其文本各部分带有关联属性（例如视觉样式、超链接或辅助功能数据）。

### Formatting and attributes

- [NSParagraphStyle](nsparagraphstyle.md) — 属性字符串的段落或标尺属性。
- [NSMutableParagraphStyle](nsmutableparagraphstyle.md) — 一个用于更改段落样式属性中子属性值的对象。
- [NSTextTab](nstexttab.md) — 段落中的一个制表符。
- [NSTextList](nstextlist.md) — 构成单个列表的一段文本。
- [Adding tables to attributed strings in UIKit](adding-tables-to-attributed-strings.md) — 在属性字符串中创建和配置表格，并将其显示在文本视图中。

### Tables

- [Adding tables to attributed strings in UIKit](adding-tables-to-attributed-strings.md) — 在属性字符串中创建和配置表格，并将其显示在文本视图中。
- [NSTextTable](nstexttable.md) — 一个对象，表示属性字符串中由行和列组成的表格。
- [NSTextTableBlock](nstexttableblock.md) — 一个文本块，表示文本表格中的单个单元格。
- [NSTextBlock](nstextblock.md) — 一个对象，定义属性字符串中某个文本块的大小、间距和外观。

### Content elements

- [Enriching your text in text views](enriching-your-text-in-text-views.md) — 在文本视图中支持行号显示、区块折叠、内联附件缓存、排除路径、文本附件和文本列表。
- [NSTextParagraph](nstextparagraph.md) — 一个类，表示以属性字符串作为内容支撑的单个段落。
- [NSTextListElement](nstextlistelement.md) — 一个类，表示文本列表节点。
- [NSTextElement](nstextelement.md) — 一个抽象基类，表示文本布局的最小单元，例如段落或附件。
- [NSTextElementProvider](nstextelementprovider.md) — 一个协议，文本内容管理器及其具体子类均遵循该协议，它定义了与文本文稿自定义内容类型交互的接口。

### Location and selection

- [NSTextRange](nstextrange.md) — 一个类，表示文稿内容中两个位置之间的一段连续范围。
- [NSTextSelection](nstextselection.md) — 一个类，表示对应于某个插入点的单个逻辑选择上下文。
- [NSTextSelectionNavigation](nstextselectionnavigation.md) — 一个接口，你用它来公开从对文本选择执行的操作中获取结果的方法。
- [NSTextLocation](nstextlocation.md) — 一个你实现的接口，表示你文稿内容中的一个抽象位置。

### Layout

- [Using TextKit 2 to interact with text](using-textkit-2-to-interact-with-text.md) — 通过管理文本选择和插入自定义文本元素来与文本交互。
- [Display text with a custom layout](display-text-with-a-custom-layout.md) — 在自定义形状的容器中布局文本，并应用字形替换。
- [Managing viewport layout and attachment reuse in text views](managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md) — 在你的文本视图子类中自定义布局，并保留附件视图。
- [NSTextLayoutManager](nstextlayoutmanager.md) — 用于管理自定义文本显示的文本布局和呈现的主要类。
- [NSTextContainer](nstextcontainer.md) — 进行文本布局的一处区域。
- [NSTextLayoutFragment](nstextlayoutfragment.md) — 一个类，表示通常对应于某个渲染表面（例如图层或视图子类）的布局片段。
- [NSTextLineFragment](nstextlinefragment.md) — 一个类，将行片段表示为文本布局片段内部作为单一文本布局与渲染单元的对象。
- [NSTextViewportLayoutController](nstextviewportlayoutcontroller.md) — 管理视口内部的布局过程，并与其委托对象交互。
- [NSTextViewportRenderingSurface](nstextviewportrenderingsurface.md) — 一个协议，用于将某个视图或图层标识为文本布局片段的可绘制元素。_(beta)_
- [NSTextViewportRenderingSurfaceKey](nstextviewportrenderingsurfacekey.md) — 一个协议，让你在存储或获取某个渲染表面时，可以使用一个对象来标识它。
- [NSTextLayoutOrientationProvider](nstextlayoutorientationprovider.md) — 一组方法，为某个对象定义文本的方向。

### Attachments

- [NSTextAttachment](nstextattachment.md) — 属性字符串及相关对象的附件特性值。
- [NSTextAttachmentViewProvider](nstextattachmentviewprovider.md) — 一个容器对象，将文稿中特定位置的文本附件与一个视图对象关联起来。
- [NSAdaptiveImageGlyph](nsadaptiveimageglyph.md) — 一个数据对象，用于表示可以出现在属性文本中的类似 emoji 的图像。
- [NSTextAttachmentContainer](nstextattachmentcontainer.md) — 一组方法，定义了从布局管理器访问文本附件对象的接口。
- [NSTextAttachmentLayout](nstextattachmentlayout.md) — 一组方法，定义了从文本布局管理器访问附件对象的接口。

### TextKit 1

- [NSTextStorage](nstextstorage.md) — TextKit 的基础存储机制，包含由系统管理的文本。
- [NSLayoutManager](nslayoutmanager.md) — 一个对象，协调文本字符的布局和显示。

## 另请参阅

### Text

- [Text display and fonts](text-display-and-fonts.md) — 显示文本、管理字体，并检查拼写。
- [Keyboards and input](keyboards-and-input.md) — 配置系统键盘，创建你自己的键盘来处理输入，或检测实体键盘上的按键。
- [Writing Tools](writing-tools.md) — 为你 App 的文本视图添加 Writing Tools 支持。
- [Handwriting recognition](handwriting-recognition.md) — 配置接受文本输入的文本栏和自定义视图，以处理来自 Apple Pencil 的输入。
