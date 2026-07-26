---
title: 'legibleMenuController(_:didRequestCaptionPreviewForProfileID:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, visionOS 26.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontroller(_:didrequestcaptionpreviewforprofileid:)'
source_url: 'https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontroller(_:didrequestcaptionpreviewforprofileid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontroller%28_%3Adidrequestcaptionpreviewforprofileid%3A%29.json'
content_hash: 'sha256:d726e19539115d35'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVLegibleMediaOptionsMenuController](../../avlegiblemediaoptionsmenucontroller.md) · [Delegate](../delegate-swift.protocol.md)

# legibleMenuController(_:didRequestCaptionPreviewForProfileID:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
optional func legibleMenuController(_ menuController: AVLegibleMediaOptionsMenuController, didRequestCaptionPreviewForProfileID profileID: String)
```

## Parameters

- `menuController` — The legible options menu controller.

- `profileID` — MACaptionAppearance profile ID as an NSString for the caption style to preview

## Discussion

Called when a caption preview should be displayed

The client should display a caption preview using the MACaptionAppearance profile ID provided. The client is responsible for rendering and positioning the preview.

## See Also

### Responding to menu changes

- [- legibleMenuController:didChangeMenuState:](<legiblemenucontroller(__didchange_).md>)
- [- legibleMenuControllerDidRequestStoppingSubtitleCaptionPreview:](<legiblemenucontrollerdidrequeststoppingsubtitlecaptionpreview(__).md>)
