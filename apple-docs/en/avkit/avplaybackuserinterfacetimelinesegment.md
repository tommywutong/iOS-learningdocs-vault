---
title: AVPlaybackUserInterfaceTimelineSegment
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift, occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacetimelinesegment
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimelinesegment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacetimelinesegment.json'
content_hash: 'sha256:489715552c80dc60'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceTimelineSegment

<sub>Class</sub>

Represents a contiguous segment of timeline content with specific playback characteristics.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class AVPlaybackUserInterfaceTimelineSegment
```

## Overview

Timeline segments divide media content into distinct regions, each with its own classification and behavior rules. Segments are typically used to distinguish between primary content and auxiliary content such as advertisements or bonus material, and to control whether users can seek or skip through specific portions of the timeline.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(coder:)](<avplaybackuserinterfacetimelinesegment/init(coder_).md>) _(beta)_
- [- initWithTimeRange:segmentType:marked:requiresLinearPlayback:identifier:](<avplaybackuserinterfacetimelinesegment/init(timerange_segmenttype_marked_requireslinearplayback_identifier_).md>) — Initializes a new timeline segment with the specified characteristics. _(beta)_

### Instance Properties

- [identifier](avplaybackuserinterfacetimelinesegment/identifier.md) — Optional external identifier for tracking or analytics purposes. May correspond to advertisement IDs, chapter markers, or other external systems. _(beta)_
- [marked](avplaybackuserinterfacetimelinesegment/ismarked.md) — Indicates whether this segment should be visually highlighted or marked in the timeline UI. _(beta)_
- [requiresLinearPlayback](avplaybackuserinterfacetimelinesegment/requireslinearplayback.md) — Indicates whether this segment must be played sequentially without seeking or skipping. Typically used for advertisements or important announcements. _(beta)_
- [segmentType](avplaybackuserinterfacetimelinesegment/segmenttype.md) — The type of content within this segment, indicating whether it is primary program content or a specific category of auxiliary content. _(beta)_
- [timeRange](avplaybackuserinterfacetimelinesegment/timerange.md) — The time range defining the segment’s position and duration within the overall timeline. _(beta)_

## See Also

### Timeline

- [AVPlaybackUserInterfaceTimeControllable](avplaybackuserinterfacetimecontrollable-50vcy.md) — Provides time control and navigation capabilities for media content. _(beta)_
- [AVPlaybackUserInterfacePlaybackPosition](avplaybackuserinterfaceplaybackposition.md) — A snapshot comprising a playback position recorded at a known host time and the rate of position advancement. _(beta)_
- [AVPlaybackUserInterfaceTimelineSegmentType](avplaybackuserinterfacetimelinesegmenttype.md) — Describes the type of content within a timeline segment. _(beta)_
