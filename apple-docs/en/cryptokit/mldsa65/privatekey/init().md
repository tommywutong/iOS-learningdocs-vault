---
title: init()
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/mldsa65/privatekey/init()
source_url: 'https://developer.apple.com/documentation/cryptokit/mldsa65/privatekey/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mldsa65/privatekey/init%28%29.json'
content_hash: 'sha256:b2675ed82b577735'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLDSA65](../../mldsa65.md) · [PrivateKey](../privatekey.md)

# init()

<sub>Initializer</sub>

Creates a random MLDSA65 private key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init() throws
```

## Discussion

This initializer is marked `throws` to support use in generic contexts, but key generation itself doesn’t produce errors.

When you call this initializer directly on a concrete type, rather than through a generic type parameter, you can safely call `try!` to create the key:

```swift
let privateKey = try! MLDSA65.PrivateKey()
```

## See Also

### Creating a private key

- [init(integrityCheckedRepresentation:)](<init(integritycheckedrepresentation_).md>) — Initializes a private key from an integrity-checked data representation.
- [init(seedRepresentation:publicKey:)](<init(seedrepresentation_publickey_).md>) — Initializes a private key from the seed representation.
