---
title: defaultHigh
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkfeaturedisplaypriority/defaulthigh
source_url: 'https://developer.apple.com/documentation/mapkit/mkfeaturedisplaypriority/defaulthigh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkfeaturedisplaypriority/defaulthigh.json'
content_hash: 'sha256:fdde37decd5f4d68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKFeatureDisplayPriority](../mkfeaturedisplaypriority.md)

# defaultHigh

<sub>Type Property</sub>

A constant indicating that the item’s display priority is high.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var defaultHigh: MKFeatureDisplayPriority { get }
```

## Discussion

An annotation view with this priority is removed from the map when its bounds collide with the bounds of another view with a higher priority. If the priorities of the two views are equal, the view furthest from the center of the map’s visible region is hidden first.

## See Also

### Priorities

- [MKFeatureDisplayPriorityRequired](required.md) — A constant indicating that the item is required.
- [MKFeatureDisplayPriorityDefaultLow](defaultlow.md) — A constant indicating that the item’s display priority is low.
