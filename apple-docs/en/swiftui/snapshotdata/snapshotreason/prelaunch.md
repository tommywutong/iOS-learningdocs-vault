---
title: SnapshotData.SnapshotReason.prelaunch
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/snapshotdata/snapshotreason/prelaunch
source_url: 'https://developer.apple.com/documentation/swiftui/snapshotdata/snapshotreason/prelaunch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/snapshotdata/snapshotreason/prelaunch.json'
content_hash: 'sha256:983753079b9636db'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SnapshotData](../../snapshotdata.md) · [SnapshotReason](../snapshotreason.md)

# SnapshotData.SnapshotReason.prelaunch

<sub>Case</sub>

The system needs a snapshot for the dock, but the app has not been launched yet.

<sub>watchOS</sub>

```swift
case prelaunch
```

## See Also

### Getting the snapshot reasons

- [SnapshotData.SnapshotReason.appBackgrounded](appbackgrounded.md) — The app transitioned from the foreground to the background.
- [SnapshotData.SnapshotReason.appScheduled](appscheduled.md) — The app scheduled this snapshot.
- [SnapshotData.SnapshotReason.complicationUpdate](complicationupdate.md) — The app updated the complication timeline.
- [SnapshotData.SnapshotReason.returnToDefaultState](returntodefaultstate.md) — It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.
