---
title: keychain
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychaincallbackinfo/keychain
source_url: 'https://developer.apple.com/documentation/security/seckeychaincallbackinfo/keychain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaincallbackinfo/keychain.json'
content_hash: 'sha256:486c2a290c8a323c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainCallbackInfo](../seckeychaincallbackinfo.md)

# keychain

<sub>Instance Property</sub>

A reference to the keychain in which the event occurred. If the event did not involve a keychain, this field is not valid.

<sub>macOS</sub>

```swift
var keychain: Unmanaged<SecKeychain>
```
