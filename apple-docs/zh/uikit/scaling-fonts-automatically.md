---
title: 自动缩放字体
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/scaling-fonts-automatically
source_url: 'https://developer.apple.com/documentation/uikit/scaling-fonts-automatically'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/scaling-fonts-automatically.json'
content_hash: 'sha256:a7ad3600ba49463c'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Text display and fonts](text-display-and-fonts.md)

# 自动缩放字体

<sub>文章</sub>

使用动态字体自动缩放界面中的文本。

## 概述

动态字体（Dynamic Type）功能允许用户选择屏幕上显示的文本内容的大小。它能帮助那些需要更大文本以获得更好可读性的用户，也能照顾那些能够阅读较小文本、希望屏幕上显示更多信息的用户。支持动态字体的 App 还能提供更一致的阅读体验。

要在你的 App 中添加对动态字体的支持，你需要使用 _文本样式_。文本样式描述了文本的用途，例如 [UIFontTextStyleHeadline](uifont/textstyle/headline.md)、[UIFontTextStyleBody](uifont/textstyle/body.md) 或 [UIFontTextStyleTitle1](uifont/textstyle/title1.md)，并让系统知道最适合如何调整其大小。你可以在 Interface Builder 中或在源代码里配置文本样式。

虽然动态字体支持自定字体，但首选字体（preferred font）在任何大小下都经过精心设计，效果良好。此外，使用首选字体能确保系统内部以及与其他 App 之间的一致性。更多信息，请参阅《人机界面指南》\> [字体排印](../design/human-interface-guidelines/typography.md)。

### 使用 Interface Builder 配置文本样式

在 Interface Builder 中，从字体菜单里选择文本样式，然后勾选动态字体右侧的"自动调整字体"复选框。

![](../../../attachments/a30c513f66f2dd990f56a243f17807df/scaling-fonts-automatically-1@2x.png)

<sub>Interface Builder 的局部屏幕截图，一个箭头指向所选标签的属性检查器中作为所选字体的文本样式"Body"。字体选择下方是"动态字体"标签，"自动调整字体"复选框已勾选。</sub>

### 在源代码中配置文本样式

在你的源代码中，调用 [+ preferredFontForTextStyle:](<uifont/preferredfont(fortextstyle_).md>) 方法。该方法返回一个可以赋给标签、文本栏或文本视图的 [UIFont](uifont.md)。接下来，将文本控制上的 [adjustsFontForContentSizeCategory](uicontentsizecategoryadjusting/adjustsfontforcontentsizecategory.md) 属性设置为 [true](../swift/true.md)。这项设置会告诉文本控制根据用户提供的动态字体设置调整文本大小。

```swift
label.font = UIFont.preferredFont(forTextStyle: .body)
label.adjustsFontForContentSizeCategory = true
```

如果 [adjustsFontForContentSizeCategory](uicontentsizecategoryadjusting/adjustsfontforcontentsizecategory.md) 属性被设置为 [false](../swift/false.md)，字体最初会是正确的大小，但不会响应用户在"设置"或控制中心里所做的文本大小更改。要检测此类更改，请在你的视图或视图控制器中重写 [- traitCollectionDidChange:](<uitraitenvironment/traitcollectiondidchange(__).md>) 方法，并检查内容大小类别特性是否发生了变化。你也可以观察 [UIContentSizeCategoryDidChangeNotification](uicontentsizecategory/didchangenotification.md)，并在通知到达时更新字体。

如果你在 App 中使用自定字体，并且希望让用户控制文本大小，你必须在源代码中创建该字体的一个缩放实例。调用 [- scaledFontForFont:](<uifontmetrics/scaledfont(for_).md>)，传入一个采用适合 [UIContentSizeCategoryLarge](uicontentsizecategory/large.md) 使用的点大小的自定字体引用。这是动态字体设置的默认值。你可以在默认字体指标上使用这个调用，也可以指定一种文本样式，例如 [UIFontTextStyleHeadline](uifont/textstyle/headline.md)。

```swift
guard let customFont = UIFont(name: "CustomFont-Light", size: UIFont.labelFontSize) else {
    fatalError("""
        Failed to load the "CustomFont-Light" font.
        Make sure the font file is included in the project and the font name is spelled correctly.
        """
    )
}
label.font = UIFontMetrics(forTextStyle: .headline).scaledFont(for: customFont)
label.adjustsFontForContentSizeCategory = true
```

> [!note] 注意
> 在 Interface Builder 中，自动调整字体的动态字体选项仅适用于文本样式或由 [UIFontMetrics](uifontmetrics.md) 返回的缩放字体。它对在 Interface Builder 中设置的自定字体没有任何效果。

通过 [UIFontMetrics](uifontmetrics.md) 创建的字体，其行为与系统提供的首选字体相同。系统会以类似于你所提供文本样式缩放的方式，缩放以匹配用户所选的文本大小。

## 另请参阅

### 字体

- [Adding a custom font to your app](adding-a-custom-font-to-your-app.md) — 为你的 App 添加自定字体，并在 App 的界面中使用它。
- [UIFont](uifont.md) — 一个提供对字体特征访问的对象。
- [UIFontDescriptor](uifontdescriptor.md) — 描述字体的一组属性的集合。
- [SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md) — 描述字体样式方面的常量。
- [UIFontMetrics](uifontmetrics.md) — 一个用于获取支持动态字体缩放的自定字体的实用工具对象。
