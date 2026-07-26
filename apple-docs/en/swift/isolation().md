---
title: isolation()
framework: Swift
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/isolation()
source_url: 'https://developer.apple.com/documentation/swift/isolation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/isolation%28%29.json'
content_hash: 'sha256:1111804fbf4dcdd2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# isolation()

<sub>Macro</sub>

Produce a reference to the actor to which the enclosing code is isolated, or `nil` if the code is nonisolated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@freestanding(expression) macro isolation<T>() -> T
```

## Overview

If the type annotation provided for `#isolation` is not `(any Actor)?`, the type must match the enclosing actor type. If no type annotation is provided, the type defaults to `(any Actor)?`.

## See Also

### Actors

- [Sendable](sendable.md) — A thread-safe type whose values can be shared across arbitrary concurrent contexts without introducing a risk of data races.
- [Actor](actor.md) — Common protocol to which all actors conform.
- [MainActor](mainactor.md) — A singleton actor whose executor is equivalent to the main dispatch queue.
- [GlobalActor](globalactor.md) — A type that represents a globally-unique actor that can be used to isolate various declarations anywhere in the program.
- [SendableMetatype](sendablemetatype.md) — A type whose metatype can be shared across arbitrary isolation domains without introducing a risk of data races.
