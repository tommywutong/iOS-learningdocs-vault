---
title: CGPDFBox
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfbox
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfbox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfbox.json'
content_hash: 'sha256:35c0b276a6c151e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFBox

<sub>Enumeration</sub>

Box types for a PDF page.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CGPDFBox
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGPDFMediaBox](cgpdfbox/mediabox.md) — The page media box—a rectangle, expressed in default user space units, that defines the boundaries of the physical medium on which the page is intended to be displayed or printed
- [kCGPDFCropBox](cgpdfbox/cropbox.md) — The page crop box—a rectangle, expressed in default user space units, that defines the visible region of default user space. When the page is displayed or printed, its contents are to be clipped to this rectangle.
- [kCGPDFBleedBox](cgpdfbox/bleedbox.md) — The page bleed box—a rectangle, expressed in default user space units, that defines the region to which the contents of the page should be clipped when output in a production environment.
- [kCGPDFTrimBox](cgpdfbox/trimbox.md) — The page trim box—a rectangle, expressed in default user space units, that defines the intended dimensions of the finished page after trimming.
- [kCGPDFArtBox](cgpdfbox/artbox.md) — The page art box—a rectangle, expressed in default user space units, defining the extent of the page’s meaningful content (including potential white space) as intended by the page’s creator.

### Initializers

- [init(rawValue:)](<cgpdfbox/init(rawvalue_).md>)
