---
title: AVPlayerVideoOutput.Sample
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayervideooutput/sample
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayervideooutput/sample'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayervideooutput/sample.json'
content_hash: 'sha256:099f47fffb86c6a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerVideoOutput](../avplayervideooutput.md)

# AVPlayerVideoOutput.Sample

<sub>Structure</sub>

A video frame along with auxiliary information for display at the specified presentation time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Sample
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Inspecting a sample

- [activeConfiguration](sample/activeconfiguration.md) — The active configuration that this sample was derived from.
- [presentationTime](sample/presentationtime.md) — A CMTime representing the true display deadline for this sample in terms of the corresponding AVPlayerItem’s timebase.
- [taggedBuffers](sample/taggedbuffers.md) — An array of CMTaggedBuffers containing the frame for the specified time.

## See Also

### Accessing video data

- [sample(forHostTime:)](<sample(forhosttime_).md>) — Retrieves a video sample along with auxiliary information for display at the specified host time.
- [taggedBuffers(forHostTime:)](<taggedbuffers(forhosttime_).md>) _(deprecated)_
- [Configuration](configuration.md) — An object that provides configuration information for the related player item.
