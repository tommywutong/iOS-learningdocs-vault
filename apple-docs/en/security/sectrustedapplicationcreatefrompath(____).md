---
title: 'SecTrustedApplicationCreateFromPath(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectrustedapplicationcreatefrompath(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustedapplicationcreatefrompath(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustedapplicationcreatefrompath%28_%3A_%3A%29.json'
content_hash: 'sha256:4caf3f51139897b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustedApplicationCreateFromPath(_:_:)

<sub>Function</sub>

Creates a trusted app instance based on the app at the given path in the file system.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecTrustedApplicationCreateFromPath(_ path: UnsafePointer<CChar>?, _ app: UnsafeMutablePointer<SecTrustedApplication?>) -> OSStatus
```

## Parameters

- `path` — The path to the app to trust. For application bundles, use the path to the bundle directory. Pass `nil` to refer to the calling app.

- `app` — On return, points to the newly created trusted app instance. Call the [CFRelease](../corefoundation/cfrelease.md) method to release this instance when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Use this method to create a trusted app instance, which both identifies an app and provides data that can be used to ensure that the app hasn’t been altered since the instance was created.

You can use the created instance as input to the [SecAccessCreate](<secaccesscreate(______).md>) method, which creates an access instance. The access instance, in turn, is used as input to the [SecKeychainItemSetAccess](<seckeychainitemsetaccess(____).md>) function to specify the set of apps that are trusted to access a specific keychain item.
