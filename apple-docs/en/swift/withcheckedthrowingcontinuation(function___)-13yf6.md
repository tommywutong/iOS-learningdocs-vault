---
title: 'withCheckedThrowingContinuation(function:_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/withcheckedthrowingcontinuation(function:_:)-13yf6'
source_url: 'https://developer.apple.com/documentation/swift/withcheckedthrowingcontinuation(function:_:)-13yf6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withcheckedthrowingcontinuation%28function%3A_%3A%29-13yf6.json'
content_hash: 'sha256:791d50d7d18e15ac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withCheckedThrowingContinuation(function:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@abi(nonisolated(nonsending) func withCheckedThrowingContinuationNonisolatedNonsending<T>(function: String, _ body: (CheckedContinuation<T, any Error>) -> Void) async throws -> sending T) nonisolated(nonsending) func withCheckedThrowingContinuation<T>(function: String = #function, _ body: (CheckedContinuation<T, any Error>) -> Void) async throws -> sending T
```

## See Also

### Continuations

- [Continuation](continuation.md) — A mechanism to interface between synchronous and asynchronous code, which enforces that the continuation is resumed exactly once. _(beta)_
- [withContinuation(of:_:)](<withcontinuation(of___).md>) — Invokes the passed in closure with a non-copyable continuation for the current task. _(beta)_
- [withContinuation(of:throwing:_:)](<withcontinuation(of_throwing___).md>) — Invokes the passed in closure with a non-copyable continuation for the current task. _(beta)_
- [CheckedContinuation](checkedcontinuation.md) — A mechanism to interface between synchronous and asynchronous code, logging correctness violations.
- [withCheckedContinuation(function:_:)](<withcheckedcontinuation(function___).md>) — Invokes the passed in closure with a checked continuation for the current task.
- [withCheckedThrowingContinuation(function:_:)](<withcheckedthrowingcontinuation(function___)-2k46m.md>) — Invokes the passed in closure with a checked continuation for the current task.
- [UnsafeContinuation](unsafecontinuation.md) — A mechanism to interface between synchronous and asynchronous code, without correctness checking.
- [withUnsafeContinuation(_:)](<withunsafecontinuation(__).md>) — Invokes the passed in closure with a unsafe continuation for the current task.
