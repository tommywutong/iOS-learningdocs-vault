---
title: AVPlayerViewControlsStyle
framework: AVKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontrolsstyle
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrolsstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrolsstyle.json'
content_hash: 'sha256:3540f9b2542a9051'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlayerViewControlsStyle

<sub>Enumeration</sub>

Constants that indicate which user interface controls the view displays.

<sub>macOS</sub>

```swift
enum AVPlayerViewControlsStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a controls style

- [init(rawValue:)](<avplayerviewcontrolsstyle/init(rawvalue_).md>)

### Controls Styles

- [AVPlayerViewControlsStyleNone](avplayerviewcontrolsstyle/none.md) — The view displays no playback controls.
- [AVPlayerViewControlsStyleInline](avplayerviewcontrolsstyle/inline.md) — The view displays playback controls in a bar along the view’s bottom edge.
- [AVPlayerViewControlsStyleFloating](avplayerviewcontrolsstyle/floating.md) — The view displays playback controls in a floating window over the video content.
- [AVPlayerViewControlsStyleMinimal](avplayerviewcontrolsstyle/minimal.md) — The view presents basic controls to play and pause playback.
- [AVPlayerViewControlsStyleDefault](avplayerviewcontrolsstyle/default.md) — The view’s default controls style.

## See Also

### Customizing the user interface

- [controlsStyle](avplayerview/controlsstyle.md) — The player view’s controls style.
- [showsFrameSteppingButtons](avplayerview/showsframesteppingbuttons.md) — A Boolean value that determines whether the player view displays frame stepping buttons.
- [showsSharingServiceButton](avplayerview/showssharingservicebutton.md) — A Boolean value that determines whether the player view displays a sharing service button.
- [showsFullScreenToggleButton](avplayerview/showsfullscreentogglebutton.md) — A Boolean value that determines whether the player view displays a full-screen toggle button.
- [showsTimecodes](avplayerview/showstimecodes.md) — A Boolean value that determines whether the player view displays timecodes, if available.
- [contentOverlayView](avplayerview/contentoverlayview.md) — A view that adds additional custom views between the video content and the controls.
- [actionPopUpButtonMenu](avplayerview/actionpopupbuttonmenu.md) — An action pop-up button menu that the player view displays.
- [updatesNowPlayingInfoCenter](avplayerview/updatesnowplayinginfocenter.md) — A Boolean value that indicates whether the player view controller updates the Now Playing info center.
