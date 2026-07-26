---
title: 'CGPDFContentStreamGetResource(_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfcontentstreamgetresource(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfcontentstreamgetresource(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfcontentstreamgetresource%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:dbae0964bf4237df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFContentStreamGetResource(_:_:_:)

<sub>Function</sub>

Gets the specified resource from a PDF content stream object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFContentStreamGetResource(_ cs: CGPDFContentStreamRef, _ category: UnsafePointer<CChar>, _ name: UnsafePointer<CChar>) -> CGPDFObjectRef?
```

## Parameters

- `cs` — A PDF content stream object.

- `category` — A string that specifies the category of the resource you want to obtain.

- `name` — A string that specifies the name of the resource you want to obtain.

## Return Value

The resource dictionary.

## Discussion

You can use this function to obtain resources used by the content stream, such as forms, patterns, color spaces, and fonts.

## See Also

### Getting Data from a PDF Content Stream Object

- [CGPDFContentStreamGetStreams](<cgpdfcontentstreamgetstreams(__).md>) — Gets the array of PDF content streams contained in a PDF content stream object.
