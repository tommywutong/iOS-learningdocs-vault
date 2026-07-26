---
title: kCFXMLTreeErrorLineNumber
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfxmltreeerrorlinenumber
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfxmltreeerrorlinenumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfxmltreeerrorlinenumber.json'
content_hash: 'sha256:1900d8be8128ce12'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFXMLTreeErrorLineNumber

<sub>Global Variable</sub>

Dictionary key whose value is a CFNumber containing the line number where the error was detected. This may not be the line number where the actual XML error is located.

<sub>macOS</sub>

```swift
let kCFXMLTreeErrorLineNumber: CFString!
```

## See Also

### Constants

- [kCFXMLTreeErrorDescription](kcfxmltreeerrordescription.md) — Dictionary key whose value is a CFString containing a readable description of the error.
- [kCFXMLTreeErrorLocation](kcfxmltreeerrorlocation.md) — Dictionary key whose value is a CFNumber containing the byte location where the error was detected.
- [kCFXMLTreeErrorStatusCode](kcfxmltreeerrorstatuscode.md) — Dictionary key whose value is a CFNumber containing the error status code. See [CFXMLParser](cfxmlparser.md) for possible status code values.
