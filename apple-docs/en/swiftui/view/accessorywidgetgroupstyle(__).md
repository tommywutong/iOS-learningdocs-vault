---
title: 'accessoryWidgetGroupStyle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/accessorywidgetgroupstyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/accessorywidgetgroupstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/accessorywidgetgroupstyle%28_%3A%29.json'
content_hash: 'sha256:176647742754bd9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# accessoryWidgetGroupStyle(_:)

<sub>Instance Method</sub>

The view modifier that can be applied to `AccessoryWidgetGroup` to specify the shape the three content views will be masked with. The value of `style` is set to `.automatic`, which is `.circular` by default.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency func accessoryWidgetGroupStyle(_ style: AccessoryWidgetGroupStyle = .automatic) -> some View

```

## Parameters

- `style` — The shape with which the content views are masked. The available shapes are circle and rounded square.
