---
title: selectedDetentIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisheetpresentationcontroller/selecteddetentidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/selecteddetentidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontroller/selecteddetentidentifier.json'
content_hash: 'sha256:2a7f8e1e97b23872'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISheetPresentationController](../uisheetpresentationcontroller.md)

# selectedDetentIdentifier

<sub>Instance Property</sub>

The identifier of the most recently selected detent.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var selectedDetentIdentifier: UISheetPresentationController.Detent.Identifier? { get set }
```

## Discussion

This property represents the most recent detent that the user selects or that you set programmatically. The default value is `nil`, which means the sheet displays at the smallest detent you specify in [detents](detents.md).

## See Also

### Specifying the height

- [detents](detents.md) — The array of heights where a sheet can rest.
- [Detent](detent.md) — An object that represents a height where a sheet naturally rests.
