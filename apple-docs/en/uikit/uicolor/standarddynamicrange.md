---
title: standardDynamicRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicolor/standarddynamicrange
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/standarddynamicrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/standarddynamicrange.json'
content_hash: 'sha256:48f81814d67f587c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# standardDynamicRange

<sub>Instance Property</sub>

In some cases it is useful to recover the color that was base SDR color that was exposed to generate the given HDR color. If a color’s `linearExposure` is \>1, then this will return the base SDR color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var standardDynamicRange: UIColor { get }
```

## See Also

### Working with high dynamic range (HDR) colors

- [- colorByApplyingContentHeadroom:](<applyingcontentheadroom(__).md>) — Reinterpret the color by applying a new `contentHeadroom` without changing the color components. Changing the `contentHeadroom` redefines the color relative to a different peak white, changing its behavior under tone mapping and the result of calling `standardDynamicRangeColor`. The new color will have a `contentHeadroom` \>= 1.0.
