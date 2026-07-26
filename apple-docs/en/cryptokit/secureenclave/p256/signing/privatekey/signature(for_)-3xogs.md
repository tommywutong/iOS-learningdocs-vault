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
doc_path: '/documentation/cryptokit/secureenclave/p256/signing/privatekey/signature(for:)-3xogs'
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave/p256/signing/privatekey/signature(for:)-3xogs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave/p256/signing/privatekey/signature%28for%3A%29-3xogs.json'
content_hash: 'sha256:0b1b8ce91966cb5b'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Apple CryptoKit](../../../../../cryptokit.md) · [SecureEnclave](../../../../secureenclave.md) · [P256](../../../p256.md) · [Signing](../../signing.md) · [PrivateKey](../privatekey.md)

# signature(for:)

<sub>Instance Method</sub>

Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the digest you provide over the P-256 elliptic curve.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func signature<D>(for digest: D) throws -> P256.Signing.ECDSASignature where D : Digest
```

## Parameters

- `digest` — The digest of the data to sign.

## Return Value

The signature corresponding to the digest. The signing algorithm employs randomization to generate a different signature on every call, even for the same digest and key.

## See Also

### Generating a signature

- [signature(for:)](<signature(for_)-76j0u.md>) — Generates an elliptic curve digital signature algorithm (ECDSA) signature of the given data over the P-256 elliptic curve, using SHA-256 as the hash function.
