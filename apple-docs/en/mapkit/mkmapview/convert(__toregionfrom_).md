---
title: 'convert(_:toRegionFrom:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/convert(_:toregionfrom:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/convert(_:toregionfrom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/convert%28_%3Atoregionfrom%3A%29.json'
content_hash: 'sha256:f76c701e083242da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# convert(_:toRegionFrom:)

<sub>Instance Method</sub>

Converts a rectangle in the specified view’s coordinate system to a map region.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func convert(_ rect: CGRect, toRegionFrom view: UIView?) -> MKCoordinateRegion
```

<sub>macOS</sub>

```swift
func convert(_ rect: CGRect, toRegionFrom view: NSView?) -> MKCoordinateRegion
```

## Parameters

- `rect` — The rectangle you want to convert.

- `view` — The view that serves as the reference coordinate system for the `rect` parameter.

## Return Value

The map region corresponding to the specified view rectangle.

## See Also

### Converting map coordinates

- [- convertCoordinate:toPointToView:](<convert(__topointto_).md>) — Converts a map coordinate to a point in the specified view.
- [- convertPoint:toCoordinateFromView:](<convert(__tocoordinatefrom_).md>) — Converts a point in the specified view’s coordinate system to a map coordinate.
- [- convertRegion:toRectToView:](<convert(__torectto_).md>) — Converts a map region to a rectangle in the specified view.
