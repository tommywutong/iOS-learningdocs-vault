---
title: SecureEnclave.P256.KeyAgreement.PrivateKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/secureenclave/p256/keyagreement/privatekey
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave/p256/keyagreement/privatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave/p256/keyagreement/privatekey.json'
content_hash: 'sha256:c47e1e43d6e5777a'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [SecureEnclave](../../../secureenclave.md) · [P256](../../p256.md) · [KeyAgreement](../keyagreement.md)

# SecureEnclave.P256.KeyAgreement.PrivateKey

<sub>Structure</sub>

A P-256 private key used for key agreement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PrivateKey
```

## Relationships

- **Conforms To**: [Copyable](../../../../swift/copyable.md), [DiffieHellmanKeyAgreement](../../../diffiehellmankeyagreement.md), [Escapable](../../../../swift/escapable.md), [HPKEDiffieHellmanPrivateKey](../../../hpkediffiehellmanprivatekey.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Creating a private key

- [init(dataRepresentation:authenticationContext:)](<privatekey/init(datarepresentation_authenticationcontext_).md>) — Creates a P-256 private key for key agreement from a data representation of the key with the given authentication context.
- [init(compactRepresentable:accessControl:authenticationContext:)](<privatekey/init(compactrepresentable_accesscontrol_authenticationcontext_).md>) — Creates a P-256 private key for key agreement with the specified access control.

### Representing the key

- [dataRepresentation](privatekey/datarepresentation.md) — A data representation of the private key.

### Finding the public key

- [publicKey](privatekey/publickey.md) — The corresponding public key.

### Creating a shared secret

- [sharedSecretFromKeyAgreement(with:)](<privatekey/sharedsecretfromkeyagreement(with_).md>) — Computes a shared secret with the provided public key from another party.
- [SharedSecret](../../../sharedsecret.md) — A key agreement result from which you can derive a symmetric cryptographic key.

### Initializers

- [init(compactRepresentable:accessControl:)](<privatekey/init(compactrepresentable_accesscontrol_).md>) — Creates a P-256 private key for key agreement with the specified access control.
- [init(dataRepresentation:)](<privatekey/init(datarepresentation_).md>) — Creates a P-256 private key for key agreement from the specified data representation.

### Default Implementations

- [DiffieHellmanKeyAgreement Implementations](privatekey/diffiehellmankeyagreement-implementations.md)
