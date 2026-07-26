---
title: 'init(center:radius:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mklocalpointsofinterestrequest/init(center:radius:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalpointsofinterestrequest/init(center:radius:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalpointsofinterestrequest/init%28center%3Aradius%3A%29.json'
content_hash: 'sha256:e4879156219211ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalPointsOfInterestRequest](../mklocalpointsofinterestrequest.md)

# init(center:radius:)

<sub>Initializer</sub>

Creates a points of interest search request centered on the provided coordinate with the provided radius.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(center coordinate: CLLocationCoordinate2D, radius: CLLocationDistance)
```

## Parameters

- `coordinate` — The center point of a circular region to search.

- `radius` — The radius of the region to search in meters.

## See Also

### Creating a point of interest request

- [- initWithCoordinateRegion:](<init(coordinateregion_).md>) — Creates a points of interest search request based on existing region.
