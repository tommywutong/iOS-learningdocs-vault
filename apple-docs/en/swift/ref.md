---
title: Ref
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/ref
source_url: 'https://developer.apple.com/documentation/swift/ref'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/ref.json'
content_hash: 'sha256:47595871662de217'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Ref

<sub>Structure</sub>

A safe reference allowing in-place reads to a shared value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Ref<Value> where Value : ~Copyable
```

## Relationships

- **Conforms To**: [BitwiseCopyable](bitwisecopyable.md), [Copyable](copyable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<ref/init(__).md>) — Initializes an instance of `Ref` with the given borrowed value. This creates a constant reference to that value preventing writes on the original value while this reference is still active. _(beta)_
- [init(unsafeAddress:borrowing:)](<ref/init(unsafeaddress_borrowing_).md>) — Unsafely initializes an instance of `Ref` using the given ‘unsafeAddress’ as the reference based on the borrowed lifetime of the given ‘owner’ argument. _(beta)_

### Instance Properties

- [value](ref/value.md) — Dereferences the constant reference allowing for in-place reads to the underlying value. _(beta)_

## See Also

### Borrowing

- [MutableRef](mutableref.md) — A safe mutable reference allowing in-place mutation to an exclusive value. _(beta)_
