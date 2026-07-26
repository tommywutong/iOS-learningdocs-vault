---
title: MKAnnotationViewZPriority
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkannotationviewzpriority
source_url: 'https://developer.apple.com/documentation/mapkit/mkannotationviewzpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkannotationviewzpriority.json'
content_hash: 'sha256:5a669086fd50663d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKAnnotationViewZPriority

<sub>Structure</sub>

Constants that indicates the priority for ordering overlapping annotation views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MKAnnotationViewZPriority
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Priorities

- [MKAnnotationViewZPriorityDefaultSelected](mkannotationviewzpriority/defaultselected.md) — The default view overlapping priority for a selected view.
- [MKAnnotationViewZPriorityDefaultUnselected](mkannotationviewzpriority/defaultunselected.md) — The default view overlapping priority for an unselected view.
- [MKAnnotationViewZPriorityMax](mkannotationviewzpriority/max.md) — The maximum allowed priority for overlapping views.
- [MKAnnotationViewZPriorityMin](mkannotationviewzpriority/min.md) — The minimum allowed priority for overlapping views.

### Initializers

- [init(_:)](<mkannotationviewzpriority/init(__).md>) — Creates an overlapping priority from the value.
- [init(rawValue:)](<mkannotationviewzpriority/init(rawvalue_).md>) — Creates an overlapping priority from the value.

## See Also

### Setting the priority for display

- [displayPriority](mkannotationview/displaypriority.md) — The display priority of the annotation view.
- [MKFeatureDisplayPriority](mkfeaturedisplaypriority.md) — Constants that indicates the display priority for annotations.
- [zPriority](mkannotationview/zpriority.md) — The relative importance of the annotation view when in an unselected state with respect to its ordering along the z-axis.
- [selectedZPriority](mkannotationview/selectedzpriority.md) — The relative importance of the annotation view when in a selected state with respect to its ordering along the z-axis.
