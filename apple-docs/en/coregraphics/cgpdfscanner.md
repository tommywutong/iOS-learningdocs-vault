---
title: CGPDFScanner
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfscanner
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfscanner'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfscanner.json'
content_hash: 'sha256:55217f5e5d169cd6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFScanner

<sub>API Collection</sub>

A parser object for handling content and operators in a PDF content stream.

## Overview

You can set up the PDF scanner object to invoke callbacks when it encounters specific PDF operators in the stream.

This object is not derived from `CFType`. In Objective-C, use [CGPDFScannerRetain](<cgpdfscannerretain(__).md>) and [CGPDFScannerRelease](<cgpdfscannerrelease(__).md>) to manage the retain count of [CGPDFScannerRef](cgpdfscannerref.md) instances; do not use [CFRetain](../corefoundation/cfretain.md) and [CFRelease](../corefoundation/cfrelease.md).

## Topics

### Creating a PDF Scanner Object

- [CGPDFScannerCreate](<cgpdfscannercreate(______).md>) — Creates a PDF scanner.

### Retaining and Releasing PDF Scanner Objects

- [CGPDFScannerRetain](<cgpdfscannerretain(__).md>) — Increments the retain count of a scanner object.
- [CGPDFScannerRelease](<cgpdfscannerrelease(__).md>) — Decrements the retain count of a scanner object.

### Parsing Content

- [CGPDFScannerScan](<cgpdfscannerscan(__).md>) — Parses the content stream of a PDF scanner object.
- [CGPDFScannerGetContentStream](<cgpdfscannergetcontentstream(__).md>) — Returns the content stream associated with a PDF scanner object.

### Getting PDF Objects from the Scanner Stack

- [CGPDFScannerPopObject](<cgpdfscannerpopobject(____).md>) — Retrieves an object from the scanner stack.
- [CGPDFScannerPopBoolean](<cgpdfscannerpopboolean(____).md>) — Retrieves a Boolean object from the scanner stack.
- [CGPDFScannerPopInteger](<cgpdfscannerpopinteger(____).md>) — Retrieves an integer object from the scanner stack.
- [CGPDFScannerPopNumber](<cgpdfscannerpopnumber(____).md>) — Retrieves a real value object from the scanner stack.
- [CGPDFScannerPopName](<cgpdfscannerpopname(____).md>) — Retrieves a character string from the scanner stack.
- [CGPDFScannerPopString](<cgpdfscannerpopstring(____).md>) — Retrieves a string object from the scanner stack.
- [CGPDFScannerPopArray](<cgpdfscannerpoparray(____).md>) — Retrieves an array object from the scanner stack.
- [CGPDFScannerPopDictionary](<cgpdfscannerpopdictionary(____).md>) — Retrieves a PDF dictionary object from the scanner stack.
- [CGPDFScannerPopStream](<cgpdfscannerpopstream(____).md>) — Retrieves a PDF stream object from the scanner stack.

### Data Types

- [CGPDFScannerRef](cgpdfscannerref.md) — A type used to parse a PDF content stream.

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
