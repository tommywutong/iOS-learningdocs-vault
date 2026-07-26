---
title: transportBarIncludesTitleView
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 15.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/transportbarincludestitleview
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/transportbarincludestitleview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/transportbarincludestitleview.json'
content_hash: 'sha256:41a930055d280cc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# transportBarIncludesTitleView

<sub>Instance Property</sub>

A Boolean value that indicates whether the player user interface shows the title view above the scrubber.

<sub>tvOS</sub>

```swift
var transportBarIncludesTitleView: Bool { get set }
```

## Discussion

By default, the player presents a title view. This view displays title ([commonIdentifierTitle](../../avfoundation/avmetadataidentifier/commonidentifiertitle.md)) and subtitle ([iTunesMetadataTrackSubTitle](../../avfoundation/avmetadataidentifier/itunesmetadatatracksubtitle.md)) metadata embedded in a media asset or set as a player item’s [externalMetadata](../../avfoundation/avplayeritem/externalmetadata.md).

The view controller ignores this property when [playbackControlsIncludeTransportBar](playbackcontrolsincludetransportbar.md) is `false`.

## See Also

### Customizing the tvOS player UI

- [playbackControlsIncludeTransportBar](playbackcontrolsincludetransportbar.md) — A Boolean value that indicates whether the player shows the transport bar and related controls.
- [playbackControlsIncludeInfoViews](playbackcontrolsincludeinfoviews.md) — A Boolean value that indicates whether the player presents video metadata, navigation markers, and playback settings views when the user requests them.
- [transportBarCustomMenuItems](transportbarcustommenuitems.md) — An array of actions and menus to display with the default player controls.
- [customInfoViewControllers](custominfoviewcontrollers.md) — An array of view controllers to display as content tabs in the player user interface.
- [infoViewActions](infoviewactions.md) — An array of actions to present in the Info content view.
- [contextualActions](contextualactions.md) — An array of action controls to present contextually during playback.
- [customOverlayViewController](customoverlayviewcontroller.md) — A view controller that presents custom content over the player view.
- [unobscuredContentGuide](unobscuredcontentguide.md) — A layout guide that represents an area that fixed-position playback controls don’t obscure when visible.
- [customInfoViewController](custominfoviewcontroller.md) — A view controller that provides client-specific content and controls alongside system-provided information and settings panels. _(deprecated)_
