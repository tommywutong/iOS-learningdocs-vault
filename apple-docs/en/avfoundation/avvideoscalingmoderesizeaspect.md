---
title: AVVideoScalingModeResizeAspect
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideoscalingmoderesizeaspect
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideoscalingmoderesizeaspect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideoscalingmoderesizeaspect.json'
content_hash: 'sha256:1cb33d0a3635ca01'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoScalingModeResizeAspect

<sub>Global Variable</sub>

The string identifier for resizing a video to its surrounding view’s shorter dimension while preserving its aspect ratio.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let AVVideoScalingModeResizeAspect: String
```

## Discussion

This mode preserves the aspect ratio of the source and fills the remaining areas with black to fit the destination dimensions.

## See Also

### Scaling mode

- [AVVideoScalingModeFit](avvideoscalingmodefit.md) — The string identifier for scaling a video to fit the surrounding view’s dimensions.
- [AVVideoScalingModeKey](avvideoscalingmodekey.md) — A key to retrieve the video scaling mode from a dictionary.
- [AVVideoScalingModeResize](avvideoscalingmoderesize.md) — The string identifier for resizing a video to fit the surrounding view’s dimensions.
- [AVVideoScalingModeResizeAspectFill](avvideoscalingmoderesizeaspectfill.md) — The string identifier for resizing a video to fit the surrounding view’s longer dimension while preserving aspect ratio.
