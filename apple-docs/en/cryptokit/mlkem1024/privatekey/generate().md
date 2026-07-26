---
title: generate()
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/mlkem1024/privatekey/generate()
source_url: 'https://developer.apple.com/documentation/cryptokit/mlkem1024/privatekey/generate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mlkem1024/privatekey/generate%28%29.json'
content_hash: 'sha256:b281b74bb5c8f2b4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLKEM1024](../../mlkem1024.md) · [PrivateKey](../privatekey.md)

# generate()

<sub>Type Method</sub>

Generates a new, random private key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func generate() throws -> MLKEM1024.PrivateKey
```

## See Also

### Creating a private key

- [init()](<init().md>) — Initializes a random private key.
- [init(integrityCheckedRepresentation:)](<init(integritycheckedrepresentation_).md>) — Initializes a private key from an integrity-checked representation.
- [init(seedRepresentation:publicKey:)](<init(seedrepresentation_publickey_).md>) — Initializes a private key from a seed representation and optional public key.
