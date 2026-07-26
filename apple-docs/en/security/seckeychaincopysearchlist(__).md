---
title: 'SecKeychainCopySearchList(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychaincopysearchlist(_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychaincopysearchlist(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaincopysearchlist%28_%3A%29.json'
content_hash: 'sha256:773e5e3025c1d6b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainCopySearchList(_:)

<sub>Function</sub>

Retrieves a keychain search list.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainCopySearchList(_ searchList: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

## Parameters

- `searchList` — On return, the returned keychain search list. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
