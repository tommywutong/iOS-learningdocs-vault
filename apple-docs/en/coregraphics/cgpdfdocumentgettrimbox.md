---
title: CGPDFDocumentGetTrimBox
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/coregraphics/cgpdfdocumentgettrimbox
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocumentgettrimbox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocumentgettrimbox.json'
content_hash: 'sha256:376567eebbc59ec4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFDocumentGetTrimBox

<sub>Function</sub>

Returns the trim box of a page in a PDF document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGRect CGPDFDocumentGetTrimBox(CGPDFDocumentRef document, int page);
```

## Parameters

- `document` — The PDF document to examine.

- `page` — A value specifying the number of the page to examine.

## Return Value

Returns a rectangle that represents the trim box for the specified page, expressed in default PDF user space units (points).

## Discussion

The replacement function for this one is [CGPDFPageGetBoxRect](<cgpdfpage/getboxrect(__).md>), which gets the rectangle associated with a type of box (art, media, crop, bleed trim) that represents a content region or page dimensions of a PDF page. For more information see [CGPDFPage](cgpdfpage.md).

The trim box defines the intended dimensions of the finished page after trimming. It may be smaller than the media box, to allow for production-related content such as printing instructions, cut marks, or color bars. The default value is the page’s crop box.

## See Also

### Getting Page Information

- [CGPDFDocumentGetArtBox](cgpdfdocumentgetartbox.md) — Returns the art box of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetBleedBox](cgpdfdocumentgetbleedbox.md) — Returns the bleed box of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetCropBox](cgpdfdocumentgetcropbox.md) — Returns the crop box of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetMediaBox](cgpdfdocumentgetmediabox.md) — Returns the media box of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetRotationAngle](cgpdfdocumentgetrotationangle.md) — Returns the rotation angle of a page in a PDF document. _(deprecated)_
