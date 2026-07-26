---
title: circularEaseOut
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/unitcurve/circulareaseout
source_url: 'https://developer.apple.com/documentation/swiftui/unitcurve/circulareaseout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/unitcurve/circulareaseout.json'
content_hash: 'sha256:5a4f0202e98f1d33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UnitCurve](../unitcurve.md)

# circularEaseOut

<sub>Type Property</sub>

A circular curve that starts out quickly, then slows down as it approaches the end.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let circularEaseOut: UnitCurve
```

## Discussion

The shape of the curve is equal to the second (top left) quadrant of a unit circle.

## See Also

### Getting easing curves

- [easeIn](easein.md) — A bezier curve that starts out slowly, then speeds up as it finishes.
- [easeOut](easeout.md) — A bezier curve that starts out quickly, then slows down as it approaches the end.
- [easeInOut](easeinout.md) — A bezier curve that starts out slowly, speeds up over the middle, then slows down again as it approaches the end.
- [circularEaseIn](circulareasein.md) — A curve that starts out slowly, then speeds up as it finishes.
- [circularEaseInOut](circulareaseinout.md) — A circular curve that starts out slowly, speeds up over the middle, then slows down again as it approaches the end.
