---
title: includingAll
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkpointofinterestfilter/includingall
source_url: 'https://developer.apple.com/documentation/mapkit/mkpointofinterestfilter/includingall'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpointofinterestfilter/includingall.json'
content_hash: 'sha256:275efee3166f3d8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPointOfInterestFilter](../mkpointofinterestfilter.md)

# includingAll

<sub>Type Property</sub>

A filter that includes all point of interest categories.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var includingAll: MKPointOfInterestFilter { get }
```

## Discussion

You can use [filterIncludingAllCategories](includingall.md)  to include all points of interest in your map view without listing all the categories individually.

## See Also

### Creating filters

- [filterExcludingAllCategories](excludingall.md) — A filter that excludes all point of interest categories.
- [- initExcludingCategories:](<init(excluding_).md>) — Initialize the point of interest filter with a list of categories to exclude.
- [- initIncludingCategories:](<init(including_).md>) — Initialize the point of interest filter with a list of categories to include.
