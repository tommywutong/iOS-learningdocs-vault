---
title: 'view(for:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（13.0 起废弃）, iPadOS 4.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkmapview/view(for:)-38z60'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/view(for:)-38z60'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/view%28for%3A%29-38z60.json'
content_hash: 'sha256:59865468c84a4295'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# view(for:)

<sub>Instance Method</sub>

Returns the view associated with the overlay object, if any.

> [!warning] Deprecated
> Use the [- rendererForOverlay:](<renderer(for_).md>) method instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func view(for overlay: any MKOverlay) -> MKOverlayView
```

## Parameters

- `overlay` — The overlay object whose view you want.

## Return Value

The view associated with the overlay object or `nil` if the overlay is not onscreen.

## See Also

### Methods

- [- mapView:didAddOverlayViews:](<../mkmapviewdelegate/mapview(__didaddoverlayviews_).md>) — Tells the delegate when the map adds one or more overlay views to the map. _(deprecated)_
- [- mapView:viewForOverlay:](<../mkmapviewdelegate/mapview(__viewfor_)-6j267.md>) — Asks the delegate for the overlay view to use when displaying the specified overlay object. _(deprecated)_
