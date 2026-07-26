---
title: kSecAttrTokenIDSecureEnclave
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattrtokenidsecureenclave
source_url: 'https://developer.apple.com/documentation/security/ksecattrtokenidsecureenclave'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattrtokenidsecureenclave.json'
content_hash: 'sha256:f8f48ffca7098b98'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrTokenIDSecureEnclave

<sub>Global Variable</sub>

Specifies an item should be stored in the device’s Secure Enclave.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrTokenIDSecureEnclave: CFString
```

## Discussion

The only keychain items supported by the Secure Enclave are 256-bit elliptic curve private keys (those that have key type [kSecAttrKeyTypeEC](ksecattrkeytypeec.md)). Such keys must be generated directly on the Secure Enclave using the [SecKeyGeneratePair](<seckeygeneratepair(______).md>) function with the [kSecAttrTokenID](ksecattrtokenid.md) key set to [kSecAttrTokenIDSecureEnclave](ksecattrtokenidsecureenclave.md) in the parameters dictionary.

> [!important] Important
> It is not possible to import pre-existing keys into the Secure Enclave.
