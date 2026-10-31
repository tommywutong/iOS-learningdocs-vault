---
title: 文本输入与输出
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text-input-and-output
source_url: 'https://developer.apple.com/documentation/swiftui/text-input-and-output'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text-input-and-output.json'
content_hash: 'sha256:6b3e742e69789cfb'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md)

# 文本输入与输出

<sub>API 集合</sub>

显示带格式的文本，并获取用户的文本输入。

## 概述

要显示只读文本，或只读文本与图像的组合，请分别使用内置的 [Text](text.md) 或 [Label](label.md) 视图。当你需要收集用户的文本输入时，请使用合适的文本输入视图，例如 [TextField](textfield.md) 或 [TextEditor](texteditor.md)。

![](../../../attachments/a8d0f352ff6dabd1c3d1e3fdfb577250/text-input-and-output-hero@2x.png)

你可以添加视图修饰符来控制文本的字体、可选性、对齐方式、布局方向等。即使你没有定义显式的 [Text](text.md) 视图，这些修饰符也会影响其他显示文本的视图，例如控制上的标签。

有关设计指引，请参阅《人机界面指南》中的[字体排印](../design/human-interface-guidelines/typography.md)。

## 主题

### 显示文本

- [Text](text.md) — 显示一行或多行只读文本的视图。
- [Label](label.md) — 用户界面条目的标准标签，由一个图标加标题组成。
- [labelStyle(_:)](<view/labelstyle(__).md>) — 设置此视图内标签的样式。

### 获取文本输入

- [构建丰富的 SwiftUI 文本体验](building-rich-swiftui-text-experiences.md) — 使用 SwiftUI 文本编辑器视图和属性字符串构建一个用于带格式文本的编辑器。
- [TextField](textfield.md) — 显示可编辑文本界面的控制。
- [textFieldStyle(_:)](<view/textfieldstyle(__).md>) — 设置此视图内文本栏的样式。
- [SecureField](securefield.md) — 人们用来安全输入私密文本的控制。
- [TextEditor](texteditor.md) — 可以显示和编辑长篇文本的视图。

### 选择文本

- [textSelection(_:)](<view/textselection(__).md>) — 控制人们能否选择此视图内的文本。
- [TextSelectability](textselectability.md) — 一种描述选择文本能力的类型。
- [TextSelection](textselection.md) — 表示一次文本选择。
- [textSelectionAffinity(_:)](<view/textselectionaffinity(__).md>) — 设置选择或光标相对于文本字符的方向。
- [textSelectionAffinity](environmentvalues/textselectionaffinity.md) — 选择或光标相对于文本字符的方向或关联的表示。在处理双向文本（同时包含 LTR 和 RTL 文字系统的文本，例如英文与阿拉伯文混合）时，这一概念会变得更加突出。
- [TextSelectionAffinity](textselectionaffinity.md) — 选择或光标相对于文本字符的方向或关联的表示。在处理双向文本（同时包含 LTR 和 RTL 文字系统的文本，例如英文与阿拉伯文混合）时，这一概念会变得更加突出。
- [AttributedTextSelection](attributedtextselection.md) — 表示一次属性文本的选择。

### 设置字体

- [为文本应用自定义字体](applying-custom-fonts-to-text.md) — 在你的 App 中添加并使用可随动态字体缩放的字体。
- [font(_:)](<view/font(__).md>) — 设置此视图中文本的默认字体。
- [fontDesign(_:)](<view/fontdesign(__).md>) — 设置此视图中文本的字体设计。
- [fontWeight(_:)](<view/fontweight(__).md>) — 设置此视图中文本的字重。
- [fontWidth(_:)](<view/fontwidth(__).md>) — 设置此视图中文本的字体宽度。
- [font](environmentvalues/font.md) — 此环境的默认字体。
- [Font](font.md) — 一种依赖环境的字体。

### 调整文本大小

- [textScale(_:isEnabled:)](<view/textscale(__isenabled_).md>) — 对视图中的文本应用文本缩放。
- [dynamicTypeSize(_:)](<view/dynamictypesize(__).md>) — 将视图内的动态字体大小设置为给定值。
- [dynamicTypeSize](environmentvalues/dynamictypesize.md) — 当前的动态字体大小。
- [DynamicTypeSize](dynamictypesize.md) — 动态字体大小，指定可缩放内容应当有多大。
- [ScaledMetric](scaledmetric.md) — 一种对数值进行缩放的动态属性。
- [TextVariantPreference](textvariantpreference.md) — 一种控制文本视图大小变体的协议。
- [FixedTextVariant](fixedtextvariant.md) — 默认的文本变体偏好，选择最大的可用变体。
- [SizeDependentTextVariant](sizedependenttextvariant.md) — 依赖于大小的变体偏好，允许文本在选择要显示的变体时将可用空间考虑在内。

### 控制文本样式

