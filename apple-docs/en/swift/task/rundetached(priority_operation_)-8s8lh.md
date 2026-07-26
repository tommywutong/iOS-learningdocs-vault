---
title: 'runDetached(priority:operation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/task/rundetached(priority:operation:)-8s8lh'
source_url: 'https://developer.apple.com/documentation/swift/task/rundetached(priority:operation:)-8s8lh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/rundetached%28priority%3Aoperation%3A%29-8s8lh.json'
content_hash: 'sha256:82826aa8d4edc352'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# runDetached(priority:operation:)

<sub>Type Method</sub>

Deprecated, available only for source compatibility reasons.

> [!warning] Deprecated
> `Task.runDetached` was replaced by `Task.detached` and will be removed shortly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult static func runDetached(priority: TaskPriority? = nil, operation: @escaping @isolated(any) @Sendable () async -> Success) -> Task<Success, Never>
```

## See Also

### Deprecated

- [Group](group.md) _(deprecated)_
- [Handle](handle.md) _(deprecated)_
- [Priority](priority.md) _(deprecated)_
- [CancellationError()](<cancellationerror().md>) _(deprecated)_
- [getResult()](<getresult().md>) _(deprecated)_
- [get()](<get()-4i2gt.md>) _(deprecated)_
- [get()](<get()-4ohks.md>) _(deprecated)_
- [sleep(_:)](<sleep(__).md>) _(deprecated)_
- [suspend()](<suspend().md>) _(deprecated)_
- [runDetached(priority:operation:)](<rundetached(priority_operation_)-88zf5.md>) — Deprecated, available only for source compatibility reasons. _(deprecated)_
- [withCancellationHandler(handler:operation:)](<withcancellationhandler(handler_operation_).md>) _(deprecated)_
- [withGroup(resultType:returning:body:)](<withgroup(resulttype_returning_body_).md>) _(deprecated)_
- [withTaskCancellationHandler(handler:operation:)](<../withtaskcancellationhandler(handler_operation_).md>) _(deprecated)_
