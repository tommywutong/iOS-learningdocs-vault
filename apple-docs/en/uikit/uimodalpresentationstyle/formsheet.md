---
title: UIModalPresentationStyle.formSheet
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS 26.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimodalpresentationstyle/formsheet
source_url: 'https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/formsheet'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimodalpresentationstyle/formsheet.json'
content_hash: 'sha256:b1f114c333e1c9fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIModalPresentationStyle](../uimodalpresentationstyle.md)

# UIModalPresentationStyle.formSheet

<sub>Case</sub>

A presentation style that displays the content centered in the screen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case formSheet
```

## Discussion

In a regular-width, regular-height size class, the system adds a layer with a Liquid Glass effect over the background content and centers the view controller’s content on top of this layer. The default content size is smaller than that of the [UIModalPresentationPageSheet](pagesheet.md) style. A part of the background content always remains visible.

To provide a custom content size, use the modal view controller’s [preferredContentSize](../uiviewcontroller/preferredcontentsize.md) property.

In a compact-width, regular-height size class, the system displays the view controller as a sheet with part of the background content visible near the top of the screen.

In a compact-height size class, the behavior is the same as [UIModalPresentationFullScreen](fullscreen.md).

Where the background content remains visible, the system doesn’t call the presenting view controller’s [- viewWillDisappear:](<../uiviewcontroller/viewwilldisappear(__).md>) and [- viewDidDisappear:](<../uiviewcontroller/viewdiddisappear(__).md>) methods.

## See Also

### Presentations

- [UIModalPresentationAutomatic](automatic.md) — The default presentation style chosen by the system.
- [UIModalPresentationNone](none.md) — A presentation style that indicates no adaptations should be made.
- [UIModalPresentationFullScreen](fullscreen.md) — A presentation style in which the presented view covers the screen.
- [UIModalPresentationPageSheet](pagesheet.md) — A presentation style that partially covers the underlying content.
- [UIModalPresentationCurrentContext](currentcontext.md) — A presentation style where the content is displayed over another view controller’s content.
- [UIModalPresentationCustom](custom.md) — A custom view presentation style that is managed by a custom presentation controller and one or more custom animator objects.
- [UIModalPresentationOverFullScreen](overfullscreen.md) — A view presentation style in which the presented view covers the screen.
- [UIModalPresentationOverCurrentContext](overcurrentcontext.md) — A presentation style where the content is displayed over another view controller’s content.
- [UIModalPresentationPopover](popover.md) — A presentation style where the content is displayed in a popover view.
- [UIModalPresentationBlurOverFullScreen](bluroverfullscreen.md) — A presentation style that blurs the underlying content before displaying new content in a full-screen presentation.
