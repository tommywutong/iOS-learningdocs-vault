---
title: 'CGPDFStringGetBytePtr(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfstringgetbyteptr(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfstringgetbyteptr(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfstringgetbyteptr%28_%3A%29.json'
content_hash: 'sha256:9249e1d9afca49be'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFStringGetBytePtr(_:)

<sub>Function</sub>

Returns a pointer to the bytes of a PDF string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFStringGetBytePtr(_ string: CGPDFStringRef) -> UnsafePointer<UInt8>?
```

## Parameters

- `string` — A PDF string.

## Return Value

Returns a pointer to the bytes of the specified string. If the string is `NULL`, the function returns `NULL`.

## See Also

### Getting PDF String Data

- [CGPDFStringGetLength](<cgpdfstringgetlength(__).md>) — Returns the number of bytes in a PDF string.
