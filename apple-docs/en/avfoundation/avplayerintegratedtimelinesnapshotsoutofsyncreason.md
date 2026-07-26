---
title: AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerintegratedtimelinesnapshotsoutofsyncreason
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerintegratedtimelinesnapshotsoutofsyncreason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerintegratedtimelinesnapshotsoutofsyncreason.json'
content_hash: 'sha256:2c4f67a0595ca857'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason

<sub>Structure</sub>

Constants that represent the reason for an out-of-sync state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the reasons

- [AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonSegmentsChanged](avplayerintegratedtimelinesnapshotsoutofsyncreason/segmentschanged.md) — The snapshot is out of sync due to a change of segments.
- [AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonCurrentSegmentChanged](avplayerintegratedtimelinesnapshotsoutofsyncreason/currentsegmentchanged.md) — The snapshot is out of sync due to a change of the current segment.
- [AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonLoadedTimeRangesChanged](avplayerintegratedtimelinesnapshotsoutofsyncreason/loadedtimerangeschanged.md) — The snapshot is out of sync due to a change of the loaded time ranges.

### Creating a reason

- [init(rawValue:)](<avplayerintegratedtimelinesnapshotsoutofsyncreason/init(rawvalue_).md>) — Creates a new out-of-sync reason from the value you specify.

## See Also

### User-information keys

- [AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonKey](avplayeritemintegratedtimeline/snapshotsoutofsyncreasonkey.md) — A key to retrieve the reason for an out-of-sync state notification.
