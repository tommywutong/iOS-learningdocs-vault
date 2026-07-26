---
title: preferredVideoStabilizationMode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureconnection/preferredvideostabilizationmode
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/preferredvideostabilizationmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/preferredvideostabilizationmode.json'
content_hash: 'sha256:fe666ac33d05b175'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# preferredVideoStabilizationMode

<sub>Instance Property</sub>

The stabilization mode that’s the most appropriate for a video connection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var preferredVideoStabilizationMode: AVCaptureVideoStabilizationMode { get set }
```

## Discussion

The property only applies to a video connection, and defaults to [AVCaptureVideoStabilizationModeOff](../avcapturevideostabilizationmode/off.md).

You can enable video stabilization by setting it to an available stabilization mode (other than [AVCaptureVideoStabilizationModeOff](../avcapturevideostabilizationmode/off.md)). Video stabilization introduces additional latency into the video capture pipeline and may consume more system memory, depending on the stabilization mode and format. If a stabilization mode isn’t available, the connection sets its [activeVideoStabilizationMode](activevideostabilizationmode.md) property to [AVCaptureVideoStabilizationModeOff](../avcapturevideostabilizationmode/off.md). You can make the connection use an appropriate capture format and frame rate by setting the property to [AVCaptureVideoStabilizationModeAuto](../avcapturevideostabilizationmode/auto.md).

> [!note] Note
> Devices with a video stabilization feature may only support a subset of available source formats.

Use key-value observing with the [activeVideoStabilizationMode](activevideostabilizationmode.md) property to determine which stabilization mode is in use.

You can monitor the [activeVideoStabilizationMode](activevideostabilizationmode.md) property to detect which stabilization mode the connection’s using. See [NSKeyValueObserving](../../objectivec/nskeyvalueobserving.md) and [Using Key-Value Observing in Swift](../../swift/using-key-value-observing-in-swift.md) for more information.

## See Also

### Stabilizing video

- [supportsVideoStabilization](isvideostabilizationsupported.md) — A Boolean value that indicates whether this connection supports video stabilization.
- [activeVideoStabilizationMode](activevideostabilizationmode.md) — The connection’s current stabilization mode.
