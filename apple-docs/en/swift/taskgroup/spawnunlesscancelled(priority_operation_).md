---
title: 'spawnUnlessCancelled(priority:operation:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/taskgroup/spawnunlesscancelled(priority:operation:)'
source_url: 'https://developer.apple.com/documentation/swift/taskgroup/spawnunlesscancelled(priority:operation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/taskgroup/spawnunlesscancelled%28priority%3Aoperation%3A%29.json'
content_hash: 'sha256:7036a57667822b89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TaskGroup](../taskgroup.md)

# spawnUnlessCancelled(priority:operation:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func spawnUnlessCancelled(priority: TaskPriority? = nil, operation: @escaping @Sendable () async -> ChildTaskResult) -> Bool
```

## See Also

### Deprecated

- [add(priority:operation:)](<add(priority_operation_).md>) _(deprecated)_
- [async(priority:operation:)](<async(priority_operation_).md>) _(deprecated)_
- [asyncUnlessCancelled(priority:operation:)](<asyncunlesscancelled(priority_operation_).md>) _(deprecated)_
- [spawn(priority:operation:)](<spawn(priority_operation_).md>) _(deprecated)_
- [waitForAll(isolation:)](<waitforall(isolation_).md>) — Wait for all of the group’s remaining tasks to complete. _(deprecated)_
