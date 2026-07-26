---
title: CGPDFArray
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfarray
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfarray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfarray.json'
content_hash: 'sha256:620198f2ddc01930'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFArray

<sub>API Collection</sub>

An array structure within a PDF document.

## Overview

PDF arrays may be heterogeneous—that is, they may contain any other PDF objects, including PDF strings, PDF dictionaries, and other PDF arrays.

Many `CGPDFArray` functions to retrieve values from a PDF array take the form:

```objc
bool CGPDFArrayGet<DataType> (
 CGPDFArrayRef array,
 size_t index,
 <DataType>Ref *value
);
```

These functions test the data type of the object at the specified index. If the object is not of the expected type, the function returns [false](../swift/false.md). If the object is of the expected type, the function returns [true](../swift/true.md), and the object is passed back in the `value` parameter.

This type is not derived from [CFTypeRef](../corefoundation/cftyperef.md) and therefore there are no functions for retaining and releasing it. [CGPDFArrayRef](cgpdfarrayref.md) objects exist only as constituent parts of a [CGPDFDocument](cgpdfdocument.md) object, and they are managed by their container.

## Topics

### Getting Data from a PDF Array

- [CGPDFArrayGetArray](<cgpdfarraygetarray(______).md>) — Returns whether an object at a given index in a PDF array is another PDF array and, if so, retrieves that array.
- [CGPDFArrayGetBoolean](<cgpdfarraygetboolean(______).md>) — Returns whether an object at a given index in a PDF array is a PDF Boolean and, if so, retrieves that Boolean.
- [CGPDFArrayGetCount](<cgpdfarraygetcount(__).md>) — Returns the number of items in a PDF array.
- [CGPDFArrayGetDictionary](<cgpdfarraygetdictionary(______).md>) — Returns whether an object at a given index in a PDF array is a PDF dictionary and, if so, retrieves that dictionary.
- [CGPDFArrayGetInteger](<cgpdfarraygetinteger(______).md>) — Returns whether an object at a given index in a PDF array is a PDF integer and, if so, retrieves that object.
- [CGPDFArrayGetName](<cgpdfarraygetname(______).md>) — Returns whether an object at a given index in a PDF array is a PDF name reference (represented as a constant C string) and, if so, retrieves that name.
- [CGPDFArrayGetNull](<cgpdfarraygetnull(____).md>) — Returns whether an object at a given index in a Quartz PDF array is a PDF null.
- [CGPDFArrayGetNumber](<cgpdfarraygetnumber(______).md>) — Returns whether an object at a given index in a PDF array is a PDF number and, if so, retrieves that object.
- [CGPDFArrayGetObject](<cgpdfarraygetobject(______).md>) — Returns whether an object at a given index in a PDF array is a PDF object and, if so, retrieves that object.
- [CGPDFArrayGetStream](<cgpdfarraygetstream(______).md>) — Returns whether an object at a given index in a PDF array is a PDF stream and, if so, retrieves that stream.
- [CGPDFArrayGetString](<cgpdfarraygetstring(______).md>) — Returns whether an object at a given index in a PDF array is a PDF string and, if so, retrieves that string.

### Data Types

- [CGPDFArrayRef](cgpdfarrayref.md) — An opaque type that encapsulates a PDF array.

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
