---
title: actionPopUpButtonMenu
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerview/actionpopupbuttonmenu
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/actionpopupbuttonmenu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/actionpopupbuttonmenu.json'
content_hash: 'sha256:033e8194a4bf9483'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# actionPopUpButtonMenu

<sub>Instance Property</sub>

An action pop-up button menu that the player view displays.

<sub>macOS</sub>

```swift
@IBOutlet var actionPopUpButtonMenu: NSMenu? { get set }
```

## Discussion

Set this property value to show an action pop-up button. Setting a custom action pop-up button is currently supported only for a [controlsStyle](controlsstyle.md) of [AVPlayerViewControlsStyleFloating](../avplayerviewcontrolsstyle/floating.md) or [AVPlayerViewControlsStyleInline](../avplayerviewcontrolsstyle/inline.md).

The default value is `nil`.

## See Also

### Customizing the user interface

- [controlsStyle](controlsstyle.md) — The player view’s controls style.
- [AVPlayerViewControlsStyle](../avplayerviewcontrolsstyle.md) — Constants that indicate which user interface controls the view displays.
- [showsFrameSteppingButtons](showsframesteppingbuttons.md) — A Boolean value that determines whether the player view displays frame stepping buttons.
- [showsSharingServiceButton](showssharingservicebutton.md) — A Boolean value that determines whether the player view displays a sharing service button.
- [showsFullScreenToggleButton](showsfullscreentogglebutton.md) — A Boolean value that determines whether the player view displays a full-screen toggle button.
- [showsTimecodes](showstimecodes.md) — A Boolean value that determines whether the player view displays timecodes, if available.
- [contentOverlayView](contentoverlayview.md) — A view that adds additional custom views between the video content and the controls.
- [updatesNowPlayingInfoCenter](updatesnowplayinginfocenter.md) — A Boolean value that indicates whether the player view controller updates the Now Playing info center.
