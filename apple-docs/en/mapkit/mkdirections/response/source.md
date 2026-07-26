---
title: source
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkdirections/response/source
source_url: 'https://developer.apple.com/documentation/mapkit/mkdirections/response/source'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdirections/response/source.json'
content_hash: 'sha256:b0afd6a84212a546'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKDirections](../../mkdirections.md) · [Response](../response.md)

# source

<sub>Instance Property</sub>

The start point of the route.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var source: MKMapItem { get }
```

## Discussion

The item in this property may contain additional details that aren’t in the original item you use to create the [Request](../request.md) object.

## See Also

### Getting the end points

- [destination](destination.md) — The end point of the route.
