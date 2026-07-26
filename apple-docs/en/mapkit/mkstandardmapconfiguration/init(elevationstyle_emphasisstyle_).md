---
title: 'init(elevationStyle:emphasisStyle:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkstandardmapconfiguration/init(elevationstyle:emphasisstyle:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkstandardmapconfiguration/init(elevationstyle:emphasisstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkstandardmapconfiguration/init%28elevationstyle%3Aemphasisstyle%3A%29.json'
content_hash: 'sha256:f9e365bffc6e10c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKStandardMapConfiguration](../mkstandardmapconfiguration.md)

# init(elevationStyle:emphasisStyle:)

<sub>Initializer</sub>

Creates a standard map configuration with the specified elevation and emphasis styles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(elevationStyle: MKMapConfiguration.ElevationStyle, emphasisStyle: MKStandardMapConfiguration.EmphasisStyle)
```

## Parameters

- `elevationStyle` — One of the [ElevationStyle](../mkmapconfiguration/elevationstyle-swift.enum.md) modes.

- `emphasisStyle` — One of the [EmphasisStyle](emphasisstyle-swift.enum.md) styles.

## See Also

### Creating a standard map configuration

- [- init](<init().md>) — Creates a new standard map configuration.
- [- initWithElevationStyle:](<init(elevationstyle_).md>) — Creates a new standard map configuration with the specified elevation style.
- [- initWithEmphasisStyle:](<init(emphasisstyle_).md>) — Creates a standard map configuration with the specified emphasis style.
- [ElevationStyle](../mkmapconfiguration/elevationstyle-swift.enum.md) — Values that control the map’s elevation style.
- [EmphasisStyle](emphasisstyle-swift.enum.md) — Values that control how the framework emphasizes map features.
