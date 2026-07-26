---
title: 'sample(forHostTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayervideooutput/sample(forhosttime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayervideooutput/sample(forhosttime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayervideooutput/sample%28forhosttime%3A%29.json'
content_hash: 'sha256:99f519396a33abb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerVideoOutput](../avplayervideooutput.md)

# sample(forHostTime:)

<sub>Instance Method</sub>

Retrieves a video sample along with auxiliary information for display at the specified host time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sample(forHostTime hostTime: CMTime) -> AVPlayerVideoOutput.Sample?
```

## Parameters

- `hostTime` — A CMTime that expresses a desired host time.

## Return Value

A sample containing the frame, presentation timestamp, and active configuration for the specified host time, or nil if no sample was available for that host time.

## See Also

### Accessing video data

- [Sample](sample.md) — A video frame along with auxiliary information for display at the specified presentation time.
- [taggedBuffers(forHostTime:)](<taggedbuffers(forhosttime_).md>) _(deprecated)_
- [Configuration](configuration.md) — An object that provides configuration information for the related player item.
