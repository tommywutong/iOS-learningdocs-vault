---
title: 'beginPage(withBounds:pageInfo:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicspdfrenderercontext/beginpage(withbounds:pageinfo:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext/beginpage(withbounds:pageinfo:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicspdfrenderercontext/beginpage%28withbounds%3Apageinfo%3A%29.json'
content_hash: 'sha256:42f0f8c0610c3aef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsPDFRendererContext](../uigraphicspdfrenderercontext.md)

# beginPage(withBounds:pageInfo:)

<sub>Instance Method</sub>

Marks the beginning of a new page in the PDF context and configures it using the specified values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func beginPage(withBounds bounds: CGRect, pageInfo: [String : Any])
```

## Parameters

- `bounds` — A rectangle that specifies the size and location of the new PDF page. This rectangle corresponds to the media box in PDF terminology.

- `pageInfo` — A dictionary that specifies additional page-related information, such as the boxes that define different parts of the page. For a list of keys you can include in this dictionary, see `Box Keys` in [Auxiliary Dictionary Keys](../../coregraphics/auxiliary-dictionary-keys.md).

## Discussion

This function ends any previous page before beginning a new one. It sets the media box of the new page to the value in the [kCGPDFContextMediaBox](../../coregraphics/kcgpdfcontextmediabox.md) key of the `pageInfo` dictionary, or to the value in the bounds parameter if the dictionary does not contain the key.

## See Also

### Marking new pages

- [- beginPage](<beginpage().md>) — Marks the beginning of a new page in the PDF context and configures it using default values.
