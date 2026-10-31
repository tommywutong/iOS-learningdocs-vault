---
title: 在 trait 更改时调整你的 App
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adapting-your-app-when-traits-change
source_url: 'https://developer.apple.com/documentation/uikit/adapting-your-app-when-traits-change'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adapting-your-app-when-traits-change.json'
content_hash: 'sha256:8b5e55ffb7ef10b2'
translated: true
---

> 导航： [Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md) · [Traits and the trait environment](traits-and-the-trait-environment.md)

# 在 trait 更改时调整你的 App

<sub>文章</sub>

找出影响你的 App 的系统更改发生时，然后高效更新你的 App。

## 概述

当某人旋转设备、启用深色模式或更新辅助功能设置时，系统会更新关联的 trait 并通过你的 App 的视图层级结构传播它们。你可以监控 trait 的更改，然后用适应已更改 trait 的代码响应这些更改。例如，当 [horizontalSizeClass](uitraitcollection/horizontalsizeclass.md) 或 [verticalSizeClass](uitraitcollection/verticalsizeclass.md) 更改时，你可能更改视图显示的内容；或者你可能调整浅色或深色外观使用的颜色。

当你在特定方法（如 [- layoutSubviews](<uiview/layoutsubviews().md>)）中引用 trait 时，UIKit 会自动监听 trait 更改。

或者，当你想在这些方法之外监听 trait 更改时，你可以使用 [UITraitChangeObservable](uitraitchangeobservable-67e94.md) 协议中的方法注册以监听特定 trait。当响应 trait 更改的代码不适合系统在每个布局通道调用的方法（如 [- layoutSubviews](<uiview/layoutsubviews().md>)）时，使用此方法。

> [!tip] 提示
> 如果你的 App 使用已弃用的 [- traitCollectionDidChange:](<uitraitenvironment/traitcollectiondidchange(__).md>) 方法来监听 trait 更改，系统会在每次 trait 更改时调用该方法，无论它是否需要通知你的代码关于该更改。迁移到 [Automatic trait tracking](automatic-trait-tracking.md) 或 [UITraitChangeObservable](uitraitchangeobservable-67e94.md) 方法，以避免额外调用并提高性能。

### 自动跟踪 trait 更改

要自动跟踪 trait 更改，请在 UIKit 支持自动 trait 跟踪的方法之一中添加引用 trait 的代码，例如 [- layoutSubviews](<uiview/layoutsubviews().md>) 中的 [horizontalSizeClass](uitraitcollection/horizontalsizeclass.md)。在以下示例中，实现会根据 size class 为较小视图应用布局（当 size class 为 [UIUserInterfaceSizeClassCompact](uiuserinterfacesizeclass/compact.md) 时），或为较大视图应用布局（当 size class 为 [UIUserInterfaceSizeClassRegular](uiuserinterfacesizeclass/regular.md) 时）：

```swift
class MyView: UIView {
    override func layoutSubviews() {
        super.layoutSubviews()

        if traitCollection.horizontalSizeClass == .compact {
          // Apply compact layout.
        } else {
          // Apply regular layout.
        }
    }
}
```

当 [horizontalSizeClass](uitraitcollection/horizontalsizeclass.md) 更改时，系统会自动使布局失效，并在下一个布局通道中调用 [- layoutSubviews](<uiview/layoutsubviews().md>)，以便你可以为 size class 应用正确的布局。

有关 UIKit 支持自动 trait 跟踪的方法的更多信息，参见 [Automatic trait tracking](automatic-trait-tracking.md)。

### 使用注册跟踪 trait 更改

要在自动方法之外跟踪特定 trait 或一组 trait，请使用 [UITraitChangeObservable](uitraitchangeobservable-67e94.md) 协议中的注册方法。选择要观察的 trait 或 trait 列表，然后指定每次这些 trait 更改时要处理的代码块或方法。例如：

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    registerForTraitChanges([
        UITraitHorizontalSizeClass.self,
        UITraitVerticalSizeClass.self
    ]) { (self: Self, previousTraitCollection: UITraitCollection) in
        self.updateLayout()
    }
}

