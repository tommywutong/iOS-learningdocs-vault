---
title: kSecCFErrorPattern
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccferrorpattern
source_url: 'https://developer.apple.com/documentation/security/kseccferrorpattern'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccferrorpattern.json'
content_hash: 'sha256:19a2524c7e7a7a2c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCFErrorPattern

<sub>Global Variable</sub>

A key whose value is a string containing a regular expression that’s part of a resource specification that did not parse correctly.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCFErrorPattern: CFString
```

## Discussion

A resource specification is an information property list (`Info.plist` file) that says which files are resources and which are not. This error is returned if any part of the resource specification can’t be parsed.
