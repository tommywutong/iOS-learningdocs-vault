---
title: captions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionrenderer/captions
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/captions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionrenderer/captions.json'
content_hash: 'sha256:e8c1a63cd30eb226'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionRenderer](../avcaptionrenderer.md)

# captions

<sub>Instance Property</sub>

The captions to render.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var captions: [AVCaption] { get set }
```

## Discussion

This property value is an empty array if there are no captions for the system to render.

## See Also

### Configuring the renderer

- [bounds](bounds.md) — The drawing bounds of caption scenes.
