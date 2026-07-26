---
title: CGPDFDocumentGetMediaBox
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/coregraphics/cgpdfdocumentgetmediabox
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocumentgetmediabox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocumentgetmediabox.json'
content_hash: 'sha256:f6008b192ec9d144'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFDocumentGetMediaBox

<sub>Function</sub>

Returns the media box of a page in a PDF document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGRect CGPDFDocumentGetMediaBox(CGPDFDocumentRef document, int page);
```

## Parameters

- `document` — The PDF document to examine.

- `page` — An integer that specifies the number of the page to examine.

## Return Value

A rectangle that represents the media box for the specified page, expressed in default PDF user space units (points).

## Discussion

The replacement function for this one is [CGPDFPageGetBoxRect](<cgpdfpage/getboxrect(__).md>), which gets the rectangle associated with a type of box (art, media, crop, bleed trim) that represents a content region or page dimensions of a PDF page. For more information see [CGPDFPage](cgpdfpage.md).

The media box defines the location and size of the physical medium on which the page is intended to be displayed or printed. For example, if the page size is 8.5 by 11 inches, this function returns the coordinate pairs `(0,0)` and (`612,792)`.

## See Also

### Getting Page Information

- [CGPDFDocumentGetArtBox](cgpdfdocumentgetartbox.md) — Returns the art box of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetBleedBox](cgpdfdocumentgetbleedbox.md) — Returns the bleed box of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetCropBox](cgpdfdocumentgetcropbox.md) — Returns the crop box of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetRotationAngle](cgpdfdocumentgetrotationangle.md) — Returns the rotation angle of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetTrimBox](cgpdfdocumentgettrimbox.md) — Returns the trim box of a page in a PDF document. _(deprecated)_
