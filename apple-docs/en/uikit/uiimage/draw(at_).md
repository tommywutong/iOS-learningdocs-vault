---
title: 'draw(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/draw(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/draw(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/draw%28at%3A%29.json'
content_hash: 'sha256:ee56be2b1a864b47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# draw(at:)

<sub>Instance Method</sub>

Draws the image at the specified point in the current context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func draw(at point: CGPoint)
```

## Parameters

- `point` — The point at which to draw the top-left corner of the image.

## Discussion

This method draws the entire image in the current graphics context, respecting the image’s orientation setting. In the default coordinate system, images are situated down and to the right of the specified point. This method respects any transforms applied to the current graphics context, however.

This method draws the image at full opacity using the [CGBlendMode.normal](../../coregraphics/cgblendmode/normal.md) blend mode.

## See Also

### Drawing images

- [- drawAtPoint:blendMode:alpha:](<draw(at_blendmode_alpha_).md>) — Draws the entire image at the specified point using the custom compositing options.
- [- drawInRect:](<draw(in_).md>) — Draws the entire image in the specified rectangle, scaling it as necessary to fit.
- [- drawInRect:blendMode:alpha:](<draw(in_blendmode_alpha_).md>) — Draws the entire image in the specified rectangle using the specified compositing options.
- [- drawAsPatternInRect:](<drawaspattern(in_).md>) — Draws a tiled Quartz pattern using the receiver’s contents as the tile pattern.
