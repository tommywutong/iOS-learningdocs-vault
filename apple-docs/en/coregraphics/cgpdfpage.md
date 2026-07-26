---
title: CGPDFPage
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfpage
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfpage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfpage.json'
content_hash: 'sha256:240bebef18ac191c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFPage

<sub>Class</sub>

A type that represents a page in a PDF document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CGPDFPage
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Getting Page Information

- [CGPDFPageGetBoxRect](<cgpdfpage/getboxrect(__).md>) — Returns the rectangle that represents a type of box for a content region or page dimensions of a PDF page.
- [CGPDFPageGetDictionary](cgpdfpage/dictionary.md) — Returns the dictionary of a PDF page.
- [CGPDFPageGetDocument](cgpdfpage/document.md) — Returns the document for a page.
- [CGPDFPageGetPageNumber](cgpdfpage/pagenumber.md) — Returns the page number of the specified PDF page.
- [CGPDFPageGetRotationAngle](cgpdfpage/rotationangle.md) — Returns the rotation angle of a PDF page, in degrees.
- [CGPDFPageGetDrawingTransform](<cgpdfpage/getdrawingtransform(__rect_rotate_preserveaspectratio_).md>) — Returns the affine transform that maps a box to a given rectangle on a PDF page.

### Working with Core Foundation Types

- [CGPDFPageGetTypeID](cgpdfpage/typeid.md) — Returns the CFType ID for PDF page objects.

### Constants

- [CGPDFBox](cgpdfbox.md) — Box types for a PDF page.

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
