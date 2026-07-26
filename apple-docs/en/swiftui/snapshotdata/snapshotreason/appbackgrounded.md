---
title: SnapshotData.SnapshotReason.appBackgrounded
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/snapshotdata/snapshotreason/appbackgrounded
source_url: 'https://developer.apple.com/documentation/swiftui/snapshotdata/snapshotreason/appbackgrounded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/snapshotdata/snapshotreason/appbackgrounded.json'
content_hash: 'sha256:bc17187af4d361c5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SnapshotData](../../snapshotdata.md) · [SnapshotReason](../snapshotreason.md)

# SnapshotData.SnapshotReason.appBackgrounded

<sub>Case</sub>

The app transitioned from the foreground to the background.

<sub>watchOS</sub>

```swift
case appBackgrounded
```

## See Also

### Getting the snapshot reasons

- [SnapshotData.SnapshotReason.appScheduled](appscheduled.md) — The app scheduled this snapshot.
- [SnapshotData.SnapshotReason.complicationUpdate](complicationupdate.md) — The app updated the complication timeline.
- [SnapshotData.SnapshotReason.prelaunch](prelaunch.md) — The system needs a snapshot for the dock, but the app has not been launched yet.
- [SnapshotData.SnapshotReason.returnToDefaultState](returntodefaultstate.md) — It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.
