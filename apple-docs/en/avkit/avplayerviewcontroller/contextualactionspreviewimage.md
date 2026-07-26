---
title: contextualActionsPreviewImage
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/contextualactionspreviewimage
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/contextualactionspreviewimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/contextualactionspreviewimage.json'
content_hash: 'sha256:0812bff020d20cd9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# contextualActionsPreviewImage

<sub>Instance Property</sub>

An image to show alongside the contextual actions.

<sub>visionOS</sub>

```swift
@NSCopying var contextualActionsPreviewImage: UIImage? { get set }
```

## Discussion

Use this to enhance a contextual action with more context. For example, if the action presents a button to jump back in time, show a preview frame of where in the movie the action skips to.

> [!note] Note
> The system only displays an image if the [contextualActions](contextualactions.md) property contains a single value.

## See Also

### Configuring the visionOS player UI

- [infoViewActions](infoviewactions.md) — An array of actions to present in the Info content view.
- [customInfoViewControllers](custominfoviewcontrollers.md) — An array of view controllers to display as content tabs in the player user interface.
- [contextualActions](contextualactions.md) — An array of action controls to present contextually during playback.
- [contextualActionsInfoView](contextualactionsinfoview.md) — A view the system shows adjacent to the contextual actions that’s suitable for showing related information.
- [requiresMonoscopicViewingMode](requiresmonoscopicviewingmode.md) — A Boolean value that indicates whether to permit playback of 2D video content only.
- [experienceController](experiencecontroller.md) — The experience controller for this view controller.
- [groupExperienceCoordinator](groupexperiencecoordinator.md) — The group experience coordinator for this view controller.
- [viewport](viewport.md) — A configuration object that manages viewport settings for different presentation modes. _(beta)_
- [AVViewport](../avviewport.md) — A configuration object that manages viewport settings for different presentation modes. _(beta)_
