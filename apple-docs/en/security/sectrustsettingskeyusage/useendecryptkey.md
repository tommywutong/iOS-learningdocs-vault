---
title: useEnDecryptKey
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectrustsettingskeyusage/useendecryptkey
source_url: 'https://developer.apple.com/documentation/security/sectrustsettingskeyusage/useendecryptkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsettingskeyusage/useendecryptkey.json'
content_hash: 'sha256:a56112ebb083f084'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecTrustSettingsKeyUsage](../sectrustsettingskeyusage.md)

# useEnDecryptKey

<sub>Type Property</sub>

The key can be used to encrypt or decrypt (wrap or unwrap) a key.

<sub>Mac Catalyst, macOS</sub>

```swift
static var useEnDecryptKey: SecTrustSettingsKeyUsage { get }
```

## Discussion

Private keys must be wrapped before they can be exported from a keychain.
