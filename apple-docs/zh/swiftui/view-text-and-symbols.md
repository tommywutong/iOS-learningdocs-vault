---
title: 文本与符号修饰符
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-text-and-symbols
source_url: 'https://developer.apple.com/documentation/swiftui/view-text-and-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-text-and-symbols.json'
content_hash: 'sha256:381642903e94b2a9'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [视图基础](view-fundamentals.md) · [View](view.md)

# 文本与符号修饰符

<sub>API 集合</sub>

管理视图中文本的渲染、选择和输入。

## 概述

SwiftUI 提供了向用户显示文本的内置视图，例如 [Text](text.md) 和 [Label](label.md)，以及从用户收集文本的视图，例如 [TextField](textfield.md) 和 [TextEditor](texteditor.md)。使用文本与符号修饰符来控制 SwiftUI 显示和管理这些文本的方式。例如，你可以设置字体、指定文本布局参数，并指明期望的输入类型。

要了解用于显示文本的视图类型以及配置这些视图的方式，请参阅[文本输入与输出](text-input-and-output.md)。

## 主题

### 字体

- [font(_:)](<view/font(__).md>) — 为此视图中的文本设置默认字体。

### 动态字体

- [dynamicTypeSize(_:)](<view/dynamictypesize(__).md>) — 将视图内的动态字体大小设置为给定值。

### 文本样式

- [bold(_:)](<view/bold(__).md>) — 为此视图中的文本应用粗体字重。
- [fontDesign(_:)](<view/fontdesign(__).md>) — 设置此视图中文本的字体设计。
- [fontWeight(_:)](<view/fontweight(__).md>) — 设置此视图中文本的字重。
- [fontWidth(_:)](<view/fontwidth(__).md>) — 设置此视图中文本的字体宽度。
- [italic(_:)](<view/italic(__).md>) — 为此视图中的文本应用斜体。
- [monospaced(_:)](<view/monospaced(__).md>) — 在可能的情况下，将所有子视图的字体修改为使用当前字体的等宽变体。
- [monospacedDigit()](<view/monospaceddigit().md>) — 在可能的情况下，将所有子视图的字体修改为使用等宽数字，同时让其他字符保持比例间距。
- [strikethrough(_:pattern:color:)](<view/strikethrough(__pattern_color_).md>) — 为此视图中的文本应用删除线。
- [textCase(_:)](<view/textcase(__).md>) — 设置此视图所包含文本在显示时的大小写变换。
- [textScale(_:isEnabled:)](<view/textscale(__isenabled_).md>) — 为视图中的文本应用文本缩放。
- [textRenderer(_:)](<view/textrenderer(__).md>) — 返回一个新视图，其中的任何文本视图都将使用 `renderer` 来绘制自身。
- [underline(_:pattern:color:)](<view/underline(__pattern_color_).md>) — 为此视图中的文本应用下划线。
- [attributedTextFormattingDefinition(_:)](<view/attributedtextformattingdefinition(__).md>) — 为嵌套视图应用文本格式定义。

### 标签配置

- [labelIconToTitleSpacing(_:)](<view/labelicontotitlespacing(__).md>) — 设置标签中图标与标题之间的间距。
- [labelReservedIconWidth(_:)](<view/labelreservediconwidth(__).md>) — 设置标签中为图标保留的宽度。

### 文本布局

- [allowsTightening(_:)](<view/allowstightening(__).md>) — 设置此视图中的文本在必要时是否可以压缩字符之间的空隙，以将文本排入一行。
- [baselineOffset(_:)](<view/baselineoffset(__).md>) — 设置此视图中文本相对于其基线的垂直偏移量。
- [flipsForRightToLeftLayoutDirection(_:)](<view/flipsforrighttoleftlayoutdirection(__).md>) — 设置当布局方向为从右到左时，此视图是否水平镜像其内容。
- [kerning(_:)](<view/kerning(__).md>) — 设置此视图中文本的字符间距（即字距调整）。
- [lineHeight(_:)](<view/lineheight(__).md>) — 视图层级结构中默认行高的修饰符。
- [minimumScaleFactor(_:)](<view/minimumscalefactor(__).md>) — 设置此视图中的文本为适应可用空间而可以缩小的最小比例。
- [tracking(_:)](<view/tracking(__).md>) — 设置此视图中文本的字距。
- [truncationMode(_:)](<view/truncationmode(__).md>) — 为长到无法放入可用空间的文本行设置截断模式。
- [typesettingLanguage(_:isEnabled:)](<view/typesettinglanguage(__isenabled_).md>) — 指定排版语言。
- [writingDirection(strategy:)](<view/writingdirection(strategy_).md>) — 视图层级结构中默认文本书写方向策略的修饰符。

### 多行文本

