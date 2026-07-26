---
title: preventsAutomaticBackgroundingDuringVideoPlayback
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/preventsautomaticbackgroundingduringvideoplayback
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/preventsautomaticbackgroundingduringvideoplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/preventsautomaticbackgroundingduringvideoplayback.json'
content_hash: 'sha256:a4f913699bfc3409'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# preventsAutomaticBackgroundingDuringVideoPlayback

<sub>Instance Property</sub>

A Boolean value that indicates whether video playback prevents the system from automatically backgrounding the app.

<sub>visionOS</sub>

```swift
nonisolated var preventsAutomaticBackgroundingDuringVideoPlayback: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md), which indicates the system doesn’t automatically background an app while it’s actively playing video. A user may still choose to background an app.

## See Also

### Preventing sleep and backgrounding

- [preventsDisplaySleepDuringVideoPlayback](preventsdisplaysleepduringvideoplayback.md) — A Boolean value that indicates whether video playback prevents display and device sleep.
