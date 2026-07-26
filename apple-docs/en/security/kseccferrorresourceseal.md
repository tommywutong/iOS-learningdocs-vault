---
title: kSecCFErrorResourceSeal
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccferrorresourceseal
source_url: 'https://developer.apple.com/documentation/security/kseccferrorresourceseal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccferrorresourceseal.json'
content_hash: 'sha256:67a6181c863047ff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCFErrorResourceSeal

<sub>Global Variable</sub>

A key whose value is a Core Foundation object containing the part of the resource seal that had a problem.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCFErrorResourceSeal: CFString
```

## Discussion

The `CodeResources` file that gets generated as part of the code signing process serves as the bundle’s seal. This file is a CFDictionary that contains a listing of all the files found within your bundle coupled with their respective hash values and a set of rule definitions. The type of object returned depends on which item in the dictionary had a problem. See [macOS Code Signing In Depth](https://developer.apple.com/library/archive/technotes/tn2206/_index.html#//apple_ref/doc/uid/DTS40007919) for more information on the `CodeResources` file.
