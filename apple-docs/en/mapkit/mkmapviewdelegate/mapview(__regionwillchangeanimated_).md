---
title: 'mapView(_:regionWillChangeAnimated:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapview(_:regionwillchangeanimated:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:regionwillchangeanimated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapview%28_%3Aregionwillchangeanimated%3A%29.json'
content_hash: 'sha256:84e8d2144ddac511'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapView(_:regionWillChangeAnimated:)

<sub>Instance Method</sub>

Tells the delegate when the region the map view is displaying is about to change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func mapView(_ mapView: MKMapView, regionWillChangeAnimated animated: Bool)
```

## Parameters

- `mapView` — The map view with the visible region that’s about to change.

- `animated` — If [true](../../swift/true.md), the map view animates the change to the new region. If [false](../../swift/false.md), the map view makes the change immediately.

## Discussion

The framework calls this method at the beginning of a change to the map’s visible region.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)

### Responding to map position changes

- [- mapViewDidChangeVisibleRegion:](<mapviewdidchangevisibleregion(__).md>) — Tells the delegate when the map view’s visible region changes.
- [- mapView:regionDidChangeAnimated:](<mapview(__regiondidchangeanimated_).md>) — Tells the delegate when the region the map view is displaying changes.
