---
title: setNeedsDropPreviewUpdate()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidragitem/setneedsdroppreviewupdate()
source_url: 'https://developer.apple.com/documentation/uikit/uidragitem/setneedsdroppreviewupdate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragitem/setneedsdroppreviewupdate%28%29.json'
content_hash: 'sha256:c9c68eaf9961367d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragItem](../uidragitem.md)

# setNeedsDropPreviewUpdate()

<sub>Instance Method</sub>

Notifies the operating system that an updated drop preview is available for the item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setNeedsDropPreviewUpdate()
```

## Discussion

Call this method to provide an updated drop preview after UIKit has started the drop animation. If the drop animation is still ongoing, UIKit calls the drop interaction delegate’s [- dropInteraction:previewForDroppingItem:withDefault:](<../uidropinteractiondelegate/dropinteraction(__previewfordropping_withdefault_).md>) method, passing the previous drop preview as the `defaultPreview`.

## See Also

### Changing the drag item preview

- [previewProvider](previewprovider.md) — A visual preview of the drag item, displayed while the user drags the item across the screen.
