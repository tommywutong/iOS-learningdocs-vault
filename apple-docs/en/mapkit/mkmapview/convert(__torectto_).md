---
title: 'convert(_:toRectTo:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/convert(_:torectto:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/convert(_:torectto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/convert%28_%3Atorectto%3A%29.json'
content_hash: 'sha256:7f383ce1c58de122'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# convert(_:toRectTo:)

<sub>Instance Method</sub>

Converts a map region to a rectangle in the specified view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func convert(_ region: MKCoordinateRegion, toRectTo view: UIView?) -> CGRect
```

<sub>macOS</sub>

```swift
func convert(_ region: MKCoordinateRegion, toRectTo view: NSView?) -> CGRect
```

## Parameters

- `region` — The map region that you want to find the corresponding view rectangle for.

- `view` — The view where you want to locate the specified map region. If this parameter is `nil`, the method specifies the returned rectangle in the window’s coordinate system. If `view` isn’t `nil`, the rectangle belongs to the same window as the map view.

## Return Value

The rectangle corresponding to the specified map region.

## See Also

### Converting map coordinates

- [- convertCoordinate:toPointToView:](<convert(__topointto_).md>) — Converts a map coordinate to a point in the specified view.
- [- convertPoint:toCoordinateFromView:](<convert(__tocoordinatefrom_).md>) — Converts a point in the specified view’s coordinate system to a map coordinate.
- [- convertRect:toRegionFromView:](<convert(__toregionfrom_).md>) — Converts a rectangle in the specified view’s coordinate system to a map region.
