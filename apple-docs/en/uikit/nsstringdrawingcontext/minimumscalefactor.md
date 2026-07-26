---
title: minimumScaleFactor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsstringdrawingcontext/minimumscalefactor
source_url: 'https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/minimumscalefactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsstringdrawingcontext/minimumscalefactor.json'
content_hash: 'sha256:1e7886b7711d9f12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSStringDrawingContext](../nsstringdrawingcontext.md)

# minimumScaleFactor

<sub>Instance Property</sub>

The scale factor that determines the smallest font size to use during drawing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var minimumScaleFactor: CGFloat { get set }
```

## Discussion

A value of `0.0` corresponds to a scale factor of `1.0`. Any value greater than `0.0` is multiplied by the font point size to get the smallest font size that is permissible to use. For example, 0.5 indicates a font that is half the size of the actual font, 0.75 is three-quarters of the font size, and so on. Typically, you specify a value between 0.0 and 1.0 to indicate how much the font can be shrunk during drawing.

The default value of this property is `0.0`.

## See Also

### Accessing the scale factors

- [actualScaleFactor](actualscalefactor.md) — The actual scale factor that the system applied to the font during drawing.
