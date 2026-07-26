---
title: 'withTaskCancellationHandler(handler:operation:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/withtaskcancellationhandler(handler:operation:)'
source_url: 'https://developer.apple.com/documentation/swift/withtaskcancellationhandler(handler:operation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withtaskcancellationhandler%28handler%3Aoperation%3A%29.json'
content_hash: 'sha256:25fb696cd11abf6c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withTaskCancellationHandler(handler:operation:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withTaskCancellationHandler<T>(handler: @Sendable () -> Void, operation: () async throws -> T) async rethrows -> T
```

## See Also

### Deprecated

- [Group](task/group.md) _(deprecated)_
- [Handle](task/handle.md) _(deprecated)_
- [Priority](task/priority.md) _(deprecated)_
- [CancellationError()](<task/cancellationerror().md>) _(deprecated)_
- [getResult()](<task/getresult().md>) _(deprecated)_
- [get()](<task/get()-4i2gt.md>) _(deprecated)_
- [get()](<task/get()-4ohks.md>) _(deprecated)_
- [sleep(_:)](<task/sleep(__).md>) _(deprecated)_
- [suspend()](<task/suspend().md>) _(deprecated)_
- [runDetached(priority:operation:)](<task/rundetached(priority_operation_)-88zf5.md>) — Deprecated, available only for source compatibility reasons. _(deprecated)_
- [runDetached(priority:operation:)](<task/rundetached(priority_operation_)-8s8lh.md>) — Deprecated, available only for source compatibility reasons. _(deprecated)_
- [withCancellationHandler(handler:operation:)](<task/withcancellationhandler(handler_operation_).md>) _(deprecated)_
- [withGroup(resultType:returning:body:)](<task/withgroup(resulttype_returning_body_).md>) _(deprecated)_
