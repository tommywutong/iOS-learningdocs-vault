---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/menuorder/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/menuorder/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menuorder/automatic.json'
content_hash: 'sha256:569c6b0c08cef29d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MenuOrder](../menuorder.md)

# automatic

<sub>Type Property</sub>

The ordering of the menu chosen by the system for the current context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let automatic: MenuOrder
```

## Discussion

On iOS, this order resolves to [fixed](fixed.md) for menus presented within scrollable content. Pickers that use the [menu](../pickerstyle/menu.md) style also default to [fixed](fixed.md) order. In all other cases, menus default to [priority](priority.md) order.

On macOS, tvOS and watchOS, the `automatic` order always resolves to [fixed](fixed.md) order.

## See Also

### Getting menu orders

- [fixed](fixed.md) — Order items from top to bottom.
- [priority](priority.md) — Keep the first items closest to user’s interaction point.
