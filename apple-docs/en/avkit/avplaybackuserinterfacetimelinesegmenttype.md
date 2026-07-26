---
title: AVPlaybackUserInterfaceTimelineSegmentType
framework: AVKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift, occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacetimelinesegmenttype
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimelinesegmenttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacetimelinesegmenttype.json'
content_hash: 'sha256:1b3833d27662f73c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceTimelineSegmentType

<sub>Enumeration</sub>

Describes the type of content within a timeline segment.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum AVPlaybackUserInterfaceTimelineSegmentType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [AVPlaybackUserInterfaceTimelineSegmentTypeAdvertisement](avplaybackuserinterfacetimelinesegmenttype/advertisement.md) — The segment contains an advertisement. _(beta)_
- [AVPlaybackUserInterfaceTimelineSegmentTypeBonus](avplaybackuserinterfacetimelinesegmenttype/bonus.md) — The segment contains bonus content, such as a post-credits scene or supplemental material. _(beta)_
- [AVPlaybackUserInterfaceTimelineSegmentTypeCredits](avplaybackuserinterfacetimelinesegmenttype/credits.md) — The segment contains end credits. _(beta)_
- [AVPlaybackUserInterfaceTimelineSegmentTypeIntro](avplaybackuserinterfacetimelinesegmenttype/intro.md) — The segment contains an opening title sequence. _(beta)_
- [AVPlaybackUserInterfaceTimelineSegmentTypeOther](avplaybackuserinterfacetimelinesegmenttype/other.md) — The segment contains auxiliary content of an unspecified type. _(beta)_
- [AVPlaybackUserInterfaceTimelineSegmentTypePrimary](avplaybackuserinterfacetimelinesegmenttype/primary.md) — The segment contains primary program content. _(beta)_
- [AVPlaybackUserInterfaceTimelineSegmentTypeRecap](avplaybackuserinterfacetimelinesegmenttype/recap.md) — The segment contains a recap of previous content. _(beta)_
- [AVPlaybackUserInterfaceTimelineSegmentTypeTrailer](avplaybackuserinterfacetimelinesegmenttype/trailer.md) — The segment contains a trailer or preview for other content. _(beta)_

### Initializers

- [init(rawValue:)](<avplaybackuserinterfacetimelinesegmenttype/init(rawvalue_).md>) _(beta)_

## See Also

### Timeline

- [AVPlaybackUserInterfaceTimeControllable](avplaybackuserinterfacetimecontrollable-50vcy.md) — Provides time control and navigation capabilities for media content. _(beta)_
- [AVPlaybackUserInterfacePlaybackPosition](avplaybackuserinterfaceplaybackposition.md) — A snapshot comprising a playback position recorded at a known host time and the rate of position advancement. _(beta)_
- [AVPlaybackUserInterfaceTimelineSegment](avplaybackuserinterfacetimelinesegment.md) — Represents a contiguous segment of timeline content with specific playback characteristics. _(beta)_
