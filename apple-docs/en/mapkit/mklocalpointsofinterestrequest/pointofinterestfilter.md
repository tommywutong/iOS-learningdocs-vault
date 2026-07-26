---
title: pointOfInterestFilter
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalpointsofinterestrequest/pointofinterestfilter
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalpointsofinterestrequest/pointofinterestfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalpointsofinterestrequest/pointofinterestfilter.json'
content_hash: 'sha256:28cb33dcc37ee57d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalPointsOfInterestRequest](../mklocalpointsofinterestrequest.md)

# pointOfInterestFilter

<sub>Instance Property</sub>

A filter that lists points of interest categories to include or exclude.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var pointOfInterestFilter: MKPointOfInterestFilter? { get set }
```

## See Also

### Configuring the request parameters

- [region](region.md) — The region of the bounding box of the request provided or the derived bounding box of the circle created by the radius.
- [coordinate](coordinate.md) — The center of the point of request as latitude and longitude.
- [radius](radius.md) — The distance provided in meters or the longest distance derived from the center point to the region’s bounding box.
