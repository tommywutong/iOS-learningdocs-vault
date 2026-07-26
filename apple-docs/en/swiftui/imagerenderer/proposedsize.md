---
title: proposedSize
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/imagerenderer/proposedsize
source_url: 'https://developer.apple.com/documentation/swiftui/imagerenderer/proposedsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/imagerenderer/proposedsize.json'
content_hash: 'sha256:5bd7d7f0aebf3090'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImageRenderer](../imagerenderer.md)

# proposedSize

<sub>Instance Property</sub>

The size proposed to the root view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor final var proposedSize: ProposedViewSize { get set }
```

## Discussion

The default value of this property, [unspecified](../proposedviewsize/unspecified.md), produces an image that matches the original view size. You can provide a custom [ProposedViewSize](../proposedviewsize.md) to override the view’s size in one or both dimensions.

## See Also

### Accessing renderer properties

- [scale](scale.md) — The scale at which to render the image.
- [isOpaque](isopaque.md) — A Boolean value that indicates whether the alpha channel of the image is fully opaque.
- [colorMode](colormode.md) — The working color space and storage format of the image.
- [allowedDynamicRange](alloweddynamicrange.md) — The allowed dynamic range of the image, or nil to mark that the dynamic range of the image should be unrestricted. This property defaults to `sdr`, i.e. HDR content will be tone mapped to SDR.
