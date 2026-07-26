---
title: 'SecKeychainGetVersion(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychaingetversion(_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychaingetversion(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaingetversion%28_%3A%29.json'
content_hash: 'sha256:f1f853e406ec4d6e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainGetVersion(_:)

<sub>Function</sub>

Determines the version of keychain services installed on the user’s system.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainGetVersion(_ returnVers: UnsafeMutablePointer<UInt32>) -> OSStatus
```

## Parameters

- `returnVers` — On return, a pointer to the version number of keychain services installed on the current system. See `Keychain Settings Version` for a list of values.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Your application can call the [SecKeychainGetVersion](<seckeychaingetversion(__).md>) function to find out which version of keychain services is installed on the user’s system.
