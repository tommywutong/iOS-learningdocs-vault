---
title: UIContextMenuInteractionDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontextmenuinteractiondelegate
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuinteractiondelegate.json'
content_hash: 'sha256:4b9618f81a34cfd7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContextMenuInteractionDelegate

<sub>Protocol</sub>

The methods for providing the set of actions to perform on your content, and for customizing the preview of that content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIContextMenuInteractionDelegate : NSObjectProtocol
```

## Overview

Use this protocol to provide UIKit with the contextual menu that you want to display. When a [UIContextMenuInteraction](uicontextmenuinteraction.md) object detects an appropriate interaction, it calls the [- contextMenuInteraction:configurationForMenuAtLocation:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__configurationformenuatlocation_).md>) method of your delegate. You use that method to specify the basic configuration details for your interface. In addition to your contextual menu, you can tell UIKit whether you want it to display a default preview interface or a custom view controller that you provide. You can also specify options for how you want UIKit to animate the presentation and dismissal of that interface.

For additional information about how to implement contextual menus, see [Adding context menus in your app](adding-context-menus-in-your-app.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIButton](uibutton.md), [UIColorWell](uicolorwell.md), [UIControl](uicontrol.md), [UIDatePicker](uidatepicker.md), [UIPageControl](uipagecontrol.md), [UIPasteControl](uipastecontrol.md), [UIRefreshControl](uirefreshcontrol.md), [UISearchTextField](uisearchtextfield.md), [UISegmentedControl](uisegmentedcontrol.md), [UISlider](uislider.md), [UIStepper](uistepper.md), [UISwitch](uiswitch.md), [UITextField](uitextfield.md)

## Topics

### Providing the preview configuration data

- [- contextMenuInteraction:configurationForMenuAtLocation:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__configurationformenuatlocation_).md>) — Returns the configuration data to use when previewing the content.
- [UIContextMenuConfiguration](uicontextmenuconfiguration.md) — An object containing the configuration details for the contextual menu.

### Customizing the preview animations

- [- contextMenuInteraction:configuration:highlightPreviewForItemWithIdentifier:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__configuration_highlightpreviewforitemwithidentifier_).md>) — Asks the delegate for a preview of the item with the specified identifier when a context-menu interaction begins.
- [- contextMenuInteraction:configuration:dismissalPreviewForItemWithIdentifier:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__configuration_dismissalpreviewforitemwithidentifier_).md>) — Asks the delegate for a preview of the item with the specified identifier when a context-menu interaction ends.
- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.

### Responding to the menu’s appearance

- [- contextMenuInteraction:willPerformPreviewActionForMenuWithConfiguration:animator:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__willperformpreviewactionformenuwith_animator_).md>) — Informs the delegate when a preview action begins.
- [UIContextMenuInteractionCommitAnimating](uicontextmenuinteractioncommitanimating.md) — Methods adopted by system-supplied animator objects when committing preview-related animations.

### Handling animations

- [- contextMenuInteraction:willDisplayMenuForConfiguration:animator:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__willdisplaymenufor_animator_).md>) — Informs the delegate when a menu display begins.
- [- contextMenuInteraction:willEndForConfiguration:animator:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__willendfor_animator_).md>) — Informs the delegate when a menu display ends.
- [UIContextMenuInteractionAnimating](uicontextmenuinteractionanimating.md) — Methods adopted by system-supplied animator objects when interacting with context menus.

### Deprecated

- [- contextMenuInteraction:previewForHighlightingMenuWithConfiguration:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__previewforhighlightingmenuwithconfiguration_).md>) — Returns the source view to use when animating the appearance of the preview interface. _(deprecated)_
- [- contextMenuInteraction:previewForDismissingMenuWithConfiguration:](<uicontextmenuinteractiondelegate/contextmenuinteraction(__previewfordismissingmenuwithconfiguration_).md>) — Returns the destination view to use when animating the appearance of the preview interface. _(deprecated)_

## See Also

### Contextual menus

- [UIContextMenuSystem](uicontextmenusystem.md) — The context menu system.
- [UIContextMenuInteraction](uicontextmenuinteraction.md) — An interaction object that you use to display relevant actions for your content.
- [UITargetedPreview](uitargetedpreview.md) — An object describing the view to use during preview-related animations.
- [UIPreviewTarget](uipreviewtarget.md) — An object that specifies the container view to use for animations.
- [UIPreviewParameters](uipreviewparameters.md) — Additional parameters to use when animating a preview interface.
