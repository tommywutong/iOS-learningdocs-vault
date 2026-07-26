---
title: dictionary
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfpage/dictionary
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfpage/dictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfpage/dictionary.json'
content_hash: 'sha256:b7ef7b958c77bc8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPDFPage](../cgpdfpage.md)

# dictionary

<sub>Instance Property</sub>

Returns the dictionary of a PDF page.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dictionary: CGPDFDictionaryRef? { get }
```

## See Also

### Getting Page Information

- [CGPDFPageGetBoxRect](<getboxrect(__).md>) — Returns the rectangle that represents a type of box for a content region or page dimensions of a PDF page.
- [CGPDFPageGetDocument](document.md) — Returns the document for a page.
- [CGPDFPageGetPageNumber](pagenumber.md) — Returns the page number of the specified PDF page.
- [CGPDFPageGetRotationAngle](rotationangle.md) — Returns the rotation angle of a PDF page, in degrees.
- [CGPDFPageGetDrawingTransform](<getdrawingtransform(__rect_rotate_preserveaspectratio_).md>) — Returns the affine transform that maps a box to a given rectangle on a PDF page.
