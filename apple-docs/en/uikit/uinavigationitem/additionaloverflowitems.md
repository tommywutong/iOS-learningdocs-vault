---
title: additionalOverflowItems
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/additionaloverflowitems
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/additionaloverflowitems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/additionaloverflowitems.json'
content_hash: 'sha256:1e447fe6b99cca67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# additionalOverflowItems

<sub>Instance Property</sub>

Additional items to present in the overflow menu.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var additionalOverflowItems: UIDeferredMenuElement? { get set }
```

## Discussion

When you assign a non-`nil` value to this property, the overflow menu button appears on the trailing edge of the navigation bar. This button appears regardless of whether you provide menu elements in the callback for the [UIDeferredMenuElement](../uideferredmenuelement.md).

The system presents any menu elements you return in the callback for [UIDeferredMenuElement](../uideferredmenuelement.md) in the overflow menu. The system also populates the overflow menu with any items that can’t fit in the navigation bar due to layout space constraints.

## See Also

### Working with the overflow menu

- [overflowPresentationSource](overflowpresentationsource.md) — The item you can use as an anchor to present a custom UI from the overflow menu button.
