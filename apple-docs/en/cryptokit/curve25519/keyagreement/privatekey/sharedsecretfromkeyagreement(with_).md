---
title: 'sharedSecretFromKeyAgreement(with:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/curve25519/keyagreement/privatekey/sharedsecretfromkeyagreement(with:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/curve25519/keyagreement/privatekey/sharedsecretfromkeyagreement(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/curve25519/keyagreement/privatekey/sharedsecretfromkeyagreement%28with%3A%29.json'
content_hash: 'sha256:50bbbff5b9a5b785'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [Curve25519](../../../curve25519.md) · [KeyAgreement](../../keyagreement.md) · [PrivateKey](../privatekey.md)

# sharedSecretFromKeyAgreement(with:)

<sub>Instance Method</sub>

Computes a shared secret with the provided public key from another party.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sharedSecretFromKeyAgreement(with publicKeyShare: Curve25519.KeyAgreement.PublicKey) throws -> SharedSecret
```

## Parameters

- `publicKeyShare` — The public key from another party to be combined with the private key from this user to create the shared secret.

## Return Value

The computed shared secret.

## See Also

### Creating a shared secret

- [SharedSecret](../../../sharedsecret.md) — A key agreement result from which you can derive a symmetric cryptographic key.
