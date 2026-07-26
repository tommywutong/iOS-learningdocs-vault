---
title: Task.Group
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swift/task/group
source_url: 'https://developer.apple.com/documentation/swift/task/group'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/group.json'
content_hash: 'sha256:48630fa2028cfe36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# Task.Group

<sub>Type Alias</sub>

> [!warning] Deprecated
> `Task.Group` was replaced by `ThrowingTaskGroup` and `TaskGroup` and will be removed shortly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Group<TaskResult> = ThrowingTaskGroup<TaskResult, any Error> where TaskResult : Sendable
```

## See Also

### Deprecated

- [Handle](handle.md) _(deprecated)_
- [Priority](priority.md) _(deprecated)_
- [CancellationError()](<cancellationerror().md>) _(deprecated)_
- [getResult()](<getresult().md>) _(deprecated)_
- [get()](<get()-4i2gt.md>) _(deprecated)_
- [get()](<get()-4ohks.md>) _(deprecated)_
- [sleep(_:)](<sleep(__).md>) _(deprecated)_
- [suspend()](<suspend().md>) _(deprecated)_
- [runDetached(priority:operation:)](<rundetached(priority_operation_)-88zf5.md>) — Deprecated, available only for source compatibility reasons. _(deprecated)_
- [runDetached(priority:operation:)](<rundetached(priority_operation_)-8s8lh.md>) — Deprecated, available only for source compatibility reasons. _(deprecated)_
- [withCancellationHandler(handler:operation:)](<withcancellationhandler(handler_operation_).md>) _(deprecated)_
- [withGroup(resultType:returning:body:)](<withgroup(resulttype_returning_body_).md>) _(deprecated)_
- [withTaskCancellationHandler(handler:operation:)](<../withtaskcancellationhandler(handler_operation_).md>) _(deprecated)_
