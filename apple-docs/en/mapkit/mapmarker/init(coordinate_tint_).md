---
title: 'init(coordinate:tint:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+（17.0 起废弃）, iPadOS 14.0+（17.0 起废弃）, Mac Catalyst 14.0+（17.0 起废弃）, macOS 11.0+（14.0 起废弃）, tvOS 14.0+（17.0 起废弃）, visionOS, watchOS 7.0+（10.0 起废弃）]
languages: [swift, swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mapmarker/init(coordinate:tint:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapmarker/init(coordinate:tint:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapmarker/init%28coordinate%3Atint%3A%29.json'
content_hash: 'sha256:e257a7c212eb8f85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapMarker](../mapmarker.md)

# init(coordinate:tint:)

<sub>Initializer</sub>

Creates a marker annotation at the map location you specify.

> [!warning] Deprecated
> Use Marker along with Map initializers that take a MapContentBuilder instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(coordinate: CLLocationCoordinate2D, tint: Color? = nil)
```

## Parameters

- `coordinate` — The location of the specified marker.

- `tint` — The color of the marker.
