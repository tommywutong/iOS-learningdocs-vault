---
title: easeIn
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/unitcurve/easein
source_url: 'https://developer.apple.com/documentation/swiftui/unitcurve/easein'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/unitcurve/easein.json'
content_hash: 'sha256:166c0d05ec550d57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UnitCurve](../unitcurve.md)

# easeIn

<sub>Type Property</sub>

A bezier curve that starts out slowly, then speeds up as it finishes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let easeIn: UnitCurve
```

## Discussion

The start and end control points are located at (x: 0.42, y: 0) and (x: 1, y: 1).

## See Also

### Getting easing curves

- [easeOut](easeout.md) — A bezier curve that starts out quickly, then slows down as it approaches the end.
- [easeInOut](easeinout.md) — A bezier curve that starts out slowly, speeds up over the middle, then slows down again as it approaches the end.
- [circularEaseIn](circulareasein.md) — A curve that starts out slowly, then speeds up as it finishes.
- [circularEaseOut](circulareaseout.md) — A circular curve that starts out quickly, then slows down as it approaches the end.
- [circularEaseInOut](circulareaseinout.md) — A circular curve that starts out slowly, speeds up over the middle, then slows down again as it approaches the end.
