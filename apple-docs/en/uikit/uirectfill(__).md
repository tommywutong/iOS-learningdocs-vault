---
title: 'UIRectFill(_:)'
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uirectfill(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uirectfill(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uirectfill%28_%3A%29.json'
content_hash: 'sha256:24d9faa56ef78eae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIRectFill(_:)

<sub>Function</sub>

Fills the specified rectangle with the current color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIRectFill(_ rect: CGRect)
```

## Parameters

- `rect` — The rectangle defining the area in which to draw.

## Discussion

Fills the specified rectangle using the fill color of the current graphics context and the `kCGBlendModeCopy` blend mode.

This function may be called from any thread of your app.

## See Also

### Paths

- [UIBezierPath](uibezierpath.md) — A path that consists of straight and curved line segments that you can render in your custom views.
- [UIRectFillUsingBlendMode](<uirectfillusingblendmode(____).md>) — Fills a rectangle with the current fill color using the specified blend mode.
- [UIRectFrame](<uirectframe(__).md>) — Draws a frame around the inside of the specified rectangle.
- [UIRectFrameUsingBlendMode](<uirectframeusingblendmode(____).md>) — Draws a frame around the inside of a rectangle using the specified blend mode.
