---
title: AVVideoAverageBitRateKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideoaveragebitratekey
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideoaveragebitratekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideoaveragebitratekey.json'
content_hash: 'sha256:4e19339bd151a33e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoAverageBitRateKey

<sub>Global Variable</sub>

A key to access the average bit rate—as bits per second—used in compressing video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let AVVideoAverageBitRateKey: String
```

## Discussion

The value for this key is an instance of `NSNumber`.

## See Also

### Compression

- [AVVideoCompressionPropertiesKey](avvideocompressionpropertieskey.md) — A key to access the dictionary of compression properties for a video asset.
- [AVVideoDecompressionPropertiesKey](avvideodecompressionpropertieskey.md) — The key that indicates the video decompression properties to pass to the video decoder.
- [AVVideoQualityKey](avvideoqualitykey.md) — A key to set the JPEG compression quality of the video.
- [AVVideoMaxKeyFrameIntervalKey](avvideomaxkeyframeintervalkey.md) — A key to access the maximum interval between keyframes.
- [AVVideoMaxKeyFrameIntervalDurationKey](avvideomaxkeyframeintervaldurationkey.md) — A key to access the maximum interval duration between keyframes.
- [AVVideoAllowFrameReorderingKey](avvideoallowframereorderingkey.md) — A key to access permission to reorder frames.
- [AVVideoAppleProRAWBitDepthKey](avvideoappleprorawbitdepthkey.md) — A key to access the Apple ProRAW bit depth.
