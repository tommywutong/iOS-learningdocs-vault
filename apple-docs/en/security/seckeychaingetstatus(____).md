---
title: 'SecKeychainGetStatus(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychaingetstatus(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychaingetstatus(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaingetstatus%28_%3A_%3A%29.json'
content_hash: 'sha256:a4accbfd0c43cdab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainGetStatus(_:_:)

<sub>Function</sub>

Retrieves status information of a keychain.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainGetStatus(_ keychain: SecKeychain?, _ keychainStatus: UnsafeMutablePointer<SecKeychainStatus>) -> OSStatus
```

## Parameters

- `keychain` — A keychain object of the keychain whose status you wish to determine for the user session. Pass `NULL` to obtain the status of the default keychain.

- `keychainStatus` — On return, a pointer to the status of the specified keychain. See [SecKeychainStatus](seckeychainstatus.md) for valid status constants.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). The result code [errSecNoSuchKeychain](errsecnosuchkeychain.md) indicates that the specified keychain could not be found. The result code [errSecInvalidKeychain](errsecinvalidkeychain.md) indicates that the specified keychain is invalid.

## Discussion

This function retrieves the status of a specified keychain. You can use this function to determine if the keychain is unlocked, readable, or writable. Note that the lock status of a keychain can change at any time due to user or system activity. Because the system automatically prompts the user to unlock a keychain when necessary, you do not usually have to worry about the lock status of a keychain. If you do need to track the lock status of a keychain, use the [SecKeychainAddCallback](<seckeychainaddcallback(______).md>) function to register for keychain notifications.