- [bold(_:)](<view/bold(__).md>) — 对此视图中的文本应用粗体字重。
- [italic(_:)](<view/italic(__).md>) — 对此视图中的文本应用斜体。
- [underline(_:pattern:color:)](<view/underline(__pattern_color_).md>) — 对此视图中的文本应用下划线。
- [strikethrough(_:pattern:color:)](<view/strikethrough(__pattern_color_).md>) — 对此视图中的文本应用删除线。
- [textCase(_:)](<view/textcase(__).md>) — 设置此视图内文本显示时的大小写转换方式。
- [textCase](environmentvalues/textcase.md) — 一种样式覆盖，使用环境的区域设置在显示时转换 `Text` 的大小写。
- [monospaced(_:)](<view/monospaced(__).md>) — 尽可能将所有子视图的字体修改为使用当前字体的等宽变体。
- [monospacedDigit()](<view/monospaceddigit().md>) — 尽可能将所有子视图的字体修改为使用等宽数字，同时让其他字符保持按比例排布。
- [AttributedTextFormattingDefinition](attributedtextformattingdefinition.md) — 一种定义文本在视图中如何设置样式的协议。
- [AttributedTextValueConstraint](attributedtextvalueconstraint.md) — 一种定义某个属性值约束的协议。
- [AttributedTextFormatting](attributedtextformatting.md) — 与属性文本格式化定义相关的类型命名空间。

### 管理文本布局

- [truncationMode(_:)](<view/truncationmode(__).md>) — 为过长而无法放入可用空间的文本行设置截断模式。
- [truncationMode](environmentvalues/truncationmode.md) — 一个值，指示布局如何截断文本的最后一行以放入可用空间。
- [allowsTightening(_:)](<view/allowstightening(__).md>) — 设置此视图中的文本在必要时是否可以压缩字符间距，以将文本放入一行。
- [allowsTightening](environmentvalues/allowstightening.md) — 一个布尔值，指示是否应收紧字符间距以将文本放入可用空间。
- [minimumScaleFactor(_:)](<view/minimumscalefactor(__).md>) — 设置此视图中的文本为放入可用空间而缩小到的最小比例。
- [minimumScaleFactor](environmentvalues/minimumscalefactor.md) — 为使文本放入可用空间而允许缩小字号的最小比例。
- [baselineOffset(_:)](<view/baselineoffset(__).md>) — 设置此视图中文本相对于其基线的垂直偏移。
- [kerning(_:)](<view/kerning(__).md>) — 设置此视图中文本的字符间距（即字距调整）。
- [tracking(_:)](<view/tracking(__).md>) — 设置此视图中文本的字距（tracking）。
- [flipsForRightToLeftLayoutDirection(_:)](<view/flipsforrighttoleftlayoutdirection(__).md>) — 设置当布局方向为从右到左时，此视图是否水平镜像其内容。
- [TextAlignment](textalignment.md) — 文本沿水平轴的对齐位置。

### 渲染文本

- [使用 SwiftUI 创建视觉效果](creating-visual-effects-with-swiftui.md) — 使用着色器和文本渲染器添加滚动效果、丰富的颜色处理、自定义过渡和高级效果。
- [TextAttribute](textattribute.md) — 一个可以附加到文本视图上的值，文本渲染器可以查询它。
- [textRenderer(_:)](<view/textrenderer(__).md>) — 返回一个新视图，使其中任何文本视图都使用 `renderer` 来绘制自身。
- [TextRenderer](textrenderer.md) — 一个可以替换默认文本视图绘制行为的值。
- [TextProxy](textproxy.md) — 自定义文本渲染器使用的文本视图代理。

### 限制多行文本的行数

- [lineLimit(_:)](<view/linelimit(__).md>) — 将此视图中文本可占用的行数设置为一个封闭范围。
- [lineLimit(_:reservesSpace:)](<view/linelimit(__reservesspace_).md>) — 为此视图中文本可占用的行数设置一个上限。
- [lineLimit](environmentvalues/linelimit.md) — 文本在一个视图中可占用的最大行数。

### 格式化多行文本

- [lineSpacing(_:)](<view/linespacing(__).md>) — 设置此视中文本行与行之间的间距。
- [lineSpacing](environmentvalues/linespacing.md) — 一个行片段底部与下一行片段顶部之间的距离（以点为单位）。
- [multilineTextAlignment(_:)](<view/multilinetextalignment(__).md>) — 设置包含多行文本的文本视图的对齐方式。
- [multilineTextAlignment](environmentvalues/multilinetextalignment.md) — 一个环境值，指示文本视图在内容换行或包含换行符时如何对齐其各行。

### 格式化日期与时间

- [SystemFormatStyle](systemformatstyle.md) — 一组格式样式，用于在文本视图中显示实时更新的时间信息。
- [TimeDataSource](timedatasource.md) — 与时间相关的数据来源。

### 管理文本输入

