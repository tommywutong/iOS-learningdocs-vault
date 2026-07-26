---
title: MapFeature
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mapfeature
source_url: 'https://developer.apple.com/documentation/mapkit/mapfeature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapfeature.json'
content_hash: 'sha256:ead05ec1cbddf540'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MapFeature

<sub>Structure</sub>

A tappable map feature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MapFeature
```

## Overview

Tappable map features can include single points of interest, such as hotels and restaurants, a territory, or a physical map feature such as an ocean, basin, river, or mountain range.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Accessing the feature’s properties

- [kind](mapfeature/kind.md) — The kind of feature represented by the map feature.
- [FeatureKind](mapfeature/featurekind.md) — The kind of feature represented by a map feature.
- [coordinate](mapfeature/coordinate.md) — The coordinate of the map feature.
- [title](mapfeature/title.md) — The title of the map feature.
- [backgroundColor](mapfeature/backgroundcolor.md) — The background color associated with the map feature.
- [image](mapfeature/image.md) — An image associated with the map feature.
- [pointOfInterestCategory](mapfeature/pointofinterestcategory.md) — The point of interest category of the map feature.

## See Also

### Map features

- [MapSelection](mapselection.md) — A value representing a selected feature on a map.
- [MapSelectable](mapselectable.md)
