---
title: 'mapRect(for:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkoverlayrenderer/maprect(for:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/maprect(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayrenderer/maprect%28for%3A%29.json'
content_hash: 'sha256:1772ce8cdcf4901e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayRenderer](../mkoverlayrenderer.md)

# mapRect(for:)

<sub>Instance Method</sub>

Returns the rectangle on the map that corresponds to the specified rectangle in the overlay renderer’s drawing area.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func mapRect(for rect: CGRect) -> MKMapRect
```

## Parameters

- `rect` — The rectangle in the overlay’s drawing area that you want to convert.

## Return Value

The rectangle on the two-dimensional map projection corresponding to the specified rectangle.

## Discussion

You may call this method safely from your view’s [- drawMapRect:zoomScale:inContext:](<draw(__zoomscale_in_).md>) method.

## See Also

### Converting points on the map

- [- pointForMapPoint:](<point(for_).md>) — Returns the point in the overlay renderer’s drawing area corresponding to the specified point on the map.
- [- mapPointForPoint:](<mappoint(for_).md>) — Returns the point on the map that corresponds to the specified point in the overlay renderer’s drawing area.
- [- rectForMapRect:](<rect(for_).md>) — Returns the rectangle in the overlay renderer’s drawing area corresponding to the specified rectangle on the map.
