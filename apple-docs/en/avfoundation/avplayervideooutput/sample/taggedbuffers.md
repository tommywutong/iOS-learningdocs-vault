---
title: taggedBuffers
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayervideooutput/sample/taggedbuffers
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayervideooutput/sample/taggedbuffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayervideooutput/sample/taggedbuffers.json'
content_hash: 'sha256:1e657dcfac239a2e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayerVideoOutput](../../avplayervideooutput.md) · [Sample](../sample.md)

# taggedBuffers

<sub>Instance Property</sub>

An array of CMTaggedBuffers containing the frame for the specified time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let taggedBuffers: [CMTaggedDynamicBuffer]
```

## See Also

### Inspecting a sample

- [activeConfiguration](activeconfiguration.md) — The active configuration that this sample was derived from.
- [presentationTime](presentationtime.md) — A CMTime representing the true display deadline for this sample in terms of the corresponding AVPlayerItem’s timebase.
