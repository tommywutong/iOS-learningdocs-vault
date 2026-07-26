---
title: 'sharedSecretFromKeyAgreement(with:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/diffiehellmankeyagreement/sharedsecretfromkeyagreement(with:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/diffiehellmankeyagreement/sharedsecretfromkeyagreement(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/diffiehellmankeyagreement/sharedsecretfromkeyagreement%28with%3A%29.json'
content_hash: 'sha256:889db6cc6de54811'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [DiffieHellmanKeyAgreement](../diffiehellmankeyagreement.md)

# sharedSecretFromKeyAgreement(with:)

<sub>Instance Method</sub>

Performs a Diffie-Hellman Key Agreement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sharedSecretFromKeyAgreement(with publicKeyShare: Self.PublicKey) throws -> SharedSecret
```

## Parameters

- `publicKeyShare` — The public key share.

## Return Value

The resulting key agreement result.