- [autocorrectionDisabled(_:)](<view/autocorrectiondisabled(__).md>) — 设置是否为此视图禁用自动更正。
- [autocorrectionDisabled](environmentvalues/autocorrectiondisabled.md) — 一个布尔值，确定视图层级结构是否启用了自动更正。
- [keyboardType(_:)](<view/keyboardtype(__).md>) — 设置此视图的键盘类型。
- [scrollDismissesKeyboard(_:)](<view/scrolldismisseskeyboard(__).md>) — 配置可滚动内容与软件键盘的交互行为。
- [textContentType(_:)](<view/textcontenttype(__).md>) — 设置此视图的文本内容类型，系统在 macOS 上用户输入文本时会用它来提供建议。
- [textInputAutocapitalization(_:)](<view/textinputautocapitalization(__).md>) — 设置键盘上的 shift 键自动启用的频率。
- [TextInputAutocapitalization](textinputautocapitalization.md) — 文本输入时应用的自动大写行为类型。
- [textInputBorderShape(_:)](<view/textinputbordershape(__).md>) — 设置视图层级结构中文本输入控制的边框形状。 _(beta)_
- [TextInputBorderShape](textinputbordershape.md) — 用于绘制文本输入控制边框的形状。 _(beta)_
- [textInputCompletion(_:)](<view/textinputcompletion(__).md>) — 当此视图用作文本输入建议时，将一个完整的字符串与该视图的值关联起来
- [textInputSuggestions(_:)](<view/textinputsuggestions(__).md>) — 为此视图配置文本输入建议。
- [textInputSuggestions(_:content:)](<view/textinputsuggestions(__content_).md>) — 为此视图配置文本输入建议。
- [textInputSuggestions(_:id:content:)](<view/textinputsuggestions(__id_content_).md>) — 为此视图配置文本输入建议。
- [textContentType(_:)](<view/textcontenttype(__)-4dqqb.md>) — 设置此视图的文本内容类型，系统在 watchOS 设备上用户输入文本时会用它来提供建议。
- [textContentType(_:)](<view/textcontenttype(__)-6fic1.md>) — 设置此视图的文本内容类型，系统在 macOS 上用户输入文本时会用它来提供建议。
- [textContentType(_:)](<view/textcontenttype(__)-ufdv.md>) — 设置此视图的文本内容类型，系统在 iOS 或 tvOS 设备上用户输入文本时会用它来提供建议。
- [textInputFormattingControlVisibility(_:for:)](<view/textinputformattingcontrolvisibility(__for_).md>) — 指定人们可以用来格式化文本的系统文本格式化控制。
- [TextInputFormattingControlPlacement](textinputformattingcontrolplacement.md) — 一种结构，定义每个平台上可用的系统文本格式化控制。

### 听写文本

- [searchDictationBehavior(_:)](<view/searchdictationbehavior(__).md>) — 为 searchable 修饰符配置的任何搜索栏配置听写行为。
- [TextInputDictationActivation](textinputdictationactivation.md)
- [TextInputDictationBehavior](textinputdictationbehavior.md)

### 配置写作工具行为

- [writingToolsBehavior(_:)](<view/writingtoolsbehavior(__).md>) — 为环境中的文本和文本输入指定写作工具行为。
- [WritingToolsBehavior](writingtoolsbehavior.md) — 针对文本和文本输入的写作工具编辑体验。
- [writingToolsAffordanceVisibility(_:)](<view/writingtoolsaffordancevisibility(__).md>) — 指定系统是否应受环境影响，为文本输入视图显示写作工具入口。

### 指定文本等效项

- [typeSelectEquivalent(_:)](<view/typeselectequivalent(__).md>) — 在集合（如列表或表格）中设置显式的键入选择等效文本。

### 本地化文本

- [为本地化准备视图](preparing-views-for-localization.md) — 指定提示并添加字符串，以本地化你的 SwiftUI 视图。
- [LocalizedStringKey](localizedstringkey.md) — 用于在字符串文件或字符串字典文件中查找条目的键。
- [locale](environmentvalues/locale.md) — 视图应使用的当前区域设置。
- [typesettingLanguage(_:isEnabled:)](<view/typesettinglanguage(__isenabled_).md>) — 指定排版语言。
- [TypesettingLanguage](typesettinglanguage.md) — 定义如何确定文本的排版语言。

### 已废弃的类型

- [ContentSizeCategory](contentsizecategory.md) — 你可以为内容指定的大小。 _(已废弃)_

## 另请参阅

### 视图

- [视图基础](view-fundamentals.md) — 使用视图层级结构定义你的 App 的视觉元素。
- [视图配置](view-configuration.md) — 调整层级结构中视图的特性。
- [视图样式](view-styles.md) — 为不同类型的视图应用内置和自定义的外观与行为。
- [动画](animations.md) — 创建流畅的视觉更新以响应状态变化。
- [图像](images.md) — 向你的 App 的用户界面添加图像和符号。
- [控制与指示符](controls-and-indicators.md) — 显示值并获取用户的选择。
- [菜单与命令](menus-and-commands.md) — 以节省空间、依赖上下文的方式提供对命令和控制的访问。
- [形状](shapes.md) — 用颜色、渐变或其他图案描边和填充内置及自定义形状。
- [绘图与图形](drawing-and-graphics.md) — 用图形效果和自定义绘图增强你的视图。
