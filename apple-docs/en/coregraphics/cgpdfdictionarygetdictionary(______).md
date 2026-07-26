---
title: 'CGPDFDictionaryGetDictionary(_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfdictionarygetdictionary(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdictionarygetdictionary(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdictionarygetdictionary%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:5df6d16fc9e2addc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFDictionaryGetDictionary(_:_:_:)

<sub>Function</sub>

Returns whether there is another PDF dictionary associated with a specified key in a PDF dictionary and, if so, retrieves that dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFDictionaryGetDictionary(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<CChar>, _ value: UnsafeMutablePointer<CGPDFDictionaryRef?>?) -> Bool
```

## Parameters

- `dict` — A PDF dictionary. If this parameter is not a valid PDF dictionary, the behavior is undefined.

- `key` — The key for the value to retrieve.

- `value` — On input, a pointer to a PDF dictionary. If the value associated with the specified key is a PDF dictionary, then on return contains that dictionary; otherwise the value is unspecified.

## Return Value

Returns [true](../swift/true.md) if there is a PDF dictionary associated with the specified key; otherwise, [false](../swift/false.md).

## See Also

### Getting Data from a Dictionary

- [CGPDFDictionaryGetArray](<cgpdfdictionarygetarray(______).md>) — Returns whether there is a PDF array associated with a specified key in a PDF dictionary and, if so, retrieves that array.
- [CGPDFDictionaryGetBoolean](<cgpdfdictionarygetboolean(______).md>) — Returns whether there is a PDF Boolean value associated with a specified key in a PDF dictionary and, if so, retrieves the Boolean value.
- [CGPDFDictionaryGetCount](<cgpdfdictionarygetcount(__).md>) — Returns the number of entries in a PDF dictionary.
- [CGPDFDictionaryGetInteger](<cgpdfdictionarygetinteger(______).md>) — Returns whether there is a PDF integer associated with a specified key in a PDF dictionary and, if so, retrieves that integer.
- [CGPDFDictionaryGetName](<cgpdfdictionarygetname(______).md>) — Returns whether an object with a specified key in a PDF dictionary is a PDF name reference (represented as a constant C string) and, if so, retrieves that name.
- [CGPDFDictionaryGetNumber](<cgpdfdictionarygetnumber(______).md>) — Returns whether there is a PDF number associated with a specified key in a PDF dictionary and, if so, retrieves that number.
- [CGPDFDictionaryGetObject](<cgpdfdictionarygetobject(______).md>) — Returns whether there is a PDF object associated with a specified key in a PDF dictionary and, if so, retrieves that object.
- [CGPDFDictionaryGetStream](<cgpdfdictionarygetstream(______).md>) — Returns whether there is a PDF stream associated with a specified key in a PDF dictionary and, if so, retrieves that stream.
- [CGPDFDictionaryGetString](<cgpdfdictionarygetstring(______).md>) — Returns whether there is a PDF string associated with a specified key in a PDF dictionary and, if so, retrieves that string.
