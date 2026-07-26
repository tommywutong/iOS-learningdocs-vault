---
title: 'UIRectFillUsingBlendMode(_:_:)'
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uirectfillusingblendmode(_:_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uirectfillusingblendmode(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uirectfillusingblendmode%28_%3A_%3A%29.json'
content_hash: 'sha256:cceeca082597c08c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIRectFillUsingBlendMode(_:_:)

<sub>Function</sub>

Fills a rectangle with the current fill color using the specified blend mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIRectFillUsingBlendMode(_ rect: CGRect, _ blendMode: CGBlendMode)
```

## Parameters

- `rect` — The rectangle defining the area in which to draw.

- `blendMode` — The blend mode to use during drawing.

## Discussion

This function draws the rectangle in the current graphics context. If the current graphics context is `nil`, this function does nothing.

This function may be called from any thread of your app.

## See Also

### Paths

- [UIBezierPath](uibezierpath.md) — A path that consists of straight and curved line segments that you can render in your custom views.
- [UIRectFill](<uirectfill(__).md>) — Fills the specified rectangle with the current color.
- [UIRectFrame](<uirectframe(__).md>) — Draws a frame around the inside of the specified rectangle.
- [UIRectFrameUsingBlendMode](<uirectframeusingblendmode(____).md>) — Draws a frame around the inside of a rectangle using the specified blend mode.
