---
title: 'convert(_:toPointTo:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/convert(_:topointto:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/convert(_:topointto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/convert%28_%3Atopointto%3A%29.json'
content_hash: 'sha256:f65f8e9e6255b3f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# convert(_:toPointTo:)

<sub>Instance Method</sub>

Converts a map coordinate to a point in the specified view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func convert(_ coordinate: CLLocationCoordinate2D, toPointTo view: UIView?) -> CGPoint
```

<sub>macOS</sub>

```swift
func convert(_ coordinate: CLLocationCoordinate2D, toPointTo view: NSView?) -> CGPoint
```

## Parameters

- `coordinate` — The map coordinate that you want to find the corresponding point for.

- `view` — The view where you want to locate the specified map coordinate. If this parameter is `nil`, the method specifies the returned point in the window’s coordinate system. If `view` isn’t `nil`, the point belongs to the same window as the map view.

## Return Value

The point (in the appropriate view or window coordinate system) corresponding to the specified latitude and longitude value.

## See Also

### Converting map coordinates

- [- convertPoint:toCoordinateFromView:](<convert(__tocoordinatefrom_).md>) — Converts a point in the specified view’s coordinate system to a map coordinate.
- [- convertRegion:toRectToView:](<convert(__torectto_).md>) — Converts a map region to a rectangle in the specified view.
- [- convertRect:toRegionFromView:](<convert(__toregionfrom_).md>) — Converts a rectangle in the specified view’s coordinate system to a map region.
