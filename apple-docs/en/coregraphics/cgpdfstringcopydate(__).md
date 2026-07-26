---
title: 'CGPDFStringCopyDate(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfstringcopydate(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfstringcopydate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfstringcopydate%28_%3A%29.json'
content_hash: 'sha256:593e188c0435e61a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFStringCopyDate(_:)

<sub>Function</sub>

Converts a string to a date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFStringCopyDate(_ string: CGPDFStringRef) -> CFDate?
```

## Parameters

- `string` — The string to convert to a date.

## Return Value

A CFDate object.

## Discussion

The PDF specification defines a specific format for strings that represent dates. This function converts strings in that form to CFDate objects.

## See Also

### Converting PDF Strings

- [CGPDFStringCopyTextString](<cgpdfstringcopytextstring(__).md>) — Returns a CFString object that represents a PDF string as a text string.
