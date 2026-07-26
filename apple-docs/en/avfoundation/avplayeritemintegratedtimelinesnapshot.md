---
title: AVPlayerItemIntegratedTimelineSnapshot
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemintegratedtimelinesnapshot
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimelinesnapshot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimelinesnapshot.json'
content_hash: 'sha256:2ef6ed9afbf07317'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemIntegratedTimelineSnapshot

<sub>Class</sub>

An immutable representation of inspectable details of an integrated timeline object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVPlayerItemIntegratedTimelineSnapshot
```

## Overview

A snapshot doesn’t reflect the new timeline state as playback progresses. You can request a new snapshot instance from an [AVPlayerItemIntegratedTimeline](avplayeritemintegratedtimeline.md) that reflect the latest timeline state.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting the snapshot

- [duration](avplayeritemintegratedtimelinesnapshot/duration.md) — The total duration of the primary item and scheduled interstitial events.
- [currentSegment](avplayeritemintegratedtimelinesnapshot/currentsegment.md) — The currently playing segment.
- [segments](avplayeritemintegratedtimelinesnapshot/segments.md) — The segments for this snapshot.
- [AVPlayerItemSegment](avplayeritemsegment.md) — An immutable object that represents a segment of time on the integrated timeline.
- [currentTime](avplayeritemintegratedtimelinesnapshot/currenttime.md) — The current time on the integrated timeline when the system created the snapshot.
- [currentDate](avplayeritemintegratedtimelinesnapshot/currentdate.md) — The current date on the integrated timeline when the system created the snapshot.

### Time mapping

- [segmentAndOffsetIntoSegment(forTimelineTime:)](<avplayeritemintegratedtimelinesnapshot/segmentandoffsetintosegment(fortimelinetime_).md>)

## See Also

### Inspecting snapshots

- [currentSnapshot](avplayeritemintegratedtimeline/currentsnapshot.md) — An immutable representation of the timeline state at time of request.
- [AVPlayerIntegratedTimelineSnapshotsOutOfSyncNotification](avplayeritemintegratedtimeline/snapshotsoutofsyncnotification.md) — A notification the system posts when the snapshot objects provided by this timeline become out of sync with the current timeline state.
