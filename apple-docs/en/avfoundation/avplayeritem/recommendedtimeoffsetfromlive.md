---
title: recommendedTimeOffsetFromLive
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/recommendedtimeoffsetfromlive
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/recommendedtimeoffsetfromlive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/recommendedtimeoffsetfromlive.json'
content_hash: 'sha256:39f976eb031bbdba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# recommendedTimeOffsetFromLive

<sub>Instance Property</sub>

A recommended time offset from the live time based on observed network conditions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var recommendedTimeOffsetFromLive: CMTime { get }
```

## Discussion

For nonlive stream content, the value is [invalid](../../coremedia/cmtime/invalid.md).

## See Also

### Managing time offsets

- [automaticallyPreservesTimeOffsetFromLive](automaticallypreservestimeoffsetfromlive.md) — A Boolean value that indicates whether the player preserves its time offset from the live time after a buffering operation.
- [configuredTimeOffsetFromLive](configuredtimeoffsetfromlive.md) — A time value that indicates the offset from the live time to start playback, or resume playback after a seek to positive infinity.
