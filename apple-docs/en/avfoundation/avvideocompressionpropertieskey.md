---
title: AVVideoCompressionPropertiesKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompressionpropertieskey
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompressionpropertieskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompressionpropertieskey.json'
content_hash: 'sha256:1544e58286c12156'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoCompressionPropertiesKey

<sub>Global Variable</sub>

A key to access the dictionary of compression properties for a video asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let AVVideoCompressionPropertiesKey: String
```

## Discussion

The value for this key is an instance of [NSDictionary](../foundation/nsdictionary.md). Add entries to this dictionary to manually change bit rate, B-frame delivery, I-frame interval, and codec quality. Querying the [- supportedOutputSettingsKeysForConnection:](<avcapturemoviefileoutput/supportedoutputsettingskeys(for_).md>) method reveals the keys supported for the current release and configuration.

## See Also

### Compression

- [AVVideoDecompressionPropertiesKey](avvideodecompressionpropertieskey.md) — The key that indicates the video decompression properties to pass to the video decoder.
- [AVVideoAverageBitRateKey](avvideoaveragebitratekey.md) — A key to access the average bit rate—as bits per second—used in compressing video.
- [AVVideoQualityKey](avvideoqualitykey.md) — A key to set the JPEG compression quality of the video.
- [AVVideoMaxKeyFrameIntervalKey](avvideomaxkeyframeintervalkey.md) — A key to access the maximum interval between keyframes.
- [AVVideoMaxKeyFrameIntervalDurationKey](avvideomaxkeyframeintervaldurationkey.md) — A key to access the maximum interval duration between keyframes.
- [AVVideoAllowFrameReorderingKey](avvideoallowframereorderingkey.md) — A key to access permission to reorder frames.
- [AVVideoAppleProRAWBitDepthKey](avvideoappleprorawbitdepthkey.md) — A key to access the Apple ProRAW bit depth.
