---
title: 'fillPath(using:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/fillpath(using:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/fillpath(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/fillpath%28using%3A%29.json'
content_hash: 'sha256:7227ec1c7e4a9a83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# fillPath(using:)

<sub>Instance Method</sub>

Paints the area within the current path, as determined by the specified fill rule.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fillPath(using rule: CGPathFillRule = .winding)
```

## Parameters

- `rule` — The rule for determining which areas to treat as the interior of the path. See [CGPathFillRule](../cgpathfillrule.md). This parameter defaults to the [CGPathFillRule.winding](../cgpathfillrule/winding.md) rule if unspecified.

## Discussion

If the current path contains any non-closed subpaths, this method treats each subpath as if it had been closed with the [CGContextClosePath](<closepath().md>) method, then applies the specified rule to determine which areas to fill.

After filling the path, this method clears the context’s current path.

## See Also

### Drawing the Current Graphics Path

- [CGContextDrawPath](<drawpath(using_).md>) — Draws the current path using the provided drawing mode.
- [CGPathDrawingMode](../cgpathdrawingmode.md) — Options for rendering a path.
- [CGContextStrokePath](<strokepath().md>) — Paints a line along the current path.
