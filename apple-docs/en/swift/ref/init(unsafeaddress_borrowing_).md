---
title: 'init(unsafeAddress:borrowing:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/ref/init(unsafeaddress:borrowing:)'
source_url: 'https://developer.apple.com/documentation/swift/ref/init(unsafeaddress:borrowing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/ref/init%28unsafeaddress%3Aborrowing%3A%29.json'
content_hash: 'sha256:d3659ea34e889f2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Ref](../ref.md)

# init(unsafeAddress:borrowing:)

<sub>Initializer</sub>

Unsafely initializes an instance of `Ref` using the given ‘unsafeAddress’ as the reference based on the borrowed lifetime of the given ‘owner’ argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Owner>(unsafeAddress pointer: UnsafePointer<Value>, borrowing owner: borrowing Owner) where Owner : ~Copyable, Owner : ~Escapable
```

## Parameters

- `owner` — The owning instance that this `Ref` instance’s lifetime is based on.
