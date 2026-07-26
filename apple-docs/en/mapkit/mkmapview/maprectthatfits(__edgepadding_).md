---
title: 'mapRectThatFits(_:edgePadding:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/maprectthatfits(_:edgepadding:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/maprectthatfits(_:edgepadding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/maprectthatfits%28_%3Aedgepadding%3A%29.json'
content_hash: 'sha256:d37ede4fceb36f06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# mapRectThatFits(_:edgePadding:)

<sub>Instance Method</sub>

Returns a centered, inset map rectangle with the same aspect ratio as the map view’s frame.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func mapRectThatFits(_ mapRect: MKMapRect, edgePadding insets: UIEdgeInsets) -> MKMapRect
```

<sub>macOS</sub>

```swift
func mapRectThatFits(_ mapRect: MKMapRect, edgePadding insets: NSEdgeInsets) -> MKMapRect
```

## Parameters

- `mapRect` — The initial map rectangle with the width and height you want to adjust.

- `insets` — The distance (in screen points) by which to inset the returned rectangle from the actual boundaries of the map view’s frame.

## Return Value

MapKit centers the map rectangle on the same point of the map, and adjusts the width and height to fit in the map view’s frame, minus its inset values.

## See Also

### Adjusting map regions and rectangles

- [- regionThatFits:](<regionthatfits(__).md>) — Adjusts the aspect ratio of the specified region to ensure that it fits in the map view’s frame.
- [- mapRectThatFits:](<maprectthatfits(__).md>) — Returns a centered map rectangle with the same aspect ratio as the map view’s frame.
