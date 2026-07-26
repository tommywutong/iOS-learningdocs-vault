---
title: 'init(consumer:mediaBox:_:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/init(consumer:mediabox:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/init(consumer:mediabox:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/init%28consumer%3Amediabox%3A_%3A%29.json'
content_hash: 'sha256:fa469db17317ef2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# init(consumer:mediaBox:_:)

<sub>Initializer</sub>

Creates a PDF graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(consumer: CGDataConsumer, mediaBox: UnsafePointer<CGRect>?, _ auxiliaryInfo: CFDictionary?)
```

## Parameters

- `consumer` — The data consumer to receive the PDF output data.

- `mediaBox` — A pointer to a rectangle that defines the size and location of the PDF page, or `NULL`. The origin of the rectangle should typically be `(0,0)`. Core Graphics uses this rectangle as the default bounds of the page’s media box. If you pass `NULL`, Core Graphics uses a default page size of 8.5 by 11 inches (612 by 792 points).

- `auxiliaryInfo` — A dictionary that specifies any additional information to be used by the PDF context when generating the PDF file, or `NULL`. The dictionary is retained by the new context, so on return you may safely release it. See [Auxiliary Dictionary Keys](../auxiliary-dictionary-keys.md) for keys you can include in the dictionary.

## Return Value

A new PDF context, or `NULL` if the context cannot be created. In Objective-C, you’re responsible for releasing this object using [CGContextRelease](../cgcontextrelease.md).

## Discussion

This function creates a PDF drawing environment to your specifications. When you draw into the new context, Core Graphics renders your drawing as a sequence of PDF drawing commands that are passed to the data consumer object.

## See Also

### Creating PDF Graphics Contexts

- [CGPDFContextCreateWithURL](<init(__mediabox___).md>) — Creates a URL-based PDF graphics context.
- [Auxiliary Dictionary Keys](../auxiliary-dictionary-keys.md) — Keys for the auxiliary info dictionary you specify when creating a PDF context.
