---
title: importOnlyOne
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeyimportexportflags/importonlyone
source_url: 'https://developer.apple.com/documentation/security/seckeyimportexportflags/importonlyone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyimportexportflags/importonlyone.json'
content_hash: 'sha256:630f6765978f0586'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeyImportExportFlags](../seckeyimportexportflags.md)

# importOnlyOne

<sub>Type Property</sub>

A flag that you set to prevent importing more than one private key.

<sub>macOS</sub>

```swift
static var importOnlyOne: SecKeyImportExportFlags { get }
```

## Discussion

Prevents the importing of more than one private key by the [SecKeychainItemImport](../seckeychainitemimport.md) function. If the `importKeychain` parameter is `NULL`, this bit is ignored. Otherwise, if this bit is set and there is more than one key in the incoming external representation, no items are imported to the specified keychain and the error `errSecMultipleKeys` is returned.
