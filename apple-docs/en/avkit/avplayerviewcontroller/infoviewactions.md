---
title: infoViewActions
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/infoviewactions
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/infoviewactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/infoviewactions.json'
content_hash: 'sha256:419ef220ddaa5011'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# infoViewActions

<sub>Instance Property</sub>

An array of actions to present in the Info content view.

<sub>tvOS, visionOS</sub>

```swift
var infoViewActions: [UIAction]! { get set }
```

## Discussion

The Info content view can display up to two custom action controls along its trailing edge. The default value of this property is a single action that plays the current media from the beginning when tapped.

## See Also

### Customizing the tvOS player UI

- [playbackControlsIncludeTransportBar](playbackcontrolsincludetransportbar.md) — A Boolean value that indicates whether the player shows the transport bar and related controls.
- [playbackControlsIncludeInfoViews](playbackcontrolsincludeinfoviews.md) — A Boolean value that indicates whether the player presents video metadata, navigation markers, and playback settings views when the user requests them.
- [transportBarIncludesTitleView](transportbarincludestitleview.md) — A Boolean value that indicates whether the player user interface shows the title view above the scrubber.
- [transportBarCustomMenuItems](transportbarcustommenuitems.md) — An array of actions and menus to display with the default player controls.
- [customInfoViewControllers](custominfoviewcontrollers.md) — An array of view controllers to display as content tabs in the player user interface.
- [contextualActions](contextualactions.md) — An array of action controls to present contextually during playback.
- [customOverlayViewController](customoverlayviewcontroller.md) — A view controller that presents custom content over the player view.
- [unobscuredContentGuide](unobscuredcontentguide.md) — A layout guide that represents an area that fixed-position playback controls don’t obscure when visible.
- [customInfoViewController](custominfoviewcontroller.md) — A view controller that provides client-specific content and controls alongside system-provided information and settings panels. _(deprecated)_
