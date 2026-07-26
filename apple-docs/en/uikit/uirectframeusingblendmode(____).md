---
title: 'UIRectFrameUsingBlendMode(_:_:)'
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uirectframeusingblendmode(_:_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uirectframeusingblendmode(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uirectframeusingblendmode%28_%3A_%3A%29.json'
content_hash: 'sha256:1e1c326437979e3d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIRectFrameUsingBlendMode(_:_:)

<sub>Function</sub>

Draws a frame around the inside of a rectangle using the specified blend mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIRectFrameUsingBlendMode(_ rect: CGRect, _ blendMode: CGBlendMode)
```

## Parameters

- `rect` — The rectangle defining the area in which to draw.

- `blendMode` — The blend mode to use during drawing.

## Discussion

This function draws a frame around the inside of rect in the fill color of the current graphics context and using the specified blend mode. The width is equal to 1.0 in the current coordinate system. Since the frame is drawn inside the rectangle, it’s visible even if drawing is clipped to the rectangle. If the current graphics context is `nil`, this function does nothing.

Because this function doesn’t draw directly on the line, but rather inside it, it uses the current fill color (not stroke color) when drawing.

This function may be called from any thread of your app.

## See Also

### Paths

- [UIBezierPath](uibezierpath.md) — A path that consists of straight and curved line segments that you can render in your custom views.
- [UIRectFill](<uirectfill(__).md>) — Fills the specified rectangle with the current color.
- [UIRectFillUsingBlendMode](<uirectfillusingblendmode(____).md>) — Fills a rectangle with the current fill color using the specified blend mode.
- [UIRectFrame](<uirectframe(__).md>) — Draws a frame around the inside of the specified rectangle.
