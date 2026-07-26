---
title: 'SecTrustedApplicationCopyData(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectrustedapplicationcopydata(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustedapplicationcopydata(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustedapplicationcopydata%28_%3A_%3A%29.json'
content_hash: 'sha256:ba8d9e3e1cf7bb26'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustedApplicationCopyData(_:_:)

<sub>Function</sub>

Retrieves the data of a trusted app instance.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecTrustedApplicationCopyData(_ appRef: SecTrustedApplication, _ data: UnsafeMutablePointer<CFData?>) -> OSStatus
```

## Parameters

- `appRef` — A trusted app from which to retrieve data. Use the [SecTrustedApplicationCreateFromPath](<sectrustedapplicationcreatefrompath(____).md>) method to create a trusted app instance.

- `data` — On return, points to an opaque data instance. Call the [CFRelease](../corefoundation/cfrelease.md) method to release the data when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The trusted app instance created by the [SecTrustedApplicationCreateFromPath](<sectrustedapplicationcreatefrompath(____).md>) method includes data that uniquely identifies the app, such as a cryptographic hash of the app. The operating system uses this data to verify that the app is unaltered since the trusted app instance was created. When an app requests access to an item in the keychain for which it is designated as a trusted app, the operating system checks this data before granting access.

Use the [SecTrustedApplicationCopyData](<sectrustedapplicationcopydata(____).md>) function to extract this data from the trusted app instance for storage or for transmission over the network. Use the [SecTrustedApplicationSetData](<sectrustedapplicationsetdata(____).md>) function to insert that data back into a trusted app instance. Note that this data is opaque: there’s no way to interpret it.
