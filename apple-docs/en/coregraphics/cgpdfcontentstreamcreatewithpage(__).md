---
title: 'CGPDFContentStreamCreateWithPage(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfcontentstreamcreatewithpage(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfcontentstreamcreatewithpage(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfcontentstreamcreatewithpage%28_%3A%29.json'
content_hash: 'sha256:229af686f30a1a45'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFContentStreamCreateWithPage(_:)

<sub>Function</sub>

Creates a content stream object from a PDF page object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFContentStreamCreateWithPage(_ page: CGPDFPage) -> CGPDFContentStreamRef
```

## Parameters

- `page` — A PDF page object.

## Return Value

A new [CGPDFContentStreamRef](cgpdfcontentstreamref.md) object. In Objective-C, you’re responsible for releasing this object by calling the [CGPDFContentStreamRelease](<cgpdfcontentstreamrelease(__).md>) function.

## Discussion

A [CGPDFContentStreamRef](cgpdfcontentstreamref.md) object can contain more than one PDF content stream. To retrieve an array of the PDF content streams in the object, call the function [CGPDFContentStreamGetStreams](<cgpdfcontentstreamgetstreams(__).md>). To obtain the resources associated with a [CGPDFContentStreamRef](cgpdfcontentstreamref.md) object, call the function [CGPDFContentStreamGetResource](<cgpdfcontentstreamgetresource(______).md>).

## See Also

### Creating a PDF Content Stream Object

- [CGPDFContentStreamCreateWithStream](<cgpdfcontentstreamcreatewithstream(______).md>) — Creates a PDF content stream object from an existing PDF content stream object.
