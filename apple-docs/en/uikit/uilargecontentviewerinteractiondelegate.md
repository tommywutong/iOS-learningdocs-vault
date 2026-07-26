---
title: UILargeContentViewerInteractionDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilargecontentviewerinteractiondelegate
source_url: 'https://developer.apple.com/documentation/uikit/uilargecontentviewerinteractiondelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilargecontentviewerinteractiondelegate.json'
content_hash: 'sha256:5b860ec69d6fa826'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UILargeContentViewerInteractionDelegate

<sub>Protocol</sub>

An object that customizes the behavior of the large content viewer interactions.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UILargeContentViewerInteractionDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Customizing large content viewer interactions

- [- largeContentViewerInteraction:didEndOnItem:atPoint:](<uilargecontentviewerinteractiondelegate/largecontentviewerinteraction(__didendon_at_).md>) — Performs an action when the large content viewer gesture ends at the location of the specified item.
- [- largeContentViewerInteraction:itemAtPoint:](<uilargecontentviewerinteractiondelegate/largecontentviewerinteraction(__itemat_).md>) — Identifies the large content viewer item for the specified interaction and location.
- [- viewControllerForLargeContentViewerInteraction:](<uilargecontentviewerinteractiondelegate/viewcontroller(for_).md>) — Specifies which view controller should display the large content viewer.

## See Also

### Content viewer

- [UILargeContentViewerInteraction](uilargecontentviewerinteraction.md) — An interaction that enables a gesture to present the large content viewer for cases when supporting the largest dynamic type sizes isn’t appropriate.
- [UILargeContentViewerItem](uilargecontentvieweritem.md) — Methods that provide details about how to display your custom content in the large content viewer.
