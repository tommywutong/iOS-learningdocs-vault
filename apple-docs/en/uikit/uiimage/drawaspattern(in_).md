---
title: 'drawAsPattern(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/drawaspattern(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/drawaspattern(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/drawaspattern%28in%3A%29.json'
content_hash: 'sha256:db9153ef50c442bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# drawAsPattern(in:)

<sub>Instance Method</sub>

Draws a tiled Quartz pattern using the receiver’s contents as the tile pattern.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func drawAsPattern(in rect: CGRect)
```

## Parameters

- `rect` — The rectangle (in the coordinate system of the graphics context) in which to draw the image.

## Discussion

This method uses a Quartz pattern to tile the image in the specified rectangle. The image is tiled with no gaps and the fill color is ignored. In the default coordinate system, the image tiles are situated down and to the right of the origin of the specified rectangle. This method respects any transforms applied to the current graphics context, however.

## See Also

### Drawing images

- [- drawAtPoint:](<draw(at_).md>) — Draws the image at the specified point in the current context.
- [- drawAtPoint:blendMode:alpha:](<draw(at_blendmode_alpha_).md>) — Draws the entire image at the specified point using the custom compositing options.
- [- drawInRect:](<draw(in_).md>) — Draws the entire image in the specified rectangle, scaling it as necessary to fit.
- [- drawInRect:blendMode:alpha:](<draw(in_blendmode_alpha_).md>) — Draws the entire image in the specified rectangle using the specified compositing options.
