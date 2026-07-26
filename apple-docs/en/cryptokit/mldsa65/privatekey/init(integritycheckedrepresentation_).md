---
title: 'init(integrityCheckedRepresentation:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/mldsa65/privatekey/init(integritycheckedrepresentation:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/mldsa65/privatekey/init(integritycheckedrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mldsa65/privatekey/init%28integritycheckedrepresentation%3A%29.json'
content_hash: 'sha256:a1c2af089be25b50'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLDSA65](../../mldsa65.md) · [PrivateKey](../privatekey.md)

# init(integrityCheckedRepresentation:)

<sub>Initializer</sub>

Initializes a private key from an integrity-checked data representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<D>(integrityCheckedRepresentation: D) throws where D : DataProtocol
```

## Parameters

- `integrityCheckedRepresentation` — The integrity-checked data representation of the private key. The parameter needs to be 64 bytes long, and contain the seed and a hash of the public key.

## See Also

### Creating a private key

- [init()](<init().md>) — Creates a random MLDSA65 private key.
- [init(seedRepresentation:publicKey:)](<init(seedrepresentation_publickey_).md>) — Initializes a private key from the seed representation.
