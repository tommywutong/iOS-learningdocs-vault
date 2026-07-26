---
title: SnapshotData.SnapshotReason.complicationUpdate
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/snapshotdata/snapshotreason/complicationupdate
source_url: 'https://developer.apple.com/documentation/swiftui/snapshotdata/snapshotreason/complicationupdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/snapshotdata/snapshotreason/complicationupdate.json'
content_hash: 'sha256:1e863a3066f3b9e4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SnapshotData](../../snapshotdata.md) · [SnapshotReason](../snapshotreason.md)

# SnapshotData.SnapshotReason.complicationUpdate

<sub>Case</sub>

The app updated the complication timeline.

<sub>watchOS</sub>

```swift
case complicationUpdate
```

## See Also

### Getting the snapshot reasons

- [SnapshotData.SnapshotReason.appBackgrounded](appbackgrounded.md) — The app transitioned from the foreground to the background.
- [SnapshotData.SnapshotReason.appScheduled](appscheduled.md) — The app scheduled this snapshot.
- [SnapshotData.SnapshotReason.prelaunch](prelaunch.md) — The system needs a snapshot for the dock, but the app has not been launched yet.
- [SnapshotData.SnapshotReason.returnToDefaultState](returntodefaultstate.md) — It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.
