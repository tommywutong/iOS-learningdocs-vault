---
title: 'point(for:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkoverlayrenderer/point(for:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/point(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayrenderer/point%28for%3A%29.json'
content_hash: 'sha256:5f3c73919135837b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayRenderer](../mkoverlayrenderer.md)

# point(for:)

<sub>Instance Method</sub>

Returns the point in the overlay renderer’s drawing area corresponding to the specified point on the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func point(for mapPoint: MKMapPoint) -> CGPoint
```

## Parameters

- `mapPoint` — A point on the two-dimensional map projection. If you have a coordinate value (latitude and longitude), you can use the [MKMapPointForCoordinate](<../mkmappoint/init(__).md>) function to convert that coordinate to a map point.

## Return Value

The point in the overlay’s drawing area that corresponds to the map point.

## Discussion

You may call this method safely from your view’s [- drawMapRect:zoomScale:inContext:](<draw(__zoomscale_in_).md>) method.

## See Also

### Converting points on the map

- [- mapPointForPoint:](<mappoint(for_).md>) — Returns the point on the map that corresponds to the specified point in the overlay renderer’s drawing area.
- [- rectForMapRect:](<rect(for_).md>) — Returns the rectangle in the overlay renderer’s drawing area corresponding to the specified rectangle on the map.
- [- mapRectForRect:](<maprect(for_).md>) — Returns the rectangle on the map that corresponds to the specified rectangle in the overlay renderer’s drawing area.
