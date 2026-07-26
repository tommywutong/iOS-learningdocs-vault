---
title: AVVideoDecompressionPropertiesKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 10.13+, tvOS 26.4+, visionOS 1.0+, watchOS 26.4+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideodecompressionpropertieskey
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideodecompressionpropertieskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideodecompressionpropertieskey.json'
content_hash: 'sha256:6ed0df1d05b17c92'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoDecompressionPropertiesKey

<sub>Global Variable</sub>

The key that indicates the video decompression properties to pass to the video decoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let AVVideoDecompressionPropertiesKey: String
```

## Discussion

The value for this key is specified as an [NSDictionary](../foundation/nsdictionary.md) object containing other keys to pass to the video decoder.

## See Also

### Compression

- [AVVideoCompressionPropertiesKey](avvideocompressionpropertieskey.md) — A key to access the dictionary of compression properties for a video asset.
- [AVVideoAverageBitRateKey](avvideoaveragebitratekey.md) — A key to access the average bit rate—as bits per second—used in compressing video.
- [AVVideoQualityKey](avvideoqualitykey.md) — A key to set the JPEG compression quality of the video.
- [AVVideoMaxKeyFrameIntervalKey](avvideomaxkeyframeintervalkey.md) — A key to access the maximum interval between keyframes.
- [AVVideoMaxKeyFrameIntervalDurationKey](avvideomaxkeyframeintervaldurationkey.md) — A key to access the maximum interval duration between keyframes.
- [AVVideoAllowFrameReorderingKey](avvideoallowframereorderingkey.md) — A key to access permission to reorder frames.
- [AVVideoAppleProRAWBitDepthKey](avvideoappleprorawbitdepthkey.md) — A key to access the Apple ProRAW bit depth.
