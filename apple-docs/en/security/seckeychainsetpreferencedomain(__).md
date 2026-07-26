---
title: 'SecKeychainSetPreferenceDomain(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainsetpreferencedomain(_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainsetpreferencedomain(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainsetpreferencedomain%28_%3A%29.json'
content_hash: 'sha256:732088d74e23412a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainSetPreferenceDomain(_:)

<sub>Function</sub>

Sets the keychain preference domain.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainSetPreferenceDomain(_ domain: SecPreferencesDomain) -> OSStatus
```

## Parameters

- `domain` — The keychain preference domain to set. See [SecPreferencesDomain](secpreferencesdomain.md) for possible domain values.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

A preference domain is a set of security-related preferences, such as the default keychain and the current keychain search list. The default preference domain for system daemons (that is, for daemons running in the root session) is the system domain. The default preference domain for all other programs is the user domain.

This function changes the preference domain for all subsequent function calls; for example, if you change from the system domain to the user domain and then call [SecKeychainLock](<seckeychainlock(__).md>) specifying `NULL` for the keychain, the function locks the default system keychain rather than the default user keychain. You might want to use this function, for example, when launching a system daemon from a user session so that the daemon uses system preferences rather than user preferences.
