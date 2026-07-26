---
title: snapshotsOutOfSyncNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemintegratedtimeline/snapshotsoutofsyncnotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/snapshotsoutofsyncnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimeline/snapshotsoutofsyncnotification.json'
content_hash: 'sha256:eb746bcc2bdc7435'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemIntegratedTimeline](../avplayeritemintegratedtimeline.md)

# snapshotsOutOfSyncNotification

<sub>Type Property</sub>

A notification the system posts when the snapshot objects provided by this timeline become out of sync with the current timeline state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let snapshotsOutOfSyncNotification: NSNotification.Name
```

## Topics

### User-information keys

- [AVPlayerIntegratedTimelineSnapshotsOutOfSyncReasonKey](snapshotsoutofsyncreasonkey.md) — A key to retrieve the reason for an out-of-sync state notification.
- [AVPlayerIntegratedTimelineSnapshotsOutOfSyncReason](../avplayerintegratedtimelinesnapshotsoutofsyncreason.md) — Constants that represent the reason for an out-of-sync state.

## See Also

### Inspecting snapshots

- [currentSnapshot](currentsnapshot.md) — An immutable representation of the timeline state at time of request.
- [AVPlayerItemIntegratedTimelineSnapshot](../avplayeritemintegratedtimelinesnapshot.md) — An immutable representation of inspectable details of an integrated timeline object.
