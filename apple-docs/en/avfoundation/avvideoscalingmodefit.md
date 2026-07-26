---
title: AVVideoScalingModeFit
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideoscalingmodefit
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideoscalingmodefit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideoscalingmodefit.json'
content_hash: 'sha256:be5b796eb7796932'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoScalingModeFit

<sub>Global Variable</sub>

The string identifier for scaling a video to fit the surrounding view’s dimensions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let AVVideoScalingModeFit: String
```

## Discussion

This mode crops the video to remove the edge processing region, preserving the aspect ratio of the cropped source by reducing the specified width or height, if necessary. It doesn’t scale a small source up to larger dimensions.

## See Also

### Scaling mode

- [AVVideoScalingModeKey](avvideoscalingmodekey.md) — A key to retrieve the video scaling mode from a dictionary.
- [AVVideoScalingModeResize](avvideoscalingmoderesize.md) — The string identifier for resizing a video to fit the surrounding view’s dimensions.
- [AVVideoScalingModeResizeAspect](avvideoscalingmoderesizeaspect.md) — The string identifier for resizing a video to its surrounding view’s shorter dimension while preserving its aspect ratio.
- [AVVideoScalingModeResizeAspectFill](avvideoscalingmoderesizeaspectfill.md) — The string identifier for resizing a video to fit the surrounding view’s longer dimension while preserving aspect ratio.
