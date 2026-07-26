---
title: requiresMonoscopicViewingMode
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/requiresmonoscopicviewingmode
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/requiresmonoscopicviewingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/requiresmonoscopicviewingmode.json'
content_hash: 'sha256:f9a00d994490beb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# requiresMonoscopicViewingMode

<sub>Instance Property</sub>

A Boolean value that indicates whether to permit playback of 2D video content only.

<sub>visionOS</sub>

```swift
var requiresMonoscopicViewingMode: Bool { get set }
```

## Discussion

The default value is `false`.

## See Also

### Configuring the visionOS player UI

- [infoViewActions](infoviewactions.md) — An array of actions to present in the Info content view.
- [customInfoViewControllers](custominfoviewcontrollers.md) — An array of view controllers to display as content tabs in the player user interface.
- [contextualActions](contextualactions.md) — An array of action controls to present contextually during playback.
- [contextualActionsInfoView](contextualactionsinfoview.md) — A view the system shows adjacent to the contextual actions that’s suitable for showing related information.
- [contextualActionsPreviewImage](contextualactionspreviewimage.md) — An image to show alongside the contextual actions.
- [experienceController](experiencecontroller.md) — The experience controller for this view controller.
- [groupExperienceCoordinator](groupexperiencecoordinator.md) — The group experience coordinator for this view controller.
- [viewport](viewport.md) — A configuration object that manages viewport settings for different presentation modes. _(beta)_
- [AVViewport](../avviewport.md) — A configuration object that manages viewport settings for different presentation modes. _(beta)_
