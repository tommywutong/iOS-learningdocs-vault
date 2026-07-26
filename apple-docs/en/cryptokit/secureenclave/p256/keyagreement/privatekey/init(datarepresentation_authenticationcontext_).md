---
title: 'init(dataRepresentation:authenticationContext:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/secureenclave/p256/keyagreement/privatekey/init(datarepresentation:authenticationcontext:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave/p256/keyagreement/privatekey/init(datarepresentation:authenticationcontext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave/p256/keyagreement/privatekey/init%28datarepresentation%3Aauthenticationcontext%3A%29.json'
content_hash: 'sha256:a1f52afba00173cf'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Apple CryptoKit](../../../../../cryptokit.md) · [SecureEnclave](../../../../secureenclave.md) · [P256](../../../p256.md) · [KeyAgreement](../../keyagreement.md) · [PrivateKey](../privatekey.md)

# init(dataRepresentation:authenticationContext:)

<sub>Initializer</sub>

Creates a P-256 private key for key agreement from a data representation of the key with the given authentication context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(dataRepresentation: Data, authenticationContext: LAContext? = nil) throws
```

## Parameters

- `dataRepresentation` — A data representation of the key.

- `authenticationContext` — A local authentication context.

## See Also

### Creating a private key

- [init(compactRepresentable:accessControl:authenticationContext:)](<init(compactrepresentable_accesscontrol_authenticationcontext_).md>) — Creates a P-256 private key for key agreement with the specified access control.
