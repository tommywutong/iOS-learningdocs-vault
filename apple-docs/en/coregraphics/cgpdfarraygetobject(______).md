---
title: 'CGPDFArrayGetObject(_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfarraygetobject(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfarraygetobject(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfarraygetobject%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:19c7137e5df2cd88'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFArrayGetObject(_:_:_:)

<sub>Function</sub>

Returns whether an object at a given index in a PDF array is a PDF object and, if so, retrieves that object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFArrayGetObject(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFObjectRef?>?) -> Bool
```

## Parameters

- `array` — A PDF array. If this parameter is not a valid PDF array, the behavior is undefined.

- `index` — The index of the value to retrieve. If the index is outside the index space of the array (`0` to `N-1`, where `N` is the count of the array), the behavior is undefined.

- `value` — On input, a pointer to a PDF object. If the value at the specified index is a PDF object, then on return contains that object, otherwise the value is undefined.

## Return Value

Returns [true](../swift/true.md) if there is a PDF object at the specified index, otherwise [false](../swift/false.md).

## See Also

### Getting Data from a PDF Array

- [CGPDFArrayGetArray](<cgpdfarraygetarray(______).md>) — Returns whether an object at a given index in a PDF array is another PDF array and, if so, retrieves that array.
- [CGPDFArrayGetBoolean](<cgpdfarraygetboolean(______).md>) — Returns whether an object at a given index in a PDF array is a PDF Boolean and, if so, retrieves that Boolean.
- [CGPDFArrayGetCount](<cgpdfarraygetcount(__).md>) — Returns the number of items in a PDF array.
- [CGPDFArrayGetDictionary](<cgpdfarraygetdictionary(______).md>) — Returns whether an object at a given index in a PDF array is a PDF dictionary and, if so, retrieves that dictionary.
- [CGPDFArrayGetInteger](<cgpdfarraygetinteger(______).md>) — Returns whether an object at a given index in a PDF array is a PDF integer and, if so, retrieves that object.
- [CGPDFArrayGetName](<cgpdfarraygetname(______).md>) — Returns whether an object at a given index in a PDF array is a PDF name reference (represented as a constant C string) and, if so, retrieves that name.
- [CGPDFArrayGetNull](<cgpdfarraygetnull(____).md>) — Returns whether an object at a given index in a Quartz PDF array is a PDF null.
- [CGPDFArrayGetNumber](<cgpdfarraygetnumber(______).md>) — Returns whether an object at a given index in a PDF array is a PDF number and, if so, retrieves that object.
- [CGPDFArrayGetStream](<cgpdfarraygetstream(______).md>) — Returns whether an object at a given index in a PDF array is a PDF stream and, if so, retrieves that stream.
- [CGPDFArrayGetString](<cgpdfarraygetstring(______).md>) — Returns whether an object at a given index in a PDF array is a PDF string and, if so, retrieves that string.
