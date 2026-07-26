---
title: 'CGPDFContentStreamGetStreams(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfcontentstreamgetstreams(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfcontentstreamgetstreams(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfcontentstreamgetstreams%28_%3A%29.json'
content_hash: 'sha256:7e8ade9aa52b36f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFContentStreamGetStreams(_:)

<sub>Function</sub>

Gets the array of PDF content streams contained in a PDF content stream object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFContentStreamGetStreams(_ cs: CGPDFContentStreamRef) -> CFArray?
```

## Parameters

- `cs` — A PDF content stream object.

## Return Value

The array of PDF content streams that make up the content stream object represented by the `cs` parameter.

## See Also

### Getting Data from a PDF Content Stream Object

- [CGPDFContentStreamGetResource](<cgpdfcontentstreamgetresource(______).md>) — Gets the specified resource from a PDF content stream object.
