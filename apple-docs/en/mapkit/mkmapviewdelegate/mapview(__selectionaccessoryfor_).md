---
title: 'mapView(_:selectionAccessoryFor:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapview(_:selectionaccessoryfor:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:selectionaccessoryfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapview%28_%3Aselectionaccessoryfor%3A%29.json'
content_hash: 'sha256:c567251349962223'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapView(_:selectionAccessoryFor:)

<sub>Instance Method</sub>

Specifies the accessory to display for a selected annotation

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional func mapView(_ mapView: MKMapView, selectionAccessoryFor annotation: any MKAnnotation) -> MKSelectionAccessory?
```

## Parameters

- `mapView` — The map view that requests the selection accessory.

- `annotation` — The annotation.

## Discussion

Called for all selected annotations. Not all types of annotations support displaying selection accessories. For example, the map item detail selection accessory is only supported for [MKMapItemAnnotation](../mkmapitemannotation.md) and [MKMapFeatureAnnotation](../mkmapfeatureannotation.md). Please return `nil` for annotations where a selection accessory is not desired.

No accessory will be displayed if…

- nil is returned
- [- mapView:selectionAccessoryForAnnotation:](<mapview(__selectionaccessoryfor_).md>) is not implemented
- the accessory returned is not supported for `annotation`

## See Also

### Managing the display of overlays

- [- mapView:rendererForOverlay:](<mapview(__rendererfor_).md>) — Asks the delegate for a renderer object to use when drawing the specified overlay.
- [- mapView:didAddOverlayRenderers:](<mapview(__didadd_)-793gj.md>) — Tells the delegate when the map view adds one or more renderer objects to the map.
- [- mapView:viewForOverlay:](<mapview(__viewfor_)-6j267.md>) — Asks the delegate for the overlay view to use when displaying the specified overlay object. _(deprecated)_
- [- mapView:didAddOverlayViews:](<mapview(__didaddoverlayviews_).md>) — Tells the delegate when the map adds one or more overlay views to the map. _(deprecated)_
