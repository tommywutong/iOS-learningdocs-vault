---
title: 'SecKeychainCopySettings(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychaincopysettings(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychaincopysettings(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaincopysettings%28_%3A_%3A%29.json'
content_hash: 'sha256:e8fbc5d3b7ee7c95'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainCopySettings(_:_:)

<sub>Function</sub>

Obtains a keychain’s settings.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainCopySettings(_ keychain: SecKeychain?, _ outSettings: UnsafeMutablePointer<SecKeychainSettings>) -> OSStatus
```

## Parameters

- `keychain` — A reference to the keychain from which to copy its settings.

- `outSettings` — On return, a pointer to a keychain settings structure. Since this structure is versioned, you must allocate the memory for it and fill in the version of the structure before passing it to the function.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
