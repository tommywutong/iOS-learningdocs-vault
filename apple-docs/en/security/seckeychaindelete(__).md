---
title: 'SecKeychainDelete(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychaindelete(_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychaindelete(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaindelete%28_%3A%29.json'
content_hash: 'sha256:48326114c6a2be17'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainDelete(_:)

<sub>Function</sub>

Deletes one or more keychains from the default keychain search list, and removes the keychain itself if it is a file.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainDelete(_ keychainOrArray: SecKeychain?) -> OSStatus
```

## Parameters

- `keychainOrArray` — A single keychain object or a reference to an array of keychains you wish to delete. To delete more than one keychain, create a `CFArray` of keychain references (type `SecKeychainRef`) and pass a reference to the array. In macOS 10.3 and later, passing `NULL` to this parameter returns an `errSecInvalidKeychain` error code. In OS X 10.2, this parameter was named `keychain` and only took a single keychain object. Passing `NULL` to this parameter deleted the user’s default keychain.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). The result code [errSecInvalidKeychain](errsecinvalidkeychain.md) is returned if the specified keychain is invalid or if the value of the `keychainOrArray` parameter is invalid or `NULL`.

## Discussion

The keychain may be a file stored locally, a smart card, or retrieved from a network server using non-file-based database protocols. This function deletes the keychain only if it is a local file.

This function does not release the memory used by the keychain object. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release each keychain object when you are finished with it.
