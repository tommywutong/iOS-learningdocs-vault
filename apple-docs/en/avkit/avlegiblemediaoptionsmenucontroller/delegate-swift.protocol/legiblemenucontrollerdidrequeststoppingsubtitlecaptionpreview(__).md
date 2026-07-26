---
title: 'legibleMenuControllerDidRequestStoppingSubtitleCaptionPreview(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, visionOS 26.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontrollerdidrequeststoppingsubtitlecaptionpreview(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontrollerdidrequeststoppingsubtitlecaptionpreview(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontrollerdidrequeststoppingsubtitlecaptionpreview%28_%3A%29.json'
content_hash: 'sha256:2a96342cca3e4cff'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVLegibleMediaOptionsMenuController](../../avlegiblemediaoptionsmenucontroller.md) · [Delegate](../delegate-swift.protocol.md)

# legibleMenuControllerDidRequestStoppingSubtitleCaptionPreview(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional func legibleMenuControllerDidRequestStoppingSubtitleCaptionPreview(_ menuController: AVLegibleMediaOptionsMenuController)
```

## Parameters

- `menuController` — The legible options menu controller.

## Discussion

Called when the caption preview should be hidden

The client should hide any active caption preview.

## See Also

### Responding to menu changes

- [- legibleMenuController:didChangeMenuState:](<legiblemenucontroller(__didchange_).md>)
- [- legibleMenuController:didRequestCaptionPreviewForProfileID:](<legiblemenucontroller(__didrequestcaptionpreviewforprofileid_).md>)
