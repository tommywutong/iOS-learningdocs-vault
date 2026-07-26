---
title: CGPDFBox.mediaBox
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfbox/mediabox
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfbox/mediabox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfbox/mediabox.json'
content_hash: 'sha256:1013b27f33953659'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPDFBox](../cgpdfbox.md)

# CGPDFBox.mediaBox

<sub>Case</sub>

The page media box—a rectangle, expressed in default user space units, that defines the boundaries of the physical medium on which the page is intended to be displayed or printed

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case mediaBox
```

## See Also

### Constants

- [kCGPDFCropBox](cropbox.md) — The page crop box—a rectangle, expressed in default user space units, that defines the visible region of default user space. When the page is displayed or printed, its contents are to be clipped to this rectangle.
- [kCGPDFBleedBox](bleedbox.md) — The page bleed box—a rectangle, expressed in default user space units, that defines the region to which the contents of the page should be clipped when output in a production environment.
- [kCGPDFTrimBox](trimbox.md) — The page trim box—a rectangle, expressed in default user space units, that defines the intended dimensions of the finished page after trimming.
- [kCGPDFArtBox](artbox.md) — The page art box—a rectangle, expressed in default user space units, defining the extent of the page’s meaningful content (including potential white space) as intended by the page’s creator.
