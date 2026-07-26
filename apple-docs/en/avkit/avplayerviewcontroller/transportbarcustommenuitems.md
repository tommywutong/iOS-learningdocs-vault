---
title: transportBarCustomMenuItems
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 15.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/transportbarcustommenuitems
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/transportbarcustommenuitems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/transportbarcustommenuitems.json'
content_hash: 'sha256:62d4265fc00578fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# transportBarCustomMenuItems

<sub>Instance Property</sub>

An array of actions and menus to display with the default player controls.

<sub>tvOS</sub>

```swift
var transportBarCustomMenuItems: [UIMenuElement] { get set }
```

## Discussion

Use this property to display custom pop-up menus in transport bar. This property only supports menu elements of type [UIAction](../../uikit/uiaction.md) and [UIMenu](../../uikit/uimenu.md), and supports displaying inline one level of submenus.

## See Also

### Customizing the tvOS player UI

- [playbackControlsIncludeTransportBar](playbackcontrolsincludetransportbar.md) — A Boolean value that indicates whether the player shows the transport bar and related controls.
- [playbackControlsIncludeInfoViews](playbackcontrolsincludeinfoviews.md) — A Boolean value that indicates whether the player presents video metadata, navigation markers, and playback settings views when the user requests them.
- [transportBarIncludesTitleView](transportbarincludestitleview.md) — A Boolean value that indicates whether the player user interface shows the title view above the scrubber.
- [customInfoViewControllers](custominfoviewcontrollers.md) — An array of view controllers to display as content tabs in the player user interface.
- [infoViewActions](infoviewactions.md) — An array of actions to present in the Info content view.
- [contextualActions](contextualactions.md) — An array of action controls to present contextually during playback.
- [customOverlayViewController](customoverlayviewcontroller.md) — A view controller that presents custom content over the player view.
- [unobscuredContentGuide](unobscuredcontentguide.md) — A layout guide that represents an area that fixed-position playback controls don’t obscure when visible.
- [customInfoViewController](custominfoviewcontroller.md) — A view controller that provides client-specific content and controls alongside system-provided information and settings panels. _(deprecated)_
