---
title: scale
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/imagerenderer/scale
source_url: 'https://developer.apple.com/documentation/swiftui/imagerenderer/scale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/imagerenderer/scale.json'
content_hash: 'sha256:ca48b753e7100d9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImageRenderer](../imagerenderer.md)

# scale

<sub>Instance Property</sub>

The scale at which to render the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor final var scale: CGFloat { get set }
```

## Discussion

This value is a ratio of view points to image pixels. This relationship means that values greater than `1.0` create an image larger than the original content view, and less than `1.0` creates a smaller image. The following example shows a 100 x 50 rectangle view and an image rendered from it with a `scale` of `2.0`, resulting in an image size of 200 x 100.

```swift
let rectangle = Rectangle()
    .frame(width: 100, height: 50)
let renderer = ImageRenderer(content: rectangle)
renderer.scale = 2.0
if let rendered = renderer.cgImage {
    print("Scaled image: \(rendered.width) x \(rendered.height)")
}
// Prints "Scaled image: 200 x 100"
```

The default value of this property is `1.0`.

## See Also

### Accessing renderer properties

- [proposedSize](proposedsize.md) — The size proposed to the root view.
- [isOpaque](isopaque.md) — A Boolean value that indicates whether the alpha channel of the image is fully opaque.
- [colorMode](colormode.md) — The working color space and storage format of the image.
- [allowedDynamicRange](alloweddynamicrange.md) — The allowed dynamic range of the image, or nil to mark that the dynamic range of the image should be unrestricted. This property defaults to `sdr`, i.e. HDR content will be tone mapped to SDR.
