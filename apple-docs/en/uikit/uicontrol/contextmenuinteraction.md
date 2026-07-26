---
title: contextMenuInteraction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/contextmenuinteraction
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/contextmenuinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/contextmenuinteraction.json'
content_hash: 'sha256:9ad3e40f1bd918eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# contextMenuInteraction

<sub>Instance Property</sub>

A context menu interaction for the control.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contextMenuInteraction: UIContextMenuInteraction? { get }
```

## Discussion

This property returns a [UIContextMenuInteraction](../uicontextmenuinteraction.md) with the control set as its delegate. Before constructing the context menu interaction, the control verifies that it can serve as a viable delegate.

## See Also

### Managing context menus

- [Adding context menus in your app](../adding-context-menus-in-your-app.md) — Provide quick access to useful actions by adding context menus to your iOS app.
- [contextMenuInteractionEnabled](iscontextmenuinteractionenabled.md) — A Boolean value that determines whether the control enables its context menu interaction.
- [showsMenuAsPrimaryAction](showsmenuasprimaryaction.md) — A Boolean value that determines whether the context menu interaction is the control’s primary action.
- [- contextMenuInteraction:configurationForMenuAtLocation:](<contextmenuinteraction(__configurationformenuatlocation_).md>)
- [- contextMenuInteraction:previewForDismissingMenuWithConfiguration:](<contextmenuinteraction(__previewfordismissingmenuwithconfiguration_).md>)
- [- contextMenuInteraction:previewForHighlightingMenuWithConfiguration:](<contextmenuinteraction(__previewforhighlightingmenuwithconfiguration_).md>)
- [- contextMenuInteraction:willDisplayMenuForConfiguration:animator:](<contextmenuinteraction(__willdisplaymenufor_animator_).md>)
- [- contextMenuInteraction:willEndForConfiguration:animator:](<contextmenuinteraction(__willendfor_animator_).md>)
- [- menuAttachmentPointForConfiguration:](<menuattachmentpoint(for_).md>) — Return a point in this control’s coordinate space to which to attach the given configuration’s menu.
