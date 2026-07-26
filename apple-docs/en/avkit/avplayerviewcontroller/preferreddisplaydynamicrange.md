---
title: preferredDisplayDynamicRange
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/preferreddisplaydynamicrange
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/preferreddisplaydynamicrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/preferreddisplaydynamicrange.json'
content_hash: 'sha256:f6012a5d6e082bad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# preferredDisplayDynamicRange

<sub>Instance Property</sub>

Describes how High Dynamic Range (HDR) video content renders.

<sub>iOS, iPadOS, Mac Catalyst</sub>

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
