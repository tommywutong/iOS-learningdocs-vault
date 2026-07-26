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
doc_path: '/documentation/uikit/uicoordinatespace/convert(_:to:)-2ub7a'
source_url: 'https://developer.apple.com/documentation/uikit/uicoordinatespace/convert(_:to:)-2ub7a'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicoordinatespace/convert%28_%3Ato%3A%29-2ub7a.json'
content_hash: 'sha256:c07243e888d8f2e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICoordinateSpace](../uicoordinatespace.md)

# convert(_:to:)

<sub>Instance Method</sub>

Converts a point from the coordinate space of the current object to the specified coordinate space.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func convert(_ point: CGPoint, to coordinateSpace: any UICoordinateSpace) -> CGPoint
```

## Parameters

- `point` — A point specified in the coordinate system of the current object.

- `coordinateSpace` — The coordinate space into which `point` is to be converted.

## Return Value

A point specified in the target coordinate space.

## See Also

### Converting between coordinate spaces

- [- convertPoint:fromCoordinateSpace:](<convert(__from_)-3w27q.md>) — Converts a point from the specified coordinate space to the coordinate space of the current object.
- [- convertRect:toCoordinateSpace:](<convert(__to_)-3imkt.md>) — Converts a rectangle from the coordinate space of the current object to the specified coordinate space.
- [- convertRect:fromCoordinateSpace:](<convert(__from_)-9921a.md>) — Converts a rectangle from the specified coordinate space to the coordinate space of the current object.
