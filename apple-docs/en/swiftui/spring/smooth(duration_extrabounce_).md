---
title: 'smooth(duration:extraBounce:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/spring/smooth(duration:extrabounce:)'
source_url: 'https://developer.apple.com/documentation/swiftui/spring/smooth(duration:extrabounce:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spring/smooth%28duration%3Aextrabounce%3A%29.json'
content_hash: 'sha256:f27d24ed67816d4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Spring](../spring.md)

# smooth(duration:extraBounce:)

<sub>Type Method</sub>

A smooth spring with a predefined duration and no bounce that can be tuned.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func smooth(duration: TimeInterval = 0.5, extraBounce: Double = 0.0) -> Spring
```

## Parameters

- `duration` — The perceptual duration, which defines the pace of the spring. This is approximately equal to the settling duration, but for very bouncy springs, will be the duration of the period of oscillation for the spring.

- `extraBounce` — How much additional bounce should be added to the base bounce of 0.

## See Also

### Getting built-in springs

- [bouncy](bouncy.md) — A spring with a predefined duration and higher amount of bounce.
- [bouncy(duration:extraBounce:)](<bouncy(duration_extrabounce_).md>) — A spring with a predefined duration and higher amount of bounce that can be tuned.
- [smooth](smooth.md) — A smooth spring with a predefined duration and no bounce.
- [snappy](snappy.md) — A spring with a predefined duration and small amount of bounce that feels more snappy.
- [snappy(duration:extraBounce:)](<snappy(duration_extrabounce_).md>) — A spring with a predefined duration and small amount of bounce that feels more snappy and can be tuned.
