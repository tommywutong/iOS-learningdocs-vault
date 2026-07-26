---
title: SnapshotData.SnapshotReason.appScheduled
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/snapshotdata/snapshotreason/appscheduled
source_url: 'https://developer.apple.com/documentation/swiftui/snapshotdata/snapshotreason/appscheduled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/snapshotdata/snapshotreason/appscheduled.json'
content_hash: 'sha256:7b18cd91fadb8938'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SnapshotData](../../snapshotdata.md) · [SnapshotReason](../snapshotreason.md)

# SnapshotData.SnapshotReason.appScheduled

<sub>Case</sub>

The app scheduled this snapshot.

<sub>watchOS</sub>

```swift
case appScheduled
```

## See Also

### Getting the snapshot reasons

- [SnapshotData.SnapshotReason.appBackgrounded](appbackgrounded.md) — The app transitioned from the foreground to the background.
- [SnapshotData.SnapshotReason.complicationUpdate](complicationupdate.md) — The app updated the complication timeline.
- [SnapshotData.SnapshotReason.prelaunch](prelaunch.md) — The system needs a snapshot for the dock, but the app has not been launched yet.
- [SnapshotData.SnapshotReason.returnToDefaultState](returntodefaultstate.md) — It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.
