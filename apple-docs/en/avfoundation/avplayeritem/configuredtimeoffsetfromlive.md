---
title: configuredTimeOffsetFromLive
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/configuredtimeoffsetfromlive
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/configuredtimeoffsetfromlive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/configuredtimeoffsetfromlive.json'
content_hash: 'sha256:bb2aba7d3da7a707'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# configuredTimeOffsetFromLive

<sub>Instance Property</sub>

A time value that indicates the offset from the live time to start playback, or resume playback after a seek to positive infinity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var configuredTimeOffsetFromLive: CMTime { get set }
```

## Discussion

For nonlive stream content, the value is [invalid](../../coremedia/cmtime/invalid.md).

## See Also

### Managing time offsets

- [automaticallyPreservesTimeOffsetFromLive](automaticallypreservestimeoffsetfromlive.md) — A Boolean value that indicates whether the player preserves its time offset from the live time after a buffering operation.
- [recommendedTimeOffsetFromLive](recommendedtimeoffsetfromlive.md) — A recommended time offset from the live time based on observed network conditions.
