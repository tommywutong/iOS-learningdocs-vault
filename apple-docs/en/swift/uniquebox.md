---
title: UniqueBox
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/uniquebox
source_url: 'https://developer.apple.com/documentation/swift/uniquebox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquebox.json'
content_hash: 'sha256:e08fa31c6ef8503e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UniqueBox

<sub>Structure</sub>

A smart pointer type that uniquely owns an instance of `Value` on the heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct UniqueBox<Value> where Value : ~Copyable
```

## Relationships

- **Conforms To**: [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<uniquebox/init(__).md>) — Initializes a value of this unqiue box with the given initial value. _(beta)_

### Instance Properties

- [mutableSpan](uniquebox/mutablespan.md) — A mutable span over the single element stored in this box. _(beta)_
- [span](uniquebox/span.md) — A span over the single element stored in this box. _(beta)_
- [value](uniquebox/value.md) — Dereferences the unique box allowing for in-place reads and writes to the stored `Value`. _(beta)_

### Instance Methods

- [clone()](<uniquebox/clone().md>) — Copies the value within the unqiue box and returns it in a new unique instance. _(beta)_
- [consume()](<uniquebox/consume().md>) — Consumes the unique box and returns the instance of `Value` that was within the box. _(beta)_

## See Also

### Heap Storage

- [UniqueArray](uniquearray.md) — A dynamically self-resizing, heap allocated, noncopyable array of potentially noncopyable elements. _(beta)_
