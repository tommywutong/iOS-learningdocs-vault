---
title: 'init(coordinate:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkpointannotation/init(coordinate:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkpointannotation/init(coordinate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpointannotation/init%28coordinate%3A%29.json'
content_hash: 'sha256:ab1fc6363359bfcf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPointAnnotation](../mkpointannotation.md)

# init(coordinate:)

<sub>Initializer</sub>

Creates a point annotation at the specified coordinate on the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(coordinate: CLLocationCoordinate2D)
```

## Parameters

- `coordinate` — The coordinate containing the latitude and longitude values for the desired point.

## See Also

### Creating a Point Annotation

- [- init](<init().md>) — Creates a map annotation that shows a title string at a point on a map.
- [- initWithCoordinate:title:subtitle:](<init(coordinate_title_subtitle_).md>) — Creates a point annotation displaying a title and subtitle string at the specified coordinate on the map.
