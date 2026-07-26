---
title: customVideoCompositor
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetreadervideocompositionoutput/customvideocompositor
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput/customvideocompositor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreadervideocompositionoutput/customvideocompositor.json'
content_hash: 'sha256:1c8a1b8adb02c2bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderVideoCompositionOutput](../avassetreadervideocompositionoutput.md)

# customVideoCompositor

<sub>Instance Property</sub>

A custom video compositor for the output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var customVideoCompositor: (any AVVideoCompositing)? { get }
```

## Discussion

This property is `nil` if there isn’t a custom video compositor, or if the internal video compositor is in use.

## See Also

### Configuring video settings

- [videoComposition](videocomposition.md) — The video composition to use for the output.
