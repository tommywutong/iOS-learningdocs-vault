---
title: Continuation
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/continuation
source_url: 'https://developer.apple.com/documentation/swift/continuation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/continuation.json'
content_hash: 'sha256:0eab59c92b244d92'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Continuation

<sub>Structure</sub>

A mechanism to interface between synchronous and asynchronous code, which enforces that the continuation is resumed exactly once.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Continuation<Success, Failure> where Failure : Error, Success : ~Copyable
```

## Overview

Unlike `CheckedContinuation`, which detects misuse at runtime, `Continuation` uses non-copyable semantics to enforce correct usage.

The continuation must only ever be resumed **exactly-once**. The compiler will prevent attempts from resuming the continuation more than once.

If a `Continuation` is destroyed without being resumed, the program traps with a diagnostic message indicating where the continuation was created. Because it is noncopyable, the compiler prevents accidental copies, and the `consuming` resume methods ensure the continuation can only be used once.

To create a continuation call [withContinuation(of:throwing:_:)](<withcontinuation(of_throwing___).md>).

To resume the task, suspended on a continuation, call `resume(returning:)`, [resume(throwing:)](<continuation/resume(throwing_).md>), [resume(with:)](<continuation/resume(with_).md>), or [resume()](<continuation/resume().md>).

> [!info] See Also
> [CheckedContinuation](checkedcontinuation.md)

## Relationships

- **Conforms To**: [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Instance Methods

- [resume()](<continuation/resume().md>) — Resume the task awaiting the continuation by having it return from its suspension point _(beta)_
- [resume(returning:)](<continuation/resume(returning_)-5fa8w.md>) — Resume the task awaiting the continuation by having it return from its suspension point _(beta)_
- [resume(returning:)](<continuation/resume(returning_)-8uw9b.md>) — Resume the task awaiting the continuation by having it return from its suspension point _(beta)_
- [resume(throwing:)](<continuation/resume(throwing_).md>) — Resume the task awaiting the continuation by having it throw an error from its suspension point _(beta)_
- [resume(with:)](<continuation/resume(with_).md>) — Resume the task awaiting the continuation by having it either return or throw an error based on the state of the given `Result` value _(beta)_

## See Also

### Continuations

- [withContinuation(of:_:)](<withcontinuation(of___).md>) — Invokes the passed in closure with a non-copyable continuation for the current task. _(beta)_
- [withContinuation(of:throwing:_:)](<withcontinuation(of_throwing___).md>) — Invokes the passed in closure with a non-copyable continuation for the current task. _(beta)_
- [CheckedContinuation](checkedcontinuation.md) — A mechanism to interface between synchronous and asynchronous code, logging correctness violations.
- [withCheckedContinuation(function:_:)](<withcheckedcontinuation(function___).md>) — Invokes the passed in closure with a checked continuation for the current task.
- [withCheckedThrowingContinuation(function:_:)](<withcheckedthrowingcontinuation(function___)-13yf6.md>)
- [withCheckedThrowingContinuation(function:_:)](<withcheckedthrowingcontinuation(function___)-2k46m.md>) — Invokes the passed in closure with a checked continuation for the current task.
- [UnsafeContinuation](unsafecontinuation.md) — A mechanism to interface between synchronous and asynchronous code, without correctness checking.
- [withUnsafeContinuation(_:)](<withunsafecontinuation(__).md>) — Invokes the passed in closure with a unsafe continuation for the current task.
