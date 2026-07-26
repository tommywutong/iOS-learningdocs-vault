---
title: privateKeyUsage
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.12.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secaccesscontrolcreateflags/privatekeyusage
source_url: 'https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/privatekeyusage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secaccesscontrolcreateflags/privatekeyusage.json'
content_hash: 'sha256:a66206f1e61926e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecAccessControlCreateFlags](../secaccesscontrolcreateflags.md)

# privateKeyUsage

<sub>Type Property</sub>

Enable a private key to be used in signing a block of data or verifying a signed block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var privateKeyUsage: SecAccessControlCreateFlags { get }
```

## Discussion

This option can be combined with any other access control flags.

You typically use this constraint when you create a key pair and store the private key inside a device’s Secure Enclave (by specifying the [kSecAttrTokenID](../ksecattrtokenid.md) attribute with a value of [kSecAttrTokenIDSecureEnclave](../ksecattrtokenidsecureenclave.md)). This makes the private key available for use in signing and verification tasks that happen inside the Secure Enclave with calls to the [SecKeyRawSign](<../seckeyrawsign(____________).md>) and [SecKeyRawVerify](<../seckeyrawverify(____________).md>) functions. An attempt to use this constraint while generating a key pair outside the Secure Enclave fails. Similarly, an attempt to sign a block with a private key generated without this constraint inside the Secure Enclave fails.
