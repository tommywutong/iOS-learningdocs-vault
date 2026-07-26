---
title: AVVideoExpectedSourceFrameRateKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideoexpectedsourceframeratekey
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideoexpectedsourceframeratekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideoexpectedsourceframeratekey.json'
content_hash: 'sha256:803a154b5abff3b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoExpectedSourceFrameRateKey

<sub>Global Variable</sub>

The expected source frame rate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let AVVideoExpectedSourceFrameRateKey: String
```

## Discussion

This is not used to control the frame rate; it is provided as a hint to the video encoder so that it can set up internal configuration before compression begins. The actual frame rate  depends on frame duration and may vary. This should be set if an auto level [AVVideoProfileLevelKey](avvideoprofilelevelkey.md) is used, or if the source content has a high frame rate higher than 30 fps. The encoder might have to drop frames to satisfy bit stream requirements if this key is not specified.

## See Also

### Frame rate

- [AVVideoAverageNonDroppableFrameRateKey](avvideoaveragenondroppableframeratekey.md) — The desired average number of non-droppable frames to be encoded for each second of video.
