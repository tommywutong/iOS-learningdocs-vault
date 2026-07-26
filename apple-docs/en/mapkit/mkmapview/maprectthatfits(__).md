---
title: 'mapRectThatFits(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/maprectthatfits(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/maprectthatfits(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/maprectthatfits%28_%3A%29.json'
content_hash: 'sha256:b03ea3d419495c01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# mapRectThatFits(_:)

<sub>Instance Method</sub>

Returns a centered map rectangle with the same aspect ratio as the map view’s frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func mapRectThatFits(_ mapRect: MKMapRect) -> MKMapRect
```

## Parameters

- `mapRect` — The initial map rectangle whose width and height you want to adjust to the view frame.

## Return Value

MapKit centers the map rectangle on the same point of the map, and adjusts the width and height to fit in the map view’s frame.

## Discussion

Returns a map rectangle with the same aspect ratio as the map view’s frame, centered at the same location as the specified map rectangle.

You can use this method to normalize map rectangle values before displaying the corresponding area. This method returns a new map rectangle that both contains the specified rectangle and fits neatly inside the map view’s frame.

## See Also

### Adjusting map regions and rectangles

- [- regionThatFits:](<regionthatfits(__).md>) — Adjusts the aspect ratio of the specified region to ensure that it fits in the map view’s frame.
- [- mapRectThatFits:edgePadding:](<maprectthatfits(__edgepadding_).md>) — Returns a centered, inset map rectangle with the same aspect ratio as the map view’s frame.
