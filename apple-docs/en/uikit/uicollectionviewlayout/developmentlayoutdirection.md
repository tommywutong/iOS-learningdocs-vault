---
title: developmentLayoutDirection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayout/developmentlayoutdirection
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/developmentlayoutdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/developmentlayoutdirection.json'
content_hash: 'sha256:b8065ffdb311a59f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# developmentLayoutDirection

<sub>Instance Property</sub>

The direction of the language you used when designing your custom layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var developmentLayoutDirection: UIUserInterfaceLayoutDirection { get }
```

## Discussion

The default value of this property is the layout direction used by the language associated with the main bundle’s development region. Subclasses may override this property and return a different value.

## See Also

### Supporting right-to-left layouts

- [flipsHorizontallyInOppositeLayoutDirection](flipshorizontallyinoppositelayoutdirection.md) — A Boolean value that indicates whether the horizontal coordinate system is automatically flipped at appropriate times.
