---
title: 'timingCurve(_:duration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animation/timingcurve(_:duration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animation/timingcurve(_:duration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/timingcurve%28_%3Aduration%3A%29.json'
content_hash: 'sha256:ee62903e70841c34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# timingCurve(_:duration:)

<sub>Type Method</sub>

Creates a new animation with speed controlled by the given curve.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func timingCurve(_ curve: UnitCurve, duration: TimeInterval) -> Animation
```

## Parameters

- `duration` — The duration of the animation, in seconds.

## See Also

### Creating custom animations

- [init(_:)](<init(__).md>) — Create an `Animation` that contains the specified custom animation.
- [timingCurve(_:_:_:_:duration:)](<timingcurve(________duration_).md>) — An animation created from a cubic Bézier timing curve.
