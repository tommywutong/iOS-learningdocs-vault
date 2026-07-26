---
title: kSecCodeInfoPList
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfoplist
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfoplist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfoplist.json'
content_hash: 'sha256:53826448c94aa759'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoPList

<sub>Global Variable</sub>

A key whose value is an information dictionary containing the contents of the secured `Info.plist` file as seen by Code Signing Services.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoPList: CFString
```

## Discussion

The value is a [CFDictionary](../corefoundation/cfdictionary.md) object. Absent if no information property list (`Info.plist`) file is known to Code Signing Services. Note that this is not necessarily the same dictionary as the one that would be returned by a [CFBundle](../corefoundation/cfbundle.md) function such as [CFBundleCopyInfoDictionaryForURL(_:)](<../corefoundation/cfbundlecopyinfodictionaryforurl(__).md>), because [CFBundle](../corefoundation/cfbundle.md) is free to add entries to the information property list).

This is generic information returned regardless of which [Code Signing Information Flags](code-signing-information-flags.md) you pass to the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) function.
