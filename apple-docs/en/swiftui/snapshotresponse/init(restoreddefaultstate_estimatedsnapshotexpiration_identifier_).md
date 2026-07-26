---
title: 'init(restoredDefaultState:estimatedSnapshotExpiration:identifier:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/snapshotresponse/init(restoreddefaultstate:estimatedsnapshotexpiration:identifier:)'
source_url: 'https://developer.apple.com/documentation/swiftui/snapshotresponse/init(restoreddefaultstate:estimatedsnapshotexpiration:identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/snapshotresponse/init%28restoreddefaultstate%3Aestimatedsnapshotexpiration%3Aidentifier%3A%29.json'
content_hash: 'sha256:194ce6a5721e0ea3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SnapshotResponse](../snapshotresponse.md)

# init(restoredDefaultState:estimatedSnapshotExpiration:identifier:)

<sub>Initializer</sub>

Creates a snapshot response.

<sub>watchOS</sub>

```swift
init(restoredDefaultState: Bool = false, estimatedSnapshotExpiration: Date? = nil, identifier: String? = nil)
```

## Parameters

- `restoredDefaultState` — Pass `true` if your app has navigated back to its default launch scene.

- `estimatedSnapshotExpiration` — The preferred date and time for the next background snapshot refresh task. Use [distantFuture](../../foundation/date/distantfuture.md) if you don’t want to schedule the next refresh.

- `identifier` — A custom string to associate with the next background snapshot refresh task. This value is assigned to the next snapshot task’s `TaskData` userInfo property. Pass `nil` if you don’t want to associate any identifier with the next task.
