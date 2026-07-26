---
title: displayPriority
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/displaypriority
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/displaypriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/displaypriority.json'
content_hash: 'sha256:375c454ce245230d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# displayPriority

<sub>Instance Property</sub>

The display priority of the annotation view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var displayPriority: MKFeatureDisplayPriority { get set }
```

## Discussion

An annotation view with a priority of [MKFeatureDisplayPriorityRequired](../mkfeaturedisplaypriority/required.md) is always visible on the map, whereas other priorities may result in a hidden annotation view. Defaults to `required`.

## See Also

### Setting the priority for display

- [MKFeatureDisplayPriority](../mkfeaturedisplaypriority.md) — Constants that indicates the display priority for annotations.
- [zPriority](zpriority.md) — The relative importance of the annotation view when in an unselected state with respect to its ordering along the z-axis.
- [selectedZPriority](selectedzpriority.md) — The relative importance of the annotation view when in a selected state with respect to its ordering along the z-axis.
- [MKAnnotationViewZPriority](../mkannotationviewzpriority.md) — Constants that indicates the priority for ordering overlapping annotation views.
