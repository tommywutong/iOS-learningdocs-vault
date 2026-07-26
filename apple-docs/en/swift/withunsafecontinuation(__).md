---
title: 'withUnsafeContinuation(_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/withunsafecontinuation(_:)'
source_url: 'https://developer.apple.com/documentation/swift/withunsafecontinuation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withunsafecontinuation%28_%3A%29.json'
content_hash: 'sha256:3ef67d6b700d13c7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withUnsafeContinuation(_:)

<sub>Function</sub>

Invokes the passed in closure with a unsafe continuation for the current task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated(nonsending) func withUnsafeContinuation<T>(_ fn: (UnsafeContinuation<T, Never>) -> Void) async -> sending T
```

## Parameters

- `fn` — A closure that takes an `UnsafeContinuation` parameter.

## Return Value

The value continuation is resumed with.

## Discussion

The body of the closure executes synchronously on the calling task, and once it returns the calling task is suspended. It is possible to immediately resume the task, or escape the continuation in order to complete it afterwards, which will then resume the suspended task.

You must invoke the continuation’s `resume` method exactly once.

Missing to invoke it (eventually) will cause the calling task to remain suspended indefinitely which will result in the task “hanging” as well as being leaked with no possibility to destroy it.

Unlike the “checked” continuation variant, the `UnsafeContinuation` does not detect or diagnose any kind of misuse, so you need to be extra careful to avoid calling `resume` twice or forgetting to call resume before letting go of the continuation object.

> [!info] See Also
> `withUnsafeThrowingContinuation(function:_:)`

> [!info] See Also
> `withCheckedContinuation(function:_:)`

> [!info] See Also
> `withCheckedThrowingContinuation(function:_:)`

## See Also

### Continuations

- [Continuation](continuation.md) — A mechanism to interface between synchronous and asynchronous code, which enforces that the continuation is resumed exactly once. _(beta)_
- [withContinuation(of:_:)](<withcontinuation(of___).md>) — Invokes the passed in closure with a non-copyable continuation for the current task. _(beta)_
- [withContinuation(of:throwing:_:)](<withcontinuation(of_throwing___).md>) — Invokes the passed in closure with a non-copyable continuation for the current task. _(beta)_
- [CheckedContinuation](checkedcontinuation.md) — A mechanism to interface between synchronous and asynchronous code, logging correctness violations.
- [withCheckedContinuation(function:_:)](<withcheckedcontinuation(function___).md>) — Invokes the passed in closure with a checked continuation for the current task.
- [withCheckedThrowingContinuation(function:_:)](<withcheckedthrowingcontinuation(function___)-13yf6.md>)
- [withCheckedThrowingContinuation(function:_:)](<withcheckedthrowingcontinuation(function___)-2k46m.md>) — Invokes the passed in closure with a checked continuation for the current task.
- [UnsafeContinuation](unsafecontinuation.md) — A mechanism to interface between synchronous and asynchronous code, without correctness checking.
