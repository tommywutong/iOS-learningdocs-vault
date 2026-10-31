---
title: 为系统视图自定 Writing Tools 行为
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/customizing-writing-tools-behavior-for-system-views
source_url: 'https://developer.apple.com/documentation/uikit/customizing-writing-tools-behavior-for-system-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/customizing-writing-tools-behavior-for-system-views.json'
content_hash: 'sha256:c1f84887a7b2e70a'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Writing Tools](writing-tools.md)

# 为系统视图自定 Writing Tools 行为

<sub>文章</sub>

修改标准 iOS 文本视图中的 Writing Tools 行为，并在该功能激活时调整你的 App 的行为。

## 概述

[UITextView](uitextview.md) 和 [UITextField](uitextfield.md) 类内置了对 Writing Tools 的支持，但你可以为你的界面自定该功能的工作方式。你可能希望更改某人在你的 App 中体验 Writing Tools 的方式，或为特定类型的内容禁用该功能。例如，你可能在用于显示代码列表的视图中禁用 Writing Tools。你还可以自定 Writing Tools 为你的文本视图生成的内容类型。

> [!note] 注意
> 如果你创建的是自定文本视图，而非使用标准系统视图，请使用可用的 API 为你的视图添加 Writing Tools 支持。更多信息，参见 [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)。

### 指定你想要的 Writing Tools UI 体验

Writing Tools 支持 Writing Tools 体验的受限版本和完整版本。受限体验在 Writing Tools 界面中保留更改，直到用户批准它们。受限体验内联显示更改，与视图其余内容并列。两种体验都让用户能够接受或拒绝更改，但完整体验提供了更交互式的方式来查看这些更改。

要指定你想要的体验，请更改视图的 [writingToolsBehavior](uitextinputtraits/writingtoolsbehavior.md) 属性的值。默认情况下系统会把最佳可用体验应用于视图，但你可以在视图中指定你偏好的体验。如果你不希望 Writing Tools 在你的视图中激活，也可以禁用该功能。要禁用该功能，把此属性的值设为 [UIWritingToolsBehaviorNone](uiwritingtoolsbehavior/none.md)。

### Writing Tools 激活时修改你的 App 的行为

Writing Tools 的大语言模型（LLM）需要时间来建议更改。用户也需要时间来审查更改并批准它们。在这些事情发生时，Writing Tools 可能会临时更改你的视图内容。在此期间，禁用任何可能干扰 Writing Tools 操作的 App 特定功能。例如，你可能选择在 Writing Tools 激活时禁用文本的基于云的更新。

在 [UITextView](uitextview.md) 中，你可以使用委托对象来确定 Writing Tools 何时激活。当文本视图使用完整体验时，系统在 Writing Tools 进行任何修改之前调用委托的 [- textViewWritingToolsWillBegin:](<uitextviewdelegate/textviewwritingtoolswillbegin(__).md>) 方法，并在合并任何最终更改之后调用 [- textViewWritingToolsDidEnd:](<uitextviewdelegate/textviewwritingtoolsdidend(__).md>) 方法。对于受限体验，系统转而调用文本视图的 [- willPresentWritingTools](<uitextinput/willpresentwritingtools().md>) 和 [- didDismissWritingTools](<uitextinput/diddismisswritingtools().md>) 方法。使用这些方法在 Writing Tools 激活时关闭任何可能干扰它的功能。

### 指定 Writing Tools 应忽略的文本范围

如果你不希望 Writing Tools 修改 [UITextView](uitextview.md) 对象的某些部分，请在委托中实现 [- textView:writingToolsIgnoredRangesInEnclosingRange:](<uitextviewdelegate/textview(__writingtoolsignoredrangesinenclosingrange_).md>) 方法。Writing Tools 为每次操作调用该方法，并提供它正在考虑的文本范围。使用你的方法实现来指定任何你希望 Writing Tools 忽略的文本子范围。你可能使用此方法来防止 Writing Tools 更改代码列表、专有名词或嵌入在文本中的直接引语。

## 另请参阅

### 配置

- [UIWritingToolsBehavior](uiwritingtoolsbehavior.md) — 指定底层视图的 Writing Tools 体验的常量。
- [UIWritingToolsResultOptions](uiwritingtoolsresultoptions.md) — 指定在 Writing Tools 建议或重写中允许的内容类型常量。
