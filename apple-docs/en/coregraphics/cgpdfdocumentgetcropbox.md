---
title: CGPDFDocumentGetCropBox
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/coregraphics/cgpdfdocumentgetcropbox
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocumentgetcropbox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocumentgetcropbox.json'
content_hash: 'sha256:b876c399d13178df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFDocumentGetCropBox

<sub>Function</sub>

Returns the crop box of a page in a PDF document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGRect CGPDFDocumentGetCropBox(CGPDFDocumentRef document, int page);
```

## Parameters

- `document` — The PDF document to examine.

- `page` — An integer that specifies the number of the page to examine.

## Return Value

A rectangle that represents the crop box for the specified page, expressed in default PDF user space units (points).

## Discussion

The replacement function for this one is [CGPDFPageGetBoxRect](<cgpdfpage/getboxrect(__).md>), which gets the rectangle associated with a type of box (art, media, crop, bleed trim) that represents a content region or page dimensions of a PDF page. For more information see [CGPDFPage](cgpdfpage.md).

The crop box defines the region to which the contents of the page are to be clipped (or cropped) when displayed or printed. Unlike the other boxes, the crop box has no defined meaning in terms of physical page geometry or intended use—it merely suggests where the page should be clipped.

## See Also

### Getting Page Information

- [CGPDFDocumentGetArtBox](cgpdfdocumentgetartbox.md) — Returns the art box of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetBleedBox](cgpdfdocumentgetbleedbox.md) — Returns the bleed box of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetMediaBox](cgpdfdocumentgetmediabox.md) — Returns the media box of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetRotationAngle](cgpdfdocumentgetrotationangle.md) — Returns the rotation angle of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetTrimBox](cgpdfdocumentgettrimbox.md) — Returns the trim box of a page in a PDF document. _(deprecated)_
