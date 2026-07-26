---
title: 'snappy(duration:extraBounce:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/spring/snappy(duration:extrabounce:)'
source_url: 'https://developer.apple.com/documentation/swiftui/spring/snappy(duration:extrabounce:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spring/snappy%28duration%3Aextrabounce%3A%29.json'
content_hash: 'sha256:4802e6e0405e66f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Spring](../spring.md)

# snappy(duration:extraBounce:)

<sub>Type Method</sub>

A spring with a predefined duration and small amount of bounce that feels more snappy and can be tuned.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func snappy(duration: TimeInterval = 0.5, extraBounce: Double = 0.0) -> Spring
```

## Parameters

- `duration` — The perceptual duration, which defines the pace of the spring. This is approximately equal to the settling duration, but for very bouncy springs, will be the duration of the period of oscillation for the spring.

- `extraBounce` — How much additional bounciness should be added to the base bounce of 0.15.

## See Also

### Getting built-in springs

- [bouncy](bouncy.md) — A spring with a predefined duration and higher amount of bounce.
- [bouncy(duration:extraBounce:)](<bouncy(duration_extrabounce_).md>) — A spring with a predefined duration and higher amount of bounce that can be tuned.
- [smooth](smooth.md) — A smooth spring with a predefined duration and no bounce.
- [smooth(duration:extraBounce:)](<smooth(duration_extrabounce_).md>) — A smooth spring with a predefined duration and no bounce that can be tuned.
- [snappy](snappy.md) — A spring with a predefined duration and small amount of bounce that feels more snappy.
