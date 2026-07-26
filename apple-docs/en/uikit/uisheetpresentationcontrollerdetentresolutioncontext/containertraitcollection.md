---
title: containerTraitCollection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisheetpresentationcontrollerdetentresolutioncontext/containertraitcollection
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontrollerdetentresolutioncontext/containertraitcollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontrollerdetentresolutioncontext/containertraitcollection.json'
content_hash: 'sha256:459d741f2cc72ee9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISheetPresentationControllerDetentResolutionContext](../uisheetpresentationcontrollerdetentresolutioncontext.md)

# containerTraitCollection

<sub>Instance Property</sub>

The trait collection of the sheet’s container view.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var containerTraitCollection: UITraitCollection { get }
```

## Discussion

The value of this property is the same as the window’s [traitCollection](../uiwindowscene/traitcollection.md), and doesn’t include overrides from the sheet’s [overrideTraitCollection](../uipresentationcontroller/overridetraitcollection.md).

## See Also

### Accessing the properties of the context

- [maximumDetentValue](maximumdetentvalue.md) — The maximum value of a detent.
