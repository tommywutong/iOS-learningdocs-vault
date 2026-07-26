---
title: preventsDisplaySleepDuringVideoPlayback
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/preventsdisplaysleepduringvideoplayback
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/preventsdisplaysleepduringvideoplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/preventsdisplaysleepduringvideoplayback.json'
content_hash: 'sha256:aba5e8841b42f8a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# preventsDisplaySleepDuringVideoPlayback

<sub>Instance Property</sub>

A Boolean value that indicates whether video playback prevents display and device sleep.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
nonisolated var preventsDisplaySleepDuringVideoPlayback: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md) in iOS, tvOS and Mac Catalyst apps, and [false](../../swift/false.md) in macOS.

Setting this property to [false](../../swift/false.md) doesn’t force the display to sleep, it only stops preventing display sleep. Other apps, or frameworks within your app may still prevent display sleep for various reasons.

> [!note] Note
> Before macOS 13, iOS 16, tvOS 16, and watchOS 9, you can only access this property from the main thread or queue.

## See Also

### Preventing sleep and backgrounding

- [preventsAutomaticBackgroundingDuringVideoPlayback](preventsautomaticbackgroundingduringvideoplayback.md) — A Boolean value that indicates whether video playback prevents the system from automatically backgrounding the app.
