---
title: kCFXMLTreeErrorStatusCode
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfxmltreeerrorstatuscode
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfxmltreeerrorstatuscode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfxmltreeerrorstatuscode.json'
content_hash: 'sha256:6b71122e2b309596'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFXMLTreeErrorStatusCode

<sub>Global Variable</sub>

Dictionary key whose value is a CFNumber containing the error status code. See [CFXMLParser](cfxmlparser.md) for possible status code values.

<sub>macOS</sub>

```swift
let kCFXMLTreeErrorStatusCode: CFString!
```

## See Also

### Constants

- [kCFXMLTreeErrorDescription](kcfxmltreeerrordescription.md) — Dictionary key whose value is a CFString containing a readable description of the error.
- [kCFXMLTreeErrorLineNumber](kcfxmltreeerrorlinenumber.md) — Dictionary key whose value is a CFNumber containing the line number where the error was detected. This may not be the line number where the actual XML error is located.
- [kCFXMLTreeErrorLocation](kcfxmltreeerrorlocation.md) — Dictionary key whose value is a CFNumber containing the byte location where the error was detected.
