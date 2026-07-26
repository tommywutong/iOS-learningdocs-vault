---
title: 'CGPDFStreamGetDictionary(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfstreamgetdictionary(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfstreamgetdictionary(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfstreamgetdictionary%28_%3A%29.json'
content_hash: 'sha256:d86658184cf893ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFStreamGetDictionary(_:)

<sub>Function</sub>

Returns the dictionary associated with a PDF stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFStreamGetDictionary(_ stream: CGPDFStreamRef) -> CGPDFDictionaryRef?
```

## Parameters

- `stream` — A PDF stream.

## Return Value

The PDF dictionary for the specified stream.

## See Also

### Getting Data from a PDF Stream

- [CGPDFStreamCopyData](<cgpdfstreamcopydata(____).md>) — Returns the data associated with a PDF stream.
