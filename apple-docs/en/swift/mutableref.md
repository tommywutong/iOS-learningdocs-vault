---
title: MutableRef
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/mutableref
source_url: 'https://developer.apple.com/documentation/swift/mutableref'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutableref.json'
content_hash: 'sha256:253bd2db0c7fb018'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# MutableRef

<sub>Structure</sub>

A safe mutable reference allowing in-place mutation to an exclusive value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct MutableRef<Value> where Value : ~Copyable
```

## Relationships

- **Conforms To**: [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<mutableref/init(__).md>) — Initializes an instance of `MutableRef` with the given mutable value. This creates a mutable reference to that value preventing writes to the original value while this mutable reference is still active. _(beta)_
- [init(unsafeAddress:mutating:)](<mutableref/init(unsafeaddress_mutating_).md>) — Unsafely initializes an instance of `MutableRef` using the given ‘unsafeAddress’ as the mutable reference based on the mutating lifetime of the given ‘owner’ argument. _(beta)_

### Instance Properties

- [value](mutableref/value.md) — Dereferences the mutable reference allowing for in-place reads and writes to the underlying value. _(beta)_

## See Also

### Borrowing

- [Ref](ref.md) — A safe reference allowing in-place reads to a shared value. _(beta)_
