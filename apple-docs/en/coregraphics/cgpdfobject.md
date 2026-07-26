---
title: CGPDFObject
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfobject
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfobject.json'
content_hash: 'sha256:bfb772227a098e02'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFObject

<sub>API Collection</sub>

An object representing content within a PDF document.

## Overview

PDF supports several basic types of object: Boolean values, integer and real numbers, strings, names, arrays, dictionaries, and streams. Most of these are represented in Core Graphics by corresponding specific types. A CGPDFObject can represent any of these types. You use CGPDFObject functions to determine the type of the object, and retrieve the object value if it is of an expected type.

This object is not derived from CFType and therefore there are no functions for retaining and releasing it. CGPDFObject objects exist as constituent parts of a CGPDFDocument object, and are managed by their container.

## Topics

### Getting Object Types and Values

- [CGPDFObjectGetType](<cgpdfobjectgettype(__).md>) — Returns the PDF type identifier of an object.
- [CGPDFObjectGetValue](<cgpdfobjectgetvalue(______).md>) — Returns whether an object is of a given type and if it is, retrieves its value.

### Data Types

- [CGPDFObjectRef](cgpdfobjectref.md) — A type that contains information about a PDF object.
- [CGPDFBoolean](cgpdfboolean.md) — A PDF Boolean value.
- [CGPDFInteger](cgpdfinteger.md) — A PDF integer value.
- [CGPDFReal](cgpdfreal.md) — A PDF real value.

### Constants

- [CGPDFObjectType](cgpdfobjecttype.md) — Types of PDF object.

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
