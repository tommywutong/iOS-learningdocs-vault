---
title: UIModalPresentationStyle.none
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimodalpresentationstyle/none
source_url: 'https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimodalpresentationstyle/none.json'
content_hash: 'sha256:88f106827ee3c93c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIModalPresentationStyle](../uimodalpresentationstyle.md)

# UIModalPresentationStyle.none

<sub>Case</sub>

A presentation style that indicates no adaptations should be made.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case none
```

## Discussion

Do not use this style to present a view controller. Instead, return it from the [- adaptivePresentationStyleForPresentationController:](<../uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for_).md>) method of an adaptive delegate when you do not want a presentation controller to adapt the style of an already presented view controller.

## See Also

### Presentations

- [UIModalPresentationAutomatic](automatic.md) — The default presentation style chosen by the system.
- [UIModalPresentationFullScreen](fullscreen.md) — A presentation style in which the presented view covers the screen.
- [UIModalPresentationPageSheet](pagesheet.md) — A presentation style that partially covers the underlying content.
- [UIModalPresentationFormSheet](formsheet.md) — A presentation style that displays the content centered in the screen.
- [UIModalPresentationCurrentContext](currentcontext.md) — A presentation style where the content is displayed over another view controller’s content.
- [UIModalPresentationCustom](custom.md) — A custom view presentation style that is managed by a custom presentation controller and one or more custom animator objects.
- [UIModalPresentationOverFullScreen](overfullscreen.md) — A view presentation style in which the presented view covers the screen.
- [UIModalPresentationOverCurrentContext](overcurrentcontext.md) — A presentation style where the content is displayed over another view controller’s content.
- [UIModalPresentationPopover](popover.md) — A presentation style where the content is displayed in a popover view.
- [UIModalPresentationBlurOverFullScreen](bluroverfullscreen.md) — A presentation style that blurs the underlying content before displaying new content in a full-screen presentation.
