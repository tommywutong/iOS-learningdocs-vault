---
title: AVVideoScalingModeResize
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideoscalingmoderesize
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideoscalingmoderesize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideoscalingmoderesize.json'
content_hash: 'sha256:2b0b0eb008bdd4d5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoScalingModeResize

<sub>Global Variable</sub>

The string identifier for resizing a video to fit the surrounding view’s dimensions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
let AVVideoScalingModeResize: String
```

## Discussion

This mode crops the video to remove the edge processing region and scales the remainder to the destination area. It doesn’t preserve the aspect ratio.

## See Also

### Scaling mode

- [AVVideoScalingModeFit](avvideoscalingmodefit.md) — The string identifier for scaling a video to fit the surrounding view’s dimensions.
- [AVVideoScalingModeKey](avvideoscalingmodekey.md) — A key to retrieve the video scaling mode from a dictionary.
- [AVVideoScalingModeResizeAspect](avvideoscalingmoderesizeaspect.md) — The string identifier for resizing a video to its surrounding view’s shorter dimension while preserving its aspect ratio.
- [AVVideoScalingModeResizeAspectFill](avvideoscalingmoderesizeaspectfill.md) — The string identifier for resizing a video to fit the surrounding view’s longer dimension while preserving aspect ratio.
