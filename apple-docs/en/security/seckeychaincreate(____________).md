---
title: 'SecKeychainCreate(_:_:_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychaincreate(_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychaincreate(_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychaincreate%28_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:38e772b1f764be69'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainCreate(_:_:_:_:_:_:)

<sub>Function</sub>

Creates an empty keychain.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainCreate(_ pathName: UnsafePointer<CChar>, _ passwordLength: UInt32, _ password: UnsafeRawPointer?, _ promptUser: Bool, _ initialAccess: SecAccess?, _ keychain: UnsafeMutablePointer<SecKeychain?>) -> OSStatus
```

## Parameters

- `pathName` — A constant character string representing the POSIX path indicating where to store the keychain.

- `passwordLength` — An unsigned 32-bit integer representing the length of the buffer pointed to by `password`. Pass `0` if the value of `password` is `NULL` and the value of `promptUser` is `TRUE`.

- `password` — A pointer to the buffer containing the password which is used to protect the new keychain. The password must be in canonical UTF-8 encoding. Pass `NULL` if the value of `passwordLength` is `0` and the value of `promptUser` is `TRUE`.

- `promptUser` — A Boolean value representing whether to display a password dialog to the user. Set this value to `TRUE` to display a password dialog or `FALSE` otherwise. If you pass `TRUE`, any values passed for `passwordLength` and `password` are ignored, and a dialog for the user to enter a password is presented.

- `initialAccess` — Ignored. Pass `NULL` for this parameter.

- `keychain` — On return, a pointer to a keychain object. You must call the `CFRelease` function to release this object when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This function creates an empty keychain. The `keychain`, `password`, and `initialAccess` parameters are optional. If user interaction to create a keychain is posted, the newly-created keychain is automatically unlocked after creation.

The system ensures that a default keychain is created for the user at login, thus, in most cases, you do not need to call this function yourself. Users can create additional keychains, or change the default, by using the Keychain Access application. However, a missing default keychain is not recreated automatically, and you may receive an `errSecNoDefaultKeychain` error from other functions if a default keychain does not exist. In that case, you can use this function followed by [SecKeychainSetDefault](<seckeychainsetdefault(__).md>), to create a new default keychain. You can also call this function to create a private temporary keychain for your application’s use, in cases where no user interaction can occur.
