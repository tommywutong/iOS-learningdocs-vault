---
title: 'menuAttachmentPoint(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontrol/menuattachmentpoint(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/menuattachmentpoint(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/menuattachmentpoint%28for%3A%29.json'
content_hash: 'sha256:ee9f310c2e6bf252'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# menuAttachmentPoint(for:)

<sub>Instance Method</sub>

Return a point in this control’s coordinate space to which to attach the given configuration’s menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func menuAttachmentPoint(for configuration: UIContextMenuConfiguration) -> CGPoint
```

## See Also

### Managing context menus

- [Adding context menus in your app](../adding-context-menus-in-your-app.md) — Provide quick access to useful actions by adding context menus to your iOS app.
- [contextMenuInteraction](contextmenuinteraction.md) — A context menu interaction for the control.
- [contextMenuInteractionEnabled](iscontextmenuinteractionenabled.md) — A Boolean value that determines whether the control enables its context menu interaction.
- [showsMenuAsPrimaryAction](showsmenuasprimaryaction.md) — A Boolean value that determines whether the context menu interaction is the control’s primary action.
- [- contextMenuInteraction:configurationForMenuAtLocation:](<contextmenuinteraction(__configurationformenuatlocation_).md>)
- [- contextMenuInteraction:previewForDismissingMenuWithConfiguration:](<contextmenuinteraction(__previewfordismissingmenuwithconfiguration_).md>)
- [- contextMenuInteraction:previewForHighlightingMenuWithConfiguration:](<contextmenuinteraction(__previewforhighlightingmenuwithconfiguration_).md>)
- [- contextMenuInteraction:willDisplayMenuForConfiguration:animator:](<contextmenuinteraction(__willdisplaymenufor_animator_).md>)
- [- contextMenuInteraction:willEndForConfiguration:animator:](<contextmenuinteraction(__willendfor_animator_).md>)
