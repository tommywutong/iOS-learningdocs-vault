---
title: allowedDynamicRange
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/imagerenderer/alloweddynamicrange
source_url: 'https://developer.apple.com/documentation/swiftui/imagerenderer/alloweddynamicrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/imagerenderer/alloweddynamicrange.json'
content_hash: 'sha256:67b86d8efaa494fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImageRenderer](../imagerenderer.md)

# allowedDynamicRange

<sub>Instance Property</sub>

The allowed dynamic range of the image, or nil to mark that the dynamic range of the image should be unrestricted. This property defaults to `sdr`, i.e. HDR content will be tone mapped to SDR.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor final var allowedDynamicRange: Image.DynamicRange? { get set }
```

## See Also

### Accessing renderer properties

- [proposedSize](proposedsize.md) — The size proposed to the root view.
- [scale](scale.md) — The scale at which to render the image.
- [isOpaque](isopaque.md) — A Boolean value that indicates whether the alpha channel of the image is fully opaque.
- [colorMode](colormode.md) — The working color space and storage format of the image.
