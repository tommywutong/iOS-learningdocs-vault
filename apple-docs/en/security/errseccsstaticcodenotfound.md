---
title: errSecCSStaticCodeNotFound
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/errseccsstaticcodenotfound
source_url: 'https://developer.apple.com/documentation/security/errseccsstaticcodenotfound'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/errseccsstaticcodenotfound.json'
content_hash: 'sha256:096543fddad30c09'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# errSecCSStaticCodeNotFound

<sub>Global Variable</sub>

Cannot find code object on disk.

<sub>Mac Catalyst, macOS</sub>

```swift
var errSecCSStaticCodeNotFound: OSStatus { get }
```

## Discussion

You can get this error if you specify a location on disk and the system can’t find the code at that location or if the system is checking the validity of running code and it can’t find the code on disk that was the source for the code in memory.
