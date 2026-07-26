---
title: 'SecKeychainCopyDomainSearchList(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychaincopydomainsearchlist(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychaincopydomainsearchlist(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaincopydomainsearchlist%28_%3A_%3A%29.json'
content_hash: 'sha256:e5a96a1da108fe71'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainCopyDomainSearchList(_:_:)

<sub>Function</sub>

Retrieves the keychain search list for a specified preference domain.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainCopyDomainSearchList(_ domain: SecPreferencesDomain, _ searchList: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

## Parameters

- `domain` — The preference domain from which you wish to retrieve the keychain search list. See [SecPreferencesDomain](secpreferencesdomain.md) for possible domain values.

- `searchList` — On return, a pointer to the keychain search list of the specified preference domain.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

A preference domain is a set of security-related preferences, such as the default keychain and the current keychain search list. Use this function if you want to retrieve the keychain search list for a specific preference domain. Use the [SecKeychainCopySearchList](<seckeychaincopysearchlist(__).md>) function if you want the keychain search list for the current preference domain. See the [SecKeychainSetPreferenceDomain](<seckeychainsetpreferencedomain(__).md>) function for a discussion of current and default preference domains.
