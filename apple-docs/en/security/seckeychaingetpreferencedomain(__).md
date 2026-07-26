---
title: 'SecKeychainGetPreferenceDomain(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychaingetpreferencedomain(_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychaingetpreferencedomain(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaingetpreferencedomain%28_%3A%29.json'
content_hash: 'sha256:ea8aa522a97ec1e5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainGetPreferenceDomain(_:)

<sub>Function</sub>

Gets the current keychain preference domain.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainGetPreferenceDomain(_ domain: UnsafeMutablePointer<SecPreferencesDomain>) -> OSStatus
```

## Parameters

- `domain` — On return, a pointer to the keychain preference domain. See [SecPreferencesDomain](secpreferencesdomain.md) for possible domain values.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

A preference domain is a set of security-related preferences, such as the default keychain and the current keychain search list. The default preference domain for system daemons (that is, for daemons running in the root session) is the system domain. The default preference domain for all other programs is the user domain. Use the [SecKeychainSetPreferenceDomain](<seckeychainsetpreferencedomain(__).md>) function to change the preference domain.
