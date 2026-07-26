---
title: Actor
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/actor
source_url: 'https://developer.apple.com/documentation/swift/actor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/actor.json'
content_hash: 'sha256:5ea868d1dd9e8274'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Actor

<sub>Protocol</sub>

Common protocol to which all actors conform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Actor : AnyObject, Sendable
```

## Overview

The `Actor` protocol generalizes over all `actor` types. Actor types implicitly conform to this protocol.

### Actors and SerialExecutors

By default, actors execute tasks on a shared global concurrency thread pool. This pool is shared by all default actors and tasks, unless an actor or task specified a more specific executor requirement.

It is possible to configure an actor to use a specific [SerialExecutor](serialexecutor.md), as well as impact the scheduling of default tasks and actors by using a [TaskExecutor](taskexecutor.md).

> [!info] See Also
> [SerialExecutor](serialexecutor.md)

> [!info] See Also
> [TaskExecutor](taskexecutor.md)

## Relationships

- **Inherits From**: [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

- **Conforming Types**: [MainActor](mainactor.md)

## Topics

### Instance Properties

- [unownedExecutor](actor/unownedexecutor.md) — Retrieve the executor for this actor as an optimized, unowned reference.

### Instance Methods

- [assertIsolated(_:file:line:)](<actor/assertisolated(__file_line_).md>) — Stops program execution if the current task is not executing on this actor’s serial executor.
- [assumeIsolated(_:file:line:)](<actor/assumeisolated(__file_line_).md>) — Assume that the current task is executing on this actor’s serial executor, or stop program execution otherwise.
- [preconditionIsolated(_:file:line:)](<actor/preconditionisolated(__file_line_).md>) — Stops program execution if the current task is not executing on this actor’s serial executor.
- [withSerialExecutor(_:)](<actor/withserialexecutor(__)-4ff11.md>) — Perform an operation with the actor’s [SerialExecutor](serialexecutor.md).
- [withSerialExecutor(_:)](<actor/withserialexecutor(__)-4ucv5.md>) — Perform an operation with the actor’s [SerialExecutor](serialexecutor.md).

## See Also

### Actors

- [Sendable](sendable.md) — A thread-safe type whose values can be shared across arbitrary concurrent contexts without introducing a risk of data races.
- [MainActor](mainactor.md) — A singleton actor whose executor is equivalent to the main dispatch queue.
- [GlobalActor](globalactor.md) — A type that represents a globally-unique actor that can be used to isolate various declarations anywhere in the program.
- [SendableMetatype](sendablemetatype.md) — A type whose metatype can be shared across arbitrary isolation domains without introducing a risk of data races.
- [isolation()](<isolation().md>) — Produce a reference to the actor to which the enclosing code is isolated, or `nil` if the code is nonisolated.
