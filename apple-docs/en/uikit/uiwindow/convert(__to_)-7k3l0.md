---
title: 'convert(_:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwindow/convert(_:to:)-7k3l0'
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/convert(_:to:)-7k3l0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/convert%28_%3Ato%3A%29-7k3l0.json'
content_hash: 'sha256:6518c891985577f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# convert(_:to:)

<sub>Instance Method</sub>

Converts a rectangle from the current window’s coordinate system to the coordinate system of another window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func convert(_ rect: CGRect, to window: UIWindow?) -> CGRect
```

## Parameters

- `rect` — A rectangle in the current window’s coordinate system.

- `window` — The window defining the destination coordinate system for `rect`. Specify `nil` to convert the rectangle to the logical coordinate system of the screen, which is measured in points.

## Return Value

The rectangle converted to the coordinate system of `window`.

## See Also

### Converting coordinates

- [- convertPoint:toWindow:](<convert(__to_)-687rw.md>) — Converts a point from the current window’s coordinate system to the coordinate system of another window.
- [- convertPoint:fromWindow:](<convert(__from_)-1gbm1.md>) — Converts a point from the coordinate system of a given window to the coordinate system of the current window.
- [- convertRect:fromWindow:](<convert(__from_)-10p2b.md>) — Converts a rectangle from the coordinate system of another window to coordinate system of the current window.
