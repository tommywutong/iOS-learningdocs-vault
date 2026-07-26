---
title: 'UIRectFrame(_:)'
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uirectframe(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uirectframe(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uirectframe%28_%3A%29.json'
content_hash: 'sha256:4a1c8170f25de442'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIRectFrame(_:)

<sub>Function</sub>

Draws a frame around the inside of the specified rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIRectFrame(_ rect: CGRect)
```

## Parameters

- `rect` — The rectangle defining the area in which to draw.

## Discussion

This function draws a frame around the inside of `rect` in the stroke color of the current graphics context and using the `kCGBlendModeCopy` blend mode. The width is equal to 1.0 in the current coordinate system. Because the frame is drawn inside the rectangle, it is visible even if drawing is clipped to the rectangle. If the current graphics context is `nil`, this function does nothing.

This function may be called from any thread of your app.

## See Also

### Paths

- [UIBezierPath](uibezierpath.md) — A path that consists of straight and curved line segments that you can render in your custom views.
- [UIRectFill](<uirectfill(__).md>) — Fills the specified rectangle with the current color.
- [UIRectFillUsingBlendMode](<uirectfillusingblendmode(____).md>) — Fills a rectangle with the current fill color using the specified blend mode.
- [UIRectFrameUsingBlendMode](<uirectframeusingblendmode(____).md>) — Draws a frame around the inside of a rectangle using the specified blend mode.
