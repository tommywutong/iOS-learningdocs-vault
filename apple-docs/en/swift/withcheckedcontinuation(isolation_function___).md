---
title: 'withCheckedContinuation(isolation:function:_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/withcheckedcontinuation(isolation:function:_:)'
source_url: 'https://developer.apple.com/documentation/swift/withcheckedcontinuation(isolation:function:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withcheckedcontinuation%28isolation%3Afunction%3A_%3A%29.json'
content_hash: 'sha256:60698deeaf2edbde'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withCheckedContinuation(isolation:function:_:)

<sub>Function</sub>

Source-compatibility overload; replaced by [withCheckedContinuation(function:_:)](<withcheckedcontinuation(function___).md>).

> [!warning] Deprecated
> Replaced by nonisolated(nonsending) overload

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: macOS 15.0, iOS 18.0, watchOS 11.0, tvOS 18.0, visionOS 2.0)
func withCheckedContinuation<T>(isolation: isolated (any Actor)?, function: String = #function, _ body: (CheckedContinuation<T, Never>) -> Void) async -> sending T
```

## See Also

### Deprecated

- [extractIsolation(_:)](<extractisolation(__).md>) _(deprecated)_
- [withCheckedThrowingContinuation(isolation:function:_:)](<withcheckedthrowingcontinuation(isolation_function___).md>) — Source-compatibility overload; replaced by `withCheckedThrowingContinuation(function:_:)`. _(deprecated)_
- [withUnsafeContinuation(isolation:_:)](<withunsafecontinuation(isolation___).md>) — Source-compatibility overload; replaced by [withUnsafeContinuation(_:)](<withunsafecontinuation(__).md>). _(deprecated)_
- [AnyActor](anyactor.md) — Common marker protocol providing a shared “base” for both (local) `Actor` and (potentially remote) `DistributedActor` types. _(deprecated)_
- [ConcurrentValue](concurrentvalue.md) _(deprecated)_
- [Job](job.md) — Deprecated equivalent of [ExecutorJob](executorjob.md). _(deprecated)_
- [PartialAsyncTask](partialasynctask.md) _(deprecated)_
- [UnsafeConcurrentValue](unsafeconcurrentvalue.md) _(deprecated)_
- [UnsafeSendable](unsafesendable.md) — A type whose values can safely be passed across concurrency domains by copying, but which disables some safety checking at the conformance site. _(deprecated)_
- [UnsafeThrowingContinuation](unsafethrowingcontinuation.md) _(deprecated)_
- [withUnsafeThrowingContinuation(_:)](<withunsafethrowingcontinuation(__)-32nwt.md>) — Invokes the passed in closure with a unsafe continuation for the current task.
- [withUnsafeThrowingContinuation(_:)](<withunsafethrowingcontinuation(__)-7zhvy.md>)
- [withUnsafeThrowingContinuation(isolation:_:)](<withunsafethrowingcontinuation(isolation___).md>) — Source-compatibility overload; replaced by `withUnsafeThrowingContinuation(_:)`. _(deprecated)_
