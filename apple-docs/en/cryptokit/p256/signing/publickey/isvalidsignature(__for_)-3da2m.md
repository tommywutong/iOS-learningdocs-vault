---
title: 'isValidSignature(_:for:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/p256/signing/publickey/isvalidsignature(_:for:)-3da2m'
source_url: 'https://developer.apple.com/documentation/cryptokit/p256/signing/publickey/isvalidsignature(_:for:)-3da2m'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p256/signing/publickey/isvalidsignature%28_%3Afor%3A%29-3da2m.json'
content_hash: 'sha256:845bcdc555914cee'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P256](../../../p256.md) · [Signing](../../signing.md) · [PublicKey](../publickey.md)

# isValidSignature(_:for:)

<sub>Instance Method</sub>

Verifies an elliptic curve digital signature algorithm (ECDSA) signature on a block of data over the P-256 elliptic curve.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isValidSignature<D>(_ signature: P256.Signing.ECDSASignature, for data: D) -> Bool where D : DataProtocol
```

## Parameters

- `signature` — The signature to verify.

- `data` — The signed data.

## Return Value

A Boolean value that’s `true` if the signature is valid for the given data; otherwise, `false`.

## See Also

### Verifying a signature

- [isValidSignature(_:for:)](<isvalidsignature(__for_)-2rsb5.md>) — Verifies an elliptic curve digital signature algorithm (ECDSA) signature on a digest over the P-256 elliptic curve.
- [ECDSASignature](../ecdsasignature.md) — A P-256 elliptic curve digital signature algorithm (ECDSA) signature.
