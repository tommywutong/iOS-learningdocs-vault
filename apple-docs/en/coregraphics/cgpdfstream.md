---
title: CGPDFStream
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfstream
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfstream.json'
content_hash: 'sha256:ec88be84b688cab7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFStream

<sub>API Collection</sub>

A stream or sequence of data bytes in a PDF document.

## Overview

A PDF stream  consists  of a dictionary that describes a sequence of bytes. Streams typically represent objects with potentially large amounts of data, such as images and page descriptions.

This object is not derived from CFType and therefore there are no functions for retaining and releasing it.

## Topics

### Getting Data from a PDF Stream

- [CGPDFStreamCopyData](<cgpdfstreamcopydata(____).md>) — Returns the data associated with a PDF stream.
- [CGPDFStreamGetDictionary](<cgpdfstreamgetdictionary(__).md>) — Returns the dictionary associated with a PDF stream.

### Data Types

- [CGPDFStreamRef](cgpdfstreamref.md) — A type that represents a PDF stream.

### Constants

- [CGPDFDataFormat](cgpdfdataformat.md) — The encoding format of PDF data.

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
