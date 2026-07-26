---
title: kCGPDFXInfo
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.4+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgpdfxinfo
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgpdfxinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgpdfxinfo.json'
content_hash: 'sha256:d776b7032171fcb8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGPDFXInfo

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCGPDFXInfo: CFString
```

## Discussion

A human-readable text string containing additional information or comments about the intended target device or production condition. This key is required if the value of [kCGPDFXOutputConditionIdentifier](kcgpdfxoutputconditionidentifier.md) does not specify a standard production condition. It is optional otherwise. If present, the value of this key must be a [CFString](../corefoundation/cfstring.md) object.

## See Also

### Output Intent Keys

- [kCGPDFXOutputIntentSubtype](kcgpdfxoutputintentsubtype.md) — The output intent subtype. This key is required.
- [kCGPDFXOutputConditionIdentifier](kcgpdfxoutputconditionidentifier.md)
- [kCGPDFXOutputCondition](kcgpdfxoutputcondition.md) — A text string identifying the intended output device or production condition in a human-readable form.
- [kCGPDFXRegistryName](kcgpdfxregistryname.md)
- [kCGPDFXDestinationOutputProfile](kcgpdfxdestinationoutputprofile.md)
