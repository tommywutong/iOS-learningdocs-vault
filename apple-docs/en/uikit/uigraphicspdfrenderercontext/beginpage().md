---
title: beginPage()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigraphicspdfrenderercontext/beginpage()
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/beginpage()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicspdfrenderercontext/beginpage%28%29.json'
content_hash: 'sha256:fd9b21899ef5883b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsPDFRendererContext](../uigraphicspdfrenderercontext.md)

# beginPage()

<sub>Instance Method</sub>

Marks the beginning of a new page in the PDF context and configures it using default values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func beginPage()
```

## Discussion

This function ends any previous page before beginning a new one. It sets the bounds of the new page to the bounds rectangle you supplied when you created the PDF renderer.

## See Also

### Marking new pages

- [- beginPageWithBounds:pageInfo:](<beginpage(withbounds_pageinfo_).md>) — Marks the beginning of a new page in the PDF context and configures it using the specified values.
