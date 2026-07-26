---
title: 'async(priority:operation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/throwingtaskgroup/async(priority:operation:)'
source_url: 'https://developer.apple.com/documentation/swift/throwingtaskgroup/async(priority:operation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingtaskgroup/async%28priority%3Aoperation%3A%29.json'
content_hash: 'sha256:4b36248994a7debc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ThrowingTaskGroup](../throwingtaskgroup.md)

# async(priority:operation:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func async(priority: TaskPriority? = nil, operation: @escaping @Sendable () async throws -> ChildTaskResult)
```

## See Also

### Deprecated

- [add(priority:operation:)](<add(priority_operation_).md>) _(deprecated)_
- [asyncUnlessCancelled(priority:operation:)](<asyncunlesscancelled(priority_operation_).md>) _(deprecated)_
- [nextResult(isolation:)](<nextresult(isolation_).md>) _(deprecated)_
- [spawn(priority:operation:)](<spawn(priority_operation_).md>) _(deprecated)_
- [spawnUnlessCancelled(priority:operation:)](<spawnunlesscancelled(priority_operation_).md>) _(deprecated)_
- [waitForAll(isolation:)](<waitforall(isolation_).md>) _(deprecated)_
