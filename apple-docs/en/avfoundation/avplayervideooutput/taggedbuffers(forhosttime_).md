---
title: 'taggedBuffers(forHostTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.2+（27.0 起废弃）, iPadOS 17.2+（27.0 起废弃）, Mac Catalyst 17.2+（27.0 起废弃）, macOS 14.2+（27.0 起废弃）, tvOS 17.2+（27.0 起废弃）, visionOS 1.1+（27.0 起废弃）, watchOS 10.2+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avplayervideooutput/taggedbuffers(forhosttime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayervideooutput/taggedbuffers(forhosttime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayervideooutput/taggedbuffers%28forhosttime%3A%29.json'
content_hash: 'sha256:a171b4f1d27a2986'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerVideoOutput](../avplayervideooutput.md)

# taggedBuffers(forHostTime:)

<sub>Instance Method</sub>

> [!warning] Deprecated
> Use AVPlayerVideoOutput.sample instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func taggedBuffers(forHostTime hostTime: CMTime) -> (taggedBufferGroup: [CMTaggedBuffer], presentationTime: CMTime, activeConfiguration: AVPlayerVideoOutput.Configuration)?
```

## See Also

### Accessing video data

- [sample(forHostTime:)](<sample(forhosttime_).md>) — Retrieves a video sample along with auxiliary information for display at the specified host time.
- [Sample](sample.md) — A video frame along with auxiliary information for display at the specified presentation time.
- [Configuration](configuration.md) — An object that provides configuration information for the related player item.
