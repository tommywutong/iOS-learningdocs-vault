---
title: excludingAll
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkpointofinterestfilter/excludingall
source_url: 'https://developer.apple.com/documentation/mapkit/mkpointofinterestfilter/excludingall'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpointofinterestfilter/excludingall.json'
content_hash: 'sha256:df3f579365ad7794'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPointOfInterestFilter](../mkpointofinterestfilter.md)

# excludingAll

<sub>Type Property</sub>

A filter that excludes all point of interest categories.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var excludingAll: MKPointOfInterestFilter { get }
```

## Discussion

You can use [filterExcludingAllCategories](excludingall.md)  to remove all points of interest from your map view without listing all the categories individually.

## See Also

### Creating filters

- [filterIncludingAllCategories](includingall.md) — A filter that includes all point of interest categories.
- [- initExcludingCategories:](<init(excluding_).md>) — Initialize the point of interest filter with a list of categories to exclude.
- [- initIncludingCategories:](<init(including_).md>) — Initialize the point of interest filter with a list of categories to include.
