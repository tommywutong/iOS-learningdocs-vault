---
title: 使用自定义特性向视图层级结构提供数据
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/providing-data-to-the-view-hierarchy-with-custom-traits
source_url: 'https://developer.apple.com/documentation/uikit/providing-data-to-the-view-hierarchy-with-custom-traits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/providing-data-to-the-view-hierarchy-with-custom-traits.json'
content_hash: 'sha256:6d83f35ff90133e3'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [App 与环境](app-and-environment.md) · [特性与特性环境](traits-and-the-trait-environment.md)

# 使用自定义特性向视图层级结构提供数据

<sub>文章</sub>

共享需要在视图层级结构（view hierarchy）的多个层级间按层级流动的数据。

## 概述

自定义特性（custom trait）是符合 [UITraitDefinition](uitraitdefinition-3572h.md) 的类型。使用自定义特性，将 App 数据（例如用户在 App 中选择的颜色主题）传递给视图层级结构中采用 [UITraitEnvironment](uitraitenvironment.md) 的对象。如果你希望实现以下目标，请使用自定义特性来表示数据：

- 将数据传播给多个子级，例如所包含的视图控制器（view controller）或子视图。
- 将数据传递给远处的组件，例如从 [UIWindowScene](uiwindowscene.md) 子类传递给视图控制器栈中的某个视图。
- 提供有关环境的上下文，例如从当前视图控制器获取其容器视图控制器的信息，而无需依赖该容器视图控制器。

对于可以直接在视图控制器和视图之间传递的数据，请避免使用自定义特性。

### 创建、设置和访问自定义特性

要创建自定义特性，请定义符合 [UITraitDefinition](uitraitdefinition-3572h.md) 的类型：

```swift
struct ContainedInSettingsTrait: UITraitDefinition {
    static let defaultValue = false
}
```

[defaultValue](uitraitdefinition-64c15/defaultvalue.md) 是唯一必需的静态属性（property）。系统会根据你为 `defaultValue` 设置的值的类型，推断自定义特性的类型。定义自定义特性后，在视图层级结构中某个对象的 `traitOverrides` 属性中使用该特性作为键，设置其值：

```swift
self.traitOverrides[ContainedInSettingsTrait.self] = true
```

随后，系统会将该特性和值传播给此对象在视图层级结构中的后代。例如，如果该对象是视图控制器，系统会将视图控制器包含覆盖值的特性集合（trait collection）传播给该视图控制器的视图和子视图，以及所有子视图控制器。

在特性集合中使用该特性作为键，访问特性的值：

```swift
let value = traitCollection[ContainedInSettingsTrait.self]
```

### 使用扩展简化自定义特性访问

向 [UITraitCollection](uitraitcollection.md) 和 [UIMutableTraits](uimutabletraits-8l00o.md) 添加便利属性，让自定义特性更易于访问。首先，使用一个属性扩展 [UITraitCollection](uitraitcollection.md)，以从特性集合中获取自定义特性的值：

```swift
extension UITraitCollection {
    var isContainedInSettings: Bool { self[ContainedInSettingsTrait.self] }
}
```

接着，扩展 [UIMutableTraits](uimutabletraits-8l00o.md)，以获取和设置自定义特性的值：

```swift
extension UIMutableTraits {
    var isContainedInSettings: Bool {
        get { self[ContainedInSettingsTrait.self] }
        set { self[ContainedInSettingsTrait.self] = newValue }
    }
}
```

然后，使用标准属性语法访问和更新自定义特性：

```swift
let traitCollection = UITraitCollection { mutableTraits in
    mutableTraits.isContainedInSettings = true
}

let value = traitCollection.isContainedInSettings
```

### 增强自定义特性交互

设置 [UITraitDefinition](uitraitdefinition-3572h.md) 的可选属性，为特性赋予额外的系统能力并改善调试：

- **[affectsColorAppearance](uitraitdefinition-3572h/affectscolorappearance.md)** — 使用自定义特性实现自定义动态颜色时，将此项设为 [true](../swift/true.md)。
- **[name](uitraitdefinition-3572h/name.md)** — 将此项设为字符串值，以便在调试器中标识自定义特性。
- **[identifier](uitraitdefinition-3572h/identifier.md)** — 将此项设为字符串值，以唯一标识自定义特性，使其可使用编码等其他功能。请使用反向 DNS 格式，使标识符在 App 中全局唯一。

以下示例演示如何设置这些可选属性：

```swift
enum MyAppTheme: Int {
    case standard, pastel, bold, monochrome
}

struct MyAppThemeTrait: UITraitDefinition {
    static let defaultValue = MyAppTheme.standard
    static let affectsColorAppearance = true
    static let name = "Theme"
    static let identifier = "com.myapp.theme"
}
```

## 另请参阅

### 自定义特性

- [UIMutableTraits](uimutabletraits-13ja5.md) — 可变的特性容器。
- [UITrait](uitrait-9423.md) — 表示特性集合中特性的类型。
- [UITraitDefinition](uitraitdefinition-64c15.md) — 表示特性集合中特性的类型。
