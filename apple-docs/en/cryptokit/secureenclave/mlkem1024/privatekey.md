---
title: SecureEnclave.MLKEM1024.PrivateKey
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/secureenclave/mlkem1024/privatekey
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave/mlkem1024/privatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave/mlkem1024/privatekey.json'
content_hash: 'sha256:96202fc0c1663d27'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [SecureEnclave](../../secureenclave.md) · [MLKEM1024](../mlkem1024.md)

# SecureEnclave.MLKEM1024.PrivateKey

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

### Accessing a key’s properties

- [dataRepresentation](privatekey/datarepresentation.md) — A data representation of the private key.
- [publicKey](privatekey/publickey.md) — The corresponding public key.

### Decapsulating shared secrets

- [decapsulate(_:)](<privatekey/decapsulate(__).md>) — Decapsulates the encapsulated shared secret

### Initializers

- [init(accessControl:)](<privatekey/init(accesscontrol_).md>)
- [init(dataRepresentation:)](<privatekey/init(datarepresentation_).md>)
