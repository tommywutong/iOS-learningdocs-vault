---
title: 'init(compactRepresentable:accessControl:authenticationContext:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/secureenclave/p256/signing/privatekey/init(compactrepresentable:accesscontrol:authenticationcontext:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave/p256/signing/privatekey/init(compactrepresentable:accesscontrol:authenticationcontext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave/p256/signing/privatekey/init%28compactrepresentable%3Aaccesscontrol%3Aauthenticationcontext%3A%29.json'
content_hash: 'sha256:9042de2d7fa1fb0c'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Apple CryptoKit](../../../../../cryptokit.md) · [SecureEnclave](../../../../secureenclave.md) · [P256](../../../p256.md) · [Signing](../../signing.md) · [PrivateKey](../privatekey.md)

# init(compactRepresentable:accessControl:authenticationContext:)

<sub>Initializer</sub>

Creates a P-256 private key for signing with the specified access control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(compactRepresentable: Bool = true, accessControl: SecAccessControl = SecAccessControlCreateWithFlags(nil, kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly, [], nil)!, authenticationContext: LAContext? = nil) throws
```

## Parameters

- `compactRepresentable` — A Boolean value that indicates whether CryptoKit creates the key with the structure to enable compact point encoding.

- `accessControl` — The protection type and flags to use when creating the associated access control object.

- `authenticationContext` — A local authentication context.

## See Also

### Creating a private key

- [init(dataRepresentation:authenticationContext:)](<init(datarepresentation_authenticationcontext_).md>) — Creates a P-256 private key for signing from a data representation of the key with the given authentication context.
