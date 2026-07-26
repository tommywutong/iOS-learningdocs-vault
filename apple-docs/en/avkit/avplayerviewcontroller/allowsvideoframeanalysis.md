---
title: allowsVideoFrameAnalysis
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 18.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/allowsvideoframeanalysis
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/allowsvideoframeanalysis'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/allowsvideoframeanalysis.json'
content_hash: 'sha256:dbf2ec05c39ed674'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# allowsVideoFrameAnalysis

<sub>Instance Property</sub>

A Boolean value that indicates whether to perform video frame analysis.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var allowsVideoFrameAnalysis: Bool { get set }
```

## Discussion

If the value is `true`, a player view controller tries to find objects, text, and people when you pause media playback. If it finds an object, the user is able to interact with it using a long press to present a context menu.

The default value is `true`.

## See Also

### Configuring frame analysis

- [toggleLookupAction](togglelookupaction.md) — An action that enables the visual lookup interface.
- [videoFrameAnalysisTypes](videoframeanalysistypes.md) — The types of analysis a player view controller performs on a paused video frame.
- [AVVideoFrameAnalysisType](../avvideoframeanalysistype.md) — Constants that define the types of analysis a player view controller may perform on a paused video frame.
