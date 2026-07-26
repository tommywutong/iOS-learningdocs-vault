---
title: UIModalPresentationStyle.custom
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimodalpresentationstyle/custom
source_url: 'https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/custom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimodalpresentationstyle/custom.json'
content_hash: 'sha256:3f1762fd10a2d34b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIModalPresentationStyle](../uimodalpresentationstyle.md)

# UIModalPresentationStyle.custom

<sub>Case</sub>

A custom view presentation style that is managed by a custom presentation controller and one or more custom animator objects.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case custom
```

## Discussion

All of these objects are provided by the presented view controller’s transitioning delegate, which is an object that conforms to the [UIViewControllerTransitioningDelegate](../uiviewcontrollertransitioningdelegate.md) protocol. Before presenting a view controller using this style, set the view controller’s  [transitioningDelegate](../uiviewcontroller/transitioningdelegate.md) property to your custom transitioning delegate.

## See Also

### Presentations

- [UIModalPresentationAutomatic](automatic.md) — The default presentation style chosen by the system.
- [UIModalPresentationNone](none.md) — A presentation style that indicates no adaptations should be made.
- [UIModalPresentationFullScreen](fullscreen.md) — A presentation style in which the presented view covers the screen.
- [UIModalPresentationPageSheet](pagesheet.md) — A presentation style that partially covers the underlying content.
- [UIModalPresentationFormSheet](formsheet.md) — A presentation style that displays the content centered in the screen.
- [UIModalPresentationCurrentContext](currentcontext.md) — A presentation style where the content is displayed over another view controller’s content.
- [UIModalPresentationOverFullScreen](overfullscreen.md) — A view presentation style in which the presented view covers the screen.
- [UIModalPresentationOverCurrentContext](overcurrentcontext.md) — A presentation style where the content is displayed over another view controller’s content.
- [UIModalPresentationPopover](popover.md) — A presentation style where the content is displayed in a popover view.
- [UIModalPresentationBlurOverFullScreen](bluroverfullscreen.md) — A presentation style that blurs the underlying content before displaying new content in a full-screen presentation.
