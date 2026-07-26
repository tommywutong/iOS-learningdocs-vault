---
title: 'draw(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/draw(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/draw(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/draw%28in%3A%29.json'
content_hash: 'sha256:cba8e605941bc7bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# draw(in:)

<sub>Instance Method</sub>

Draws the entire image in the specified rectangle, scaling it as necessary to fit.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func draw(in rect: CGRect)
```

## Parameters

- `rect` — The rectangle (in the coordinate system of the graphics context) in which to draw the image.

## Discussion

This method draws the entire image in the current graphics context, respecting the image’s orientation setting. In the default coordinate system, images are situated down and to the right of the origin of the specified rectangle. This method respects any transforms applied to the current graphics context, however.

This method draws the image at full opacity using the [CGBlendMode.normal](../../coregraphics/cgblendmode/normal.md) blend mode.

## See Also

### Drawing images

- [- drawAtPoint:](<draw(at_).md>) — Draws the image at the specified point in the current context.
- [- drawAtPoint:blendMode:alpha:](<draw(at_blendmode_alpha_).md>) — Draws the entire image at the specified point using the custom compositing options.
- [- drawInRect:blendMode:alpha:](<draw(in_blendmode_alpha_).md>) — Draws the entire image in the specified rectangle using the specified compositing options.
- [- drawAsPatternInRect:](<drawaspattern(in_).md>) — Draws a tiled Quartz pattern using the receiver’s contents as the tile pattern.
