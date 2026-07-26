---
title: 'hkdfDerivedSymmetricKey(using:salt:sharedInfo:outputByteCount:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/sharedsecret/hkdfderivedsymmetrickey(using:salt:sharedinfo:outputbytecount:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/sharedsecret/hkdfderivedsymmetrickey(using:salt:sharedinfo:outputbytecount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/sharedsecret/hkdfderivedsymmetrickey%28using%3Asalt%3Asharedinfo%3Aoutputbytecount%3A%29.json'
content_hash: 'sha256:7e4e907936c294b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [SharedSecret](../sharedsecret.md)

# hkdfDerivedSymmetricKey(using:salt:sharedInfo:outputByteCount:)

<sub>Instance Method</sub>

Derives a symmetric encryption key from the secret using HKDF key derivation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hkdfDerivedSymmetricKey<H, Salt, SI>(using hashFunction: H.Type, salt: Salt, sharedInfo: SI, outputByteCount: Int) -> SymmetricKey where H : HashFunction, Salt : DataProtocol, SI : DataProtocol
```

## Parameters

- `hashFunction` — The hash function to use for key derivation.

- `salt` — The salt to use for key derivation.

- `sharedInfo` — The shared information to use for key derivation.

- `outputByteCount` — The length in bytes of resulting symmetric key.

## Return Value

The derived symmetric key.

## See Also

### Deriving keys

- [x963DerivedSymmetricKey(using:sharedInfo:outputByteCount:)](<x963derivedsymmetrickey(using_sharedinfo_outputbytecount_).md>) — Derives a symmetric encryption key from the secret using x9.63 key derivation.
