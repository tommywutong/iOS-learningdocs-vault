---
title: UIModalPresentationStyle.currentContext
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimodalpresentationstyle/currentcontext
source_url: 'https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/currentcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimodalpresentationstyle/currentcontext.json'
content_hash: 'sha256:85f601da3783c517'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIModalPresentationStyle](../uimodalpresentationstyle.md)

# UIModalPresentationStyle.currentContext

<sub>Case</sub>

A presentation style where the content is displayed over another view controller’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case currentContext
```

## Discussion

Using this presentation style, the current view controller’s content is displayed over the view controller whose [definesPresentationContext](../uiviewcontroller/definespresentationcontext.md) property is [true](../../swift/true.md). UIKit may walk up the view controller hierarchy to find a view controller that wants to define the presentation context. The views belonging to the presenting view controller are removed after the presentation completes.

When presenting a view controller in a popover, this presentation style is supported only if the transition style is [UIModalTransitionStyleCoverVertical](../uimodaltransitionstyle/coververtical.md). Attempting to use a different transition style triggers an exception. However, you may use other transition styles (except the partial curl transition) if the parent view controller is not in a popover.

## See Also

### Presentations

- [UIModalPresentationAutomatic](automatic.md) — The default presentation style chosen by the system.
- [UIModalPresentationNone](none.md) — A presentation style that indicates no adaptations should be made.
- [UIModalPresentationFullScreen](fullscreen.md) — A presentation style in which the presented view covers the screen.
- [UIModalPresentationPageSheet](pagesheet.md) — A presentation style that partially covers the underlying content.
- [UIModalPresentationFormSheet](formsheet.md) — A presentation style that displays the content centered in the screen.
- [UIModalPresentationCustom](custom.md) — A custom view presentation style that is managed by a custom presentation controller and one or more custom animator objects.
- [UIModalPresentationOverFullScreen](overfullscreen.md) — A view presentation style in which the presented view covers the screen.
- [UIModalPresentationOverCurrentContext](overcurrentcontext.md) — A presentation style where the content is displayed over another view controller’s content.
- [UIModalPresentationPopover](popover.md) — A presentation style where the content is displayed in a popover view.
- [UIModalPresentationBlurOverFullScreen](bluroverfullscreen.md) — A presentation style that blurs the underlying content before displaying new content in a full-screen presentation.
