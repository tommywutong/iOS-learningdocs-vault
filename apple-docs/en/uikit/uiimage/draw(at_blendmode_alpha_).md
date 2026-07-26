---
title: 'draw(at:blendMode:alpha:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/draw(at:blendmode:alpha:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/draw(at:blendmode:alpha:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/draw%28at%3Ablendmode%3Aalpha%3A%29.json'
content_hash: 'sha256:0837c1a001350387'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# draw(at:blendMode:alpha:)

<sub>Instance Method</sub>

Draws the entire image at the specified point using the custom compositing options.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func draw(at point: CGPoint, blendMode: CGBlendMode, alpha: CGFloat)
```

## Parameters

- `point` — The point at which to draw the top-left corner of the image.

- `blendMode` — The blend mode to use when compositing the image.

- `alpha` — The desired opacity of the image, specified as a value between 0.0 and 1.0. A value of 0.0 renders the image totally transparent while 1.0 renders it fully opaque. Values larger than 1.0 are interpreted as 1.0.

## Discussion

This method draws the entire image in the current graphics context, respecting the image’s orientation setting. In the default coordinate system, images are situated down and to the right of the specified point. This method respects any transforms applied to the current graphics context, however.

## See Also

### Drawing images

- [- drawAtPoint:](<draw(at_).md>) — Draws the image at the specified point in the current context.
- [- drawInRect:](<draw(in_).md>) — Draws the entire image in the specified rectangle, scaling it as necessary to fit.
- [- drawInRect:blendMode:alpha:](<draw(in_blendmode_alpha_).md>) — Draws the entire image in the specified rectangle using the specified compositing options.
- [- drawAsPatternInRect:](<drawaspattern(in_).md>) — Draws a tiled Quartz pattern using the receiver’s contents as the tile pattern.
