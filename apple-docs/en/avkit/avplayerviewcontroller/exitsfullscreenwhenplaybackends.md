---
title: exitsFullScreenWhenPlaybackEnds
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/exitsfullscreenwhenplaybackends
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/exitsfullscreenwhenplaybackends'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/exitsfullscreenwhenplaybackends.json'
content_hash: 'sha256:f883b8be0a23b09e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# exitsFullScreenWhenPlaybackEnds

<sub>Instance Property</sub>

A Boolean value that indicates whether the player exits full-screen mode when playback ends.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var exitsFullScreenWhenPlaybackEnds: Bool { get set }
```

## Discussion

If you enqueue multiple player items, the player exits full-screen mode after it plays all remaining items in the queue.

The default value is `false`.

## See Also

### Managing full-screen behavior

- [entersFullScreenWhenPlaybackBegins](entersfullscreenwhenplaybackbegins.md) — A Boolean value that determines whether the player automatically displays in full screen when the user taps the play button.
