---
title: 'init(compactRepresentable:accessControl:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [tvOS 13.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/secureenclave/p256/keyagreement/privatekey/init(compactrepresentable:accesscontrol:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave/p256/keyagreement/privatekey/init(compactrepresentable:accesscontrol:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave/p256/keyagreement/privatekey/init%28compactrepresentable%3Aaccesscontrol%3A%29.json'
content_hash: 'sha256:c9896dba085cc1fa'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Apple CryptoKit](../../../../../cryptokit.md) · [SecureEnclave](../../../../secureenclave.md) · [P256](../../../p256.md) · [KeyAgreement](../../keyagreement.md) · [PrivateKey](../privatekey.md)

# init(compactRepresentable:accessControl:)

<sub>Initializer</sub>

Creates a P-256 private key for key agreement with the specified access control.

<sub>tvOS, watchOS</sub>

```swift
init(compactRepresentable: Bool = true, accessControl: SecAccessControl = SecAccessControlCreateWithFlags(nil, kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly, [], nil)!) throws
```

## Parameters

- `compactRepresentable` — A Boolean value that indicates whether CryptoKit creates the key with the structure to enable compact point encoding.

- `accessControl` — The protection type and flags to use when creating the associated access control object.
