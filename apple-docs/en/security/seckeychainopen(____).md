---
title: 'SecKeychainOpen(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainopen(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainopen(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainopen%28_%3A_%3A%29.json'
content_hash: 'sha256:8a722e16f90a23bb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainOpen(_:_:)

<sub>Function</sub>

Opens a keychain.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainOpen(_ pathName: UnsafePointer<CChar>, _ keychain: UnsafeMutablePointer<SecKeychain?>) -> OSStatus
```

## Parameters

- `pathName` — A constant character string representing the POSIX path to the keychain to open.

- `keychain` — On return, a pointer to the keychain object. You must call the `CFRelease` function to release this object when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Use this function to retrieve a pointer to a keychain object given the path of the keychain. You don’t need to close the keychain, but do release the memory that the pointer occupies when you are finished with it.
