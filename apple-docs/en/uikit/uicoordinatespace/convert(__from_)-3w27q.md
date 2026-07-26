---
title: 'convert(_:from:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicoordinatespace/convert(_:from:)-3w27q'
source_url: 'https://developer.apple.com/documentation/uikit/uicoordinatespace/convert(_:from:)-3w27q'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicoordinatespace/convert%28_%3Afrom%3A%29-3w27q.json'
content_hash: 'sha256:96985358ff106e28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICoordinateSpace](../uicoordinatespace.md)

# convert(_:from:)

<sub>Instance Method</sub>

Converts a point from the specified coordinate space to the coordinate space of the current object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func convert(_ point: CGPoint, from coordinateSpace: any UICoordinateSpace) -> CGPoint
```

## Parameters

- `point` — A point in the specified coordinate space.

- `coordinateSpace` — The coordinate space in which `point` is specified.

## Return Value

A point specified in the coordinate space of the current object.

## See Also

### Converting between coordinate spaces

- [- convertPoint:toCoordinateSpace:](<convert(__to_)-2ub7a.md>) — Converts a point from the coordinate space of the current object to the specified coordinate space.
- [- convertRect:toCoordinateSpace:](<convert(__to_)-3imkt.md>) — Converts a rectangle from the coordinate space of the current object to the specified coordinate space.
- [- convertRect:fromCoordinateSpace:](<convert(__from_)-9921a.md>) — Converts a rectangle from the specified coordinate space to the coordinate space of the current object.
