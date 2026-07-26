---
title: SnapshotData
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/snapshotdata
source_url: 'https://developer.apple.com/documentation/swiftui/snapshotdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/snapshotdata.json'
content_hash: 'sha256:731a9f2c9ed34f8e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SnapshotData

<sub>Structure</sub>

The associated data of a snapshot background task.

<sub>watchOS</sub>

```swift
struct SnapshotData
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the data

- [identifier](snapshotdata/identifier.md) — The identifier associated with this snapshot request.
- [reason](snapshotdata/reason.md) — The reason for a background snapshot task.
- [SnapshotReason](snapshotdata/snapshotreason.md) — The reason for a background snapshot task.

## See Also

### Handling background tasks

- [backgroundTask(_:action:)](<scene/backgroundtask(__action_).md>) — Runs the specified action when the system provides a background task.
- [BackgroundTask](backgroundtask.md) — The kinds of background tasks that your app or extension can handle.
- [SnapshotResponse](snapshotresponse.md) — Your application’s response to a snapshot background task.
