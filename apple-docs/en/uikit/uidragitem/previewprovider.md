---
title: previewProvider
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidragitem/previewprovider
source_url: 'https://developer.apple.com/documentation/uikit/uidragitem/previewprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragitem/previewprovider.json'
content_hash: 'sha256:c90043dd21581216'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragItem](../uidragitem.md)

# previewProvider

<sub>Instance Property</sub>

A visual preview of the drag item, displayed while the user drags the item across the screen.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var previewProvider: (() -> UIDragPreview?)? { get set }
```

## Discussion

As the user drags an item across the screen, the system displays a preview. You can change the preview by setting [previewProvider](previewprovider.md) to a block that returns a [UIDragPreview](../uidragpreview.md) object. The system invokes the block if and when it needs the drag item preview.

To use the default preview, set [previewProvider](previewprovider.md) to `nil`. To hide the preview, set [previewProvider](previewprovider.md) to a block that returns `nil`.

## See Also

### Changing the drag item preview

- [- setNeedsDropPreviewUpdate](<setneedsdroppreviewupdate().md>) — Notifies the operating system that an updated drop preview is available for the item.
