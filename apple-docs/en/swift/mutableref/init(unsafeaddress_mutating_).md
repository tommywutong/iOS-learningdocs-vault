---
title: 'init(unsafeAddress:mutating:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/mutableref/init(unsafeaddress:mutating:)'
source_url: 'https://developer.apple.com/documentation/swift/mutableref/init(unsafeaddress:mutating:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutableref/init%28unsafeaddress%3Amutating%3A%29.json'
content_hash: 'sha256:b79d6239a2606d83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableRef](../mutableref.md)

# init(unsafeAddress:mutating:)

<sub>Initializer</sub>

Unsafely initializes an instance of `MutableRef` using the given ‘unsafeAddress’ as the mutable reference based on the mutating lifetime of the given ‘owner’ argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Owner>(unsafeAddress pointer: UnsafeMutablePointer<Value>, mutating owner: inout Owner) where Owner : ~Copyable, Owner : ~Escapable
```

## Parameters

- `owner` — The owning instance that this `MutableRef` instance’s lifetime is based on.
