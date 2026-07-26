---
title: kCGPDFXRegistryName
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.4+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgpdfxregistryname
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgpdfxregistryname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgpdfxregistryname.json'
content_hash: 'sha256:510fae969c3dbe12'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGPDFXRegistryName

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCGPDFXRegistryName: CFString
```

## Discussion

A string identifying the registry in which the condition designated by [kCGPDFXOutputConditionIdentifier](kcgpdfxoutputconditionidentifier.md) is defined. This key is optional. If present, the value of this key must be a [CFString](../corefoundation/cfstring.md) object. For best results, the string should be lossless in ASCII encoding.

## See Also

### Output Intent Keys

- [kCGPDFXOutputIntentSubtype](kcgpdfxoutputintentsubtype.md) — The output intent subtype. This key is required.
- [kCGPDFXOutputConditionIdentifier](kcgpdfxoutputconditionidentifier.md)
- [kCGPDFXOutputCondition](kcgpdfxoutputcondition.md) — A text string identifying the intended output device or production condition in a human-readable form.
- [kCGPDFXInfo](kcgpdfxinfo.md)
- [kCGPDFXDestinationOutputProfile](kcgpdfxdestinationoutputprofile.md)
