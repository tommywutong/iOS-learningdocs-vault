---
title: 'dismissPreview(animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentinteractioncontroller/dismisspreview(animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/dismisspreview(animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontroller/dismisspreview%28animated%3A%29.json'
content_hash: 'sha256:20160d7af9cb05b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionController](../uidocumentinteractioncontroller.md)

# dismissPreview(animated:)

<sub>Instance Method</sub>

Dismisses the currently active document preview.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func dismissPreview(animated: Bool)
```

## Parameters

- `animated` — Specify [true](../../swift/true.md) to animate the dismissal of the document preview or [false](../../swift/false.md) to dismiss it immediately.

## Discussion

Use this method to dismiss the document preview programmatically. The document interaction controller may also dismiss the document preview automatically in response to user actions.

## See Also

### Presenting and dismissing a document preview

- [- presentPreviewAnimated:](<presentpreview(animated_).md>) — Displays a full-screen preview of the target document.
