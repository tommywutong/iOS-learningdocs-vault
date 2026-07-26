---
title: actualScaleFactor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsstringdrawingcontext/actualscalefactor
source_url: 'https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/actualscalefactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsstringdrawingcontext/actualscalefactor.json'
content_hash: 'sha256:0f04a009936fa78d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSStringDrawingContext](../nsstringdrawingcontext.md)

# actualScaleFactor

<sub>Instance Property</sub>

The actual scale factor that the system applied to the font during drawing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var actualScaleFactor: CGFloat { get }
```

## Discussion

If you specified a custom value in the [minimumScaleFactor](minimumscalefactor.md) property, when drawing is complete, this property contains the actual scale factor value that was used to draw the string.

## See Also

### Accessing the scale factors

- [minimumScaleFactor](minimumscalefactor.md) — The scale factor that determines the smallest font size to use during drawing.
