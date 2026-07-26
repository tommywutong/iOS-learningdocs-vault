---
title: 'beginPage(mediaBox:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/beginpage(mediabox:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/beginpage(mediabox:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/beginpage%28mediabox%3A%29.json'
content_hash: 'sha256:2f1a22e8021e6bbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# beginPage(mediaBox:)

<sub>Instance Method</sub>

Starts a new page in a page-based graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func beginPage(mediaBox: UnsafePointer<CGRect>?)
```

## Parameters

- `mediaBox` — A rectangle defining the bounds of the new page, expressed in units of the default user space, or `NULL`. These bounds supersede any supplied for the media box when you created the context. If you pass `NULL`, Core Graphics uses the rectangle you supplied for the media box when the graphics context was created.

## Discussion

When using a graphics context that supports multiple pages, you should call this function together with [CGContextEndPage](<endpage().md>) to delineate the page boundaries in the output. In other words, each page should be bracketed by calls to `CGContextBeginPage` and `CGContextEndPage`. Core Graphics ignores all drawing operations performed outside a page boundary in a page-based context.

## See Also

### Managing a Page-Based Graphics Context

- [CGContextEndPage](<endpage().md>) — Ends the current page in a page-based graphics context.
