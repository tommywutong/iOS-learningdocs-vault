---
title: 'render(in:for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaptionrenderer/render(in:for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/render(in:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionrenderer/render%28in%3Afor%3A%29.json'
content_hash: 'sha256:337a25902bda2b3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionRenderer](../avcaptionrenderer.md)

# render(in:for:)

<sub>Instance Method</sub>

Draw the captions for the time you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func render(in ctx: CGContext, for time: CMTime)
```

## Parameters

- `ctx` — The drawing content.

- `time` — The time value for which the system draws the captions.
