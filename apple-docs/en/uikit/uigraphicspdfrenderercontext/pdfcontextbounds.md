---
title: pdfContextBounds
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicspdfrenderercontext/pdfcontextbounds
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/pdfcontextbounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicspdfrenderercontext/pdfcontextbounds.json'
content_hash: 'sha256:5ba70f54f1208038'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsPDFRendererContext](../uigraphicspdfrenderercontext.md)

# pdfContextBounds

<sub>Instance Property</sub>

The bounds of the PDF context for the current page.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var pdfContextBounds: CGRect { get }
```

## Discussion

This value represents the bounds provided to the [- beginPageWithBounds:pageInfo:](<beginpage(withbounds_pageinfo_).md>) method that created the current page. If the current page was created using the [- beginPage](<beginpage().md>) method, the bounds are equal to those provided at the initialization of the PDF renderer.
