---
title: 在特性变化时调整你的 App
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

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [App 与环境](app-and-environment.md) · [特性与特性环境](traits-and-the-trait-environment.md)

# 在特性变化时调整你的 App

<sub>文章</sub>

了解影响你的 App 的系统变化何时发生，然后高效地更新你的 App。

## 概述

当用户旋转设备、启用深色模式或更新辅助功能设置时，系统会更新相关的特性（trait），并把它们传播到你 App 的视图层级结构中。你可以监视特性的变化，然后用适应新特性的代码响应这些变化。例如，你可以在 [horizontalSizeClass](uitraitcollection/horizontalsizeclass.md) 或 [verticalSizeClass](uitraitcollection/verticalsizeclass.md) 变化时改变视图显示的内容，或者在浅色与深色外观下调整所用颜色。

当你在特定方法（如 [- layoutSubviews](<uiview/layoutsubviews().md>)）中引用特性时，UIKit 会自动监听特性变化。

或者，当你想在这些方法之外监听特性变化时，可以用 [UITraitChangeObservable](uitraitchangeobservable-67e94.md) 协议中的方法注册监听特定特性。当你的响应特性变化的代码不适合放在系统每次布局都会调用的 [- layoutSubviews](<uiview/layoutsubviews().md>) 这类方法里时，就采用这种方式。

> [!tip] 提示
> 如果你的 App 使用已废弃的 [- traitCollectionDidChange:](<uitraitenvironment/traitcollectiondidchange(__).md>) 方法监听特性变化，那么每次特性变化系统都会调用该方法，无论是否需要把这次变化告知你的代码。迁移到[自动特性跟踪](automatic-trait-tracking.md)或 [UITraitChangeObservable](uitraitchangeobservable-67e94.md) 方法，避免多余的调用并提升性能。

### 自动跟踪特性变化

要自动跟踪特性变化，把引用某个特性的代码加到 UIKit 支持自动特性跟踪的方法之一里，例如 [- layoutSubviews](<uiview/layoutsubviews().md>) 中的 [horizontalSizeClass](uitraitcollection/horizontalsizeclass.md)。下面的例子在尺寸类别为 [UIUserInterfaceSizeClassCompact](uiuserinterfacesizeclass/compact.md) 时应用适合较小视图的布局，为 [UIUserInterfaceSizeClassRegular](uiuserinterfacesizeclass/regular.md) 时应用适合较大视图的布局：

```swift
class MyView: UIView {
    override func layoutSubviews() {
        super.layoutSubviews()

        if traitCollection.horizontalSizeClass == .compact {
          // 应用紧凑布局。
        } else {
          // 应用常规布局。
        }
    }
}
```

当 [horizontalSizeClass](uitraitcollection/horizontalsizeclass.md) 变化时，系统会自动让布局失效，并在下一次布局中调用 [- layoutSubviews](<uiview/layoutsubviews().md>)，你就能为尺寸类别应用正确的布局。

关于 UIKit 支持自动特性跟踪的方法的更多信息，参见[自动特性跟踪](automatic-trait-tracking.md)。

### 通过注册跟踪特性变化

要在自动方法之外跟踪某个特性或一组特性，使用 [UITraitChangeObservable](uitraitchangeobservable-67e94.md) 协议中的注册方法。选定你要观察的特性或特性列表，然后指定一段代码或方法，在每次这些特性变化时执行。例如：

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
    // 根据尺寸类别更新你的布局。
}
```

任何被注册的特性发生变化时，你的处理程序都会执行。如果你需要确定具体是哪个特性变了，可以把之前的特性集合与当前的对比。

UIKit 提供了预定义的特性集合，把常见用例的相关特性成组打包，例如颜色变化或图片查找。当你需要响应多个相关特性时，这些语义化的集合能简化你的代码。

下面的例子用 [systemTraitsAffectingColorAppearance](uitraitcollection/systemtraitsaffectingcolorappearance-64z7q.md) 注册所有影响颜色外观的特性，包括用户界面风格、对比度级别和辅助功能设置：

```swift
registerForTraitChanges(UITraitCollection.systemTraitsAffectingColorAppearance) {
    (self: Self, previousTraitCollection: UITraitCollection) in
    self.updateColors()
}
```

其他有用的语义特性集合包括：

- **[systemTraitsAffectingImageLookup](uitraitcollection/systemtraitsaffectingimagelookup-4jv5.md)** — 影响显示哪个图片变体的特性列表。
- **[systemTraitsAffectingColorAppearance](uitraitcollection/systemtraitsaffectingcolorappearance-64z7q.md)** — 影响颜色与外观的特性列表。

特性注册在创建它的对象的生命周期内保持有效。当视图或视图控制器被销毁时，UIKit 会自动移除所有关联的特性注册，多数情况下无需手动清理。

如果你需要在销毁前注销，请保存注册方法返回的 [UITraitChangeRegistration](uitraitchangeregistration.md) 令牌，并调用 [unregisterForTraitChanges(_:)](<uitraitchangeobservable-67e94/unregisterfortraitchanges(__).md>) 方法：

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

### 从已废弃方法迁移

如果你的代码当前使用 [- traitCollectionDidChange:](<uitraitenvironment/traitcollectiondidchange(__).md>)，请迁移到自动特性跟踪或特性注册，以获得更好的性能与可维护性。

删除在 [- traitCollectionDidChange:](<uitraitenvironment/traitcollectiondidchange(__).md>) 中检查特性变化的实现，例如下例：

```swift
override func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) {
    super.traitCollectionDidChange(previousTraitCollection)

    if traitCollection.horizontalSizeClass != previousTraitCollection?.horizontalSizeClass {
        updateLayout()
    }
}
```

把它们替换为支持自动特性跟踪的方法中的实现，例如下例：

```swift
override func layoutSubviews() {
    super.layoutSubviews()

    updateLayout(traitCollection.horizontalSizeClass)
}
```

或者替换为在初始化代码中建立特性注册的实现，如下例：

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    registerForTraitChanges([UITraitHorizontalSizeClass.self]) {
        (self: Self, previousTraitCollection: UITraitCollection) in
        self.updateLayout()
    }
}
```

自动特性跟踪与特性注册这两种方式都比使用 [- traitCollectionDidChange:](<uitraitenvironment/traitcollectiondidchange(__).md>) 高效，因为你的处理程序只在你指定的特性真正变化时执行，而不是在系统每次特性变化时都执行。
