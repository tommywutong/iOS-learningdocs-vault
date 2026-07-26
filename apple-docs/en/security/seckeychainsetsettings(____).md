---
title: 'SecKeychainSetSettings(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainsetsettings(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainsetsettings(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainsetsettings%28_%3A_%3A%29.json'
content_hash: 'sha256:4b31a39bbe7bbe10'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainSetSettings(_:_:)

<sub>Function</sub>

Changes the settings of a keychain.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainSetSettings(_ keychain: SecKeychain?, _ newSettings: UnsafePointer<SecKeychainSettings>) -> OSStatus
```

## Parameters

- `keychain` — A reference to a keychain whose settings you wish to change. Pass `NULL` to change the settings of the default keychain.

- `newSettings` — A pointer to a keychain settings structure that defines whether the keychain locks when sleeping, or locks after a set time period of inactivity.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
