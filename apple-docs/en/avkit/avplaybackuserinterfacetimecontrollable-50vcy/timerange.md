---
title: timeRange
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacetimecontrollable-50vcy/timerange
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-50vcy/timerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacetimecontrollable-50vcy/timerange.json'
content_hash: 'sha256:ed3b082e97e35ec8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceTimeControllable](../avplaybackuserinterfacetimecontrollable-50vcy.md)

# timeRange

<sub>Instance Property</sub>

The time range representing the total duration and bounds of the media content.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor var timeRange: CMTimeRange { get }
```

## Discussion

For on-demand content, `start` is typically zero and `duration` is the total length of the content.

For live content without DVR, set [timeRange](timerange.md) to a zero-duration range at the current live edge and advance it as the edge moves; [seekableTimeRanges](seekabletimeranges.md) must be nil or empty.

For live content with DVR, set [timeRange](timerange.md) to the available DVR window and advance both `start` and `end` as the window rolls. Use [seekableTimeRanges](seekabletimeranges.md) to indicate which portion is seekable.

The duration is always a finite, non-negative value.
