---
title: 'CGPDFStringCopyTextString(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfstringcopytextstring(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfstringcopytextstring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfstringcopytextstring%28_%3A%29.json'
content_hash: 'sha256:3cbbc71b150e684a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFStringCopyTextString(_:)

<sub>Function</sub>

Returns a CFString object that represents a PDF string as a text string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFStringCopyTextString(_ string: CGPDFStringRef) -> CFString?
```

## Parameters

- `string` — A PDF string. If this value is `NULL`, it will cause an error.

## Return Value

Returns a CFString object that represents the specified PDF string as a text string. You are responsible for releasing this object.

## See Also

### Converting PDF Strings

- [CGPDFStringCopyDate](<cgpdfstringcopydate(__).md>) — Converts a string to a date.
