---
title: 在 UI 中配置和显示符号图像
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/configuring-and-displaying-symbol-images-in-your-ui
source_url: 'https://developer.apple.com/documentation/uikit/configuring-and-displaying-symbol-images-in-your-ui'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/configuring-and-displaying-symbol-images-in-your-ui.json'
content_hash: 'sha256:a8389267c5b936dc'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [外观自定](appearance-customization.md) · [在界面中支持深色模式](supporting-dark-mode-in-your-interface.md)

# 在 UI 中配置和显示符号图像

<sub>文章</sub>

创建可随你 App 文本缩放的图像，并动态调整这些图像的外观。

## 概述

符号图像为你的 App 提供一组一致的图标，并保证这些图标能够适应不同大小和 App 特有的内容。符号图像包含基于矢量的形状，缩放时不会失去清晰度。你可以通过应用色调颜色来生成最终外观；如果使用 [SF Symbols](https://developer.apple.com/design/resources/#sf-symbols)，还可以应用多种颜色，为符号增添深度和强调效果。符号图像适用于显示简单形状或字形的位置，例如栏按钮条目。

尽管符号属于图像，但它们支持许多通常与文本相关联的特性。事实上，多个系统符号图像的内容中都包含字母、数字或符号字符。例如，系统为加、减、乘、除数学运算符提供了符号图像。你也可以将文本相关特性应用于符号图像，使其外观与周围文本一致：

- 将字体文本样式应用于符号图像，使它与采用相同样式的文本匹配。字体文本样式还会使符号图像随当前动态字体（Dynamic Type）设置进行缩放。
- 将细体、粗体或加粗等字重应用于符号图像。
- 缩放符号图像并设置样式，使其与文本所用字体匹配。
- 使用图像的基线将符号图像与相邻文本对齐。

系统提供一组标准符号图像，其中包括文件夹、废纸篓和收藏条目等许多图像。符号图像还会适应当前特性环境，从而减少支持不同大小界面所需的工作。要浏览可用的符号图像，请使用 SF Symbols App；你可以从 [Apple Design Resources](https://developer.apple.com/design/resources/) 下载它。

你还可以为 App 的自定图标创建符号图像文件，具体方法请参阅[为你的 App 创建自定符号图像](creating-custom-symbol-images-for-your-app.md)。

### 加载符号图像

在 Storyboard 文件中配置图像视图时，可以在 Attribute inspector 中浏览符号图像名称列表。通过代码加载符号图像时，使用 SF Symbols App 查找符号图像的名称。对于自定符号图像，请在资源目录中创建 Symbol Image Set 资源，并按名称加载该资源。

SwiftUI、UIKit 和 AppKit 都提供了加载符号图像的方法。在每个框架中，按名称加载系统图像时需要使用特定方法；加载自定符号图像时则使用另一组方法。每种方法只会查找其指定的图像类型，从而避免自定图像与系统图像之间发生命名空间冲突。

以下示例展示了如何在各框架中加载系统符号和自定符号。

在 SwiftUI 中，使用 `Image(systemName:)` 加载系统符号图像，并使用 `Image(_:)` 加载自定符号，如以下代码所示：

```swift
// 创建系统符号图像。
Image(systemName: "multiply.circle.fill")

// 使用 Xcode 资源目录中的资源创建自定符号图像。
Image("custom.multiply.circle")
```

在 UIKit 中，[UIImage](uiimage.md) 对象包含使用特定特性或配置选项加载符号图像的方法。加载系统符号图像时，请使用 [+ systemImageNamed:](<uiimage/init(systemname_).md>)、[+ systemImageNamed:compatibleWithTraitCollection:](<uiimage/init(systemname_compatiblewith_).md>) 或 [+ systemImageNamed:withConfiguration:](<uiimage/init(systemname_withconfiguration_).md>)。从资源目录加载自定符号图像时，请使用 [+ imageNamed:](<uiimage/init(named_).md>)、[+ imageNamed:inBundle:compatibleWithTraitCollection:](<uiimage/init(named_in_compatiblewith_).md>) 或 [+ imageNamed:inBundle:withConfiguration:](<uiimage/init(named_in_with_).md>)。

```swift
// 创建系统符号图像。
let image = UIImage(systemName: "multiply.circle.fill")                  

// 使用 Xcode 资源目录中的资源创建自定符号图像。
let image = UIImage(named: "custom.multiply.circle")
```

使用 AppKit 时，请用 [init(systemSymbolName:accessibilityDescription:)](<../appkit/nsimage/init(systemsymbolname_accessibilitydescription_).md>) 加载系统符号图像，并用 [init(named:)](<../appkit/nsimage/init(named_).md>) 加载自定符号图像。

```swift
// 创建带有辅助功能描述的系统符号图像。
let image = NSImage(systemSymbolName: "multiply.circle.fill",
                    accessibilityDescription: "A multiply symbol inside a filled circle.")

// 使用 Xcode 资源目录中的资源创建自定符号图像。
let image = NSImage(named: "custom.multiply.circle")
```

### 为符号图像应用特定外观

UIKit 和 AppKit 方法会返回包含符号图像信息的图像对象。在图像视图中显示该符号图像时，系统会向它应用默认样式。采用默认样式的图像放在加粗文本或使用标题文本样式的文本旁边时，可能显得格格不入。

要让符号图像与其余内容协调一致，请创建 [SymbolConfiguration](uiimage/symbolconfiguration-swift.class.md) 或 [NSImage.SymbolConfiguration](../appkit/nsimage/symbolconfiguration-swift.class.md) 对象，其中包含如何设置符号图像样式的信息。使用相邻标签和文本视图所采用的文本样式配置该对象，或者指定这些视图所使用的字体。你可以添加字重信息，让符号图像的外观看起来更细或更粗，也可以指定图像相对于相邻文本略大或略小。

在 UIKit 中，将配置数据分配给包含符号图像的 `UIImageView` 的 [preferredSymbolConfiguration](uiimageview/preferredsymbolconfiguration.md) 属性。通常，你只会将配置数据应用于图像视图。对于其他类型的系统视图，UIKit 会根据系统要求提供配置数据。例如，栏会配置其栏按钮条目中的符号图像，使它们与栏的配置匹配。另一种可能使用配置数据的情况是直接绘制图像。此时，请使用 [- configurationByApplyingConfiguration:](<uiimage/configuration-swift.class/applying(__).md>) 方法创建包含指定配置数据的图像版本。

```swift
// 创建由系统使用两种调色板颜色初始化的配置对象。
var config = UIImage.SymbolConfiguration(paletteColors: [.systemTeal, .systemGray5])

// 应用缩放至系统字体 42 点大小的配置。
config = config.applying(UIImage.SymbolConfiguration(font: .systemFont(ofSize: 42.0)))

// 将配置应用于图像视图。
imageView.preferredSymbolConfiguration = config
```

如果使用 SwiftUI，可以使用多个修饰器来配置符号图像，如以下代码所示：

```swift
Image(systemName: "multiply.circle.fill")
      .foregroundStyle(.teal, .gray)
      .font(.system(size: 42.0))
```

在 AppKit 中，创建配置对象，并在 [NSImageView](../appkit/nsimageview.md) 上设置 [symbolConfiguration](../appkit/nsimageview/symbolconfiguration.md)。

```swift
var configuration = NSImage.SymbolConfiguration(paletteColors: [.systemTeal, .systemGray])
configuration = config.applying(.init(textStyle: .title1))
imageView.symbolConfiguration = config
```

### 更新符号的渲染模式

SF Symbols 包含四种渲染模式：单色、调色板、分层和多色。符号没有固有颜色，因此系统默认使用色调颜色来渲染。例如，以下代码演示了如何向整个图像应用色调颜色：

```swift
// 使用 SwiftUI 创建系统符号图像并应用色调颜色。
Image(systemName: "multiply.circle.fill")
      .foregroundColor(.red)

// 使用 UIKit 创建带色调颜色的符号图像。
imageView.image = image?.withTintColor(.systemRed, renderingMode: .alwaysOriginal)
```

在 SwiftUI 中，使用 [symbolRenderingMode(_:)](<../swiftui/image/symbolrenderingmode(__).md>) 设置渲染模式，并使用 `foregroundStyle(_:)` 应用颜色。如果符号不支持你选择的渲染模式，系统会使用单色版本。将 `foregroundStyle` 与多种颜色配合使用意味着切换到调色板渲染模式，因此可以省略渲染模式设置。

```swift
// 以调色板渲染模式创建系统符号图像。
Image(systemName: "multiply.circle.fill")
      .foregroundStyle(.teal, .gray)
```

在 UIKit 和 AppKit 中，使用符号配置对象修改符号的渲染模式。在 AppKit 中，使用 [withSymbolConfiguration(_:)](<../appkit/nsimage/withsymbolconfiguration(__).md>) 应用配置；而在 UIKit 中，则使用 [- imageByApplyingSymbolConfiguration:](<uiimage/applyingsymbolconfiguration(__).md>) 应用配置，如以下代码所示：

```swift
// 创建为调色板渲染模式配置的对象。
let config = UIImage.SymbolConfiguration(paletteColors: [.systemTeal, .systemGray])

// 使用配置对象创建新的符号图像。
imageView.image = image.applyingSymbolConfiguration(config)
```

从 iOS 16 开始，如果没有指定模式，符号不会自动以单色模式渲染。例如，系统符号“airpodsmax”默认使用分层模式。如果你的 App 需要以单色方式渲染某个符号，请使用 [+ configurationPreferringMonochrome](<uiimage/symbolconfiguration-swift.class/preferringmonochrome().md>)。要确定符号的默认渲染模式，请在 SF Symbols App 中找到该符号并检查颜色边栏。

### 应用可变渲染（variable rendering）

在 iOS 16 及更高版本中，系统可以使用百分比值动态地向系统符号和自定符号应用颜色，以传达强度或随时间推移的进度。例如，以下代码创建一个扬声器声波符号，其中三个弧线中的两个被高亮显示：

```swift
// 创建强度为 36% 的系统符号图像。
let image = UIImage(systemName: "speaker.wave.3", variableValue: 0.36)
```

要在 AppKit 中使用可变渲染，请参阅 [init(symbolName:variableValue:)](<../appkit/nsimage/init(symbolname_variablevalue_).md>)。

### 更新符号的字重和缩放比例

符号有九种字重，分别对应 San Francisco 系统字体的一种字重，有助于你精确匹配符号与相邻文本的字重，同时灵活支持不同大小和上下文。

通过指定缩放比例，可以调整符号相对于相邻文本的强调程度，而不会破坏与采用相同点大小的文本之间的字重匹配。请参阅 [imageScale](../swiftui/environmentvalues/imagescale.md)（SwiftUI）、[SymbolScale](uiimage/symbolscale.md)（UIKit）和 [NSImage.SymbolScale](../appkit/nsimage/symbolscale.md)（AppKit）。

```swift
// 使用 SwiftUI 创建大型缩放符号图像。
Image(systemName: "multiply.circle.fill")
      .imageScale(.large)

// 使用 UIKit 创建大型缩放符号图像。
var config = UIImage.SymbolConfiguration(scale: .large)
imageView.image = image.applyingSymbolConfiguration(config)

// 使用 AppKit 创建大型缩放符号图像。
var config = NSImage.SymbolConfiguration(scale: .large)
imageView.image = image.withSymbolConfiguration(config)
```

### 应用符号图像变体

SF Symbols 定义了轮廓、填充、斜线和封闭等设计变体，在保持 UI 视觉一致且简洁的同时，帮助你传达准确的状态和操作。例如，可以使用斜线变体表示某项操作不可用，或者使用填充变体表示用户何时选中了某项内容。

> [!note] 注意
> 如果某个符号不存在相应变体，系统会使用基础符号。例如，iOS 中的标签页栏默认使用填充变体，因此选择没有填充变体的符号会使用原始符号。

在 SwiftUI 中，使用修饰器 `symbolVariant(_:)` 应用变体。在 SF Symbols App 中搜索，找出乘号符号支持的变体，例如 `circle`、`circle.fill`、`square` 和 `square.fill`。

```swift
// 创建以填充圆圈变体封闭的系统符号图像。
Image(systemName: "multiply")
      .symbolVariant(.circle.fill)
```

### 使用基线将符号图像与文本标签对齐

由于 SF Symbols 具有排版特性，当你将包含符号图像的图像视图放在标签旁边时，应使用基线将这些视图对齐。要在 Storyboard 中对齐视图，请选择两个视图并添加首基线约束。要以编程方式创建此约束，请将两个视图的 [firstBaselineAnchor](uiview/firstbaselineanchor.md) 设为相等，如以下代码示例所示：

**Swift**

```swift
NSLayoutConstraint.activate([
    imageView!.firstBaselineAnchor.constraint(equalTo: label!.firstBaselineAnchor)
])
```

**Objective-C**

```swift
[NSLayoutConstraint activateConstraints:@[
    [self.imageView.firstBaselineAnchor
     constraintEqualToAnchor:self.label.firstBaselineAnchor]
]];
```

所有系统符号图像都包含基线信息，而 `UIImage` 会将基线值公开为相对于图像底部的偏移量。通常，符号图像的基线与图像中出现的所有文本底部对齐，但即使是不含文本的符号图像也有基线。在 AppKit 中，符号的基线对应 [alignmentRect](../appkit/nsimage/alignmentrect.md) 属性的底部；在 UIKit 中，可以调用图像的 [- imageWithBaselineOffsetFromBottom:](<uiimage/withbaselineoffset(frombottom_).md>) 方法，为任意图像添加基线。

```swift
// 创建自定符号图像。
let image = UIImage(named: "custom.multiply.circle")

// 添加相对于基线的 2.0 点偏移量。
let baselineImage = image?.withBaselineOffset(fromBottom: 2.0)
```

在 SwiftUI 中，使用 [firstTextBaseline](../swiftui/verticalalignment/firsttextbaseline.md) 将符号与文本按基线对齐。

```swift
HStack(alignment: .firstTextBaseline) {
    Image(systemName: "menucard")
    Text("SF Symbols")
}
```

### 为已废弃的符号名称变更使用回退资源

符号名称可能随操作系统版本和 SF Symbols App 版本变化，因此支持新版本时需要检查符号的使用情况。在 SF Symbols App 中浏览时，请查看部署目标；如果要向后部署，请使用旧名称。

如果符号未在你的 App 中渲染，请使用 SF Symbols App 搜索符号名称，并选取「View \> Inspectors \> Show Info Sidebar」来查看可用性更新。

根据所支持的操作系统，你可能需要提供回退资源。例如，SF Symbols 仅在 iOS 13 及更高版本中受支持。资源目录中可以包含名为 `gamecontroller` 的符号图像，以及同名的回退 PNG 资源，后者用于较早的操作系统版本。使用 Interface Builder 时，将图像视图设为使用名为 `gamecontroller` 的资源，系统就会根据平台加载第一个可用资源。

以编程方式实现时，需要使用 #`available` 来正确加载资源。

```swift
if #available(iOS 13.0, *) {
    // 加载 SF 符号图像。
} else {
    // 加载 PNG 资源。
}
```

## 另请参阅

### 图像

- [为不同外观提供图像](providing-images-for-different-appearances.md) — 提供适合浅色、深色外观和高对比度环境的图像资源。
