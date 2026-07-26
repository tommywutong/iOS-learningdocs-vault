---
title: 'draw(at:from:operation:fraction:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/draw(at:from:operation:fraction:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/draw(at:from:operation:fraction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/draw%28at%3Afrom%3Aoperation%3Afraction%3A%29.json'
content_hash: 'sha256:273e49b8b080fd8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# draw(at:from:operation:fraction:)

<sub>Instance Method</sub>

Draws all or part of the image at the specified point in the current coordinate system.

<sub>macOS</sub>

```swift
func draw(at point: NSPoint, from fromRect: NSRect, operation op: NSCompositingOperation, fraction delta: CGFloat)
```

## Parameters

- `point` — The location in the current coordinate system at which to draw the image.

- `fromRect` — The source rectangle specifying the portion of the image you want to draw. The coordinates of this rectangle must be specified using the image’s own coordinate system.

- `op` — The compositing operation to use when drawing the image. For details, see [NSCompositingOperation](../../appkit/nscompositingoperation.md).

- `delta` — The opacity of the image, specified as a value from `0.0` to `1.0`. Specifying a value of `0.0` draws the image as fully transparent while a value of `1.0` draws the image as fully opaque. Values greater than `1.0` are interpreted as `1.0`.

## Discussion

The image content is drawn at its current resolution and is not scaled unless the CTM of the current coordinate system itself contains a scaling factor. The image is otherwise positioned and oriented using the current coordinate system.

## See Also

### Drawing Images

- [- drawInRect:fromRect:operation:fraction:](<draw(in_from_operation_fraction_).md>) — Draws all or part of the image in the specified rectangle in the current coordinate system
