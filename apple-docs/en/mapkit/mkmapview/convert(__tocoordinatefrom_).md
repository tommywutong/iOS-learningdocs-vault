---
title: 'convert(_:toCoordinateFrom:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/convert(_:tocoordinatefrom:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/convert(_:tocoordinatefrom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/convert%28_%3Atocoordinatefrom%3A%29.json'
content_hash: 'sha256:436c899bf15279cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# convert(_:toCoordinateFrom:)

<sub>Instance Method</sub>

Converts a point in the specified view’s coordinate system to a map coordinate.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func convert(_ point: CGPoint, toCoordinateFrom view: UIView?) -> CLLocationCoordinate2D
```

<sub>macOS</sub>

```swift
func convert(_ point: CGPoint, toCoordinateFrom view: NSView?) -> CLLocationCoordinate2D
```

## Parameters

- `point` — The point you want to convert.

- `view` — The view that serves as the reference coordinate system for the `point` parameter.

## Return Value

The map coordinate at the specified point.

## See Also

### Converting map coordinates

- [- convertCoordinate:toPointToView:](<convert(__topointto_).md>) — Converts a map coordinate to a point in the specified view.
- [- convertRegion:toRectToView:](<convert(__torectto_).md>) — Converts a map region to a rectangle in the specified view.
- [- convertRect:toRegionFromView:](<convert(__toregionfrom_).md>) — Converts a rectangle in the specified view’s coordinate system to a map region.
