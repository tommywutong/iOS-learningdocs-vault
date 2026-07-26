---
title: 'addTask(priority:operation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/throwingdiscardingtaskgroup/addtask(priority:operation:)'
source_url: 'https://developer.apple.com/documentation/swift/throwingdiscardingtaskgroup/addtask(priority:operation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingdiscardingtaskgroup/addtask%28priority%3Aoperation%3A%29.json'
content_hash: 'sha256:0e8ca6f6ef520497'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ThrowingDiscardingTaskGroup](../throwingdiscardingtaskgroup.md)

# addTask(priority:operation:)

<sub>Instance Method</sub>

Adds a child task to the group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addTask(priority: TaskPriority? = nil, operation: sending @escaping @isolated(any) () async throws -> Void)
```

## Parameters

- `priority` — The priority of the operation task. Omit this parameter or pass `nil` to inherit the task group’s base priority.

- `operation` — The operation to execute as part of the task group.

## Discussion

This method doesn’t throw an error, even if the child task does. Instead, the corresponding call to `ThrowingTaskGroup.next()` rethrows that error.
