---
title: controlsStyle
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerview/controlsstyle
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/controlsstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/controlsstyle.json'
content_hash: 'sha256:17a53a0b350c88bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# controlsStyle

<sub>Instance Property</sub>

The player view’s controls style.

<sub>macOS</sub>

```swift
var controlsStyle: AVPlayerViewControlsStyle { get set }
```

## Discussion

The player view supports several different control styles that you can use to customize the player view’s appearance and behavior. See [AVPlayerViewControlsStyle](../avplayerviewcontrolsstyle.md) for the possible values.

## See Also

### Customizing the user interface

- [AVPlayerViewControlsStyle](../avplayerviewcontrolsstyle.md) — Constants that indicate which user interface controls the view displays.
- [showsFrameSteppingButtons](showsframesteppingbuttons.md) — A Boolean value that determines whether the player view displays frame stepping buttons.
- [showsSharingServiceButton](showssharingservicebutton.md) — A Boolean value that determines whether the player view displays a sharing service button.
- [showsFullScreenToggleButton](showsfullscreentogglebutton.md) — A Boolean value that determines whether the player view displays a full-screen toggle button.
- [showsTimecodes](showstimecodes.md) — A Boolean value that determines whether the player view displays timecodes, if available.
- [contentOverlayView](contentoverlayview.md) — A view that adds additional custom views between the video content and the controls.
- [actionPopUpButtonMenu](actionpopupbuttonmenu.md) — An action pop-up button menu that the player view displays.
- [updatesNowPlayingInfoCenter](updatesnowplayinginfocenter.md) — A Boolean value that indicates whether the player view controller updates the Now Playing info center.
