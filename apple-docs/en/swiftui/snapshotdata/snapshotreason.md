---
title: SnapshotData.SnapshotReason
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/snapshotdata/snapshotreason
source_url: 'https://developer.apple.com/documentation/swiftui/snapshotdata/snapshotreason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/snapshotdata/snapshotreason.json'
content_hash: 'sha256:0d770af39ce188a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SnapshotData](../snapshotdata.md)

# SnapshotData.SnapshotReason

<sub>Enumeration</sub>

The reason for a background snapshot task.

<sub>watchOS</sub>

```swift
enum SnapshotReason
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the snapshot reasons

- [SnapshotData.SnapshotReason.appBackgrounded](snapshotreason/appbackgrounded.md) — The app transitioned from the foreground to the background.
- [SnapshotData.SnapshotReason.appScheduled](snapshotreason/appscheduled.md) — The app scheduled this snapshot.
- [SnapshotData.SnapshotReason.complicationUpdate](snapshotreason/complicationupdate.md) — The app updated the complication timeline.
- [SnapshotData.SnapshotReason.prelaunch](snapshotreason/prelaunch.md) — The system needs a snapshot for the dock, but the app has not been launched yet.
- [SnapshotData.SnapshotReason.returnToDefaultState](snapshotreason/returntodefaultstate.md) — It has been more than an hour since the user’s last interaction with the app; the app’s snapshot should return to its default state.

## See Also

### Getting the data

- [identifier](identifier.md) — The identifier associated with this snapshot request.
- [reason](reason.md) — The reason for a background snapshot task.
