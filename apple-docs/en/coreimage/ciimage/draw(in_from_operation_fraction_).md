---
title: 'draw(in:from:operation:fraction:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/draw(in:from:operation:fraction:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/draw(in:from:operation:fraction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/draw%28in%3Afrom%3Aoperation%3Afraction%3A%29.json'
content_hash: 'sha256:328c5fdb908a6b88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# draw(in:from:operation:fraction:)

<sub>Instance Method</sub>

Draws all or part of the image in the specified rectangle in the current coordinate system

<sub>macOS</sub>

```swift
func draw(in rect: NSRect, from fromRect: NSRect, operation op: NSCompositingOperation, fraction delta: CGFloat)
```

## Parameters

- `rect` — The rectangle in which to draw the image.

- `fromRect` — The source rectangle specifying the portion of the image you want to draw. The coordinates of this rectangle must be specified using the image’s own coordinate system.

- `op` — The compositing operation to use when drawing the image. For details, see [NSCompositingOperation](../../appkit/nscompositingoperation.md).

- `delta` — The opacity of the image, specified as a value from `0.0` to `1.0`. Specifying a value of `0.0` draws the image as fully transparent while a value of `1.0` draws the image as fully opaque. Values greater than `1.0` are interpreted as `1.0`.

## Discussion

If the `srcRect` and `dstRect` rectangles have different sizes, the source portion of the image is scaled to fit the specified destination rectangle. The image is otherwise positioned and oriented using the current coordinate system.

## See Also

### Drawing Images

- [- drawAtPoint:fromRect:operation:fraction:](<draw(at_from_operation_fraction_).md>) — Draws all or part of the image at the specified point in the current coordinate system.
