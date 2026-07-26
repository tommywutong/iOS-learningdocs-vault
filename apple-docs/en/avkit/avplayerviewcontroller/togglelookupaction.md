---
title: toggleLookupAction
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 18.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/togglelookupaction
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/togglelookupaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/togglelookupaction.json'
content_hash: 'sha256:fc5135ba476c6848'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# toggleLookupAction

<sub>Instance Property</sub>

An action that enables the visual lookup interface.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var toggleLookupAction: UIAction { get }
```

## Discussion

When a user toggles the lookup UI, the state property is [UIMenuElement.State.on](../../uikit/uimenuelement/state/on.md), and is [UIMenuElement.State.off](../../uikit/uimenuelement/state/off.md) otherwise. The system disables the action’s attributes when there isn’t visual lookup data available or when the media is playing.

## See Also

### Configuring frame analysis

- [allowsVideoFrameAnalysis](allowsvideoframeanalysis.md) — A Boolean value that indicates whether to perform video frame analysis.
- [videoFrameAnalysisTypes](videoframeanalysistypes.md) — The types of analysis a player view controller performs on a paused video frame.
- [AVVideoFrameAnalysisType](../avvideoframeanalysistype.md) — Constants that define the types of analysis a player view controller may perform on a paused video frame.
