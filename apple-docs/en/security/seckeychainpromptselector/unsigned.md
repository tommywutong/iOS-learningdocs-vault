---
title: unsigned
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychainpromptselector/unsigned
source_url: 'https://developer.apple.com/documentation/security/seckeychainpromptselector/unsigned'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainpromptselector/unsigned.json'
content_hash: 'sha256:03c436a942793ac0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainPromptSelector](../seckeychainpromptselector.md)

# unsigned

<sub>Type Property</sub>

Indicates that a passphrase should be required when an unsigned application attempts to use the keychain, overriding the system default.

<sub>macOS</sub>

```swift
static var unsigned: SecKeychainPromptSelector { get }
```
