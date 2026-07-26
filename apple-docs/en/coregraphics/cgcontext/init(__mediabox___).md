---
title: 'init(_:mediaBox:_:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/init(_:mediabox:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/init(_:mediabox:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/init%28_%3Amediabox%3A_%3A%29.json'
content_hash: 'sha256:e9ef2e806fc6d1c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# init(_:mediaBox:_:)

<sub>Initializer</sub>

Creates a URL-based PDF graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ url: CFURL, mediaBox: UnsafePointer<CGRect>?, _ auxiliaryInfo: CFDictionary?)
```

## Parameters

- `url` — A Core Foundation URL that specifies where you want to place the resulting PDF file.

- `mediaBox` — A rectangle that specifies the bounds of the PDF. The origin of the rectangle should typically be `(0,0)`. The `CGPDFContextCreateWithURL` function uses this rectangle as the default page media bounding box. If you pass `NULL`, `CGPDFContextCreateWithURL` uses a default page size of 8.5 by 11 inches (612 by 792 points).

- `auxiliaryInfo` — A dictionary that specifies any additional information to be used by the PDF context when generating the PDF file, or `NULL`. The dictionary is retained by the new context, so on return you may safely release it.

## Return Value

A new PDF context, or `NULL` if a context could not be created. In Objective-C, you’re responsible for releasing this object using [CGContextRelease](../cgcontextrelease.md).

## Discussion

When you call this function, Core Graphics creates a PDF drawing environment—that is, a graphics context—to your specifications. When you draw into the resulting context, Core Graphics renders your drawing as a series of PDF drawing commands stored in the specified location.

## See Also

### Creating PDF Graphics Contexts

- [CGPDFContextCreate](<init(consumer_mediabox___).md>) — Creates a PDF graphics context.
- [Auxiliary Dictionary Keys](../auxiliary-dictionary-keys.md) — Keys for the auxiliary info dictionary you specify when creating a PDF context.
