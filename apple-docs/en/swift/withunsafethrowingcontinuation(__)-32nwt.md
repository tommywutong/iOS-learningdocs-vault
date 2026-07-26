---
title: 'withUnsafeThrowingContinuation(_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/withunsafethrowingcontinuation(_:)-32nwt'
source_url: 'https://developer.apple.com/documentation/swift/withunsafethrowingcontinuation(_:)-32nwt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withunsafethrowingcontinuation%28_%3A%29-32nwt.json'
content_hash: 'sha256:eee564cbb92cb2c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withUnsafeThrowingContinuation(_:)

<sub>Function</sub>

Invokes the passed in closure with a unsafe continuation for the current task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated(nonsending) func withUnsafeThrowingContinuation<T, E>(_ fn: (UnsafeContinuation<T, E>) -> Void) async throws(E) -> sending T where E : Error
```

## Parameters

- `fn` — A closure that takes an `UnsafeContinuation` parameter.

## Return Value

The value continuation is resumed with.

## Discussion

The body of the closure executes synchronously on the calling task, and once it returns the calling task is suspended. It is possible to immediately resume the task, or escape the continuation in order to complete it afterwards, which will then resume the suspended task.

If `resume(throwing:)` is called on the continuation, this function throws that error.

You must invoke the continuation’s `resume` method exactly once.

Missing to invoke it (eventually) will cause the calling task to remain suspended indefinitely which will result in the task “hanging” as well as being leaked with no possibility to destroy it.

Unlike the “checked” continuation variant, the `UnsafeContinuation` does not detect or diagnose any kind of misuse, so you need to be extra careful to avoid calling `resume` twice or forgetting to call resume before letting go of the continuation object.

> [!info] See Also
> `withUnsafeContinuation(function:_:)`

> [!info] See Also
> `withCheckedContinuation(function:_:)`

> [!info] See Also
> `withCheckedThrowingContinuation(function:_:)`

## See Also

### Deprecated

- [extractIsolation(_:)](<extractisolation(__).md>) _(deprecated)_
- [withCheckedContinuation(isolation:function:_:)](<withcheckedcontinuation(isolation_function___).md>) — Source-compatibility overload; replaced by [withCheckedContinuation(function:_:)](<withcheckedcontinuation(function___).md>). _(deprecated)_
- [withCheckedThrowingContinuation(isolation:function:_:)](<withcheckedthrowingcontinuation(isolation_function___).md>) — Source-compatibility overload; replaced by `withCheckedThrowingContinuation(function:_:)`. _(deprecated)_
- [withUnsafeContinuation(isolation:_:)](<withunsafecontinuation(isolation___).md>) — Source-compatibility overload; replaced by [withUnsafeContinuation(_:)](<withunsafecontinuation(__).md>). _(deprecated)_
- [AnyActor](anyactor.md) — Common marker protocol providing a shared “base” for both (local) `Actor` and (potentially remote) `DistributedActor` types. _(deprecated)_
- [ConcurrentValue](concurrentvalue.md) _(deprecated)_
- [Job](job.md) — Deprecated equivalent of [ExecutorJob](executorjob.md). _(deprecated)_
- [PartialAsyncTask](partialasynctask.md) _(deprecated)_
- [UnsafeConcurrentValue](unsafeconcurrentvalue.md) _(deprecated)_
- [UnsafeSendable](unsafesendable.md) — A type whose values can safely be passed across concurrency domains by copying, but which disables some safety checking at the conformance site. _(deprecated)_
- [UnsafeThrowingContinuation](unsafethrowingcontinuation.md) _(deprecated)_
- [withUnsafeThrowingContinuation(_:)](<withunsafethrowingcontinuation(__)-7zhvy.md>)
- [withUnsafeThrowingContinuation(isolation:_:)](<withunsafethrowingcontinuation(isolation___).md>) — Source-compatibility overload; replaced by `withUnsafeThrowingContinuation(_:)`. _(deprecated)_
