---
title: 'SecKeychainAddGenericPassword(_:_:_:_:_:_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainaddgenericpassword(_:_:_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainaddgenericpassword(_:_:_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainaddgenericpassword%28_%3A_%3A_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:67e7974a8fe6ca6e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainAddGenericPassword(_:_:_:_:_:_:_:_:)

<sub>Function</sub>

Adds a new generic password to a keychain.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainAddGenericPassword(_ keychain: SecKeychain?, _ serviceNameLength: UInt32, _ serviceName: UnsafePointer<CChar>?, _ accountNameLength: UInt32, _ accountName: UnsafePointer<CChar>?, _ passwordLength: UInt32, _ passwordData: UnsafeRawPointer, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus
```

## Parameters

- `keychain` — A reference to the keychain in which to store a generic password. Pass `NULL` to specify the default keychain.

- `serviceNameLength` — The length of the `serviceName` character string.

- `serviceName` — A UTF-8 encoded character string representing the service name.

- `accountNameLength` — The length of the `accountName` character string.

- `accountName` — A UTF-8 encoded character string representing the account name.

- `passwordLength` — The length of the `passwordData` buffer.

- `passwordData` — A pointer to a buffer containing the password data to be stored in the keychain. Before calling this function, allocate enough memory for the buffer to hold the data you want to store.

- `itemRef` — On return, a pointer to a reference to the new keychain item. Pass `NULL` if you don’t want to obtain this object. You must allocate the memory for this pointer. You must call the `CFRelease` function to release this object when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). The result code [errSecNoDefaultKeychain](errsecnodefaultkeychain.md) indicates that no default keychain could be found. The result code [errSecDuplicateItem](errsecduplicateitem.md) indicates that you tried to add a password that already exists in the keychain. The result code [errSecDataTooLarge](errsecdatatoolarge.md) indicates that you tried to add more data than is allowed for a structure of this type.

## Discussion

This function adds a new generic password to the specified keychain. Required parameters to identify the password are `serviceName` and `accountName`, which are application-defined strings. This function optionally returns a reference to the newly added item.

You can use this function to add passwords for accounts other than the Internet. For example, you might add AppleShare passwords, or passwords for your database or scheduling programs.

This function sets the initial access rights for the new keychain item so that the application creating the item is given trusted access.

This function automatically calls the function [SecKeychainUnlock](<seckeychainunlock(________).md>) to display the Unlock Keychain dialog box if the keychain is currently locked.
