---
title: 'convert(_:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicoordinatespace/convert(_:to:)-3imkt'
source_url: 'https://developer.apple.com/documentation/uikit/uicoordinatespace/convert(_:to:)-3imkt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicoordinatespace/convert%28_%3Ato%3A%29-3imkt.json'
content_hash: 'sha256:016b03ffde37642a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICoordinateSpace](../uicoordinatespace.md)

# convert(_:to:)

<sub>Instance Method</sub>

Converts a rectangle from the coordinate space of the current object to the specified coordinate space.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func convert(_ rect: CGRect, to coordinateSpace: any UICoordinateSpace) -> CGRect
```

## Parameters

- `rect` — A rectangle specified in the coordinate system of the current object.

- `coordinateSpace` — The coordinate space into which `rect` is to be converted.

## Return Value

A rectangle specified in the target coordinate space.

## See Also

### Converting between coordinate spaces

- [- convertPoint:toCoordinateSpace:](<convert(__to_)-2ub7a.md>) — Converts a point from the coordinate space of the current object to the specified coordinate space.
- [- convertPoint:fromCoordinateSpace:](<convert(__from_)-3w27q.md>) — Converts a point from the specified coordinate space to the coordinate space of the current object.
- [- convertRect:fromCoordinateSpace:](<convert(__from_)-9921a.md>) — Converts a rectangle from the specified coordinate space to the coordinate space of the current object.
