---
title: AVVideoQualityKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideoqualitykey
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideoqualitykey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideoqualitykey.json'
content_hash: 'sha256:cfa3c762ad289bfb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoQualityKey

<sub>Global Variable</sub>

A key to set the JPEG compression quality of the video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let AVVideoQualityKey: String
```

## Discussion

The corresponding value is an instance of `NSNumber` 0.0-1.0.

## See Also

### Compression

- [AVVideoCompressionPropertiesKey](avvideocompressionpropertieskey.md) — A key to access the dictionary of compression properties for a video asset.
- [AVVideoDecompressionPropertiesKey](avvideodecompressionpropertieskey.md) — The key that indicates the video decompression properties to pass to the video decoder.
- [AVVideoAverageBitRateKey](avvideoaveragebitratekey.md) — A key to access the average bit rate—as bits per second—used in compressing video.
- [AVVideoMaxKeyFrameIntervalKey](avvideomaxkeyframeintervalkey.md) — A key to access the maximum interval between keyframes.
- [AVVideoMaxKeyFrameIntervalDurationKey](avvideomaxkeyframeintervaldurationkey.md) — A key to access the maximum interval duration between keyframes.
- [AVVideoAllowFrameReorderingKey](avvideoallowframereorderingkey.md) — A key to access permission to reorder frames.
- [AVVideoAppleProRAWBitDepthKey](avvideoappleprorawbitdepthkey.md) — A key to access the Apple ProRAW bit depth.
