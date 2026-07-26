---
title: 'mapView(_:didAddOverlayViews:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（13.0 起废弃）, iPadOS 4.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapview(_:didaddoverlayviews:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:didaddoverlayviews:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapview%28_%3Adidaddoverlayviews%3A%29.json'
content_hash: 'sha256:7d2fc8093cc068a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapView(_:didAddOverlayViews:)

<sub>Instance Method</sub>

Tells the delegate when the map adds one or more overlay views to the map.

> [!warning] Deprecated
> Implement the [- mapView:didAddOverlayRenderers:](<mapview(__didadd_)-793gj.md>) method instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func mapView(_ mapView: MKMapView, didAddOverlayViews overlayViews: [Any])
```

## Parameters

- `mapView` — The map view that adds the overlay views.

- `overlayViews` — An array of [MKOverlayView](../mkoverlayview.md) objects representing the views that the map view adds.

## Discussion

By the time the map view calls this method, MapKit has added the specified views to the map.

## See Also

### Methods

- [- viewForOverlay:](<../mkmapview/view(for_)-38z60.md>) — Returns the view associated with the overlay object, if any. _(deprecated)_
- [- mapView:viewForOverlay:](<mapview(__viewfor_)-6j267.md>) — Asks the delegate for the overlay view to use when displaying the specified overlay object. _(deprecated)_
