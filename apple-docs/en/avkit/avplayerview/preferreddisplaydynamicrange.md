---
title: preferredDisplayDynamicRange
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerview/preferreddisplaydynamicrange
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/preferreddisplaydynamicrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/preferreddisplaydynamicrange.json'
content_hash: 'sha256:104a9db6ab0716f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# preferredDisplayDynamicRange

<sub>Instance Property</sub>

Describes how High Dynamic Range (HDR) video content renders.

<sub>macOS</sub>

```swift
var preferredDisplayDynamicRange: AVDisplayDynamicRange { get set }
```

## Discussion

Defaults to `AVDisplayDynamicRangeAutomatic`.

> [!note] Note
> This property will only have effect if the video content supports HDR.

## See Also

### High dynamic range

- [AVDisplayDynamicRange](../avdisplaydynamicrange.md) — Describes how High Dynamic Range (HDR) video content renders.
