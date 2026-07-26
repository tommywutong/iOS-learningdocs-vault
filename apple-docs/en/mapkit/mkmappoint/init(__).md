---
title: 'init(_:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmappoint/init(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmappoint/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmappoint/init%28_%3A%29.json'
content_hash: 'sha256:8fe2b3bfffd55f3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapPoint](../mkmappoint.md)

# init(_:)

<sub>Initializer</sub>

Creates the map point data structure that corresponds to the specified coordinate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ coordinate: CLLocationCoordinate2D)
```

## Parameters

- `coordinate` — The coordinate containing the latitude and longitude values for the desired point.

## Return Value

The map point value that corresponds to the specified coordinate on a two-dimensional map projection.

## See Also

### Creating a map point

- [init()](<init().md>) — Creates a map point at an unspecified point.
- [init(x:y:)](<init(x_y_).md>) — Creates a new map point structure from the specified values.
