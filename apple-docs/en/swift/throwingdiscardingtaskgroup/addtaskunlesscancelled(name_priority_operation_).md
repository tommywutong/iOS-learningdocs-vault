---
title: 'addTaskUnlessCancelled(name:priority:operation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/throwingdiscardingtaskgroup/addtaskunlesscancelled(name:priority:operation:)'
source_url: 'https://developer.apple.com/documentation/swift/throwingdiscardingtaskgroup/addtaskunlesscancelled(name:priority:operation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingdiscardingtaskgroup/addtaskunlesscancelled%28name%3Apriority%3Aoperation%3A%29.json'
content_hash: 'sha256:0bd0cd1cc3bdcfb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ThrowingDiscardingTaskGroup](../throwingdiscardingtaskgroup.md)

# addTaskUnlessCancelled(name:priority:operation:)

<sub>Instance Method</sub>

Adds a child task to the group, unless the group has been canceled. Returns a boolean value indicating if the task was successfully added to the group or not.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addTaskUnlessCancelled(name: String?, priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async throws -> Void) -> Bool
```

## Parameters

- `name` — Human readable name of this task.

- `priority` — The priority of the operation task. Omit this parameter or pass `nil` to inherit the task group’s base priority.

- `operation` — The operation to execute as part of the task group.

## Return Value

`true` if the child task was added to the group; otherwise `false`.

## Discussion

This method doesn’t throw an error, even if the child task does. Instead, the corresponding call to `ThrowingTaskGroup.next()` rethrows that error.
