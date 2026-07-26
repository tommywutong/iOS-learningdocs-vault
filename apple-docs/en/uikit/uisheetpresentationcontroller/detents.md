---
title: detents
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisheetpresentationcontroller/detents
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/detents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontroller/detents.json'
content_hash: 'sha256:e97b31ab547ba631'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISheetPresentationController](../uisheetpresentationcontroller.md)

# detents

<sub>Instance Property</sub>

The array of heights where a sheet can rest.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var detents: [UISheetPresentationController.Detent] { get set }
```

## Discussion

The default value is an array that contains the value [+ largeDetent](<detent/large().md>). This array must contain at least one element. When you set this value, specify detents in order from smallest to largest height.

## See Also

### Specifying the height

- [selectedDetentIdentifier](selecteddetentidentifier.md) — The identifier of the most recently selected detent.
- [Detent](detent.md) — An object that represents a height where a sheet naturally rests.
