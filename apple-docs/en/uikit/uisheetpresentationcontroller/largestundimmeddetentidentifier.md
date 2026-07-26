---
title: largestUndimmedDetentIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisheetpresentationcontroller/largestundimmeddetentidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/largestundimmeddetentidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontroller/largestundimmeddetentidentifier.json'
content_hash: 'sha256:d56e57cc1da8cde2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISheetPresentationController](../uisheetpresentationcontroller.md)

# largestUndimmedDetentIdentifier

<sub>Instance Property</sub>

The largest detent that doesn’t dim the view underneath the sheet.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var largestUndimmedDetentIdentifier: UISheetPresentationController.Detent.Identifier? { get set }
```

## Discussion

The default value is `nil`, which means the system adds a noninteractive dimming view underneath the sheet at all detents. Set this property to only add the dimming view at detents larger than the detent you specify. For example, set this property to [UISheetPresentationControllerDetentIdentifierMedium](detent/identifier-swift.struct/medium.md) to add the dimming view at the [UISheetPresentationControllerDetentIdentifierLarge](detent/identifier-swift.struct/large.md) detent.

Without a dimming view, the undimmed area around the sheet responds to user interaction, allowing for a nonmodal experience. You can use this behavior for sheets with interactive content underneath them.

## See Also

### Managing user interaction

- [prefersScrollingExpandsWhenScrolledToEdge](prefersscrollingexpandswhenscrolledtoedge.md) — A Boolean value that determines whether scrolling expands the sheet to a larger detent.
