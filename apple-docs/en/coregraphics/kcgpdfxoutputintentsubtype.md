---
title: kCGPDFXOutputIntentSubtype
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.4+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgpdfxoutputintentsubtype
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgpdfxoutputintentsubtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgpdfxoutputintentsubtype.json'
content_hash: 'sha256:3147c49a280602e3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGPDFXOutputIntentSubtype

<sub>Global Variable</sub>

The output intent subtype. This key is required.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCGPDFXOutputIntentSubtype: CFString
```

## Discussion

The value of this key must be a [CFString](../corefoundation/cfstring.md) object equal to `"GTS_PDFX"`; otherwise, the dictionary is ignored.

## See Also

### Output Intent Keys

- [kCGPDFXOutputConditionIdentifier](kcgpdfxoutputconditionidentifier.md)
- [kCGPDFXOutputCondition](kcgpdfxoutputcondition.md) — A text string identifying the intended output device or production condition in a human-readable form.
- [kCGPDFXRegistryName](kcgpdfxregistryname.md)
- [kCGPDFXInfo](kcgpdfxinfo.md)
- [kCGPDFXDestinationOutputProfile](kcgpdfxdestinationoutputprofile.md)
