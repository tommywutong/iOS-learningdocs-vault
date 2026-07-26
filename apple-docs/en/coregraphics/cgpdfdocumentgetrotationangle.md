---
title: CGPDFDocumentGetRotationAngle
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.5 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/coregraphics/cgpdfdocumentgetrotationangle
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocumentgetrotationangle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocumentgetrotationangle.json'
content_hash: 'sha256:d3a7e88ef4046ca4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFDocumentGetRotationAngle

<sub>Function</sub>

Returns the rotation angle of a page in a PDF document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern int CGPDFDocumentGetRotationAngle(CGPDFDocumentRef document, int page);
```

## Parameters

- `document` — The PDF document to examine.

- `page` — An integer that specifies the number of the page to examine.

## Return Value

The rotation angle of the page, expressed in degrees. If the specified page does not exist, returns `0`.

## Discussion

The replacement function for this one is [CGPDFPageGetRotationAngle](cgpdfpage/rotationangle.md). For more information see [CGPDFPage](cgpdfpage.md).

## See Also

### Getting Page Information

- [CGPDFDocumentGetArtBox](cgpdfdocumentgetartbox.md) — Returns the art box of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetBleedBox](cgpdfdocumentgetbleedbox.md) — Returns the bleed box of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetCropBox](cgpdfdocumentgetcropbox.md) — Returns the crop box of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetMediaBox](cgpdfdocumentgetmediabox.md) — Returns the media box of a page in a PDF document. _(deprecated)_
- [CGPDFDocumentGetTrimBox](cgpdfdocumentgettrimbox.md) — Returns the trim box of a page in a PDF document. _(deprecated)_
