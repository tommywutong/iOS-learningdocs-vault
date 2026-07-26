---
title: videoGravity
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/videogravity
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/videogravity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/videogravity.json'
content_hash: 'sha256:21f20b7c993dff89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# videoGravity

<sub>Instance Property</sub>

A string that specifies how the video displays within the bounds of the view controller’s view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var videoGravity: AVLayerVideoGravity { get set }
```

## Discussion

The player view controller supports the following video gravity values: [resizeAspect](../../avfoundation/avlayervideogravity/resizeaspect.md), [resizeAspectFill](../../avfoundation/avlayervideogravity/resizeaspectfill.md), and [resize](../../avfoundation/avlayervideogravity/resize.md).

The default value is [resizeAspect](../../avfoundation/avlayervideogravity/resizeaspect.md).

## See Also

### Configuring presentation

- [showsPlaybackControls](showsplaybackcontrols.md) — A Boolean value that indicates whether the player view controller shows playback controls.
- [contentOverlayView](contentoverlayview.md) — A view that displays between the video content and the playback controls.
- [videoBounds](videobounds.md) — The size and position of the video image within the bounds of the view controller’s view.
- [showsTimecodes](showstimecodes.md) — A Boolean value that determines whether the player view displays timecodes, if available.
- [appliesPreferredDisplayCriteriaAutomatically](appliespreferreddisplaycriteriaautomatically.md) — A Boolean value that indicates whether the view controller automatically sets the screen’s display criteria to match that of the currently playing asset.
