---
title: prefersScrollingExpandsWhenScrolledToEdge
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisheetpresentationcontroller/prefersscrollingexpandswhenscrolledtoedge
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/prefersscrollingexpandswhenscrolledtoedge'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontroller/prefersscrollingexpandswhenscrolledtoedge.json'
content_hash: 'sha256:d49b56515a92b903'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISheetPresentationController](../uisheetpresentationcontroller.md)

# prefersScrollingExpandsWhenScrolledToEdge

<sub>Instance Property</sub>

A Boolean value that determines whether scrolling expands the sheet to a larger detent.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var prefersScrollingExpandsWhenScrolledToEdge: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md), which means if the sheet can expand to a larger detent than [selectedDetentIdentifier](selecteddetentidentifier.md), scrolling up in the sheet increases its detent instead of scrolling the sheet’s content. After the sheet reaches its largest detent, scrolling begins.

Set this value to [false](../../swift/false.md) if you want to avoid letting a scroll gesture expand the sheet. For example, you can set this value on a nonmodal sheet to avoid obscuring the content underneath the sheet.

## See Also

### Managing user interaction

- [largestUndimmedDetentIdentifier](largestundimmeddetentidentifier.md) — The largest detent that doesn’t dim the view underneath the sheet.
