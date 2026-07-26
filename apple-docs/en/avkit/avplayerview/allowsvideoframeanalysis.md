---
title: allowsVideoFrameAnalysis
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerview/allowsvideoframeanalysis
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/allowsvideoframeanalysis'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/allowsvideoframeanalysis.json'
content_hash: 'sha256:8f966e4fdcb313e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# allowsVideoFrameAnalysis

<sub>Instance Property</sub>

A Boolean value that indicates whether to perform video frame analysis.

<sub>macOS</sub>

```swift
var allowsVideoFrameAnalysis: Bool { get set }
```

## Discussion

If the value is `true`, a player view tries to find objects, text, and people when you pause media playback. If it finds an object, the user is able to interact with it using a long press to present a context menu.

The default value is `true`.

## See Also

### Configuring frame analysis

- [videoFrameAnalysisTypes](videoframeanalysistypes.md)
- [AVVideoFrameAnalysisType](../avvideoframeanalysistype.md) — Constants that define the types of analysis a player view controller may perform on a paused video frame.
