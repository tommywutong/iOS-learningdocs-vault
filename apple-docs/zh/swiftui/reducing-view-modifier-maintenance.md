---
title: 减少视图修饰符的维护工作
framework: SwiftUI
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/reducing-view-modifier-maintenance
source_url: 'https://developer.apple.com/documentation/swiftui/reducing-view-modifier-maintenance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/reducing-view-modifier-maintenance.json'
content_hash: 'sha256:eb2f2794bfe6fecd'
translated: true
---

> 导航：[技术](../technologies.md) · [SwiftUI](../swiftui.md) · [视图基础](view-fundamentals.md)

# 减少视图修饰符的维护工作

<sub>文章</sub>

把你经常重用的视图修饰符打包成一个自定视图修饰符。

## 概述

为了创建一致的视图，你可能会在各视图中反复重用同一个视图修饰符或一组修饰符。例如，你可能在整个 App 中为许多文本实例应用相同的字体和前景色，使它们彼此匹配。遗憾的是，这会带来维护上的挑战，因为即使是格式上的微小更改（例如不同的字号），也需要修改代码中许多不同的部分。

为避免这种开销，可以使用 [ViewModifier](viewmodifier.md) 协议的一个实例，把一组修饰符收集到一个位置。然后，用一个使用你的修饰符的方法扩展 [View](view.md) 协议，使其易于使用和理解。把修饰符收集在一起，可以为你提供一个在想要更改它们时的唯一更新位置。

### 创建自定视图修饰符

创建自定修饰符时，请为它取一个能反映该集合用途的名字。例如，如果你反复为视图应用 [caption](font/caption.md) 字体样式和次要配色方案来表示次要样式，就可以把它们一起收集为 `CaptionTextFormat`：

```swift
struct CaptionTextFormat: ViewModifier {
    func body(content: Content) -> some View {
        content
            .font(.caption)
            .foregroundColor(.secondary)
    }
}
```

使用 [modifier(_:)](<view/modifier(__).md>) 方法应用你的修饰符。以下代码将上面的示例应用到一个 [Text](text.md) 实例：

```swift
Text("Some additional information...")
    .modifier(CaptionTextFormat())
```

### 扩展 View 协议以提供流畅的修饰符访问

为了让你的自定视图修饰符便于使用，请用一个应用你的修饰符的函数来扩展 [View](view.md) 协议：

```swift
extension View {
    func captionTextFormat() -> some View {
        modifier(CaptionTextFormat())
    }
}
```

通过包含以下扩展，将修饰符应用到文本视图：

```swift
Text("Some additional information...")
    .captionTextFormat()
```

## 另请参阅

### 修改视图

- [Configuring views](configuring-views.md) — 通过应用视图修饰符调整视图的特性。
- [modifier(_:)](<view/modifier(__).md>) — 将修饰符应用于视图并返回一个新视图。
- [ViewModifier](viewmodifier.md) — 一种应用于视图或另一个视图修饰符的修饰符，会产生原始值的一个不同版本。
- [EmptyModifier](emptymodifier.md) — 空的（即恒等的）修饰符，在开发期间用于在编译期切换修饰符。
- [ModifiedContent](modifiedcontent.md) — 应用了修饰符的值。
- [EnvironmentalModifier](environmentalmodifier.md) — 一种必须先在环境中解析为具体修饰符才能使用的修饰符。
- [ManipulableModifier](manipulablemodifier.md)
- [ManipulableResponderModifier](manipulablerespondermodifier.md)
- [ManipulableTransformBindingModifier](manipulabletransformbindingmodifier.md)
- [ManipulationGeometryModifier](manipulationgeometrymodifier.md)
- [ManipulationGestureModifier](manipulationgesturemodifier.md)
- [ManipulationUsingGestureStateModifier](manipulationusinggesturestatemodifier.md)
- [Manipulable](manipulable.md) — 各种可操控相关类型的命名空间。
