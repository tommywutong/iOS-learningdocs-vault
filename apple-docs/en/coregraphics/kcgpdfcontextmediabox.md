---
title: kCGPDFContextMediaBox
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgpdfcontextmediabox
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgpdfcontextmediabox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgpdfcontextmediabox.json'
content_hash: 'sha256:d2fbdf40da75f397'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGPDFContextMediaBox

<sub>Global Variable</sub>

The media box for the document or for a given page.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCGPDFContextMediaBox: CFString
```

## Discussion

This key is optional. If present, the value of this key must be a [CFData](../corefoundation/cfdata.md) object that contains a [CGRect](../corefoundation/cgrect.md) (stored by value, not by reference).

## See Also

### Box Keys

- [kCGPDFContextCropBox](kcgpdfcontextcropbox.md) — The crop box for the document or for a given page.
- [kCGPDFContextBleedBox](kcgpdfcontextbleedbox.md) — The bleed box for the document or for a given page.
- [kCGPDFContextTrimBox](kcgpdfcontexttrimbox.md) — The trim box for the document or for a given page.
- [kCGPDFContextArtBox](kcgpdfcontextartbox.md) — The art box for the document or for a given page.
