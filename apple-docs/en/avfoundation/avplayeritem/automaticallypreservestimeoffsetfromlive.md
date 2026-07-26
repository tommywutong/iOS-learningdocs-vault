---
title: automaticallyPreservesTimeOffsetFromLive
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/automaticallypreservestimeoffsetfromlive
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/automaticallypreservestimeoffsetfromlive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/automaticallypreservestimeoffsetfromlive.json'
content_hash: 'sha256:dd3fe240a9d036a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# automaticallyPreservesTimeOffsetFromLive

<sub>Instance Property</sub>

A Boolean value that indicates whether the player preserves its time offset from the live time after a buffering operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var automaticallyPreservesTimeOffsetFromLive: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md). If the value is [true](../../swift/true.md), the player seeks forward after it finishes buffering to restore the position that the playhead had when buffering began, relative to the end of the player item’s [seekableTimeRanges](seekabletimeranges.md) property value.

> [!note] Note
> This property value has no effect if the asset isn’t a live stream.

## See Also

### Managing time offsets

- [recommendedTimeOffsetFromLive](recommendedtimeoffsetfromlive.md) — A recommended time offset from the live time based on observed network conditions.
- [configuredTimeOffsetFromLive](configuredtimeoffsetfromlive.md) — A time value that indicates the offset from the live time to start playback, or resume playback after a seek to positive infinity.
