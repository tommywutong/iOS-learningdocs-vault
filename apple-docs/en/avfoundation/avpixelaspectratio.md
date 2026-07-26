---
title: AVPixelAspectRatio
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpixelaspectratio
source_url: 'https://developer.apple.com/documentation/avfoundation/avpixelaspectratio'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpixelaspectratio.json'
content_hash: 'sha256:74240929c519b0d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPixelAspectRatio

<sub>Structure</sub>

A structure that defines a pixel aspect ratio for a rendering context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVPixelAspectRatio
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Spacing

- [horizontalSpacing](avpixelaspectratio/horizontalspacing.md) — The pixel aspect ratio’s horizontal spacing value.
- [verticalSpacing](avpixelaspectratio/verticalspacing.md) — The pixel aspect ratio’s vertical spacing value.

### Initializers

- [init()](<avpixelaspectratio/init().md>) — Creates an empty pixel aspect ratio.
- [init(horizontalSpacing:verticalSpacing:)](<avpixelaspectratio/init(horizontalspacing_verticalspacing_).md>) — Creates a pixel aspect ratio with horizontal and vertical spacing values.

## See Also

### Getting pixel and edge width information

- [edgeWidths](avvideocompositionrendercontext/edgewidths.md) — The width of the edge processing region on the left, top, right, and bottom edges, in pixels.
- [AVEdgeWidths](avedgewidths.md) — A structure that defines edge processing region widths.
- [pixelAspectRatio](avvideocompositionrendercontext/pixelaspectratio.md) — The pixel aspect ratio for rendered frames.
