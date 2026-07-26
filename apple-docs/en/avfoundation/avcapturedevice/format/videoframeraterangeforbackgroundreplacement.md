---
title: videoFrameRateRangeForBackgroundReplacement
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/videoframeraterangeforbackgroundreplacement
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforbackgroundreplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforbackgroundreplacement.json'
content_hash: 'sha256:1eb2e39c82f90b33'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# videoFrameRateRangeForBackgroundReplacement

<sub>Instance Property</sub>

The minimum and maximum frame rates available when Background Replacement is active.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var videoFrameRateRangeForBackgroundReplacement: AVFrameRateRange? { get }
```

## Discussion

Devices may support a limited frame rate range when Background Replacement is active. If this device format doesn’t support this feature, the value of this property is `nil`.

## See Also

### Determining background replacement support

- [backgroundReplacementSupported](isbackgroundreplacementsupported.md) — A Boolean value that indicates whether the format supports background replacement.
