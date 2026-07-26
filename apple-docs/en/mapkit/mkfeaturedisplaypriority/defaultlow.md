---
title: defaultLow
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkfeaturedisplaypriority/defaultlow
source_url: 'https://developer.apple.com/documentation/mapkit/mkfeaturedisplaypriority/defaultlow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkfeaturedisplaypriority/defaultlow.json'
content_hash: 'sha256:8c6d069851a8bf3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKFeatureDisplayPriority](../mkfeaturedisplaypriority.md)

# defaultLow

<sub>Type Property</sub>

A constant indicating that the item’s display priority is low.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var defaultLow: MKFeatureDisplayPriority { get }
```

## Discussion

An annotation view with this priority is removed from the map when its bounds collide with the bounds of another view with a higher priority. If the priorities of the two views are equal, the view furthest from the center of the map’s visible region is hidden first.

## See Also

### Priorities

- [MKFeatureDisplayPriorityRequired](required.md) — A constant indicating that the item is required.
- [MKFeatureDisplayPriorityDefaultHigh](defaulthigh.md) — A constant indicating that the item’s display priority is high.
