---
title: 'init(accessControl:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [tvOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/secureenclave/mlkem768/privatekey/init(accesscontrol:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave/mlkem768/privatekey/init(accesscontrol:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave/mlkem768/privatekey/init%28accesscontrol%3A%29.json'
content_hash: 'sha256:ffc3dbbe4e703a1d'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [SecureEnclave](../../../secureenclave.md) · [MLKEM768](../../mlkem768.md) · [PrivateKey](../privatekey.md)

# init(accessControl:)

<sub>Initializer</sub>

<sub>tvOS</sub>

```swift
init(accessControl: SecAccessControl = SecAccessControlCreateWithFlags(nil, kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly, [], nil)!) throws
```
