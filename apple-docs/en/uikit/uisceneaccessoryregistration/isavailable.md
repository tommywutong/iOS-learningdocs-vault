---
title: isAvailable
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uisceneaccessoryregistration/isavailable
source_url: 'https://developer.apple.com/documentation/uikit/uisceneaccessoryregistration/isavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneaccessoryregistration/isavailable.json'
content_hash: 'sha256:500e4f20428171c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneAccessoryRegistration](../uisceneaccessoryregistration.md)

# isAvailable

<sub>Instance Property</sub>

Whether the associated scene accessory is available for display by the system or not.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isAvailable: Bool { get }
```

## Discussion

This value is observable during the `updateProperties` and `layoutSubviews` lifecycle events.

## See Also

### Observing availability and controlling display

- [enabled](isenabled.md) — Whether the content defined by this scene accessory should be displayed or not. _(beta)_
