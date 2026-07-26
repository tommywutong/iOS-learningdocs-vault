---
title: CGPDFDocumentGetBleedBox
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/coregraphics/cgpdfdocumentgetbleedbox
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocumentgetbleedbox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocumentgetbleedbox.json'
content_hash: 'sha256:b71998ed0fe32a53'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFDocumentGetBleedBox

<sub>Function</sub>

Returns the bleed box of a page in a PDF document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGRect CGPDFDocumentGetBleedBox(CGPDFDocumentRef document, int page);
```

## Parameters

- `document` — The PDF document to examine.

- `page` — An integer that specifies the number of the page to examine.

## Return Value

A rectangle that represents the bleed box for the specified page, expressed in default PDF user space units (points).

## Discussion

The replacement function for this one is [CGPDFPageGetBoxRect](<cgpdfpage/getboxrect(__).md>), which gets the rectangle associated with a type of box (art, media, crop, bleed trim) that represents a content region or page dimensions of a PDF page. For more information see [CGPDFPage](cgpdfpage.md).

The bleed box defines the bounds to which the contents of the page should be clipped when output in a production environment. The default value is the page’s crop box.

## See Also

### Getting Page Information

- [CGPDFDocumentGetArtBox](cgpdfdocumentgetartbox.md) — Returns the art box of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetCropBox](cgpdfdocumentgetcropbox.md) — Returns the crop box of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetMediaBox](cgpdfdocumentgetmediabox.md) — Returns the media box of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetRotationAngle](cgpdfdocumentgetrotationangle.md) — Returns the rotation angle of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetTrimBox](cgpdfdocumentgettrimbox.md) — Returns the trim box of a page in a PDF document. _(deprecated)_
