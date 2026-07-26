---
title: 'pathContains(_:mode:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/pathcontains(_:mode:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/pathcontains(_:mode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/pathcontains%28_%3Amode%3A%29.json'
content_hash: 'sha256:e5b208b83b22c963'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# pathContains(_:mode:)

<sub>Instance Method</sub>

Checks to see whether the specified point is contained in the current path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func pathContains(_ point: CGPoint, mode: CGPathDrawingMode) -> Bool
```

## Parameters

- `point` — The point to check, specified in user space units.

- `mode` — A path drawing mode. See [CGPathDrawingMode](../cgpathdrawingmode.md).

## Return Value

Returns `true` if `point` is inside the current path of the graphics context; `false` otherwise.

## Discussion

A point is contained within the path of a graphics context if the point is inside the painted region when the path is stroked or filled with opaque colors using the specified path drawing mode. A point can be inside a path only if the path is explicitly closed by calling the function [CGContextClosePath](<closepath().md>) for paths drawn directly to the current context, or [CGPathCloseSubpath](<../cgmutablepath/closesubpath().md>) for paths first created as [CGPath](../cgpath.md) objects and then drawn to the current context.

## See Also

### Examining the Current Graphics Path

- [CGContextGetPathBoundingBox](boundingboxofpath.md) — Returns the smallest rectangle that contains the current path.
- [CGContextGetPathCurrentPoint](currentpointofpath.md) — Returns the current point in a non-empty path.
- [CGContextIsPathEmpty](ispathempty.md) — Indicates whether the current path contains any subpaths.
