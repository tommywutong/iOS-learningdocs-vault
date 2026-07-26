---
title: customInfoViewController
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 11.0+（15.0 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avkit/avplayerviewcontroller/custominfoviewcontroller
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/custominfoviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/custominfoviewcontroller.json'
content_hash: 'sha256:5d6e31362117823c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# customInfoViewController

<sub>Instance Property</sub>

A view controller that provides client-specific content and controls alongside system-provided information and settings panels.

> [!warning] Deprecated
> Use [customInfoViewControllers](custominfoviewcontrollers.md) instead.

<sub>tvOS</sub>

```swift
var customInfoViewController: UIViewController? { get set }
```

## Discussion

Use [preferredContentSize](../../uikit/uiviewcontroller/preferredcontentsize.md) to provide the desired view size for the view.

## See Also

### Customizing the tvOS player UI

- [playbackControlsIncludeTransportBar](playbackcontrolsincludetransportbar.md) — A Boolean value that indicates whether the player shows the transport bar and related controls.
- [playbackControlsIncludeInfoViews](playbackcontrolsincludeinfoviews.md) — A Boolean value that indicates whether the player presents video metadata, navigation markers, and playback settings views when the user requests them.
- [transportBarIncludesTitleView](transportbarincludestitleview.md) — A Boolean value that indicates whether the player user interface shows the title view above the scrubber.
- [transportBarCustomMenuItems](transportbarcustommenuitems.md) — An array of actions and menus to display with the default player controls.
- [customInfoViewControllers](custominfoviewcontrollers.md) — An array of view controllers to display as content tabs in the player user interface.
- [infoViewActions](infoviewactions.md) — An array of actions to present in the Info content view.
- [contextualActions](contextualactions.md) — An array of action controls to present contextually during playback.
- [customOverlayViewController](customoverlayviewcontroller.md) — A view controller that presents custom content over the player view.
- [unobscuredContentGuide](unobscuredcontentguide.md) — A layout guide that represents an area that fixed-position playback controls don’t obscure when visible.
