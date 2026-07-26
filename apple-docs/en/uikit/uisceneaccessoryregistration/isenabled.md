---
title: isEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uisceneaccessoryregistration/isenabled
source_url: 'https://developer.apple.com/documentation/uikit/uisceneaccessoryregistration/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneaccessoryregistration/isenabled.json'
content_hash: 'sha256:fac2541540888f73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneAccessoryRegistration](../uisceneaccessoryregistration.md)

# isEnabled

<sub>Instance Property</sub>

Whether the content defined by this scene accessory should be displayed or not.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

This value does not reflect the availability of the scene accessory, which is determined by the system.

## See Also

### Observing availability and controlling display

- [available](isavailable.md) — Whether the associated scene accessory is available for display by the system or not. _(beta)_
