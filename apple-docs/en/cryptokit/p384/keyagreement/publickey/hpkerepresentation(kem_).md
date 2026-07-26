---
title: 'hpkeRepresentation(kem:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/p384/keyagreement/publickey/hpkerepresentation(kem:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/p384/keyagreement/publickey/hpkerepresentation(kem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p384/keyagreement/publickey/hpkerepresentation%28kem%3A%29.json'
content_hash: 'sha256:c7c8d0592473f52f'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P384](../../../p384.md) · [KeyAgreement](../../keyagreement.md) · [PublicKey](../publickey.md)

# hpkeRepresentation(kem:)

<sub>Instance Method</sub>

Creates a serialized representation of the public key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hpkeRepresentation(kem: HPKE.KEM) throws -> Data
```

## Return Value

The serialized representation of the public key.

## Discussion

- kem: The Key Encapsulation Mechanism to use with the public key.

> [!danger] Throws
> [HPKE.Errors.inconsistentCiphersuiteAndKey](../../../hpke/errors/inconsistentciphersuiteandkey.md) if the key encapsulation mechanism requested is incompatible with this public key.
