---
title: 'CGPDFStreamCopyData(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfstreamcopydata(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfstreamcopydata(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfstreamcopydata%28_%3A_%3A%29.json'
content_hash: 'sha256:aeadfb428b74fabf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFStreamCopyData(_:_:)

<sub>Function</sub>

Returns the data associated with a PDF stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFStreamCopyData(_ stream: CGPDFStreamRef, _ format: UnsafeMutablePointer<CGPDFDataFormat>) -> CFData?
```

## Parameters

- `stream` — A PDF stream.

- `format` — On return, contains a constant that specifies the format of the data returned—[CGPDFDataFormatRaw](cgpdfdataformat/raw.md), [CGPDFDataFormatJPEGEncoded](cgpdfdataformat/jpegencoded.md), or [CGPDFDataFormatJPEG2000](cgpdfdataformat/jpeg2000.md).

## Return Value

A CFData object that contains a copy of the stream data. You are responsible for releasing this object.

## See Also

### Getting Data from a PDF Stream

- [CGPDFStreamGetDictionary](<cgpdfstreamgetdictionary(__).md>) — Returns the dictionary associated with a PDF stream.
