---
title: contextualActionsInfoView
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/contextualactionsinfoview
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/contextualactionsinfoview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/contextualactionsinfoview.json'
content_hash: 'sha256:7c7985dadb673264'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# contextualActionsInfoView

<sub>Instance Property</sub>

A view the system shows adjacent to the contextual actions that’s suitable for showing related information.

<sub>visionOS</sub>

```swift
var contextualActionsInfoView: UIView { get }
```

## Discussion

Use this view to add additional metadata, information, and artwork as subviews.

## See Also

### Configuring the visionOS player UI

- [infoViewActions](infoviewactions.md) — An array of actions to present in the Info content view.
- [customInfoViewControllers](custominfoviewcontrollers.md) — An array of view controllers to display as content tabs in the player user interface.
- [contextualActions](contextualactions.md) — An array of action controls to present contextually during playback.
- [contextualActionsPreviewImage](contextualactionspreviewimage.md) — An image to show alongside the contextual actions.
- [requiresMonoscopicViewingMode](requiresmonoscopicviewingmode.md) — A Boolean value that indicates whether to permit playback of 2D video content only.
- [experienceController](experiencecontroller.md) — The experience controller for this view controller.
- [groupExperienceCoordinator](groupexperiencecoordinator.md) — The group experience coordinator for this view controller.
- [viewport](viewport.md) — A configuration object that manages viewport settings for different presentation modes. _(beta)_
- [AVViewport](../avviewport.md) — A configuration object that manages viewport settings for different presentation modes. _(beta)_
