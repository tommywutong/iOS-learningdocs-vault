---
title: 'SecKeychainUnlock(_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainunlock(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainunlock(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainunlock%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:f0f807567231e6f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainUnlock(_:_:_:_:)

<sub>Function</sub>

Unlocks a keychain.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainUnlock(_ keychain: SecKeychain?, _ passwordLength: UInt32, _ password: UnsafeRawPointer?, _ usePassword: Bool) -> OSStatus
```

## Parameters

- `keychain` — A reference to the keychain to unlock. Pass `NULL` to specify the default keychain. If you pass a locked keychain, this function displays the Unlock Keychain dialog box if you have not provided a password. If the specified keychain is currently unlocked, the Unlock Keychain dialog box is not displayed and this function returns `noErr`. You must call the `CFRelease` function to release this object when you are finished using it.

- `passwordLength` — An unsigned 32-bit integer representing the length of the password buffer.

- `password` — A buffer containing the password for the keychain. Pass `NULL` if the user password is unknown. In this case, this function displays the Unlock Keychain dialog to prompt the user for the keychain password.

- `usePassword` — A Boolean value indicating whether the password parameter is used. You should pass `TRUE` if you are passing a password or `FALSE` if it is to be ignored.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). The result code [errSecUserCanceled](errsecusercanceled.md) indicates that the user pressed the Cancel button in the Unlock Keychain dialog box. The result code [errSecAuthFailed](errsecauthfailed.md) indicates that authentication failed because of too many unsuccessful retries. The result code [errSecInteractionRequired](errsecinteractionrequired.md) indicates that user interaction is required to unlock the keychain.

## Discussion

In most cases, your application does not need to call this function directly, since most Keychain Services functions that require an unlocked keychain do so for you. If your application needs to verify that a keychain is unlocked, call the function [SecKeychainGetStatus](<seckeychaingetstatus(____).md>).