func updateLayout() {
    let isCompact = traitCollection.horizontalSizeClass == .compact
    // Update your layout based on the size class.
}
```

每当注册的任何 trait 更改时，你的处理程序就会执行。如果你需要确定哪个具体 trait 更改了，请比较之前的 trait collection 与当前的。

UIKit 提供了预定义的 trait 集，将相关 trait 分组以供常见用例使用，例如颜色更改或图像查找。这些语义集在你需要响应多个相关 trait 时简化了代码。

以下示例使用 [systemTraitsAffectingColorAppearance](uitraitcollection/systemtraitsaffectingcolorappearance-64z7q.md) 注册所有影响颜色外观的 trait，包括用户界面样式、对比度级别和辅助功能设置：

```swift
registerForTraitChanges(UITraitCollection.systemTraitsAffectingColorAppearance) {
    (self: Self, previousTraitCollection: UITraitCollection) in
    self.updateColors()
}
```

其他有用的语义 trait 集包括：

- **[systemTraitsAffectingImageLookup](uitraitcollection/systemtraitsaffectingimagelookup-4jv5.md)** — 影响显示哪个图像变体的 trait 列表。
- **[systemTraitsAffectingColorAppearance](uitraitcollection/systemtraitsaffectingcolorappearance-64z7q.md)** — 影响颜色和外观的 trait 列表。

trait 注册在创建它们的对象的生命周期内保持活动。当视图或视图控制器释放时，UIKit 会自动移除所有关联的 trait 注册，从而在大多数情况下无需手动清理。

如果你需要在释放前取消注册，请存储注册方法返回的 [UITraitChangeRegistration](uitraitchangeregistration.md) token，并调用 [unregisterForTraitChanges(_:)](<uitraitchangeobservable-67e94/unregisterfortraitchanges(__).md>) 方法：

```swift
private var traitRegistration: UITraitChangeRegistration?

func startObservingTraits() {
    traitRegistration = registerForTraitChanges([UITraitHorizontalSizeClass.self]) {
        (self: Self, previousTraitCollection: UITraitCollection) in
        self.updateLayout()
    }
}

func stopObservingTraits() {
    unregisterForTraitChanges(traitRegistration)
    traitRegistration = nil
}
```

### 从已弃用的方法迁移

如果你的代码当前使用 [- traitCollectionDidChange:](<uitraitenvironment/traitcollectiondidchange(__).md>)，请迁移到自动 trait 跟踪或 trait 注册以获得更好的性能和可维护性。

移除在 [- traitCollectionDidChange:](<uitraitenvironment/traitcollectiondidchange(__).md>) 中检查 trait 更改的实现，例如此示例：

```swift
override func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) {
    super.traitCollectionDidChange(previousTraitCollection)

    if traitCollection.horizontalSizeClass != previousTraitCollection?.horizontalSizeClass {
        updateLayout()
    }
}
```

将它们替换为支持自动 trait 跟踪的方法中的实现，例如此示例：

```swift
override func layoutSubviews() {
    super.layoutSubviews()

    updateLayout(traitCollection.horizontalSizeClass)
}
```

或者，将它们替换为在设置代码中设置 trait 注册的实现，如下例：

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    registerForTraitChanges([UITraitHorizontalSizeClass.self]) {
        (self: Self, previousTraitCollection: UITraitCollection) in
        self.updateLayout()
    }
}
```

自动 trait 跟踪和 trait 注册方法比使用 [- traitCollectionDidChange:](<uitraitenvironment/traitcollectiondidchange(__).md>) 更高效，因为你的处理程序只在你指定的 trait 实际更改时执行，而不是在系统中的每次 trait 更改时执行。
