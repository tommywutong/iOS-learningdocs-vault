---
title: kCGPDFXOutputConditionIdentifier
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.4+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgpdfxoutputconditionidentifier
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgpdfxoutputconditionidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgpdfxoutputconditionidentifier.json'
content_hash: 'sha256:6b86e85e81f0b26f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGPDFXOutputConditionIdentifier

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCGPDFXOutputConditionIdentifier: CFString
```

## Discussion

A string identifying the intended output device or production condition in a human- or machine-readable form. This key is required. The value of this key must be a [CFString](../corefoundation/cfstring.md) object. For best results, the string should be restricted to characters in the ASCII character set.

## See Also

### Output Intent Keys

- [kCGPDFXOutputIntentSubtype](kcgpdfxoutputintentsubtype.md) — The output intent subtype. This key is required.
- [kCGPDFXOutputCondition](kcgpdfxoutputcondition.md) — A text string identifying the intended output device or production condition in a human-readable form.
- [kCGPDFXRegistryName](kcgpdfxregistryname.md)
- [kCGPDFXInfo](kcgpdfxinfo.md)
- [kCGPDFXDestinationOutputProfile](kcgpdfxdestinationoutputprofile.md)
