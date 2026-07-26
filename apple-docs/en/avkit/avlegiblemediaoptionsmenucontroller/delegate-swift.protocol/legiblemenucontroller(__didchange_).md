---
title: 'legibleMenuController(_:didChange:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, visionOS 26.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontroller(_:didchange:)'
source_url: 'https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontroller(_:didchange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontroller%28_%3Adidchange%3A%29.json'
content_hash: 'sha256:5c06653df777ea72'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVLegibleMediaOptionsMenuController](../../avlegiblemediaoptionsmenucontroller.md) · [Delegate](../delegate-swift.protocol.md)

# legibleMenuController(_:didChange:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional func legibleMenuController(_ menuController: AVLegibleMediaOptionsMenuController, didChange state: AVLegibleMediaOptionsMenuState)
```

## Parameters

- `menuController` — The legible options menu controller.

- `state` — The new menu state.

## Discussion

Tells the delegate, when legible media options menu state changes.

## See Also

### Responding to menu changes

- [- legibleMenuController:didRequestCaptionPreviewForProfileID:](<legiblemenucontroller(__didrequestcaptionpreviewforprofileid_).md>)
- [- legibleMenuControllerDidRequestStoppingSubtitleCaptionPreview:](<legiblemenucontrollerdidrequeststoppingsubtitlecaptionpreview(__).md>)
