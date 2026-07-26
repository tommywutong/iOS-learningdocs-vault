---
title: circularEaseInOut
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/unitcurve/circulareaseinout
source_url: 'https://developer.apple.com/documentation/swiftui/unitcurve/circulareaseinout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/unitcurve/circulareaseinout.json'
content_hash: 'sha256:fffb9ae8edf18cdb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UnitCurve](../unitcurve.md)

# circularEaseInOut

<sub>Type Property</sub>

A circular curve that starts out slowly, speeds up over the middle, then slows down again as it approaches the end.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let circularEaseInOut: UnitCurve
```

## Discussion

The shape of the curve is defined by a piecewise combination of `circularEaseIn` and `circularEaseOut`.

## See Also

### Getting easing curves

- [easeIn](easein.md) — A bezier curve that starts out slowly, then speeds up as it finishes.
- [easeOut](easeout.md) — A bezier curve that starts out quickly, then slows down as it approaches the end.
- [easeInOut](easeinout.md) — A bezier curve that starts out slowly, speeds up over the middle, then slows down again as it approaches the end.
- [circularEaseIn](circulareasein.md) — A curve that starts out slowly, then speeds up as it finishes.
- [circularEaseOut](circulareaseout.md) — A circular curve that starts out quickly, then slows down as it approaches the end.
