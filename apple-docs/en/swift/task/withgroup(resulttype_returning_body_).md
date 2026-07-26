---
title: 'withGroup(resultType:returning:body:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/task/withgroup(resulttype:returning:body:)'
source_url: 'https://developer.apple.com/documentation/swift/task/withgroup(resulttype:returning:body:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/withgroup%28resulttype%3Areturning%3Abody%3A%29.json'
content_hash: 'sha256:666688a9986e6d58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# withGroup(resultType:returning:body:)

<sub>Type Method</sub>

> [!warning] Deprecated
> `Task.withGroup` was replaced by `withThrowingTaskGroup` and `withTaskGroup` and will be removed shortly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func withGroup<TaskResult, BodyResult>(resultType: TaskResult.Type, returning returnType: BodyResult.Type = BodyResult.self, body: (inout Task<Success, Failure>.Group<TaskResult>) async throws -> BodyResult) async rethrows -> BodyResult where TaskResult : Sendable
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
- [runDetached(priority:operation:)](<rundetached(priority_operation_)-8s8lh.md>) — Deprecated, available only for source compatibility reasons. _(deprecated)_
- [withCancellationHandler(handler:operation:)](<withcancellationhandler(handler_operation_).md>) _(deprecated)_
- [withTaskCancellationHandler(handler:operation:)](<../withtaskcancellationhandler(handler_operation_).md>) _(deprecated)_
