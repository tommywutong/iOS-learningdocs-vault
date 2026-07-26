---
title: sampleBufferRenderer
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayer/samplebufferrenderer
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/samplebufferrenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer/samplebufferrenderer.json'
content_hash: 'sha256:49c52882817086b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferDisplayLayer](../avsamplebufferdisplaylayer.md)

# sampleBufferRenderer

<sub>Instance Property</sub>

An object that enqueues video sample buffers for rendering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sampleBufferRenderer: AVSampleBufferVideoRenderer { get }
```

## Discussion

This object allows you to safely enqueue sample buffers from a background thread.
