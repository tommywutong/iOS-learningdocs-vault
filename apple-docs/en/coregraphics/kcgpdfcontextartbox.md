---
title: kCGPDFContextArtBox
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgpdfcontextartbox
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgpdfcontextartbox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgpdfcontextartbox.json'
content_hash: 'sha256:86b3c190ca84d173'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGPDFContextArtBox

<sub>Global Variable</sub>

The art box for the document or for a given page.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCGPDFContextArtBox: CFString
```

## Discussion

This key is optional. If present, the value of this key must be a [CFData](../corefoundation/cfdata.md) object that contains a [CGRect](../corefoundation/cgrect.md) (stored by value, not by reference).

## See Also

### Box Keys

- [kCGPDFContextMediaBox](kcgpdfcontextmediabox.md) — The media box for the document or for a given page.
- [kCGPDFContextCropBox](kcgpdfcontextcropbox.md) — The crop box for the document or for a given page.
- [kCGPDFContextBleedBox](kcgpdfcontextbleedbox.md) — The bleed box for the document or for a given page.
- [kCGPDFContextTrimBox](kcgpdfcontexttrimbox.md) — The trim box for the document or for a given page.
