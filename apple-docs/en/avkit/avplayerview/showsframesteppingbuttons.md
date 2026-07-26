---
title: showsFrameSteppingButtons
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerview/showsframesteppingbuttons
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/showsframesteppingbuttons'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/showsframesteppingbuttons.json'
content_hash: 'sha256:a8820c9a21d72d5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# showsFrameSteppingButtons

<sub>Instance Property</sub>

A Boolean value that determines whether the player view displays frame stepping buttons.

<sub>macOS</sub>

```swift
var showsFrameSteppingButtons: Bool { get set }
```

## Discussion

Setting this property value to `true` results in the player view replacing its fast-forward and rewind controls with frame stepping buttons. This property is currently supported only with a [controlsStyle](controlsstyle.md) of [AVPlayerViewControlsStyleFloating](../avplayerviewcontrolsstyle/floating.md).

The default value is `false`.

## See Also

### Customizing the user interface

- [controlsStyle](controlsstyle.md) — The player view’s controls style.
- [AVPlayerViewControlsStyle](../avplayerviewcontrolsstyle.md) — Constants that indicate which user interface controls the view displays.
- [showsSharingServiceButton](showssharingservicebutton.md) — A Boolean value that determines whether the player view displays a sharing service button.
- [showsFullScreenToggleButton](showsfullscreentogglebutton.md) — A Boolean value that determines whether the player view displays a full-screen toggle button.
- [showsTimecodes](showstimecodes.md) — A Boolean value that determines whether the player view displays timecodes, if available.
- [contentOverlayView](contentoverlayview.md) — A view that adds additional custom views between the video content and the controls.
- [actionPopUpButtonMenu](actionpopupbuttonmenu.md) — An action pop-up button menu that the player view displays.
- [updatesNowPlayingInfoCenter](updatesnowplayinginfocenter.md) — A Boolean value that indicates whether the player view controller updates the Now Playing info center.
