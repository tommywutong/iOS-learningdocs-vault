---
title: videoBounds
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/videobounds
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/videobounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/videobounds.json'
content_hash: 'sha256:6b8e8f6b4bc9e615'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# videoBounds

<sub>Instance Property</sub>

The size and position of the video image within the bounds of the view controller’s view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var videoBounds: CGRect { get }
```

## Discussion

The size and position of this rectangle depend on the aspect ratio of the media (like 16:9 or 4:3), the bounds of the player view controller’s view, and the view controller’s [videoGravity](videogravity.md).

This property is key-value observable.

## See Also

### Configuring presentation

- [showsPlaybackControls](showsplaybackcontrols.md) — A Boolean value that indicates whether the player view controller shows playback controls.
- [contentOverlayView](contentoverlayview.md) — A view that displays between the video content and the playback controls.
- [videoGravity](videogravity.md) — A string that specifies how the video displays within the bounds of the view controller’s view.
- [showsTimecodes](showstimecodes.md) — A Boolean value that determines whether the player view displays timecodes, if available.
- [appliesPreferredDisplayCriteriaAutomatically](appliespreferreddisplaycriteriaautomatically.md) — A Boolean value that indicates whether the view controller automatically sets the screen’s display criteria to match that of the currently playing asset.
