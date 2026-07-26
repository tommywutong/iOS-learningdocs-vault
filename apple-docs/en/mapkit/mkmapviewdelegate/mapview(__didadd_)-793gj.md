---
title: 'mapView(_:didAdd:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapviewdelegate/mapview(_:didadd:)-793gj'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:didadd:)-793gj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapviewdelegate/mapview%28_%3Adidadd%3A%29-793gj.json'
content_hash: 'sha256:1152baf07234f330'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapViewDelegate](../mkmapviewdelegate.md)

# mapView(_:didAdd:)

<sub>Instance Method</sub>

Tells the delegate when the map view adds one or more renderer objects to the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func mapView(_ mapView: MKMapView, didAdd renderers: [MKOverlayRenderer])
```

## Parameters

- `mapView` — The map view that adds the renderer objects.

- `renderers` — The renderer objects that the map view adds.

## Discussion

The map view adds renderer objects when it needs them to draw their contents, which might be prior to those contents appearing onscreen. It calls this method to let you know that the renderer is active and in use. By the time the map view calls this method, it has already added specified renderers to the map.

## See Also

### Managing the display of overlays

- [- mapView:selectionAccessoryForAnnotation:](<mapview(__selectionaccessoryfor_).md>) — Specifies the accessory to display for a selected annotation
- [- mapView:rendererForOverlay:](<mapview(__rendererfor_).md>) — Asks the delegate for a renderer object to use when drawing the specified overlay.
- [- mapView:viewForOverlay:](<mapview(__viewfor_)-6j267.md>) — Asks the delegate for the overlay view to use when displaying the specified overlay object. _(deprecated)_
- [- mapView:didAddOverlayViews:](<mapview(__didaddoverlayviews_).md>) — Tells the delegate when the map adds one or more overlay views to the map. _(deprecated)_
