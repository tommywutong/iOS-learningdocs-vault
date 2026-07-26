---
title: currentSnapshot
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemintegratedtimeline/currentsnapshot
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/currentsnapshot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimeline/currentsnapshot.json'
content_hash: 'sha256:3706e2d082a1cd07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemIntegratedTimeline](../avplayeritemintegratedtimeline.md)

# currentSnapshot

<sub>Instance Property</sub>

An immutable representation of the timeline state at time of request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentSnapshot: AVPlayerItemIntegratedTimelineSnapshot { get }
```

## Discussion

A timeline snapshot provides a read-only view of the details of the timeline. Because a snapshot provides a fixed view of the timeline at the time of the request, its state doesn’t update as playback continues.

## See Also

### Inspecting snapshots

- [AVPlayerItemIntegratedTimelineSnapshot](../avplayeritemintegratedtimelinesnapshot.md) — An immutable representation of inspectable details of an integrated timeline object.
- [AVPlayerIntegratedTimelineSnapshotsOutOfSyncNotification](snapshotsoutofsyncnotification.md) — A notification the system posts when the snapshot objects provided by this timeline become out of sync with the current timeline state.
