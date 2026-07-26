---
title: appliesPreferredDisplayCriteriaAutomatically
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 11.2+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/appliespreferreddisplaycriteriaautomatically
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/appliespreferreddisplaycriteriaautomatically'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/appliespreferreddisplaycriteriaautomatically.json'
content_hash: 'sha256:0526e134beef9cb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# appliesPreferredDisplayCriteriaAutomatically

<sub>Instance Property</sub>

A Boolean value that indicates whether the view controller automatically sets the screen’s display criteria to match that of the currently playing asset.

<sub>tvOS, visionOS</sub>

```swift
var appliesPreferredDisplayCriteriaAutomatically: Bool { get set }
```

## Discussion

If this property value is `true`, the player uses the preferred display criteria of the video asset when playing the content in fullscreen. The display criteria is reset to the display’s default criteria when full-screen playback ends. Don’t change this value during full-screen presentation unless you’ve disposed of the player or player item.

## See Also

### Configuring presentation

- [showsPlaybackControls](showsplaybackcontrols.md) — A Boolean value that indicates whether the player view controller shows playback controls.
- [contentOverlayView](contentoverlayview.md) — A view that displays between the video content and the playback controls.
- [videoGravity](videogravity.md) — A string that specifies how the video displays within the bounds of the view controller’s view.
- [videoBounds](videobounds.md) — The size and position of the video image within the bounds of the view controller’s view.
- [showsTimecodes](showstimecodes.md) — A Boolean value that determines whether the player view displays timecodes, if available.
