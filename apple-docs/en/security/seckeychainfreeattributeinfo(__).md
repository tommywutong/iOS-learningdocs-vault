---
title: 'SecKeychainFreeAttributeInfo(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainfreeattributeinfo(_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainfreeattributeinfo(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainfreeattributeinfo%28_%3A%29.json'
content_hash: 'sha256:b4d3e1071646040d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainFreeAttributeInfo(_:)

<sub>Function</sub>

Releases the memory acquired by calling the `SecKeychainAttributeInfoForItemID` function.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainFreeAttributeInfo(_ info: UnsafeMutablePointer<SecKeychainAttributeInfo>) -> OSStatus
```

## Parameters

- `info` — A pointer to the keychain attribute information to release.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
