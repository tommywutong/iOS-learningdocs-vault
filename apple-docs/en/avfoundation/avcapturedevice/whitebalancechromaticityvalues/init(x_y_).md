---
title: 'init(x:y:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/whitebalancechromaticityvalues/init(x:y:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancechromaticityvalues/init(x:y:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/whitebalancechromaticityvalues/init%28x%3Ay%3A%29.json'
content_hash: 'sha256:22157e1e882c50eb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [WhiteBalanceChromaticityValues](../whitebalancechromaticityvalues.md)

# init(x:y:)

<sub>Initializer</sub>

Creates a structure for white balance chromaticity values from its x and y coordinates.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
init(x: Float, y: Float)
```

## Parameters

- `x` — The x-coordinate in the CIE 1931 chromaticity diagram, which spans the range between `0` and `0.8`.

- `y` — The y-coordinate in the CIE 1931 chromaticity diagram, which spans the range between `0` and `0.85`.

## See Also

### Creating chromaticity values

- [init()](<init().md>) — Creates a structure for white balance chromaticity values.
