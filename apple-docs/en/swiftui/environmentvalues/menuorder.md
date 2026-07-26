---
title: menuOrder
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/menuorder
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/menuorder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/menuorder.json'
content_hash: 'sha256:9c5c3feb79f0a0c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# menuOrder

<sub>Instance Property</sub>

The preferred order of items for menus presented from this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var menuOrder: MenuOrder { get set }
```

## Discussion

Set this value for a view hierarchy by calling the [menuOrder(_:)](<../view/menuorder(__).md>) view modifier.

## See Also

### Setting a preferred order

- [menuOrder(_:)](<../view/menuorder(__).md>) — Sets the preferred order of items for menus presented from this view.
- [MenuOrder](../menuorder.md) — The order in which a menu presents its content.
