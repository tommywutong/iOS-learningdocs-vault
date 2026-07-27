---
title: 在 UIKit 中使用观察跟踪自动更新视图
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/updating-views-automatically-with-observation-tracking-in-uikit
source_url: 'https://developer.apple.com/documentation/uikit/updating-views-automatically-with-observation-tracking-in-uikit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/updating-views-automatically-with-observation-tracking-in-uikit.json'
content_hash: 'sha256:96a07cae0f7c9dd9'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [App 与环境](app-and-environment.md)

# 在 UIKit 中使用观察跟踪自动更新视图

<sub>文章</sub>

使用 Swift Observation 和自动跟踪，根据模型数据更新来更新你的视图。

## 概述

以往，当 App 的模型数据发生变化时，你需要使用新数据更新视图。根据更新内容的不同，你可能还需要手动调用 [- setNeedsLayout](<uiview/setneedslayout().md>) 或 [- setNeedsDisplay](<uiview/setneedsdisplay().md>) 等方法来刷新视图布局。这种方式要求你记住何时、何处使视图失效（invalidate），容易产生错误和过时的显示内容。

Swift [Observation](../observation.md) 提供 [Observable](../observation/observable.md) 宏，用于标记模型以自动跟踪变化。当你将 `Observable` 模型与 UIKit 结合使用时，系统会自动监视属性变化并更新视图。你不需要手动让任何内容失效，UIKit 会代你处理。

UIKit 在多个对象中提供了会进行[自动观察跟踪（automatic observation tracking）](automatic-observation-tracking.md)的方法和闭包。在视图子类中，[- updateProperties](<uiview/updateproperties().md>) 和 [- layoutSubviews](<uiview/layoutsubviews().md>) 是更新会获得自动观察跟踪的两个方法示例。`updateProperties` 方法在布局之前运行，非常适合配置文本、颜色和可见性等属性。`layoutSubviews` 方法负责几何信息和定位。这两个方法都会自动跟踪你读取的所有 `Observable` 属性；当这些属性发生变化时，UIKit 会更新你的视图。

> [!note] 注意
> 在 iOS 18 中，系统默认不启用自动观察跟踪。若要启用，请将 [UIObservationTrackingEnabled](../bundleresources/information-property-list/uiobservationtrackingenabled.md) 键添加到 App 的信息属性列表，并将该键的值设为 [true](../swift/true.md)。

### 自动更新视图属性

[- updateProperties](<uiviewcontroller/updateproperties().md>) 方法会自动跟踪 `Observable` 属性，并在属性变化时更新视图。例如，若要显示一份消息列表，其中的状态标签会显示未读消息信息，首先创建一个包含视图所需属性的 `Observable` 模型：

```swift
@Observable
class MessageModel {
    var showStatus: Bool
    var statusText: String
}
```

然后，在视图控制器（view controller）的 `updateProperties()` 方法中使用这些属性：

```swift
override func updateProperties() {
    super.updateProperties()
    statusLabel.alpha = model.showStatus ? 1.0 : 0.0
    statusLabel.text = model.statusText
}
```

视图首次出现时，UIKit 会运行 `updateProperties()`，并跟踪你读取了 `showStatus` 和 `statusText`。如果其中任一属性之后发生变化，UIKit 会再次自动运行 `updateProperties()` 来更新标签。

你也可以使用 [- updateProperties](<uiview/updateproperties().md>) 自动跟踪自定视图中的变化。

> [!note] 注意
> 若要在 iOS 18 中获得自动观察跟踪，请使用 [- viewWillLayoutSubviews](<uiviewcontroller/viewwilllayoutsubviews().md>)。

### 自动配置集合视图和表格视图单元格

集合视图（collection view）和表格视图（table view）单元格也通过其配置更新处理程序支持自动观察跟踪。例如，若要显示一个列表，让每个单元格都显示来自 `Observable` 模型的信息，首先为列表条目创建一个 `Observable` 模型：

```swift
@Observable
class ListItemModel {
    var icon: UIImage?
    var title: String
    var subtitle: String
}
```

然后，在单元格提供程序中设置配置更新处理程序，以使用该模型：

```swift
cell.configurationUpdateHandler = { cell, state in
    var config = UIListContentConfiguration.cell()
    config.image = model.icon
    config.text = model.title
    config.secondaryText = model.subtitle
    cell.contentConfiguration = config
}
```

UIKit 会自动跟踪你在处理程序中使用的 `Observable` 模型属性。当单元格可见期间其中任何属性发生变化时，UIKit 会再次运行处理程序来更新该单元格。这种模式尤其适合 App 中模型数据频繁变化的列表。

### 将属性更新与布局分离

使用 `updateProperties()` 配置内容和样式，例如将文本放入标签，以及根据数据调整颜色。只将 `layoutSubviews()` 用于几何计算，例如在 Auto Layout 约束不适合你的场景时设置视图的 frame。这种分离方式可避免不必要的布局阶段，从而提升性能。

以下示例展示了一个徽章视图，它会更新计数而不触发布局：

```swift
override func updateProperties() {
    super.updateProperties()
    badgeItem.badge = "\(model.count)"
}
```

通过使用 `updateProperties()` 而非 `layoutSubviews()`，可以避免在徽章计数变化时重新运行布局代码。视图只会更新徽章文本，而不会更新其大小或位置。对于经常更新的视图，将不影响布局的代码移入 `updateProperties()` 尤为重要。

如果需要手动触发属性更新，请在视图控制器上调用 [- setNeedsUpdateProperties](<uiviewcontroller/setneedsupdateproperties().md>)，或在视图上调用 [- setNeedsUpdateProperties](<uiview/setneedsupdateproperties().md>)。此方法会指示 UIKit 在下一次更新阶段调用 `updateProperties()`。

### 优化 UIKit 更新阶段

UIKit 按特定顺序执行更新，以帮助你的视图正确显示。将代码放在正确的方法中，可以让用户界面保持最新并避免性能问题。

更新阶段遵循以下步骤：

1. 特性集合（trait collection）使用当前环境值进行更新。
2. 如有必要，UIKit 会运行 `updateProperties()`，你可以在其中配置属性和样式。
3. 如有必要，UIKit 会运行 `layoutSubviews()`，你可以在其中计算几何信息和定位。
4. 显示阶段会渲染绘制方法，生成视觉输出。
5. 系统在屏幕上呈现渲染后的帧。

如果任何步骤导致其他视图需要更新，UIKit 会重复此过程，直到所有视图都处于最新状态。

因为 `updateProperties()` 在特性集合更新后运行，所以你的 App 可以在其中安全地读取特性值。`updateProperties()` 在 `layoutSubviews()` 之前运行，因此 App 可以按需使布局失效，而布局阶段会紧随其后运行。如果没有待处理的变化需要更新，UIKit 可能会在更新阶段跳过调用 `updateProperties()` 或 `layoutSubviews()`。

## 另请参阅

### 数据观察

- [自动观察跟踪](automatic-observation-tracking.md) — 通过在支持自动观察跟踪的方法中进行更新，简化数据变化时的视图更新。
