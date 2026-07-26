---
title: kSecCodeInfoChangedFiles
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfochangedfiles
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfochangedfiles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfochangedfiles.json'
content_hash: 'sha256:307fe49058912f09'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoChangedFiles

<sub>Global Variable</sub>

A key whose value is a list of all files in the code that may have been modified by the process of signing it.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoChangedFiles: CFString
```

## Discussion

The value is a [CFArray](../corefoundation/cfarray.md) array of [CFURL](../corefoundation/cfurl.md) objects. Files not in this list have not been touched by the signing operation.

Specify the [kSecCSContentInformation](kseccscontentinformation.md) flag when calling the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) function to get this information.
