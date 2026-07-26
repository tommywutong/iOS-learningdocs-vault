---
title: 'init(coordinate:tint:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+（16.0 起废弃）, iPadOS 14.0+（16.0 起废弃）, Mac Catalyst 14.0+（16.0 起废弃）, macOS 11.0+（13.0 起废弃）, tvOS 14.0+（16.0 起废弃）, visionOS, watchOS 7.0+（9.0 起废弃）]
languages: [swift, swift, swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mappin/init(coordinate:tint:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mappin/init(coordinate:tint:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mappin/init%28coordinate%3Atint%3A%29.json'
content_hash: 'sha256:eebb75267ee730f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapPin](../mappin.md)

# init(coordinate:tint:)

<sub>Initializer</sub>

Creates a map pin at the map location that you specify.

> [!warning] Deprecated
> Use Marker

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(coordinate: CLLocationCoordinate2D, tint: Color? = nil)
```

## Parameters

- `coordinate` — The location of the specified pin.

- `tint` — The color of the pin.
