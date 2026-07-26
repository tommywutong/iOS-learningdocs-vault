---
title: get()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/tasklocal/get()
source_url: 'https://developer.apple.com/documentation/swift/tasklocal/get()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/tasklocal/get%28%29.json'
content_hash: 'sha256:c75566a77291fc00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TaskLocal](../tasklocal.md)

# get()

<sub>Instance Method</sub>

Gets the value currently bound to this task-local from the current task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@abi(final func get_aeic() -> Value) final func get() -> Value
```

## Discussion

If no current value binding is available in the context where this call is made, or if the task-local has no value bound, this will return the `defaultValue` of the task local.

A task local value may still be bound and read even without a Swift concurrency task present, as the underlying storage will fallback to using a managed thread-local value when no task is available. From the perspective of task local APIs, the presented semantics remain exactly the same as when a task is present.
