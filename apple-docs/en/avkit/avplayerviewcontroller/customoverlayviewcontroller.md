---
title: customOverlayViewController
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 13.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/customoverlayviewcontroller
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/customoverlayviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/customoverlayviewcontroller.json'
content_hash: 'sha256:41d2b5ace9bb3a19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# customOverlayViewController

<sub>Instance Property</sub>

A view controller that presents custom content over the player view.

<sub>tvOS</sub>

```swift
var customOverlayViewController: UIViewController? { get set }
```

## Discussion

The system presents the overlay view when the user swipes up on the Siri Remote during playback when the transport bar is hidden, or when they select a button when the transport bar is visible.

> [!important] Important
> Set a custom overlay view controller instead of installing a custom swipe gesture recognizer.

## See Also

### Customizing the tvOS player UI

- [playbackControlsIncludeTransportBar](playbackcontrolsincludetransportbar.md) — A Boolean value that indicates whether the player shows the transport bar and related controls.
- [playbackControlsIncludeInfoViews](playbackcontrolsincludeinfoviews.md) — A Boolean value that indicates whether the player presents video metadata, navigation markers, and playback settings views when the user requests them.
- [transportBarIncludesTitleView](transportbarincludestitleview.md) — A Boolean value that indicates whether the player user interface shows the title view above the scrubber.
- [transportBarCustomMenuItems](transportbarcustommenuitems.md) — An array of actions and menus to display with the default player controls.
- [customInfoViewControllers](custominfoviewcontrollers.md) — An array of view controllers to display as content tabs in the player user interface.
- [infoViewActions](infoviewactions.md) — An array of actions to present in the Info content view.
- [contextualActions](contextualactions.md) — An array of action controls to present contextually during playback.
- [unobscuredContentGuide](unobscuredcontentguide.md) — A layout guide that represents an area that fixed-position playback controls don’t obscure when visible.
- [customInfoViewController](custominfoviewcontroller.md) — A view controller that provides client-specific content and controls alongside system-provided information and settings panels. _(deprecated)_
