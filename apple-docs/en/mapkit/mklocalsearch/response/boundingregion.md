---
title: boundingRegion
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.1+, iPadOS 6.1+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearch/response/boundingregion
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearch/response/boundingregion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearch/response/boundingregion.json'
content_hash: 'sha256:ebfb5513ff42e803'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKLocalSearch](../../mklocalsearch.md) · [Response](../response.md)

# boundingRegion

<sub>Instance Property</sub>

The map region that encloses the returned search results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var boundingRegion: MKCoordinateRegion { get }
```

## Discussion

The returned region is the smallest bounding box that encloses all of the map items. If there’s only one search result, the size of the region may be `(0, 0)`.

## See Also

### Getting the search results

- [mapItems](mapitems.md) — An array of map items representing the search results.
