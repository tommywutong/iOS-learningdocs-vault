---
title: 文本显示与字体
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/text-display-and-fonts
source_url: 'https://developer.apple.com/documentation/uikit/text-display-and-fonts'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/text-display-and-fonts.json'
content_hash: 'sha256:b93150bfe672d6ef'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md)

# 文本显示与字体

<sub>API 集合</sub>

显示文本、管理字体，并检查拼写。

## 主题

### Text views

- [UILabel](uilabel.md) — 显示一行或多行信息性文本的视图。
- [UITextField](uitextfield.md) — 在你的界面中显示可编辑文本区域的对象。
- [UITextView](uitextview.md) — 一个可滚动的多行文本区域。
- [Drag and drop customization](drag-and-drop-customization.md) — 扩展文本视图的标准拖放支持，使其包含自定义类型的内容。

### Text bounds sizing

- [UILetterformAwareAdjusting](uiletterformawareadjusting.md) — 用于处理包含超大字符的字体文本的排版边界大小调整行为。

### Text formatting

- [UITextFormattingCoordinator](uitextformattingcoordinator.md) — 使用标准 Mac 字体面板协调文本格式设置的对象。
- [UITextAttributesConversionHandler](uitextattributesconversionhandler.md) — 用当前字体面板设置更新文本的处理程序。

### Fonts

- [Scaling fonts automatically](scaling-fonts-automatically.md) — 使用动态字体自动缩放你界面中的文本。
- [Adding a custom font to your app](adding-a-custom-font-to-your-app.md) — 为你的 App 添加自定义字体，并在 App 界面中使用它。
- [UIFont](uifont.md) — 提供对字体特性访问的对象。
- [UIFontDescriptor](uifontdescriptor.md) — 描述字体的一组属性。
- [SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md) — 描述字体风格方面的常量。
- [UIFontMetrics](uifontmetrics.md) — 一个用于获取能自动缩放以支持动态字体的自定义字体的实用工具对象。

### Font picker

- [UIFontPickerViewController](uifontpickerviewcontroller.md) — 一个管理界面的视图控制器，用于选择系统提供或用户安装的字体。
- [UIFontPickerViewControllerDelegate](uifontpickerviewcontrollerdelegate.md) — 一组用于接收用户与字体选择器交互消息的可选方法。
- [Configuration](uifontpickerviewcontroller/configuration-swift.class.md) — 字体选择器视图控制器用来设置字体选择器的筛选条件和显示设置。

### Spell checking

- [UITextChecker](uitextchecker.md) — 一个用于检查字符串（通常是文稿的文本）中拼写错误单词的对象。

### Text manipulations

- [init(_:)](<../coretext/cttextalignment/init(__).md>) — 将 UIKit 的文本对齐常量值转换为 Core Text 使用的对应常量值。
- [NSTextAlignmentFromCTTextAlignment](<nstextalignment/init(__).md>) — 将 Core Text 的对齐常量值转换为 UIKit 中对应的常量值。

### Metrics

- [UITextPosition](uitextposition.md) — 文本容器中的一个位置——即文本显示视图中支撑字符串的一个索引。
- [UITextRange](uitextrange.md) — 文本容器中的一段字符范围，在支撑文本输入对象的字符串中具有起始索引和结束索引。
- [UITextSelectionRect](uitextselectionrect.md) — 对文稿中所选文本范围信息的封装。

## 另请参阅

### Text

- [TextKit](textkit.md) — 管理文本存储，并在你 App 的视图中对基于文本的内容执行自定义布局。
- [Keyboards and input](keyboards-and-input.md) — 配置系统键盘，创建你自己的键盘来处理输入，或检测实体键盘上的按键。
- [Writing Tools](writing-tools.md) — 为你 App 的文本视图添加 Writing Tools 支持。
- [Handwriting recognition](handwriting-recognition.md) — 配置接受文本输入的文本栏和自定义视图，以处理来自 Apple Pencil 的输入。
