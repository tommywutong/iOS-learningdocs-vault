---
title: 'signature(for:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/p521/signing/privatekey/signature(for:)-7rxva'
source_url: 'https://developer.apple.com/documentation/cryptokit/p521/signing/privatekey/signature(for:)-7rxva'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p521/signing/privatekey/signature%28for%3A%29-7rxva.json'
content_hash: 'sha256:1da1bebf266c4182'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P521](../../../p521.md) · [Signing](../../signing.md) · [PrivateKey](../privatekey.md)

# signature(for:)

<sub>Instance Method</sub>

Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the digest you provide over the P-521 elliptic curve.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func signature<D>(for digest: D) throws -> P521.Signing.ECDSASignature where D : Digest
```

## Parameters

- `digest` — The digest of the data to sign.

## Return Value

The signature corresponding to the digest. The signing algorithm employs randomization to generate a different signature on every call, even for the same data and key.

## See Also

### Creating a signature

- [signature(for:)](<signature(for_)-34g01.md>) — Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the data you provide over the P-521 elliptic curve, using SHA-512 as the hash function.
- [ECDSASignature](../ecdsasignature.md) — A P-521 elliptic curve digital signature algorithm (ECDSA) signature.
