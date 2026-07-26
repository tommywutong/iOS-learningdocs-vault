---
title: experienceController
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 2.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/experiencecontroller
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/experiencecontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/experiencecontroller.json'
content_hash: 'sha256:0c18614b5d7e512b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# experienceController

<sub>Instance Property</sub>

The experience controller for this view controller.

<sub>visionOS</sub>

```swift
@MainActor @preconcurrency var experienceController: AVExperienceController { get }
```

## Discussion

Use an experience controller to transition a player to different experiences and observe experience transitions.

The use of the experience controller is mutually exclusive with a view controller’s existing API for managing the experience. After accessing the `experienceController` property, those methods will log an error and have no effect. Attempting to access this property may fail if these mutually-exclusive properties and methods have been used.

## See Also

### Configuring the visionOS player UI

- [infoViewActions](infoviewactions.md) — An array of actions to present in the Info content view.
- [customInfoViewControllers](custominfoviewcontrollers.md) — An array of view controllers to display as content tabs in the player user interface.
- [contextualActions](contextualactions.md) — An array of action controls to present contextually during playback.
- [contextualActionsInfoView](contextualactionsinfoview.md) — A view the system shows adjacent to the contextual actions that’s suitable for showing related information.
- [contextualActionsPreviewImage](contextualactionspreviewimage.md) — An image to show alongside the contextual actions.
- [requiresMonoscopicViewingMode](requiresmonoscopicviewingmode.md) — A Boolean value that indicates whether to permit playback of 2D video content only.
- [groupExperienceCoordinator](groupexperiencecoordinator.md) — The group experience coordinator for this view controller.
- [viewport](viewport.md) — A configuration object that manages viewport settings for different presentation modes. _(beta)_
- [AVViewport](../avviewport.md) — A configuration object that manages viewport settings for different presentation modes. _(beta)_
