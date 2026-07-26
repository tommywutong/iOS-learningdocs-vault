---
title: kSecCodeInfoMainExecutable
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfomainexecutable
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfomainexecutable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfomainexecutable.json'
content_hash: 'sha256:4b7bf12b05c4274b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoMainExecutable

<sub>Global Variable</sub>

A key whose value is a URL locating the main executable file of the code.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoMainExecutable: CFString
```

## Discussion

The value is a [CFURL](../corefoundation/cfurl.md) object. For single files, the URL locates the file itself. For bundles, it locates the main executable as identified by the bundle’s `Info.plist` file.

This is generic information returned regardless of which [Code Signing Information Flags](code-signing-information-flags.md) you pass to the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) function.
