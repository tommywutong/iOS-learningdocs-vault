---
title: bounce
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionlayoutsectionorthogonalscrollingproperties/bounce-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionlayoutsectionorthogonalscrollingproperties/bounce-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionlayoutsectionorthogonalscrollingproperties/bounce-swift.property.json'
content_hash: 'sha256:2cfd5e9c8e791a79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionLayoutSectionOrthogonalScrollingProperties](../uicollectionlayoutsectionorthogonalscrollingproperties.md)

# bounce

<sub>Instance Property</sub>

A value that specifies whether the orthogonal scrolling section bounces past the edge of content and back again.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var bounce: UICollectionLayoutSectionOrthogonalScrollingProperties.Bounce { get set }
```

## Discussion

Set this value to specify whether the section stops scrolling immediately upon encountering the content boundary, or if it continues scrolling past the boundary and then bounces back.

## See Also

### Specifying the bounce behavior

- [Bounce](bounce-swift.enum.md) — Constants that specify whether the orthogonal scrolling section bounces past the edge of content and back again.
