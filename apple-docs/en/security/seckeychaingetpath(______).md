---
title: 'SecKeychainGetPath(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychaingetpath(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychaingetpath(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaingetpath%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:5675df8438b78ab5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainGetPath(_:_:_:)

<sub>Function</sub>

Determines the path of a keychain.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainGetPath(_ keychain: SecKeychain?, _ ioPathLength: UnsafeMutablePointer<UInt32>, _ pathName: UnsafeMutablePointer<CChar>) -> OSStatus
```

## Parameters

- `keychain` — A reference to a keychain whose path you wish to obtain.

- `ioPathLength` — On entry, a pointer to a variable containing the length (in bytes) of the buffer specified by `pathName`. On return, the string length of `pathName`, not including the null termination.

- `pathName` — On entry, a pointer to a buffer that you have allocated. On return, the buffer contains POSIX path of the keychain as a null-terminated UTF-8 encoded string. The function returns [errSecBufferTooSmall](errsecbuffertoosmall.md) if the provided buffer is too small to hold the string with the null terminator byte.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
