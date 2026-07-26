---
title: 'CGPDFStringGetLength(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfstringgetlength(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfstringgetlength(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfstringgetlength%28_%3A%29.json'
content_hash: 'sha256:19205a675b3df9a6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFStringGetLength(_:)

<sub>Function</sub>

Returns the number of bytes in a PDF string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFStringGetLength(_ string: CGPDFStringRef) -> Int
```

## Parameters

- `string` — A PDF string.

## Return Value

Returns the number of bytes referenced by the string, or `0` if the string is `NULL`.

## See Also

### Getting PDF String Data

- [CGPDFStringGetBytePtr](<cgpdfstringgetbyteptr(__).md>) — Returns a pointer to the bytes of a PDF string.
