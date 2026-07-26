---
title: allowsCaptureOfClearKeyVideo
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 26.4+, visionOS 26.4+, watchOS 26.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/allowscaptureofclearkeyvideo
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/allowscaptureofclearkeyvideo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/allowscaptureofclearkeyvideo.json'
content_hash: 'sha256:7f72ba07b3bd8fc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# allowsCaptureOfClearKeyVideo

<sub>Instance Property</sub>

Indicates whether the video output of ClearKey Encrypted Video can be captured

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var allowsCaptureOfClearKeyVideo: Bool { get set }
```

## Discussion

When set to YES, and the video being played by AVPlayer is Clear Key encrypted, allows video to be captured in screenshots and screen recordings, and via APIs like AVPlayerItemVideoOutput and ScreenCaptureKit. When NO, Clear Key encrypted video will not be included in such captured video. This property has no effect on content protected by FairPlay Streaming. Default is NO.
