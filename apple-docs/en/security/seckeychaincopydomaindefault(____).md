---
title: 'SecKeychainCopyDomainDefault(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychaincopydomaindefault(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychaincopydomaindefault(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaincopydomaindefault%28_%3A_%3A%29.json'
content_hash: 'sha256:7ea50e6c935b5463'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainCopyDomainDefault(_:_:)

<sub>Function</sub>

Retrieves the default keychain from a specified preference domain.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainCopyDomainDefault(_ domain: SecPreferencesDomain, _ keychain: UnsafeMutablePointer<SecKeychain?>) -> OSStatus
```

## Parameters

- `domain` — The preference domain from which you wish to retrieve the default keychain. See [SecPreferencesDomain](secpreferencesdomain.md) for possible domain values.

- `keychain` — On return, a pointer to the keychain object of the default keychain in the specified preference domain.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

A preference domain is a set of security-related preferences, such as the default keychain and the current keychain search list. Use this function if you want to retrieve the default keychain for a specific preference domain. Use the [SecKeychainCopyDefault](<seckeychaincopydefault(__).md>) function if you want the default keychain for the current preference domain. See the [SecKeychainSetPreferenceDomain](<seckeychainsetpreferencedomain(__).md>) function for a discussion of current and default preference domains.
