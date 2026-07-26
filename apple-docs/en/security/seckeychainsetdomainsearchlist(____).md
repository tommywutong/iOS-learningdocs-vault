---
title: 'SecKeychainSetDomainSearchList(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainsetdomainsearchlist(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainsetdomainsearchlist(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainsetdomainsearchlist%28_%3A_%3A%29.json'
content_hash: 'sha256:36135f968270b69f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainSetDomainSearchList(_:_:)

<sub>Function</sub>

Sets the keychain search list for a specified preference domain.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainSetDomainSearchList(_ domain: SecPreferencesDomain, _ searchList: CFArray) -> OSStatus
```

## Parameters

- `domain` — The preference domain for which you wish to set the default keychain search list. See [SecPreferencesDomain](secpreferencesdomain.md)for possible domain values.

- `searchList` — A pointer to a keychain search list to set in the preference domain.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

A preference domain is a set of security-related preferences, such as the default keychain and the current keychain search list. Use this function if you want to set the keychain search list for a specific preference domain. Use the [SecKeychainSetSearchList](<seckeychainsetsearchlist(__).md>) function if you want to set the keychain search list for the current preference domain. See the [SecKeychainSetPreferenceDomain](<seckeychainsetpreferencedomain(__).md>) function for a discussion of current and default preference domains.
