---
title: CGPDFBox.trimBox
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfbox/trimbox
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfbox/trimbox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfbox/trimbox.json'
content_hash: 'sha256:b36c07bd2f192620'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPDFBox](../cgpdfbox.md)

# CGPDFBox.trimBox

<sub>Case</sub>

The page trim box—a rectangle, expressed in default user space units, that defines the intended dimensions of the finished page after trimming.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case trimBox
```

## See Also

### Constants

- [kCGPDFMediaBox](mediabox.md) — The page media box—a rectangle, expressed in default user space units, that defines the boundaries of the physical medium on which the page is intended to be displayed or printed
- [kCGPDFCropBox](cropbox.md) — The page crop box—a rectangle, expressed in default user space units, that defines the visible region of default user space. When the page is displayed or printed, its contents are to be clipped to this rectangle.
- [kCGPDFBleedBox](bleedbox.md) — The page bleed box—a rectangle, expressed in default user space units, that defines the region to which the contents of the page should be clipped when output in a production environment.
- [kCGPDFArtBox](artbox.md) — The page art box—a rectangle, expressed in default user space units, defining the extent of the page’s meaningful content (including potential white space) as intended by the page’s creator.
