---
title: 'init(accessControl:authenticationContext:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/secureenclave/mlkem1024/privatekey/init(accesscontrol:authenticationcontext:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave/mlkem1024/privatekey/init(accesscontrol:authenticationcontext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave/mlkem1024/privatekey/init%28accesscontrol%3Aauthenticationcontext%3A%29.json'
content_hash: 'sha256:58e55fcee08bec5c'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [SecureEnclave](../../../secureenclave.md) · [MLKEM1024](../../mlkem1024.md) · [PrivateKey](../privatekey.md)

# init(accessControl:authenticationContext:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(accessControl: SecAccessControl = SecAccessControlCreateWithFlags(nil, kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly, [], nil)!, authenticationContext: LAContext? = nil) throws
```

## See Also

### Creating a private key

- [generate()](<generate().md>) — Generates a new random private key.
- [init(dataRepresentation:authenticationContext:)](<init(datarepresentation_authenticationcontext_).md>)
