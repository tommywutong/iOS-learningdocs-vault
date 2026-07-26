---
title: CheckedContinuation
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/checkedcontinuation
source_url: 'https://developer.apple.com/documentation/swift/checkedcontinuation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/checkedcontinuation.json'
content_hash: 'sha256:abb55878a22a713d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# CheckedContinuation

<sub>Structure</sub>

A mechanism to interface between synchronous and asynchronous code, logging correctness violations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CheckedContinuation<T, E> where E : Error
```

## Overview

A _continuation_ is an opaque representation of program state. To create a continuation in asynchronous code, call the `withCheckedContinuation(isolation:function:_:)` or `withCheckedThrowingContinuation(isolation:function:_:)` function. To resume the asynchronous task, call the `resume(returning:)`, `resume(throwing:)`, `resume(with:)`, or `resume()` method.

> [!important] Important
> You must call a resume method exactly once on every execution path throughout the program.

Resuming from a continuation more than once is undefined behavior. Never resuming leaves the task in a suspended state indefinitely, and leaks any associated resources. `CheckedContinuation` logs a message if either of these invariants is violated.

`CheckedContinuation` performs runtime checks for missing or multiple resume operations. `UnsafeContinuation` avoids enforcing these invariants at runtime because it aims to be a low-overhead mechanism for interfacing Swift tasks with event loops, delegate methods, callbacks, and other non-`async` scheduling mechanisms. However, during development, the ability to verify that the invariants are being upheld in testing is important. Because both types have the same interface, you can replace one with the other in most circumstances, without making other changes.

## Relationships

- **Conforms To**: [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init(_:function:)](<checkedcontinuation/init(__function_).md>) — Convert a non-copyable continuation to a [CheckedContinuation](checkedcontinuation.md) _(beta)_
- [init(continuation:function:)](<checkedcontinuation/init(continuation_function_).md>) — Creates a checked continuation from an unsafe continuation.

### Instance Methods

- [resume()](<checkedcontinuation/resume().md>) — Resume the task awaiting the continuation by having it return normally from its suspension point.
- [resume(returning:)](<checkedcontinuation/resume(returning_).md>) — Resume the task awaiting the continuation by having it return normally from its suspension point.
- [resume(throwing:)](<checkedcontinuation/resume(throwing_).md>) — Resume the task awaiting the continuation by having it throw an error from its suspension point.
- [resume(with:)](<checkedcontinuation/resume(with_)-3gh60.md>) — Resume the task awaiting the continuation by having it either return normally or throw an error based on the state of the given `Result` value.
- [resume(with:)](<checkedcontinuation/resume(with_)-5n1a5.md>) — Resume the task awaiting the continuation by having it either return normally or throw an error based on the state of the given `Result` value.

## See Also

### Continuations

- [Continuation](continuation.md) — A mechanism to interface between synchronous and asynchronous code, which enforces that the continuation is resumed exactly once. _(beta)_
- [withContinuation(of:_:)](<withcontinuation(of___).md>) — Invokes the passed in closure with a non-copyable continuation for the current task. _(beta)_
- [withContinuation(of:throwing:_:)](<withcontinuation(of_throwing___).md>) — Invokes the passed in closure with a non-copyable continuation for the current task. _(beta)_
- [withCheckedContinuation(function:_:)](<withcheckedcontinuation(function___).md>) — Invokes the passed in closure with a checked continuation for the current task.
- [withCheckedThrowingContinuation(function:_:)](<withcheckedthrowingcontinuation(function___)-13yf6.md>)
- [withCheckedThrowingContinuation(function:_:)](<withcheckedthrowingcontinuation(function___)-2k46m.md>) — Invokes the passed in closure with a checked continuation for the current task.
- [UnsafeContinuation](unsafecontinuation.md) — A mechanism to interface between synchronous and asynchronous code, without correctness checking.
- [withUnsafeContinuation(_:)](<withunsafecontinuation(__).md>) — Invokes the passed in closure with a unsafe continuation for the current task.