- [lineLimit(_:)](<view/linelimit(__).md>) — 将文本在此视图中可占用的行数设置为一个闭区间。
- [lineLimit(_:reservesSpace:)](<view/linelimit(__reservesspace_).md>) — 设置文本在此视图中可占用行数的上限。
- [lineSpacing(_:)](<view/linespacing(__).md>) — 设置此视图中文本行与行之间的间距。
- [multilineTextAlignment(_:)](<view/multilinetextalignment(__).md>) — 设置包含多行文本的文本视图的对齐方式。
- [multilineTextAlignment(strategy:)](<view/multilinetextalignment(strategy_).md>) — 视图层级结构中默认文本对齐策略的修饰符。

### 文本选择

- [textSelection(_:)](<view/textselection(__).md>) — 控制人们是否可以选择此视图内的文本。
- [textSelectionAffinity(_:)](<view/textselectionaffinity(__).md>) — 设置选区或光标相对于文本字符的方向。

### 数据检测

- [dataDetection(_:options:)](<view/datadetection(__options_).md>) — 异步检测视图内容中的数据，并为其设置样式以表明可点击。 _(beta)_

### 文本输入

- [autocorrectionDisabled(_:)](<view/autocorrectiondisabled(__).md>) — 设置是否对此视图停用自动更正。
- [keyboardType(_:)](<view/keyboardtype(__).md>) — 设置此视图的键盘类型。
- [scrollDismissesKeyboard(_:)](<view/scrolldismisseskeyboard(__).md>) — 配置可滚动内容与软件键盘交互的行为。
- [textInputAutocapitalization(_:)](<view/textinputautocapitalization(__).md>) — 设置键盘的 shift 键自动启用的频率。
- [textInputBorderShape(_:)](<view/textinputbordershape(__).md>) — 设置视图层级结构中文本输入控制的边框形状。 _(beta)_
- [textInputCompletion(_:)](<view/textinputcompletion(__).md>) — 当此视图用作文本输入建议时，将一个完整成形的字符串与其值关联
- [textInputSuggestions(_:)](<view/textinputsuggestions(__).md>) — 为此视图配置文本输入建议。
- [textInputSuggestions(_:content:)](<view/textinputsuggestions(__content_).md>) — 为此视图配置文本输入建议。
- [textInputSuggestions(_:id:content:)](<view/textinputsuggestions(__id_content_).md>) — 为此视图配置文本输入建议。
- [textContentType(_:)](<view/textcontenttype(__).md>) — 设置此视图的文本内容类型，系统在用户于 macOS 上输入文本时用它来提供建议。
- [textContentType(_:)](<view/textcontenttype(__)-4dqqb.md>) — 设置此视图的文本内容类型，系统在用户于 watchOS 设备上输入文本时用它来提供建议。
- [textContentType(_:)](<view/textcontenttype(__)-6fic1.md>) — 设置此视图的文本内容类型，系统在用户于 macOS 上输入文本时用它来提供建议。
- [textContentType(_:)](<view/textcontenttype(__)-ufdv.md>) — 设置此视图的文本内容类型，系统在用户于 iOS 或 tvOS 设备上输入文本时用它来提供建议。
- [textInputFormattingControlVisibility(_:for:)](<view/textinputformattingcontrolvisibility(__for_).md>) — 指定哪些系统文本格式控制可供人们用来编排文本格式。

### 查找与替换

- [findNavigator(isPresented:)](<view/findnavigator(ispresented_).md>) — 以编程方式呈现文本编辑器视图的查找和替换界面。
- [findDisabled(_:)](<view/finddisabled(__).md>) — 阻止文本编辑器中的查找和替换操作。
- [replaceDisabled(_:)](<view/replacedisabled(__).md>) — 阻止文本编辑器中的替换操作。

### 符号外观

- [symbolRenderingMode(_:)](<view/symbolrenderingmode(__).md>) — 设置此视图内符号图像的渲染模式。
- [symbolColorRenderingMode(_:)](<view/symbolcolorrenderingmode(__).md>) — 设置符号图像的颜色渲染模式。
- [symbolVariableValueMode(_:)](<view/symbolvariablevaluemode(__).md>) — 设置此视图内符号图像的变量值模式。
- [symbolVariant(_:)](<view/symbolvariant(__).md>) — 让视图内的符号显示特定的变体。

### 书写工具

- [writingToolsAffordanceVisibility(_:)](<view/writingtoolsaffordancevisibility(__).md>) — 指定系统是否应为受环境影响的文本输入视图显示书写工具入口。
- [writingToolsBehavior(_:)](<view/writingtoolsbehavior(__).md>) — 为环境中的文本和文本输入指定书写工具行为。
- [WritingToolsBehavior](writingtoolsbehavior.md) — 文本和文本输入的书写工具编辑体验。

## 另请参阅

### 配置视图元素

- [辅助功能修饰符](view-accessibility.md) — 让你的 SwiftUI App 对每个人（包括残障人士）都具备辅助功能。
- [外观修饰符](view-appearance.md) — 配置视图的前景和背景样式、控制以及可见性。
- [辅助视图修饰符](view-auxiliary-views.md) — 添加并配置工具栏和上下文菜单等辅助视图。
- [图表视图修饰符](view-chart-view.md) — 配置你用 Swift Charts 声明的图表。
