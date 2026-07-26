---
title: 'mapViewDidChangeVisibleRegion(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapviewdidchangevisibleregion(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapviewdidchangevisibleregion(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapviewdidchangevisibleregion%28_%3A%29.json'
content_hash: 'sha256:f10f060af98748b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapViewDidChangeVisibleRegion(_:)

<sub>Instance Method</sub>

Tells the delegate when the map view’s visible region changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func mapViewDidChangeVisibleRegion(_ mapView: MKMapView)
```

## Parameters

- `mapView` — The map view with the visible region that changes.

## Discussion

Use this method to update the map in response to intermediate changes to the region. The map view calls this method each time the value of its visible region changes.

> [!important] Important
> Because the map may call this method many times during the scrolling of the map, your implementation needs to be lightweight. Use this method to record the new region values or to make fast updates to your app’s interface. Don’t start any long-running synchronous tasks in this method.

## See Also

### Responding to map position changes

- [- mapView:regionWillChangeAnimated:](<mapview(__regionwillchangeanimated_).md>) — Tells the delegate when the region the map view is displaying is about to change.
- [- mapView:regionDidChangeAnimated:](<mapview(__regiondidchangeanimated_).md>) — Tells the delegate when the region the map view is displaying changes.
