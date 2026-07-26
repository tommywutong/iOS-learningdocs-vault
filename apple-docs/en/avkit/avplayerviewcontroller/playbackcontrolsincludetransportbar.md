---
title: playbackControlsIncludeTransportBar
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 11.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/playbackcontrolsincludetransportbar
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/playbackcontrolsincludetransportbar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/playbackcontrolsincludetransportbar.json'
content_hash: 'sha256:8041a2beab90dee1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# playbackControlsIncludeTransportBar

<sub>Instance Property</sub>

A Boolean value that indicates whether the player shows the transport bar and related controls.

<sub>tvOS</sub>

```swift
var playbackControlsIncludeTransportBar: Bool { get set }
```

## Discussion

Set this property to `false`, and set [showsPlaybackControls](showsplaybackcontrols.md) to `true`, to selectively prevent the player from presenting the transport bar during user interaction. Changing the value of this property doesn’t immediately change the visibility of the transport bar.

The default value is `true`.

## See Also

### Customizing the tvOS player UI

- [playbackControlsIncludeInfoViews](playbackcontrolsincludeinfoviews.md) — A Boolean value that indicates whether the player presents video metadata, navigation markers, and playback settings views when the user requests them.
- [transportBarIncludesTitleView](transportbarincludestitleview.md) — A Boolean value that indicates whether the player user interface shows the title view above the scrubber.
- [transportBarCustomMenuItems](transportbarcustommenuitems.md) — An array of actions and menus to display with the default player controls.
- [customInfoViewControllers](custominfoviewcontrollers.md) — An array of view controllers to display as content tabs in the player user interface.
- [infoViewActions](infoviewactions.md) — An array of actions to present in the Info content view.
- [contextualActions](contextualactions.md) — An array of action controls to present contextually during playback.
- [customOverlayViewController](customoverlayviewcontroller.md) — A view controller that presents custom content over the player view.
- [unobscuredContentGuide](unobscuredcontentguide.md) — A layout guide that represents an area that fixed-position playback controls don’t obscure when visible.
- [customInfoViewController](custominfoviewcontroller.md) — A view controller that provides client-specific content and controls alongside system-provided information and settings panels. _(deprecated)_
