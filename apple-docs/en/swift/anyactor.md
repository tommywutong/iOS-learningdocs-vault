---
title: AnyActor
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swift/anyactor
source_url: 'https://developer.apple.com/documentation/swift/anyactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyactor.json'
content_hash: 'sha256:51ca0b2953110a87'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AnyActor

<sub>Type Alias</sub>

Common marker protocol providing a shared “base” for both (local) `Actor` and (potentially remote) `DistributedActor` types.

> [!warning] Deprecated
> Use 'any Actor' with 'DistributedActor.asLocalActor' instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias AnyActor = AnyObject & Sendable
```

## Discussion

The `AnyActor` marker protocol generalizes over all actor types, including distributed ones. In practice, this protocol can be used to restrict protocols, or generic parameters to only be usable with actors, which provides the guarantee that calls may be safely made on instances of given type without worrying about the thread-safety of it – as they are guaranteed to follow the actor-style isolation semantics.

While both local and distributed actors are conceptually “actors”, there are some important isolation model differences between the two, which make it impossible for one to refine the other.

## See Also

### Deprecated

- [extractIsolation(_:)](<extractisolation(__).md>) _(deprecated)_
- [withCheckedContinuation(isolation:function:_:)](<withcheckedcontinuation(isolation_function___).md>) — Source-compatibility overload; replaced by [withCheckedContinuation(function:_:)](<withcheckedcontinuation(function___).md>). _(deprecated)_
- [withCheckedThrowingContinuation(isolation:function:_:)](<withcheckedthrowingcontinuation(isolation_function___).md>) — Source-compatibility overload; replaced by `withCheckedThrowingContinuation(function:_:)`. _(deprecated)_
- [withUnsafeContinuation(isolation:_:)](<withunsafecontinuation(isolation___).md>) — Source-compatibility overload; replaced by [withUnsafeContinuation(_:)](<withunsafecontinuation(__).md>). _(deprecated)_
- [ConcurrentValue](concurrentvalue.md) _(deprecated)_
- [Job](job.md) — Deprecated equivalent of [ExecutorJob](executorjob.md). _(deprecated)_
- [PartialAsyncTask](partialasynctask.md) _(deprecated)_
- [UnsafeConcurrentValue](unsafeconcurrentvalue.md) _(deprecated)_
- [UnsafeSendable](unsafesendable.md) — A type whose values can safely be passed across concurrency domains by copying, but which disables some safety checking at the conformance site. _(deprecated)_
- [UnsafeThrowingContinuation](unsafethrowingcontinuation.md) _(deprecated)_
- [withUnsafeThrowingContinuation(_:)](<withunsafethrowingcontinuation(__)-32nwt.md>) — Invokes the passed in closure with a unsafe continuation for the current task.
- [withUnsafeThrowingContinuation(_:)](<withunsafethrowingcontinuation(__)-7zhvy.md>)
- [withUnsafeThrowingContinuation(isolation:_:)](<withunsafethrowingcontinuation(isolation___).md>) — Source-compatibility overload; replaced by `withUnsafeThrowingContinuation(_:)`. _(deprecated)_
