---
title: UIModalPresentationStyle.popover
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimodalpresentationstyle/popover
source_url: 'https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/popover'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimodalpresentationstyle/popover.json'
content_hash: 'sha256:734aa5427a616a94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIModalPresentationStyle](../uimodalpresentationstyle.md)

# UIModalPresentationStyle.popover

<sub>Case</sub>

A presentation style where the content is displayed in a popover view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case popover
```

## Discussion

In a horizontally regular environment, this style displays the view controller in a popover view. The background content is dimmed and taps outside the popover cause the popover to be dismissed. If you do not want taps to dismiss the popover, you can assign one or more views to the [passthroughViews](../uipopoverpresentationcontroller/passthroughviews.md) property of the associated [UIPopoverPresentationController](../uipopoverpresentationcontroller.md) object, which you can get from the [popoverPresentationController](../uiviewcontroller/popoverpresentationcontroller.md) property.

In iOS 13 and later, for horizontally or vertically compact environments, this option behaves the same as [UIModalPresentationFormSheet](formsheet.md).

In iOS 12 and earlier:

- For horizontally compact environments, this option behaves the same as [UIModalPresentationFullScreen](fullscreen.md).
- For horizontally regular and vertically compact environments, this option behaves the same as [UIModalPresentationFormSheet](formsheet.md).

For more information about horizontal and vertical size classes, see [UIUserInterfaceSizeClass](../uiuserinterfacesizeclass.md).

## See Also

### Presentations

- [UIModalPresentationAutomatic](automatic.md) — The default presentation style chosen by the system.
- [UIModalPresentationNone](none.md) — A presentation style that indicates no adaptations should be made.
- [UIModalPresentationFullScreen](fullscreen.md) — A presentation style in which the presented view covers the screen.
- [UIModalPresentationPageSheet](pagesheet.md) — A presentation style that partially covers the underlying content.
- [UIModalPresentationFormSheet](formsheet.md) — A presentation style that displays the content centered in the screen.
- [UIModalPresentationCurrentContext](currentcontext.md) — A presentation style where the content is displayed over another view controller’s content.
- [UIModalPresentationCustom](custom.md) — A custom view presentation style that is managed by a custom presentation controller and one or more custom animator objects.
- [UIModalPresentationOverFullScreen](overfullscreen.md) — A view presentation style in which the presented view covers the screen.
- [UIModalPresentationOverCurrentContext](overcurrentcontext.md) — A presentation style where the content is displayed over another view controller’s content.
- [UIModalPresentationBlurOverFullScreen](bluroverfullscreen.md) — A presentation style that blurs the underlying content before displaying new content in a full-screen presentation.
