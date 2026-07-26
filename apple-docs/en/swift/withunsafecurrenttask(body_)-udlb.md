---
title: 'withUnsafeCurrentTask(body:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/withunsafecurrenttask(body:)-udlb'
source_url: 'https://developer.apple.com/documentation/swift/withunsafecurrenttask(body:)-udlb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withunsafecurrenttask%28body%3A%29-udlb.json'
content_hash: 'sha256:78cf8adc1dc6b593'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withUnsafeCurrentTask(body:)

<sub>Function</sub>

Calls a closure with an unsafe reference to the current task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@abi(nonisolated(nonsending) func withUnsafeCurrentTaskNonsending<T>(body: nonisolated(nonsending) (UnsafeCurrentTask?) async throws -> T) async rethrows -> T) nonisolated(nonsending) func withUnsafeCurrentTask<T>(body: nonisolated(nonsending) (UnsafeCurrentTask?) async throws -> T) async rethrows -> T
```

## Parameters

- `body` — A closure that takes an `UnsafeCurrentTask` parameter. If `body` has a return value, that value is also used as the return value for the `withUnsafeCurrentTask(body:)` function.

## Return Value

The return value, if any, of the `body` closure.

## Discussion

If you call this function from the body of an asynchronous function, the unsafe task handle passed to the closure is always non-`nil` because an asynchronous function always runs in the context of a task.

The operation is guaranteed to execute on the caller’s isolation.

Storing an unsafe reference to a task doesn’t affect the task’s actual life cycle, and the behavior of accessing an unsafe task reference outside of the `withUnsafeCurrentTask(body:)` method’s closure is unsafe and undefined behavior. There’s no safe way to retrieve a reference to the current task and save it for long-term use. To query the current task without saving a reference to it, use properties like `currentPriority`. If you need to store a reference to a task, create an unstructured task using `Task.detached(priority:operation:)` instead.

## See Also

### Getting an Unsafe Reference to the Current Task

- [withUnsafeCurrentTask(body:)](<withunsafecurrenttask(body_)-6gvhl.md>) — Calls a closure with an unsafe reference to the current task.
