---
title: preventsDisplaySleepDuringVideoPlayback
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayer/preventsdisplaysleepduringvideoplayback
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/preventsdisplaysleepduringvideoplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer/preventsdisplaysleepduringvideoplayback.json'
content_hash: 'sha256:4caac66e230f3456'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferDisplayLayer](../avsamplebufferdisplaylayer.md)

# preventsDisplaySleepDuringVideoPlayback

<sub>Instance Property</sub>

A Boolean value that indicates whether the layer prevents the system from sleeping during video playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var preventsDisplaySleepDuringVideoPlayback: Bool { get set }
```

## Discussion

Setting this property to [false](../../swift/false.md) doesn’t force the display to sleep; it only stops preventing display sleep. Other apps or frameworks within your app may still be preventing display sleep for various reasons.

The default value is [true](../../swift/true.md) in iOS, tvOS, and Mac Catalyst. The default value in macOS is [false](../../swift/false.md).

> [!note] Note
> If you enqueue sample buffers for playback at the user’s request, you should ensure that you set the value of this property to [true](../../swift/true.md). If your app isn’t displaying video as part of the user’s primary focus, set the value of this property to [false](../../swift/false.md).

## See Also

### Preventing backgrounding

- [preventsAutomaticBackgroundingDuringVideoPlayback](preventsautomaticbackgroundingduringvideoplayback.md) — A Boolean value that indicates whether video playback prevents the system from automatically backgrounding an app.
