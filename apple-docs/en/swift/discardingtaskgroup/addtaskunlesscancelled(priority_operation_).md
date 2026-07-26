---
title: 'addTaskUnlessCancelled(priority:operation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/discardingtaskgroup/addtaskunlesscancelled(priority:operation:)'
source_url: 'https://developer.apple.com/documentation/swift/discardingtaskgroup/addtaskunlesscancelled(priority:operation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/discardingtaskgroup/addtaskunlesscancelled%28priority%3Aoperation%3A%29.json'
content_hash: 'sha256:772cbc85dcbfc3b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DiscardingTaskGroup](../discardingtaskgroup.md)

# addTaskUnlessCancelled(priority:operation:)

<sub>Instance Method</sub>

Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addTaskUnlessCancelled(priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async -> Void) -> Bool
```

## Parameters

- `priority` — The priority of the operation task. Omit this parameter or pass `nil` to inherit the task group’s base priority.

- `operation` — The operation to execute as part of the task group.

## Return Value

`true` if the child task was added to the group; otherwise `false`.
