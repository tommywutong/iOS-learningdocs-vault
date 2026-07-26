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
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayer/preventsautomaticbackgroundingduringvideoplayback
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/preventsautomaticbackgroundingduringvideoplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer/preventsautomaticbackgroundingduringvideoplayback.json'
content_hash: 'sha256:d2c8cee732fbc6f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferDisplayLayer](../avsamplebufferdisplaylayer.md)

# preventsAutomaticBackgroundingDuringVideoPlayback

<sub>Instance Property</sub>

A Boolean value that indicates whether video playback prevents the system from automatically backgrounding an app.

<sub>visionOS</sub>

```swift
var preventsAutomaticBackgroundingDuringVideoPlayback: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md), which indicates the system doesn’t automatically background an app while playing video. The value of this property doesn’t prevent the user from backgrounding an app.

> [!note] Note
> When enqueuing sample buffers for playback at the user’s request, set the value to [true](../../swift/true.md), and when video playback isn’t the user’s primary focus, set it to [false](../../swift/false.md).

## See Also

### Preventing backgrounding

- [preventsDisplaySleepDuringVideoPlayback](preventsdisplaysleepduringvideoplayback.md) — A Boolean value that indicates whether the layer prevents the system from sleeping during video playback.
