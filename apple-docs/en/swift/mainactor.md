---
title: MainActor
framework: Swift
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/mainactor
source_url: 'https://developer.apple.com/documentation/swift/mainactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mainactor.json'
content_hash: 'sha256:6db8a2dbc43f6408'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# MainActor

<sub>Class</sub>

A singleton actor whose executor is equivalent to the main dispatch queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@globalActor final actor MainActor
```

## Relationships

- **Conforms To**: [Actor](actor.md), [GlobalActor](globalactor.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Instance Properties

- [unownedExecutor](mainactor/unownedexecutor.md) — Retrieve the executor for this actor as an optimized, unowned reference.

### Instance Methods

- [enqueue(_:)](<mainactor/enqueue(__).md>)

### Type Aliases

- [ActorType](mainactor/actortype.md) — The type of the shared actor instance that will be used to provide mutually-exclusive access to declarations annotated with the given global actor type.

### Type Properties

- [shared](mainactor/shared.md) — The shared actor instance that will be used to provide mutually-exclusive access to declarations annotated with the given global actor type.
- [sharedUnownedExecutor](mainactor/sharedunownedexecutor.md) — Shorthand for referring to the `shared.unownedExecutor` of this global actor.

### Type Methods

- [assumeIsolated(_:file:line:)](<mainactor/assumeisolated(__file_line_).md>) — Assume that the current task is executing on the main actor’s serial executor, or stop program execution.
- [run(resultType:body:)](<mainactor/run(resulttype_body_).md>) — Execute the given body closure on the main actor.

### Default Implementations

- [Actor Implementations](mainactor/actor-implementations.md)
- [GlobalActor Implementations](mainactor/globalactor-implementations.md)

## See Also

### Actors

- [Sendable](sendable.md) — A thread-safe type whose values can be shared across arbitrary concurrent contexts without introducing a risk of data races.
- [Actor](actor.md) — Common protocol to which all actors conform.
- [GlobalActor](globalactor.md) — A type that represents a globally-unique actor that can be used to isolate various declarations anywhere in the program.
- [SendableMetatype](sendablemetatype.md) — A type whose metatype can be shared across arbitrary isolation domains without introducing a risk of data races.
- [isolation()](<isolation().md>) — Produce a reference to the actor to which the enclosing code is isolated, or `nil` if the code is nonisolated.
