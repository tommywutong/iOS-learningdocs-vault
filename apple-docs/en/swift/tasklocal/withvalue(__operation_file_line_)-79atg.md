---
title: 'withValue(_:operation:file:line:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/tasklocal/withvalue(_:operation:file:line:)-79atg'
source_url: 'https://developer.apple.com/documentation/swift/tasklocal/withvalue(_:operation:file:line:)-79atg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/tasklocal/withvalue%28_%3Aoperation%3Afile%3Aline%3A%29-79atg.json'
content_hash: 'sha256:7b0d8d3bdce43f27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TaskLocal](../tasklocal.md)

# withValue(_:operation:file:line:)

<sub>Instance Method</sub>

Binds the task-local to the specific value for the duration of the synchronous operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult final func withValue<R>(_ valueDuringOperation: Value, operation: () throws -> R, file: String = #fileID, line: UInt = #line) rethrows -> R
```

## Discussion

The value is available throughout the execution of the operation closure, including any `get` operations performed by child-tasks created during the execution of the operation closure.

If the same task-local is bound multiple times, be it in the same task, or in specific child tasks, the “more specific” binding is returned when the value is read.

If the value is a reference type, it will be retained for the duration of the operation closure.

If this method is called form a context where no current Swift concurrency task is available, a fallback thread-local is used to manage the task locals and all existing semantics of task-locals are upheld as-if a task was actually available.
