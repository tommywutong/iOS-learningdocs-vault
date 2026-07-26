---
title: MKFeatureDisplayPriority
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkfeaturedisplaypriority
source_url: 'https://developer.apple.com/documentation/mapkit/mkfeaturedisplaypriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkfeaturedisplaypriority.json'
content_hash: 'sha256:77f1fa5191b3f814'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKFeatureDisplayPriority

<sub>Structure</sub>

Constants that indicates the display priority for annotations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MKFeatureDisplayPriority
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Priorities

- [MKFeatureDisplayPriorityRequired](mkfeaturedisplaypriority/required.md) — A constant indicating that the item is required.
- [MKFeatureDisplayPriorityDefaultHigh](mkfeaturedisplaypriority/defaulthigh.md) — A constant indicating that the item’s display priority is high.
- [MKFeatureDisplayPriorityDefaultLow](mkfeaturedisplaypriority/defaultlow.md) — A constant indicating that the item’s display priority is low.

### Creating Feature Display Priorities

- [init(_:)](<mkfeaturedisplaypriority/init(__).md>) — Creates a feature display priority using the specified floating point value.
- [init(rawValue:)](<mkfeaturedisplaypriority/init(rawvalue_).md>) — Creates a feature display priority using the specified raw floating point value.

## See Also

### Setting the priority for display

- [displayPriority](mkannotationview/displaypriority.md) — The display priority of the annotation view.
- [zPriority](mkannotationview/zpriority.md) — The relative importance of the annotation view when in an unselected state with respect to its ordering along the z-axis.
- [selectedZPriority](mkannotationview/selectedzpriority.md) — The relative importance of the annotation view when in a selected state with respect to its ordering along the z-axis.
- [MKAnnotationViewZPriority](mkannotationviewzpriority.md) — Constants that indicates the priority for ordering overlapping annotation views.
