---
title: 'CGPDFObjectGetType(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfobjectgettype(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfobjectgettype(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfobjectgettype%28_%3A%29.json'
content_hash: 'sha256:40c7c13b7c45c5dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFObjectGetType(_:)

<sub>Function</sub>

Returns the PDF type identifier of an object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFObjectGetType(_ object: CGPDFObjectRef) -> CGPDFObjectType
```

## Parameters

- `object` — A PDF object. If the value if not a PDF object, the behavior is unspecified.

## Return Value

Returns the type of the `object` parameter. See [Abstract Types for PDF Document Content](cgpdfdocument.md#Abstract-Types-for-PDF-Document-Content).

## See Also

### Getting Object Types and Values

- [CGPDFObjectGetValue](<cgpdfobjectgetvalue(______).md>) — Returns whether an object is of a given type and if it is, retrieves its value.
