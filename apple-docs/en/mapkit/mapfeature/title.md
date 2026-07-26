---
title: title
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapfeature/title
source_url: 'https://developer.apple.com/documentation/mapkit/mapfeature/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapfeature/title.json'
content_hash: 'sha256:908275d30414f979'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapFeature](../mapfeature.md)

# title

<sub>Instance Property</sub>

The title of the map feature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var title: String? { get }
```

## Discussion

If the feature doesn’t have a title this property is `nil`.

## See Also

### Accessing the feature’s properties

- [kind](kind.md) — The kind of feature represented by the map feature.
- [FeatureKind](featurekind.md) — The kind of feature represented by a map feature.
- [coordinate](coordinate.md) — The coordinate of the map feature.
- [backgroundColor](backgroundcolor.md) — The background color associated with the map feature.
- [image](image.md) — An image associated with the map feature.
- [pointOfInterestCategory](pointofinterestcategory.md) — The point of interest category of the map feature.
