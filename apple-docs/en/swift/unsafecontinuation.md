---
title: UnsafeContinuation
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafecontinuation
source_url: 'https://developer.apple.com/documentation/swift/unsafecontinuation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafecontinuation.json'
content_hash: 'sha256:9244c1bc4898c972'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UnsafeContinuation

<sub>Structure</sub>

A mechanism to interface between synchronous and asynchronous code, without correctness checking.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct UnsafeContinuation<T, E> where E : Error
```

## Overview

A _continuation_ is an opaque representation of program state. To create a continuation in asynchronous code, call the `withUnsafeContinuation(_:)` or `withUnsafeThrowingContinuation(_:)` function. To resume the asynchronous task, call the `resume(returning:)`, `resume(throwing:)`, `resume(with:)`, or `resume()` method.

> [!important] Important
> You must call a resume method exactly once on every execution path throughout the program. Resuming from a continuation more than once is undefined behavior. Never resuming leaves the task in a suspended state indefinitely, and leaks any associated resources.

`CheckedContinuation` performs runtime checks for missing or multiple resume operations. `UnsafeContinuation` avoids enforcing these invariants at runtime because it aims to be a low-overhead mechanism for interfacing Swift tasks with event loops, delegate methods, callbacks, and other non-`async` scheduling mechanisms. However, during development, the ability to verify that the invariants are being upheld in testing is important. Because both types have the same interface, you can replace one with the other in most circumstances, without making other changes.

## Relationships

- **Conforms To**: [BitwiseCopyable](bitwisecopyable.md), [Copyable](copyable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<unsafecontinuation/init(__).md>) — Convert a non-copyable continuation to an [UnsafeContinuation](unsafecontinuation.md). _(beta)_

### Instance Methods

- [resume()](<unsafecontinuation/resume().md>) — Resume the task that’s awaiting the continuation by returning.
- [resume(returning:)](<unsafecontinuation/resume(returning_)-41kka.md>) — Resume the task that’s awaiting the continuation by returning the given value.
- [resume(returning:)](<unsafecontinuation/resume(returning_)-8rtni.md>) — Resume the task that’s awaiting the continuation by returning the given value.
- [resume(throwing:)](<unsafecontinuation/resume(throwing_).md>) — Resume the task that’s awaiting the continuation by throwing the given error.
- [resume(with:)](<unsafecontinuation/resume(with_)-4t59h.md>) — Resume the task that’s awaiting the continuation by returning or throwing the given result value.
- [resume(with:)](<unsafecontinuation/resume(with_)-7t959.md>) — Resume the task that’s awaiting the continuation by returning or throwing the given result value.

## See Also

### Continuations

- [Continuation](continuation.md) — A mechanism to interface between synchronous and asynchronous code, which enforces that the continuation is resumed exactly once. _(beta)_
- [withContinuation(of:_:)](<withcontinuation(of___).md>) — Invokes the passed in closure with a non-copyable continuation for the current task. _(beta)_
- [withContinuation(of:throwing:_:)](<withcontinuation(of_throwing___).md>) — Invokes the passed in closure with a non-copyable continuation for the current task. _(beta)_
- [CheckedContinuation](checkedcontinuation.md) — A mechanism to interface between synchronous and asynchronous code, logging correctness violations.
- [withCheckedContinuation(function:_:)](<withcheckedcontinuation(function___).md>) — Invokes the passed in closure with a checked continuation for the current task.
- [withCheckedThrowingContinuation(function:_:)](<withcheckedthrowingcontinuation(function___)-13yf6.md>)
- [withCheckedThrowingContinuation(function:_:)](<withcheckedthrowingcontinuation(function___)-2k46m.md>) — Invokes the passed in closure with a checked continuation for the current task.
- [withUnsafeContinuation(_:)](<withunsafecontinuation(__).md>) — Invokes the passed in closure with a unsafe continuation for the current task.
