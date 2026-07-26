---
title: 'mapView(_:regionDidChangeAnimated:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapview(_:regiondidchangeanimated:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:regiondidchangeanimated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapview%28_%3Aregiondidchangeanimated%3A%29.json'
content_hash: 'sha256:cd616e2f3a669a6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapView(_:regionDidChangeAnimated:)

<sub>Instance Method</sub>

Tells the delegate when the region the map view is displaying changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func mapView(_ mapView: MKMapView, regionDidChangeAnimated animated: Bool)
```

## Parameters

- `mapView` — The map view with the visible region that changes.

- `animated` — If [true](../../swift/true.md), the map view animates the change to the new region.

## Discussion

The map view calls this method at the end of a change to the map’s visible region.

## See Also

### Responding to map position changes

- [- mapView:regionWillChangeAnimated:](<mapview(__regionwillchangeanimated_).md>) — Tells the delegate when the region the map view is displaying is about to change.
- [- mapViewDidChangeVisibleRegion:](<mapviewdidchangevisibleregion(__).md>) — Tells the delegate when the map view’s visible region changes.
