---
title: accessories
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointerstyle/accessories
source_url: 'https://developer.apple.com/documentation/uikit/uipointerstyle/accessories'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerstyle/accessories.json'
content_hash: 'sha256:7b271957958a3860'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerStyle](../uipointerstyle.md)

# accessories

<sub>Instance Property</sub>

Accessories to display alongside the pointer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var accessories: [UIPointerAccessory] { get set }
```

## Discussion

This property supports up to four pointer accessories. The system animates between neighboring or similar accessories.

## See Also

### Specifying pointer accessories

- [UIPointerAccessory](../uipointeraccessory.md) — Constants that describe accessories to display alongside the primary pointer.
