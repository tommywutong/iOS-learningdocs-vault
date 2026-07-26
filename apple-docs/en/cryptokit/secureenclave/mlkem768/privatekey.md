---
title: SecureEnclave.MLKEM768.PrivateKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/secureenclave/mlkem768/privatekey
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave/mlkem768/privatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave/mlkem768/privatekey.json'
content_hash: 'sha256:49a0fc5fd7b6121e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [SecureEnclave](../../secureenclave.md) · [MLKEM768](../mlkem768.md)

# SecureEnclave.MLKEM768.PrivateKey

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PrivateKey
```

## Relationships

- **Conforms To**: [KEMPrivateKey](../../kemprivatekey.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating a private key

- [generate()](<privatekey/generate().md>) — Generates a new random private key.
- [init(accessControl:authenticationContext:)](<privatekey/init(accesscontrol_authenticationcontext_).md>)
- [init(dataRepresentation:authenticationContext:)](<privatekey/init(datarepresentation_authenticationcontext_).md>)

### Accessing the key’s properties

- [dataRepresentation](privatekey/datarepresentation.md) — A data representation of the private key.
- [publicKey](privatekey/publickey.md) — The corresponding public key.

### Decapsulating shared secrets

- [decapsulate(_:)](<privatekey/decapsulate(__).md>) — Decapsulates the encapsulated shared secret

### Initializers

- [init(accessControl:)](<privatekey/init(accesscontrol_).md>)
- [init(dataRepresentation:)](<privatekey/init(datarepresentation_).md>)
