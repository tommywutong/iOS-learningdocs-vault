---
title: AVVideoMaxKeyFrameIntervalKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideomaxkeyframeintervalkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideomaxkeyframeintervalkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideomaxkeyframeintervalkey.json'
content_hash: 'sha256:d9bd2705429b046a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoMaxKeyFrameIntervalKey

<sub>Global Variable</sub>

A key to access the maximum interval between keyframes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let AVVideoMaxKeyFrameIntervalKey: String
```

## Discussion

The value for this key is an instance of `NSNumber`. A value of `1` signifies keyframes only.

## See Also

### Compression

- [AVVideoCompressionPropertiesKey](avvideocompressionpropertieskey.md) — A key to access the dictionary of compression properties for a video asset.
- [AVVideoDecompressionPropertiesKey](avvideodecompressionpropertieskey.md) — The key that indicates the video decompression properties to pass to the video decoder.
- [AVVideoAverageBitRateKey](avvideoaveragebitratekey.md) — A key to access the average bit rate—as bits per second—used in compressing video.
- [AVVideoQualityKey](avvideoqualitykey.md) — A key to set the JPEG compression quality of the video.
- [AVVideoMaxKeyFrameIntervalDurationKey](avvideomaxkeyframeintervaldurationkey.md) — A key to access the maximum interval duration between keyframes.
- [AVVideoAllowFrameReorderingKey](avvideoallowframereorderingkey.md) — A key to access permission to reorder frames.
- [AVVideoAppleProRAWBitDepthKey](avvideoappleprorawbitdepthkey.md) — A key to access the Apple ProRAW bit depth.
