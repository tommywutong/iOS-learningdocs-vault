---
title: 'velocity(at:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/unitcurve/velocity(at:)'
source_url: 'https://developer.apple.com/documentation/swiftui/unitcurve/velocity(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/unitcurve/velocity%28at%3A%29.json'
content_hash: 'sha256:35e3a65438feba54'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UnitCurve](../unitcurve.md)

# velocity(at:)

<sub>Instance Method</sub>

Returns the rate of change (first derivative) of the output value of the curve at the given time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func velocity(at progress: Double) -> Double
```

## Parameters

- `progress` — The input progress (x component). The provided value is clamped to the range [0,1].

## Return Value

The velocity of the output value (y component) of the curve at the given time.

## See Also

### Getting curve characteristics

- [value(at:)](<value(at_).md>) — Returns the output value (y component) of the curve at the given time.
