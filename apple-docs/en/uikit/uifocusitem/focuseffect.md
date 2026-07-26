---
title: focusEffect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusitem/focuseffect
source_url: 'https://developer.apple.com/documentation/uikit/uifocusitem/focuseffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusitem/focuseffect.json'
content_hash: 'sha256:a7eb245f43499f63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusItem](../uifocusitem.md)

# focusEffect

<sub>Instance Property</sub>

The visual effect to apply when the item becomes focused.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@NSCopying optional var focusEffect: UIFocusEffect? { get }
```

## Discussion

A `nil` value indicates that the system shouldn’t apply any visual effects when the item becomes focused.

If you don’t implement this property, its value is `nil`.
