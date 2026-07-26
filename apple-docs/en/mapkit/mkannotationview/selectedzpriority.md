---
title: selectedZPriority
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/selectedzpriority
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/selectedzpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/selectedzpriority.json'
content_hash: 'sha256:62d33aa3a4011b37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# selectedZPriority

<sub>Instance Property</sub>

The relative importance of the annotation view when in a selected state with respect to its ordering along the z-axis.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var selectedZPriority: MKAnnotationViewZPriority { get set }
```

## Discussion

The constant [MKAnnotationViewZPriorityDefaultSelected](../mkannotationviewzpriority/defaultselected.md) is the default value for [selectedZPriority](selectedzpriority.md).

## See Also

### Setting the priority for display

- [displayPriority](displaypriority.md) — The display priority of the annotation view.
- [MKFeatureDisplayPriority](../mkfeaturedisplaypriority.md) — Constants that indicates the display priority for annotations.
- [zPriority](zpriority.md) — The relative importance of the annotation view when in an unselected state with respect to its ordering along the z-axis.
- [MKAnnotationViewZPriority](../mkannotationviewzpriority.md) — Constants that indicates the priority for ordering overlapping annotation views.
