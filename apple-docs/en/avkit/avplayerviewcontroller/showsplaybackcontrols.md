---
title: showsPlaybackControls
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/showsplaybackcontrols
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/showsplaybackcontrols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/showsplaybackcontrols.json'
content_hash: 'sha256:16643f8c4c308a2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# showsPlaybackControls

<sub>Instance Property</sub>

A Boolean value that indicates whether the player view controller shows playback controls.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var showsPlaybackControls: Bool { get set }
```

## Discussion

Set this property to `false` if you don’t want the system-provided playback controls visible over your content. Hiding the playback controls can be useful in situations where you need a non-interactive video presentation, such as a video splash screen.

The default value is `true`.

> [!important] Important
> Don’t use this property to change the visibility of the playback controls while the player view controller is onscreen. Doing so creates or destroys user interface elements.

## See Also

### Configuring presentation

- [contentOverlayView](contentoverlayview.md) — A view that displays between the video content and the playback controls.
- [videoGravity](videogravity.md) — A string that specifies how the video displays within the bounds of the view controller’s view.
- [videoBounds](videobounds.md) — The size and position of the video image within the bounds of the view controller’s view.
- [showsTimecodes](showstimecodes.md) — A Boolean value that determines whether the player view displays timecodes, if available.
- [appliesPreferredDisplayCriteriaAutomatically](appliespreferreddisplaycriteriaautomatically.md) — A Boolean value that indicates whether the view controller automatically sets the screen’s display criteria to match that of the currently playing asset.
