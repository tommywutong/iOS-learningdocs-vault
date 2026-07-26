---
title: 'jpegData(withCompressionQuality:actions:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicsimagerenderer/jpegdata(withcompressionquality:actions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer/jpegdata(withcompressionquality:actions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerenderer/jpegdata%28withcompressionquality%3Aactions%3A%29.json'
content_hash: 'sha256:91bcfa3f6b9921dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsImageRenderer](../uigraphicsimagerenderer.md)

# jpegData(withCompressionQuality:actions:)

<sub>Instance Method</sub>

Creates a JPEG-encoded image from a set of drawing instructions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func jpegData(withCompressionQuality compressionQuality: CGFloat, actions: (UIGraphicsImageRendererContext) -> Void) -> Data
```

## Parameters

- `compressionQuality` — A [CGFloat](../../corefoundation/cgfloat-swift.struct.md) value between `0.0` and `1.0`, representing the compression level the JPEG encoder should use. A value of `1.0` specifies lossless compression, and a value of `0.0` specifies maximum compression.

- `actions` — A [DrawingActions](drawingactions.md) block that, when invoked by the renderer, executes a set of drawing instructions to create the output image.

## Return Value

A [Data](../../foundation/data.md) object representing a JPEG-encoded representation of the image created by the supplied drawing actions.

## Discussion

You provide a set of drawing instructions as the block argument to this method, and the method returns the resulting image as a JPEG-encoded [Data](../../foundation/data.md) object.

The JPEG format does not support transparency, so this method is only appropriate for use with opaque images.

You can call this method repeatedly to create multiple images, each of which has identical dimensions and format.

## See Also

### Creating images

- [- imageWithActions:](<image(actions_).md>) — Creates an image from a set of drawing instructions.
- [- PNGDataWithActions:](<pngdata(actions_).md>) — Creates a PNG-encoded image from a set of drawing instructions.
- [DrawingActions](drawingactions.md) — A closure for drawing an image.
