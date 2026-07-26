---
title: Gradient.Stop
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gradient/stop
source_url: 'https://developer.apple.com/documentation/swiftui/gradient/stop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gradient/stop.json'
content_hash: 'sha256:995bb51472b37638'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Gradient](../gradient.md)

# Gradient.Stop

<sub>Structure</sub>

One color stop in the gradient.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Stop
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a gradient stop

- [init(color:location:)](<stop/init(color_location_).md>) — Creates a color stop with a color and location.

### Configuring a gradient stop

- [color](stop/color.md) — The color for the stop.
- [location](stop/location.md) — The parametric location of the stop.

## See Also

### Creating a gradient from stops

- [init(stops:)](<init(stops_).md>) — Creates a gradient from an array of color stops.
- [stops](stops.md) — The array of color stops.
