---
title: mapItems
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.1+, iPadOS 6.1+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearch/response/mapitems
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearch/response/mapitems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearch/response/mapitems.json'
content_hash: 'sha256:91d7697a33c7967d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKLocalSearch](../../mklocalsearch.md) · [Response](../response.md)

# mapItems

<sub>Instance Property</sub>

An array of map items representing the search results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mapItems: [MKMapItem] { get }
```

## Discussion

This property contains an array of [MKMapItem](../../mkmapitem.md) objects, each of which represents a returned search result. You can use these objects to retrieve information about the search result, such as the name of the point of interest, the address, the geographic location, and so on.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)

### Getting the search results

- [boundingRegion](boundingregion.md) — The map region that encloses the returned search results.
