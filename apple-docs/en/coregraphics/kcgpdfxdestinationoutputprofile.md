---
title: kCGPDFXDestinationOutputProfile
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.4+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgpdfxdestinationoutputprofile
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgpdfxdestinationoutputprofile'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgpdfxdestinationoutputprofile.json'
content_hash: 'sha256:e688c04dfd75db79'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGPDFXDestinationOutputProfile

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCGPDFXDestinationOutputProfile: CFString
```

## Discussion

An ICC profile stream defining the transformation from the PDF document’s source colors to output device colorants. This key is required if the value of [kCGPDFXOutputConditionIdentifier](kcgpdfxoutputconditionidentifier.md) does not specify a standard production condition. It is optional otherwise. If present, the value of this key must be an ICC-based color space specified as a `CGColorSpace` object.

## See Also

### Output Intent Keys

- [kCGPDFXOutputIntentSubtype](kcgpdfxoutputintentsubtype.md) — The output intent subtype. This key is required.
- [kCGPDFXOutputConditionIdentifier](kcgpdfxoutputconditionidentifier.md)
- [kCGPDFXOutputCondition](kcgpdfxoutputcondition.md) — A text string identifying the intended output device or production condition in a human-readable form.
- [kCGPDFXRegistryName](kcgpdfxregistryname.md)
- [kCGPDFXInfo](kcgpdfxinfo.md)
