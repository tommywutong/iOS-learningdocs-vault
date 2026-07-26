---
title: AVEdgeWidths
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avedgewidths
source_url: 'https://developer.apple.com/documentation/avfoundation/avedgewidths'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avedgewidths.json'
content_hash: 'sha256:ef39b24b6ac9b95b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVEdgeWidths

<sub>Structure</sub>

A structure that defines edge processing region widths.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVEdgeWidths
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Edge widths

- [left](avedgewidths/left.md) — The left-edge width.
- [top](avedgewidths/top.md) — The top-edge width.
- [right](avedgewidths/right.md) — The right-edge width.
- [bottom](avedgewidths/bottom.md) — The bottom-edge width.

### Initializers

- [init()](<avedgewidths/init().md>) — Creates an empty edge widths structure.
- [init(left:top:right:bottom:)](<avedgewidths/init(left_top_right_bottom_).md>) — Creates an edge widths structure with floating-point values.

## See Also

### Getting pixel and edge width information

- [edgeWidths](avvideocompositionrendercontext/edgewidths.md) — The width of the edge processing region on the left, top, right, and bottom edges, in pixels.
- [pixelAspectRatio](avvideocompositionrendercontext/pixelaspectratio.md) — The pixel aspect ratio for rendered frames.
- [AVPixelAspectRatio](avpixelaspectratio.md) — A structure that defines a pixel aspect ratio for a rendering context.
