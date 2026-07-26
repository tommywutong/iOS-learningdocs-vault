---
title: 'x963DerivedSymmetricKey(using:sharedInfo:outputByteCount:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/sharedsecret/x963derivedsymmetrickey(using:sharedinfo:outputbytecount:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/sharedsecret/x963derivedsymmetrickey(using:sharedinfo:outputbytecount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/sharedsecret/x963derivedsymmetrickey%28using%3Asharedinfo%3Aoutputbytecount%3A%29.json'
content_hash: 'sha256:32c6f236689bf710'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [SharedSecret](../sharedsecret.md)

# x963DerivedSymmetricKey(using:sharedInfo:outputByteCount:)

<sub>Instance Method</sub>

Derives a symmetric encryption key from the secret using x9.63 key derivation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func x963DerivedSymmetricKey<H, SI>(using hashFunction: H.Type, sharedInfo: SI, outputByteCount: Int) -> SymmetricKey where H : HashFunction, SI : DataProtocol
```

## Parameters

- `hashFunction` — The hash function to use for key derivation.

- `sharedInfo` — The shared information to use for key derivation.

- `outputByteCount` — The length in bytes of resulting symmetric key.

## Return Value

The derived symmetric key.

## See Also

### Deriving keys

- [hkdfDerivedSymmetricKey(using:salt:sharedInfo:outputByteCount:)](<hkdfderivedsymmetrickey(using_salt_sharedinfo_outputbytecount_).md>) — Derives a symmetric encryption key from the secret using HKDF key derivation.
