---
title: customInfoViewControllers
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/custominfoviewcontrollers
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/custominfoviewcontrollers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/custominfoviewcontrollers.json'
content_hash: 'sha256:d4d3dc84147a993d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# customInfoViewControllers

<sub>Instance Property</sub>

An array of view controllers to display as content tabs in the player user interface.

<sub>tvOS, visionOS</sub>

```swift
var customInfoViewControllers: [UIViewController] { get set }
```

## Discussion

The system uses a view controller’s [title](../../uikit/uiviewcontroller/title.md) property value as the content tab title. Set this property value before adding it to the array so that the title renders correctly in the player’s user interface.

Similarly, set a [preferredContentSize](../../uikit/uiviewcontroller/preferredcontentsize.md) value on the custom view controllers, or define appropriate auto layout constraints on their views, so the system sizes them correctly in the player user interface.

> [!important] Important
> The view with the greatest height determines the height of all of the content views. Set the height of your content views consistently to simplify layout, or verify that your content renders as intended if the system resizes it.

## See Also

### Customizing the tvOS player UI

- [playbackControlsIncludeTransportBar](playbackcontrolsincludetransportbar.md) — A Boolean value that indicates whether the player shows the transport bar and related controls.
- [playbackControlsIncludeInfoViews](playbackcontrolsincludeinfoviews.md) — A Boolean value that indicates whether the player presents video metadata, navigation markers, and playback settings views when the user requests them.
- [transportBarIncludesTitleView](transportbarincludestitleview.md) — A Boolean value that indicates whether the player user interface shows the title view above the scrubber.
- [transportBarCustomMenuItems](transportbarcustommenuitems.md) — An array of actions and menus to display with the default player controls.
- [infoViewActions](infoviewactions.md) — An array of actions to present in the Info content view.
- [contextualActions](contextualactions.md) — An array of action controls to present contextually during playback.
- [customOverlayViewController](customoverlayviewcontroller.md) — A view controller that presents custom content over the player view.
- [unobscuredContentGuide](unobscuredcontentguide.md) — A layout guide that represents an area that fixed-position playback controls don’t obscure when visible.
- [customInfoViewController](custominfoviewcontroller.md) — A view controller that provides client-specific content and controls alongside system-provided information and settings panels. _(deprecated)_
