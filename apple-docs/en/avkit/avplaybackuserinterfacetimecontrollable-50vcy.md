---
title: AVPlaybackUserInterfaceTimeControllable
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacetimecontrollable-50vcy
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-50vcy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacetimecontrollable-50vcy.json'
content_hash: 'sha256:e35f6e6d112dd194'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceTimeControllable

<sub>Protocol</sub>

Provides time control and navigation capabilities for media content.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor protocol AVPlaybackUserInterfaceTimeControllable : AnyObject, Observable
```

## Relationships

- **Inherits From**: [Observable](../observation/observable.md)

- **Inherited By**: [AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-92fri.md)

## Topics

### Instance Properties

- [currentSegment](avplaybackuserinterfacetimecontrollable-50vcy/currentsegment.md) — The segment containing the current playback position. _(beta)_
- [playbackPosition](avplaybackuserinterfacetimecontrollable-50vcy/playbackposition.md) — A snapshot of the current playback position. Must be updated — with a fresh `hostTime` — on play, pause, seek, scan, and buffering state changes. Must be observable. _(beta)_
- [seekableTimeRanges](avplaybackuserinterfacetimecontrollable-50vcy/seekabletimeranges.md) — Time ranges within the timeline where seeking operations are permitted. _(beta)_
- [segments](avplaybackuserinterfacetimecontrollable-50vcy/segments.md) — Segments representing different content types within the timeline. _(beta)_
- [timeRange](avplaybackuserinterfacetimecontrollable-50vcy/timerange.md) — The time range representing the total duration and bounds of the media content. _(beta)_

### Instance Methods

- [seek(to:tolerance:)](<avplaybackuserinterfacetimecontrollable-50vcy/seek(to_tolerance_).md>) — Requests a seek to the specified position. _(beta)_

## See Also

### Timeline

- [AVPlaybackUserInterfacePlaybackPosition](avplaybackuserinterfaceplaybackposition.md) — A snapshot comprising a playback position recorded at a known host time and the rate of position advancement. _(beta)_
- [AVPlaybackUserInterfaceTimelineSegment](avplaybackuserinterfacetimelinesegment.md) — Represents a contiguous segment of timeline content with specific playback characteristics. _(beta)_
- [AVPlaybackUserInterfaceTimelineSegmentType](avplaybackuserinterfacetimelinesegmenttype.md) — Describes the type of content within a timeline segment. _(beta)_
