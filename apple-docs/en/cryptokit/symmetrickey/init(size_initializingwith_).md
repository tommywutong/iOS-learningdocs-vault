---
title: 'init(size:initializingWith:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/cryptokit/symmetrickey/init(size:initializingwith:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/symmetrickey/init(size:initializingwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/symmetrickey/init%28size%3Ainitializingwith%3A%29.json'
content_hash: 'sha256:7462d5eeb5663aab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [SymmetricKey](../symmetrickey.md)

# init(size:initializingWith:)

<sub>Initializer</sub>

Creates a new key of the given size where the key contents are initialized via a callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<E>(size: SymmetricKeySize, initializingWith callback: @_lifetime(0: copy 0) (inout OutputRawSpan) throws(E) -> Void) throws(E) where E : Error
```

## Parameters

- `size` — The size of the key to generate. You can use one of the standard sizes, like [bits256](../symmetrickeysize/bits256.md), or you can create a key of custom length by initializing a [SymmetricKeySize](../symmetrickeysize.md) instance with a non-standard value.

- `callback` — A callback that will be invoked to initialize the contents of the key. It must initialize the full set of size.bitCount / 8 bytes in the provided output span.
