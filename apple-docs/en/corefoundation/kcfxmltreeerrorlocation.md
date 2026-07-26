---
title: kCFXMLTreeErrorLocation
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfxmltreeerrorlocation
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfxmltreeerrorlocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfxmltreeerrorlocation.json'
content_hash: 'sha256:d8cef585ba422486'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFXMLTreeErrorLocation

<sub>Global Variable</sub>

Dictionary key whose value is a CFNumber containing the byte location where the error was detected.

<sub>macOS</sub>

```swift
let kCFXMLTreeErrorLocation: CFString!
```

## See Also

### Constants

- [kCFXMLTreeErrorDescription](kcfxmltreeerrordescription.md) — Dictionary key whose value is a CFString containing a readable description of the error.
- [kCFXMLTreeErrorLineNumber](kcfxmltreeerrorlinenumber.md) — Dictionary key whose value is a CFNumber containing the line number where the error was detected. This may not be the line number where the actual XML error is located.
- [kCFXMLTreeErrorStatusCode](kcfxmltreeerrorstatuscode.md) — Dictionary key whose value is a CFNumber containing the error status code. See [CFXMLParser](cfxmlparser.md) for possible status code values.
