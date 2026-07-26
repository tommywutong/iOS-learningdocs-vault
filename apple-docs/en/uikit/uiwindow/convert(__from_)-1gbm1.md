---
title: 'convert(_:from:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwindow/convert(_:from:)-1gbm1'
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/convert(_:from:)-1gbm1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/convert%28_%3Afrom%3A%29-1gbm1.json'
content_hash: 'sha256:36e6302d80b232c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# convert(_:from:)

<sub>Instance Method</sub>

Converts a point from the coordinate system of a given window to the coordinate system of the current window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func convert(_ point: CGPoint, from window: UIWindow?) -> CGPoint
```

## Parameters

- `point` — A point specifying a location in the coordinate system of `window`.

- `window` — The source window containing the specified `point`. Specify `nil` to convert the point from the logical coordinate system of the screen, which is measured in points.

## Return Value

The point converted to the coordinate system of the current window.

## See Also

### Converting coordinates

- [- convertPoint:toWindow:](<convert(__to_)-687rw.md>) — Converts a point from the current window’s coordinate system to the coordinate system of another window.
- [- convertRect:toWindow:](<convert(__to_)-7k3l0.md>) — Converts a rectangle from the current window’s coordinate system to the coordinate system of another window.
- [- convertRect:fromWindow:](<convert(__from_)-10p2b.md>) — Converts a rectangle from the coordinate system of another window to coordinate system of the current window.
