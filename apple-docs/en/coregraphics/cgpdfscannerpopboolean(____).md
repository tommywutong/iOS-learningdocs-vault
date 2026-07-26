---
title: 'CGPDFScannerPopBoolean(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfscannerpopboolean(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfscannerpopboolean(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfscannerpopboolean%28_%3A_%3A%29.json'
content_hash: 'sha256:a65255d44b327e20'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFScannerPopBoolean(_:_:)

<sub>Function</sub>

Retrieves a Boolean object from the scanner stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFScannerPopBoolean(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFBoolean>?) -> Bool
```

## Parameters

- `scanner` — A valid scanner object.

- `value` — On output, points to the PDF Boolean object popped from the scanner stack.

## Return Value

[true](../swift/true.md) if the boolean object is retrieved successfully; otherwise, [false](../swift/false.md).

## See Also

### Getting PDF Objects from the Scanner Stack

- [CGPDFScannerPopObject](<cgpdfscannerpopobject(____).md>) — Retrieves an object from the scanner stack.
- [CGPDFScannerPopInteger](<cgpdfscannerpopinteger(____).md>) — Retrieves an integer object from the scanner stack.
- [CGPDFScannerPopNumber](<cgpdfscannerpopnumber(____).md>) — Retrieves a real value object from the scanner stack.
- [CGPDFScannerPopName](<cgpdfscannerpopname(____).md>) — Retrieves a character string from the scanner stack.
- [CGPDFScannerPopString](<cgpdfscannerpopstring(____).md>) — Retrieves a string object from the scanner stack.
- [CGPDFScannerPopArray](<cgpdfscannerpoparray(____).md>) — Retrieves an array object from the scanner stack.
- [CGPDFScannerPopDictionary](<cgpdfscannerpopdictionary(____).md>) — Retrieves a PDF dictionary object from the scanner stack.
- [CGPDFScannerPopStream](<cgpdfscannerpopstream(____).md>) — Retrieves a PDF stream object from the scanner stack.
