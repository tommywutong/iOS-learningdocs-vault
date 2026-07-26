---
title: 'mapView(_:rendererFor:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapview(_:rendererfor:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:rendererfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapview%28_%3Arendererfor%3A%29.json'
content_hash: 'sha256:333062ec9e0a790f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapView(_:rendererFor:)

<sub>Instance Method</sub>

Asks the delegate for a renderer object to use when drawing the specified overlay.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func mapView(_ mapView: MKMapView, rendererFor overlay: any MKOverlay) -> MKOverlayRenderer
```

## Parameters

- `mapView` — The map view that requests the renderer object.

- `overlay` — The overlay object that the map view is about to display.

## Return Value

The renderer to use when presenting the specified overlay on the map.

## Discussion

Implement this method and use it to provide an appropriate renderer object for your overlays. The renderer object is responsible for drawing the contents of your overlay when the map view requests it to. MapKit supports many different types of standard renderer objects and you may also define your own custom renderers.

## See Also

### Managing the display of overlays

- [- mapView:selectionAccessoryForAnnotation:](<mapview(__selectionaccessoryfor_).md>) — Specifies the accessory to display for a selected annotation
- [- mapView:didAddOverlayRenderers:](<mapview(__didadd_)-793gj.md>) — Tells the delegate when the map view adds one or more renderer objects to the map.
- [- mapView:viewForOverlay:](<mapview(__viewfor_)-6j267.md>) — Asks the delegate for the overlay view to use when displaying the specified overlay object. _(deprecated)_
- [- mapView:didAddOverlayViews:](<mapview(__didaddoverlayviews_).md>) — Tells the delegate when the map adds one or more overlay views to the map. _(deprecated)_
