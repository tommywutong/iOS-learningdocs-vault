---
title: 'withContinuation(of:throwing:_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/withcontinuation(of:throwing:_:)'
source_url: 'https://developer.apple.com/documentation/swift/withcontinuation(of:throwing:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withcontinuation%28of%3Athrowing%3A_%3A%29.json'
content_hash: 'sha256:c9fbfbc615e5d575'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withContinuation(of:throwing:_:)

<sub>Function</sub>

Invokes the passed in closure with a non-copyable continuation for the current task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated(nonsending) func withContinuation<Success, Failure>(of: Success.Type = Success.self, throwing: Failure.Type, _ body: (consuming Continuation<Success, Failure>) -> Void) async throws(Failure) -> sending Success where Failure : Error, Success : ~Copyable
```

## Parameters

- `of` — The `Success` type returned by the continuation

- `throwing` — The `Failure` type that may be thrown

- `body` — A closure that takes a `Continuation` parameter

## Return Value

The value the continuation is resumed with

## Discussion

The body of the closure executes synchronously on the calling task, and once it returns the calling task is suspended. It is possible to immediately resume the task, or escape the continuation in order to complete it afterwards, which will then resume the suspended task.

You must invoke the continuation’s `resume` method exactly once. The continuation is a noncopyable type, and therefore multiple resume calls are prevented at compile time (as resuming the continuation consumes it). However, if the continuation is dropped without being resumed, the program traps.

## See Also

### Continuations

- [Continuation](continuation.md) — A mechanism to interface between synchronous and asynchronous code, which enforces that the continuation is resumed exactly once. _(beta)_
- [withContinuation(of:_:)](<withcontinuation(of___).md>) — Invokes the passed in closure with a non-copyable continuation for the current task. _(beta)_
- [CheckedContinuation](checkedcontinuation.md) — A mechanism to interface between synchronous and asynchronous code, logging correctness violations.
- [withCheckedContinuation(function:_:)](<withcheckedcontinuation(function___).md>) — Invokes the passed in closure with a checked continuation for the current task.
- [withCheckedThrowingContinuation(function:_:)](<withcheckedthrowingcontinuation(function___)-13yf6.md>)
- [withCheckedThrowingContinuation(function:_:)](<withcheckedthrowingcontinuation(function___)-2k46m.md>) — Invokes the passed in closure with a checked continuation for the current task.
- [UnsafeContinuation](unsafecontinuation.md) — A mechanism to interface between synchronous and asynchronous code, without correctness checking.
- [withUnsafeContinuation(_:)](<withunsafecontinuation(__).md>) — Invokes the passed in closure with a unsafe continuation for the current task.
