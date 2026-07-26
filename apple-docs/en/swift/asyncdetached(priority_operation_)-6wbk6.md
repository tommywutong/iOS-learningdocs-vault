---
title: 'asyncDetached(priority:operation:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/asyncdetached(priority:operation:)-6wbk6'
source_url: 'https://developer.apple.com/documentation/swift/asyncdetached(priority:operation:)-6wbk6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncdetached%28priority%3Aoperation%3A%29-6wbk6.json'
content_hash: 'sha256:10e88b8e03c3eed3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# asyncDetached(priority:operation:)

<sub>Function</sub>

Deprecated, available only for source compatibility reasons.

> [!warning] Deprecated
> `asyncDetached` was replaced by `Task.detached` and will be removed shortly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func asyncDetached<Success>(priority: TaskPriority? = nil, operation: @escaping @isolated(any) @Sendable () async -> Success) -> Task<Success, Never> where Success : Sendable
```

## See Also

### Deprecated Functions

- [async(priority:operation:)](<async(priority_operation_)-2y0dc.md>) — Deprecated, available only for source compatibility reasons. _(deprecated)_
- [async(priority:operation:)](<async(priority_operation_)-684z0.md>) — Deprecated, available only for source compatibility reasons. _(deprecated)_
- [asyncDetached(priority:operation:)](<asyncdetached(priority_operation_)-79mp7.md>) — Deprecated, available only for source compatibility reasons. _(deprecated)_
- [asyncDetached(priority:operation:)](<asyncdetached(priority_operation_)-79mp7.md>) — Deprecated, available only for source compatibility reasons. _(deprecated)_
- [detach(priority:operation:)](<detach(priority_operation_)-2h9ty.md>) — Deprecated, available only for source compatibility reasons. _(deprecated)_
- [detach(priority:operation:)](<detach(priority_operation_)-4948v.md>) — Deprecated, available only for source compatibility reasons. _(deprecated)_
