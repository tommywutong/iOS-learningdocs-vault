---
title: 'init(_:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfdocument/init(_:)-2gtsd'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocument/init(_:)-2gtsd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocument/init%28_%3A%29-2gtsd.json'
content_hash: 'sha256:35f2326fc76234f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPDFDocument](../cgpdfdocument.md)

# init(_:)

<sub>Initializer</sub>

Creates a Core Graphics PDF document using data specified by a URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ url: CFURL)
```

## Parameters

- `url` — The URL address at which the PDF document data is located.

## Return Value

A new Core Graphics PDF document, or `NULL` if a document could not be created. In Objective-C, you’re responsible for releasing the object using [CGPDFDocumentRelease](../cgpdfdocumentrelease.md).

## Discussion

Distributing individual pages of a PDF document to separate threads is not supported. If you want to use threads, consider creating a separate document for each thread and operating on a block of pages per thread.

## See Also

### Creating PDF Documents

- [CGPDFDocumentCreateWithProvider](<init(__)-gbq6.md>) — Creates a Core Graphics PDF document using a data provider.
