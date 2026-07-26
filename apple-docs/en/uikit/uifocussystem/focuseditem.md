---
title: focusedItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocussystem/focuseditem
source_url: 'https://developer.apple.com/documentation/uikit/uifocussystem/focuseditem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocussystem/focuseditem.json'
content_hash: 'sha256:c0f17bd5cc0f33b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusSystem](../uifocussystem.md)

# focusedItem

<sub>Instance Property</sub>

The item that’s currently focused.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var focusedItem: (any UIFocusItem)? { get }
```

## Discussion

If the current object or none of its children are focused, this property is set to `nil`.
