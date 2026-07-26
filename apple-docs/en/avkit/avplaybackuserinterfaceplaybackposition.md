---
title: AVPlaybackUserInterfacePlaybackPosition
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift, occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfaceplaybackposition
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfaceplaybackposition.json'
content_hash: 'sha256:4df7ea9e7b436621'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfacePlaybackPosition

<sub>Class</sub>

A snapshot comprising a playback position recorded at a known host time and the rate of position advancement.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class AVPlaybackUserInterfacePlaybackPosition
```

## Overview

All three fields must be captured atomically by the conformer.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(coder:)](<avplaybackuserinterfaceplaybackposition/init(coder_).md>) _(beta)_
- [- initWithPosition:hostTime:rate:](<avplaybackuserinterfaceplaybackposition/init(position_hosttime_rate_).md>) — Creates a new playback position snapshot. _(beta)_

### Instance Properties

- [hostTime](avplaybackuserinterfaceplaybackposition/hosttime.md) — The mach host time at which `position` was accurate. _(beta)_
- [position](avplaybackuserinterfaceplaybackposition/position.md) — The playback position at the time of the snapshot. _(beta)_
- [rate](avplaybackuserinterfaceplaybackposition/rate.md) — The rate of position advancement at the time of the snapshot. Zero when paused; negative during reverse scan. _(beta)_

## See Also

### Timeline

- [AVPlaybackUserInterfaceTimeControllable](avplaybackuserinterfacetimecontrollable-50vcy.md) — Provides time control and navigation capabilities for media content. _(beta)_
- [AVPlaybackUserInterfaceTimelineSegment](avplaybackuserinterfacetimelinesegment.md) — Represents a contiguous segment of timeline content with specific playback characteristics. _(beta)_
- [AVPlaybackUserInterfaceTimelineSegmentType](avplaybackuserinterfacetimelinesegmenttype.md) — Describes the type of content within a timeline segment. _(beta)_
