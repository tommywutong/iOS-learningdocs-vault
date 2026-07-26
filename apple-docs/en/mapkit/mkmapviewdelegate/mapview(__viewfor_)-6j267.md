---
title: 'mapView(_:viewFor:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（13.0 起废弃）, iPadOS 4.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapview(_:viewfor:)-6j267'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:viewfor:)-6j267'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapview%28_%3Aviewfor%3A%29-6j267.json'
content_hash: 'sha256:3da29feaccf8bbce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapView(_:viewFor:)

<sub>Instance Method</sub>

Asks the delegate for the overlay view to use when displaying the specified overlay object.

> [!warning] Deprecated
> Implement the [- mapView:rendererForOverlay:](<mapview(__rendererfor_).md>) method instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func mapView(_ mapView: MKMapView, viewFor overlay: any MKOverlay) -> MKOverlayView
```

## Parameters

- `mapView` — The map view that requests the overlay view.

- `overlay` — The object representing the overlay that the map view is about to display.

## Return Value

The view to use when presenting the specified overlay on the map. If you return `nil`, no view  displays for the specified overlay object.

## See Also

### Methods

- [- viewForOverlay:](<../mkmapview/view(for_)-38z60.md>) — Returns the view associated with the overlay object, if any. _(deprecated)_
- [- mapView:didAddOverlayViews:](<mapview(__didaddoverlayviews_).md>) — Tells the delegate when the map adds one or more overlay views to the map. _(deprecated)_
