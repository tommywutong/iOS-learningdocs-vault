---
title: zPriority
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationview/zpriority
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationview/zpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationview/zpriority.json'
content_hash: 'sha256:1cf47e5dd0c77c21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAnnotationView](../mkannotationview.md)

# zPriority

<sub>Instance Property</sub>

The relative importance of the annotation view when in an unselected state with respect to its ordering along the z-axis.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var zPriority: MKAnnotationViewZPriority { get set }
```

## Discussion

The constant [MKAnnotationViewZPriorityDefaultUnselected](../mkannotationviewzpriority/defaultunselected.md) is the default value for [zPriority](zpriority.md).

## See Also

### Setting the priority for display

- [displayPriority](displaypriority.md) — The display priority of the annotation view.
- [MKFeatureDisplayPriority](../mkfeaturedisplaypriority.md) — Constants that indicates the display priority for annotations.
- [selectedZPriority](selectedzpriority.md) — The relative importance of the annotation view when in a selected state with respect to its ordering along the z-axis.
- [MKAnnotationViewZPriority](../mkannotationviewzpriority.md) — Constants that indicates the priority for ordering overlapping annotation views.
