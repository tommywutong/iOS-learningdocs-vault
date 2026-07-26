---
title: CGPDFString
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfstring
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfstring.json'
content_hash: 'sha256:8a29eb13ab182cba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFString

<sub>API Collection</sub>

A text string in a PDF document.

## Overview

A PDF string object is a series of bytes—unsigned integer values in the range 0 to 255.

The string elements are not integer objects, but are stored in a more compact format. For more information on the representation of strings in PDF, see the latest version of _PDF Reference_, Adobe Systems Incorporated.

This object is not derived from CFType and therefore there are no functions for retaining and releasing it. CGPDFString objects exist as constituent parts of a CGPDFDocument object, and are managed by their container.

## Topics

### Converting PDF Strings

- [CGPDFStringCopyTextString](<cgpdfstringcopytextstring(__).md>) — Returns a CFString object that represents a PDF string as a text string.
- [CGPDFStringCopyDate](<cgpdfstringcopydate(__).md>) — Converts a string to a date.

### Getting PDF String Data

- [CGPDFStringGetBytePtr](<cgpdfstringgetbyteptr(__).md>) — Returns a pointer to the bytes of a PDF string.
- [CGPDFStringGetLength](<cgpdfstringgetlength(__).md>) — Returns the number of bytes in a PDF string.

### Data Types

- [CGPDFStringRef](cgpdfstringref.md) — A data type that represents a string in a PDF document.

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
