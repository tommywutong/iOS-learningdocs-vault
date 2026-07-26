---
title: SecureEnclave.MLDSA87.PrivateKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/secureenclave/mldsa87/privatekey
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave/mldsa87/privatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave/mldsa87/privatekey.json'
content_hash: 'sha256:ceb826de20e64736'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [SecureEnclave](../../secureenclave.md) · [MLDSA87](../mldsa87.md)

# SecureEnclave.MLDSA87.PrivateKey

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PrivateKey
```

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(accessControl:)](<privatekey/init(accesscontrol_).md>)
- [init(accessControl:authenticationContext:)](<privatekey/init(accesscontrol_authenticationcontext_).md>)
- [init(dataRepresentation:)](<privatekey/init(datarepresentation_).md>)
- [init(dataRepresentation:authenticationContext:)](<privatekey/init(datarepresentation_authenticationcontext_).md>)

### Instance Properties

- [dataRepresentation](privatekey/datarepresentation.md) — A data representation of the private key.
- [publicKey](privatekey/publickey.md) — The corresponding public key.

### Instance Methods

- [signature(for:)](<privatekey/signature(for_).md>) — Generates a MLDSA87 signature
- [signature(for:context:)](<privatekey/signature(for_context_).md>) — Generates a MLDSA87 signature, with context
