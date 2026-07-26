---
title: UIInteraction
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinteraction
source_url: 'https://developer.apple.com/documentation/uikit/uiinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinteraction.json'
content_hash: 'sha256:66f6a8a9f7127980'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIInteraction

<sub>Protocol</sub>

The protocol that an interaction implements to access the view that owns it.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIInteraction : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIBandSelectionInteraction](uibandselectioninteraction.md), [UICanvasFeedbackGenerator](uicanvasfeedbackgenerator.md), [UIContextMenuInteraction](uicontextmenuinteraction.md), [UIDragInteraction](uidraginteraction.md), [UIDropInteraction](uidropinteraction.md), [UIEditMenuInteraction](uieditmenuinteraction.md), [UIFeedbackGenerator](uifeedbackgenerator.md), [UIFindInteraction](uifindinteraction.md), [UIImpactFeedbackGenerator](uiimpactfeedbackgenerator.md), [UIIndirectScribbleInteraction](uiindirectscribbleinteraction-1nfjm.md), [UILargeContentViewerInteraction](uilargecontentviewerinteraction.md), [UILookToScrollInteraction](uilooktoscrollinteraction.md), [UINotificationFeedbackGenerator](uinotificationfeedbackgenerator.md), [UIPencilInteraction](uipencilinteraction.md), [UIPointerInteraction](uipointerinteraction.md), [UIScribbleInteraction](uiscribbleinteraction.md), [UIScrollEdgeElementContainerInteraction](uiscrolledgeelementcontainerinteraction.md), [UISelectionFeedbackGenerator](uiselectionfeedbackgenerator.md), [UISpringLoadedInteraction](uispringloadedinteraction.md), [UITextInteraction](uitextinteraction.md), [UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md), [UIToolTipInteraction](uitooltipinteraction.md), [ActivationInteraction](uiwindowscene/activationinteraction.md), [UIWindowSceneDragInteraction](uiwindowscenedraginteraction.md), [UIWritingToolsCoordinator](uiwritingtoolscoordinator.md)

## Topics

### Getting the View

- [view](uiinteraction/view.md) — The view that owns the interaction.

### Tracking the Movements

- [- didMoveToView:](<uiinteraction/didmove(to_).md>) — Tells the interaction that a view added or removed it from the view’s interactions array.
- [- willMoveToView:](<uiinteraction/willmove(to_).md>) — Tells the interaction that a view will add or remove it from the view’s interactions array.

## See Also

### Adding and removing interactions

- [- addInteraction:](<uiview/addinteraction(__).md>) — Adds an interaction to the view.
- [- removeInteraction:](<uiview/removeinteraction(__).md>) — Removes an interaction from the view.
- [interactions](uiview/interactions.md) — The array of interactions for the view.
