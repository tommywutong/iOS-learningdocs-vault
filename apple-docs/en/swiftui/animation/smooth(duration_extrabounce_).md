---
title: 'smooth(duration:extraBounce:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/animation/smooth(duration:extrabounce:)'
source_url: 'https://developer.apple.com/documentation/swiftui/animation/smooth(duration:extrabounce:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animation/smooth%28duration%3Aextrabounce%3A%29.json'
content_hash: 'sha256:c6246fd7778bd8c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Animation](../animation.md)

# smooth(duration:extraBounce:)

<sub>Type Method</sub>

A smooth spring animation with a predefined duration and no bounce that can be tuned.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func smooth(duration: TimeInterval = 0.5, extraBounce: Double = 0.0) -> Animation
```

## Parameters

- `duration` — The perceptual duration, which defines the pace of the spring. This is approximately equal to the settling duration, but for very bouncy springs, will be the duration of the period of oscillation for the spring.

- `extraBounce` — How much additional bounce should be added to the base bounce of 0.

## See Also

### Getting built-in spring animations

- [bouncy](bouncy.md) — A spring animation with a predefined duration and higher amount of bounce.
- [bouncy(duration:extraBounce:)](<bouncy(duration_extrabounce_).md>) — A spring animation with a predefined duration and higher amount of bounce that can be tuned.
- [smooth](smooth.md) — A smooth spring animation with a predefined duration and no bounce.
- [snappy](snappy.md) — A spring animation with a predefined duration and small amount of bounce that feels more snappy.
- [snappy(duration:extraBounce:)](<snappy(duration_extrabounce_).md>) — A spring animation with a predefined duration and small amount of bounce that feels more snappy and can be tuned.
