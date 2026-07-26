---
title: SnapshotResponse
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/snapshotresponse
source_url: 'https://developer.apple.com/documentation/swiftui/snapshotresponse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/snapshotresponse.json'
content_hash: 'sha256:741c0d07488fd5c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SnapshotResponse

<sub>Structure</sub>

Your application’s response to a snapshot background task.

<sub>watchOS</sub>

```swift
struct SnapshotResponse
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a response

- [init(restoredDefaultState:estimatedSnapshotExpiration:identifier:)](<snapshotresponse/init(restoreddefaultstate_estimatedsnapshotexpiration_identifier_).md>) — Creates a snapshot response.

## See Also

### Handling background tasks

- [backgroundTask(_:action:)](<scene/backgroundtask(__action_).md>) — Runs the specified action when the system provides a background task.
- [BackgroundTask](backgroundtask.md) — The kinds of background tasks that your app or extension can handle.
- [SnapshotData](snapshotdata.md) — The associated data of a snapshot background task.
