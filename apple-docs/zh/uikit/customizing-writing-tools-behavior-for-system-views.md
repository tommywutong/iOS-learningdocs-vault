---
title: 为 UIKit 视图自定义写作工具行为
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

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [写作工具](writing-tools.md)

# 为 UIKit 视图自定义写作工具行为

<sub>文章</sub>

修改写作工具（Writing Tools）在标准 iOS 文本视图中的行为，并在该功能处于活动状态时调整你的 App 的行为。

## 概述

[UITextView](uitextview.md) 和 [UITextField](uitextfield.md) 类内建了对写作工具（Writing Tools）的支持，但你可以为你的界面自定义这一功能的工作方式。你可以改变用户在你的 App 中体验写作工具的方式，或对特定类型的内容禁用它。例如，你可以在用于显示代码清单的视图中禁用写作工具。你还可以自定义写作工具为你的文本视图生成的内容类型。

> [!note] 注意
> 如果你创建的是自定义文本视图而非使用标准系统视图，请使用可用的 API 为你的视图添加写作工具支持。更多信息参见[为自定义 UIKit 视图添加写作工具支持](adding-writing-tools-support-to-a-custom-uiview.md)。

### 指定你想要的写作工具 UI 体验

写作工具同时支持有限版与完整版的写作工具体验。有限体验会把改动保留在写作工具界面中，直到用户批准它们。有限体验会把改动内联显示在你视图内容的其余部分之中。两种体验都允许用户接受或拒绝改动，但完整体验提供了一种更具交互性的方式来查看这些改动。

要指定你想要的体验，更改你的视图的 [writingToolsBehavior](uitextinputtraits/writingtoolsbehavior.md) 属性的值。默认情况下，系统会为视图应用可用的最佳体验，但你可以在视图中指定你偏好的体验。如果你不想在你的视图中启用写作工具，也可以禁用它。要禁用该功能，把此属性的值设为 [UIWritingToolsBehaviorNone](uiwritingtoolsbehavior/none.md)。

### 在写作工具活动期间修改你的 App 的行为

写作工具的大型语言模型（LLM）提出修改建议需要时间。用户审阅并批准这些改动也需要时间。在这些事情发生期间，写作工具可能会对你的视图内容做临时改动。此时应禁用任何可能干扰写作工具运行的 App 专属功能。例如，你可以选择在写作工具活动期间禁用你的基于云的文本更新。

在 [UITextView](uitextview.md) 中，你可以通过委托对象判断写作工具何时处于活动状态。当文本视图使用完整体验时，系统会在写作工具做任何修改之前调用委托的 [- textViewWritingToolsWillBegin:](<uitextviewdelegate/textviewwritingtoolswillbegin(__).md>) 方法，并在并入所有最终改动之后调用 [- textViewWritingToolsDidEnd:](<uitextviewdelegate/textviewwritingtoolsdidend(__).md>) 方法。对于有限体验，系统会改为调用文本视图的 [- willPresentWritingTools](<uitextinput/willpresentwritingtools().md>) 和 [- didDismissWritingTools](<uitextinput/diddismisswritingtools().md>) 方法。用这些方法关闭任何可能在写作工具活动期间干扰它的功能。

### 指定写作工具要忽略的文本范围

如果你不想让写作工具修改你的 [UITextView](uitextview.md) 对象的某些部分，在你的委托中实现 [- textView:writingToolsIgnoredRangesInEnclosingRange:](<uitextviewdelegate/textview(__writingtoolsignoredrangesinenclosingrange_).md>) 方法。写作工具在每次操作时都会调用该方法，把它正在考虑的文本范围提供给你。在该方法的实现中指定你希望写作工具忽略的任何子范围。你可以用这个方法阻止写作工具改动代码清单、专有名称或文本中嵌入的直接引语。

## 另请参阅

### 配置

- [UIWritingToolsBehavior](uiwritingtoolsbehavior.md) — 为底层视图指定写作工具体验的常量。
- [UIWritingToolsResultOptions](uiwritingtoolsresultoptions.md) — 指定写作工具建议或改写中允许的内容类型的常量。
