---
title: showsFullScreenToggleButton
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerview/showsfullscreentogglebutton
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/showsfullscreentogglebutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/showsfullscreentogglebutton.json'
content_hash: 'sha256:2f1ec87c58f24324'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# showsFullScreenToggleButton

<sub>Instance Property</sub>

A Boolean value that determines whether the player view displays a full-screen toggle button.

<sub>macOS</sub>

```swift
var showsFullScreenToggleButton: Bool { get set }
```

## Discussion

This property is currently supported only with a [controlsStyle](controlsstyle.md) of [AVPlayerViewControlsStyleFloating](../avplayerviewcontrolsstyle/floating.md) or [AVPlayerViewControlsStyleInline](../avplayerviewcontrolsstyle/inline.md).

The default value is `false`.

## See Also

### Customizing the user interface

- [controlsStyle](controlsstyle.md) — The player view’s controls style.
- [AVPlayerViewControlsStyle](../avplayerviewcontrolsstyle.md) — Constants that indicate which user interface controls the view displays.
- [showsFrameSteppingButtons](showsframesteppingbuttons.md) — A Boolean value that determines whether the player view displays frame stepping buttons.
- [showsSharingServiceButton](showssharingservicebutton.md) — A Boolean value that determines whether the player view displays a sharing service button.
- [showsTimecodes](showstimecodes.md) — A Boolean value that determines whether the player view displays timecodes, if available.
- [contentOverlayView](contentoverlayview.md) — A view that adds additional custom views between the video content and the controls.
- [actionPopUpButtonMenu](actionpopupbuttonmenu.md) — An action pop-up button menu that the player view displays.
- [updatesNowPlayingInfoCenter](updatesnowplayinginfocenter.md) — A Boolean value that indicates whether the player view controller updates the Now Playing info center.
