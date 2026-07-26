---
title: 'init(videoDisplay:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemrenderedlegibleoutput/init(videodisplay:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutput/init(videodisplay:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemrenderedlegibleoutput/init%28videodisplay%3A%29.json'
content_hash: 'sha256:2286b5ac219df215'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemRenderedLegibleOutput](../avplayeritemrenderedlegibleoutput.md)

# init(videoDisplay:)

<sub>Initializer</sub>

Creates a rendered legible output object.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
init(videoDisplay videoDisplaySize: CGSize)
```

## Parameters

- `videoDisplaySize` — The size of the video display.

## Discussion

You can also choose to reset the [videoDisplaySize](videodisplaysize.md) value after initialization or during playback.

> [!important] Important
> Attempting to set a video display size of [zero](../../corefoundation/cgsize/zero.md) results in the system throwing an exception.
