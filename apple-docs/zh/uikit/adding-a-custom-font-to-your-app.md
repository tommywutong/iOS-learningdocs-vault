---
title: 为你的 App 添加自定字体
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adding-a-custom-font-to-your-app
source_url: 'https://developer.apple.com/documentation/uikit/adding-a-custom-font-to-your-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adding-a-custom-font-to-your-app.json'
content_hash: 'sha256:39ee01811d497793'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [文本显示与字体](text-display-and-fonts.md)

# 为你的 App 添加自定字体

<sub>文章</sub>

为你的 App 添加自定字体，并在 App 的界面中使用它。

## 概述

你的 App 并不限于使用 iOS 提供的自定字体。例如，如果你的公司有自己的品牌字体，就可以在你的 App 中使用它。把包含你的字体的字体文件添加到 App bundle 中，然后像使用任何 iOS 提供的自定字体一样使用你的字体。

### 将字体文件添加到你的 Xcode 项目

要将字体文件添加到你的 Xcode 项目，可以从菜单栏选取 _File \> Add Files to “Your Project Name”_，或者把文件从访达（Finder）拖放进你的 Xcode 项目。你可以添加 True Type Font（.ttf）和 Open Type Font（.otf）文件。

![项目导航器的屏幕快照，显示已添加到 CustomFont 项目中的自定字体文件。](../../../attachments/16adcb2425ff69c1754dac73fdc4ab7b/adding-a-custom-font-to-your-app-1@2x.png)

另外，请确保该字体文件是你的 App 的一个 target 成员；否则，项目不会把这个字体文件作为你 App 的一部分分发。

![文件检查器的屏幕快照，显示所选字体文件是 CustomFont target 的成员。](../../../attachments/d6e6408416bdd2136be6d6f9d4bc0261/adding-a-custom-font-to-your-app-2@2x.png)

### 向 iOS 注册你的字体文件

把字体文件添加到项目后，你需要让 iOS 知道这个字体。为此，在信息属性列表（information property list）中添加“Fonts provided by application”键（原始键名为 `UIAppFonts`）。Xcode 会为该键创建一个数组值；把每个字体文件的名称作为条目添加到该数组中。务必让文件扩展名成为名称的一部分。

![](../../../attachments/c26b6e009ff7648d7b3108a0362511de/adding-a-custom-font-to-your-app-3@2x.png)

<sub>Xcode 的屏幕快照，显示 Info.plist 文件的内容。“Fonts provided by application”键包含两个字体文件的文件名。</sub>

把你添加到项目中的每个字体文件都收录进这个数组；否则，你的 App 将无法使用该字体。

### 在 Interface Builder 中使用你的自定字体

把字体文件添加到你的 Xcode 项目及其 _Info.plist_ 之后，就可以开始把该字体指定给 [UILabel](uilabel.md) 和 [UITextField](uitextfield.md) 这类 UI 对象了。如果你在使用 Interface Builder，可以使用属性检查器（Attribute Inspector）把 UI 对象的 _Font_ 设置指定为你的自定字体。

![Interface Builder 的屏幕快照，显示标签的字体为“CustomFont 17.0”。](../../../attachments/da57e8ce6b34b8e2896a97931995291d/adding-a-custom-font-to-your-app-4@2x.png)

### 在源代码中使用你的自定字体

你可以在源代码中创建自定字体的实例。为此，你需要知道字体名称。然而，字体名称并不总是显而易见的，也很少与字体文件名一致。查找字体名称的一个快捷方法是获取你的 App 可用的字体列表，你可以用以下代码来实现：

```swift
for family in UIFont.familyNames.sorted() {
    let names = UIFont.fontNames(forFamilyName: family)
    print("Family: \(family) Font names: \(names)")
}
```

知道字体名称后，使用 [UIFont](uifont.md) 创建这个自定字体的实例。如果你的 App 支持“动态字体”（Dynamic Type），你还可以获取你的字体的一个缩放实例，如下所示：

```swift
guard let customFont = UIFont(name: "CustomFont-Light", size: UIFont.labelFontSize) else {
    fatalError("""
        Failed to load the "CustomFont-Light" font.
        Make sure the font file is included in the project and the font name is spelled correctly.
        """
    )
}
label.font = UIFontMetrics.default.scaledFont(for: customFont)
label.adjustsFontForContentSizeCategory = true
```

有关使用缩放字体的更多信息，参见[自动缩放字体](scaling-fonts-automatically.md)。

## 另请参阅

### 字体

- [自动缩放字体](scaling-fonts-automatically.md) — 使用动态字体自动缩放界面中的文本。
- [UIFont](uifont.md) — 一个提供对字体特征访问的对象。
- [UIFontDescriptor](uifontdescriptor.md) — 描述字体的一组属性的集合。
- [SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md) — 描述字体样式方面的常量。
- [UIFontMetrics](uifontmetrics.md) — 一个用于获取支持动态字体缩放的自定字体的实用工具对象。
