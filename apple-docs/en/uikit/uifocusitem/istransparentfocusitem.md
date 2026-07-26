---
title: isTransparentFocusItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 18.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusitem/istransparentfocusitem
source_url: 'https://developer.apple.com/documentation/uikit/uifocusitem/istransparentfocusitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusitem/istransparentfocusitem.json'
content_hash: 'sha256:c618aaa527b40b2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusItem](../uifocusitem.md)

# isTransparentFocusItem

<sub>Instance Property</sub>

Indicates if the focus item is transparent, which allows items behind it to become focused.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var isTransparentFocusItem: Bool { get }
```

## Discussion

The system ignores this value when the item is focusable, in which case the item is never considered transparent.
