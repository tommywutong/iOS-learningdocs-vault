---
title: 'nextResult(isolation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/throwingtaskgroup/nextresult(isolation:)'
source_url: 'https://developer.apple.com/documentation/swift/throwingtaskgroup/nextresult(isolation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/throwingtaskgroup/nextresult%28isolation%3A%29.json'
content_hash: 'sha256:0f32f9502ef4ee90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ThrowingTaskGroup](../throwingtaskgroup.md)

# nextResult(isolation:)

<sub>Instance Method</sub>

> [!warning] Deprecated
> Replaced by nonisolated(nonsending) overload

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func nextResult(isolation: isolated (any Actor)? = #isolation) async -> Result<ChildTaskResult, Failure>?
```

## See Also

### Deprecated

- [add(priority:operation:)](<add(priority_operation_).md>) _(deprecated)_
- [async(priority:operation:)](<async(priority_operation_).md>) _(deprecated)_
- [asyncUnlessCancelled(priority:operation:)](<asyncunlesscancelled(priority_operation_).md>) _(deprecated)_
- [spawn(priority:operation:)](<spawn(priority_operation_).md>) _(deprecated)_
- [spawnUnlessCancelled(priority:operation:)](<spawnunlesscancelled(priority_operation_).md>) _(deprecated)_
- [waitForAll(isolation:)](<waitforall(isolation_).md>) _(deprecated)_
