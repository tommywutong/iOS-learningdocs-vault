---
title: 'SecKeychainSetDomainDefault(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainsetdomaindefault(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainsetdomaindefault(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainsetdomaindefault%28_%3A_%3A%29.json'
content_hash: 'sha256:e44a093ae085843b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainSetDomainDefault(_:_:)

<sub>Function</sub>

Sets the default keychain for a specified preference domain.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainSetDomainDefault(_ domain: SecPreferencesDomain, _ keychain: SecKeychain?) -> OSStatus
```

## Parameters

- `domain` — The preference domain for which you wish to set the default keychain. See [SecPreferencesDomain](secpreferencesdomain.md) for possible domain values.

- `keychain` — A reference to the keychain you wish to set as default in the specified preference domain.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

A preference domain is a set of security-related preferences, such as the default keychain and the current keychain search list. Use this function if you want to set the default keychain for a specific preference domain. Use the [SecKeychainSetDefault](<seckeychainsetdefault(__).md>) function if you want to set the default keychain for the current preference domain. See the [SecKeychainSetPreferenceDomain](<seckeychainsetpreferencedomain(__).md>) function for a discussion of current and default preference domains.
