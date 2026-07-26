---
title: AVVideoCleanApertureKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocleanaperturekey
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocleanaperturekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocleanaperturekey.json'
content_hash: 'sha256:162523e17c692bd7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoCleanApertureKey

<sub>Global Variable</sub>

A key that defines the region within the video dimension displayed during playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let AVVideoCleanApertureKey: String
```

## Discussion

The value for this key is an instance of `NSDictionary` containing one or more of the following keys: [AVVideoCleanApertureWidthKey](avvideocleanaperturewidthkey.md), [AVVideoCleanApertureHeightKey](avvideocleanapertureheightkey.md), [AVVideoCleanApertureHorizontalOffsetKey](avvideocleanaperturehorizontaloffsetkey.md), or [AVVideoCleanApertureVerticalOffsetKey](avvideocleanapertureverticaloffsetkey.md). If no clean aperture region is specified, the playback displays the entire frame.

## See Also

### Clean aperture

- [AVVideoCleanApertureWidthKey](avvideocleanaperturewidthkey.md) — A key to access the width of video that’s free from transition artifacts caused by signal encoding.
- [AVVideoCleanApertureHeightKey](avvideocleanapertureheightkey.md) — A key to access the height of video that’s free from transition artifacts caused by signal encoding.
- [AVVideoCleanApertureVerticalOffsetKey](avvideocleanapertureverticaloffsetkey.md) — A key to access the vertical offset of video that’s free from transition artifacts caused by signal encoding.
- [AVVideoCleanApertureHorizontalOffsetKey](avvideocleanaperturehorizontaloffsetkey.md) — A key to access the horizontal offset of video that’s free from transition artifacts caused by signal encoding.
