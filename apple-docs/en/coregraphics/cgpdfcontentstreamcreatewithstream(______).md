---
title: 'CGPDFContentStreamCreateWithStream(_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfcontentstreamcreatewithstream(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfcontentstreamcreatewithstream(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfcontentstreamcreatewithstream%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0e2348de23a507dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFContentStreamCreateWithStream(_:_:_:)

<sub>Function</sub>

Creates a PDF content stream object from an existing PDF content stream object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFContentStreamCreateWithStream(_ stream: CGPDFStreamRef, _ streamResources: CGPDFDictionaryRef, _ parent: CGPDFContentStreamRef) -> CGPDFContentStreamRef
```

## Parameters

- `stream` — The PDF stream you want to create a content stream from.

- `streamResources` — A PDF dictionary that contains the resources associated with the stream you want to retrieve.

- `parent` — The content stream of the page on which `stream` appears. Supply the `parent` parameter when you create a content stream that’s used within a page.

## Return Value

A PDF content stream object created from the `stream` parameter. In Objective-C, you’re responsible for releasing this object by calling the [CGPDFContentStreamRelease](<cgpdfcontentstreamrelease(__).md>) function.

## Discussion

You can use this function to get access to the contents of a form, pattern, Type3 font, or any PDF stream.

## See Also

### Creating a PDF Content Stream Object

- [CGPDFContentStreamCreateWithPage](<cgpdfcontentstreamcreatewithpage(__).md>) — Creates a content stream object from a PDF page object.
