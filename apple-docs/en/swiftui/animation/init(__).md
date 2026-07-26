---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animation/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animation/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/init%28_%3A%29.json'
content_hash: 'sha256:cc3a8c29b48e8923'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# init(_:)

<sub>Initializer</sub>

Create an `Animation` that contains the specified custom animation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<A>(_ base: A) where A : CustomAnimation
```

## See Also

### Creating custom animations

- [timingCurve(_:duration:)](<timingcurve(__duration_).md>) — Creates a new animation with speed controlled by the given curve.
- [timingCurve(_:_:_:_:duration:)](<timingcurve(________duration_).md>) — An animation created from a cubic Bézier timing curve.
