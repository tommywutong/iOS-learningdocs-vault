---
title: kCGPDFXOutputCondition
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.4+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgpdfxoutputcondition
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgpdfxoutputcondition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgpdfxoutputcondition.json'
content_hash: 'sha256:839d845a7fbe5c1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGPDFXOutputCondition

<sub>Global Variable</sub>

A text string identifying the intended output device or production condition in a human-readable form.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCGPDFXOutputCondition: CFString
```

## Discussion

This key is optional. If present, the value of this key must be a [CFString](../corefoundation/cfstring.md) object.

## See Also

### Output Intent Keys

- [kCGPDFXOutputIntentSubtype](kcgpdfxoutputintentsubtype.md) — The output intent subtype. This key is required.
- [kCGPDFXOutputConditionIdentifier](kcgpdfxoutputconditionidentifier.md)
- [kCGPDFXRegistryName](kcgpdfxregistryname.md)
- [kCGPDFXInfo](kcgpdfxinfo.md)
- [kCGPDFXDestinationOutputProfile](kcgpdfxdestinationoutputprofile.md)
