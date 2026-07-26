---
title: centerStageRectOfInterestSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/centerstagerectofinterestsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/centerstagerectofinterestsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/centerstagerectofinterestsupported.json'
content_hash: 'sha256:56bb4c5c86c25e83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# centerStageRectOfInterestSupported

<sub>Instance Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly, getter=isCenterStageRectOfInterestSupported) BOOL centerStageRectOfInterestSupported;
```

## Discussion

Indicates whether the device supports the Center Stage Rect of Interest feature.

This property returns YES if the device supports Center Stage Rect of Interest.

## See Also

### Configuring Center Stage

- [centerStageActive](iscenterstageactive.md) — A Boolean value that indicates whether Center Stage is active on a device.
- [centerStageEnabled](iscenterstageenabled.md) — A Boolean value that indicates whether a user or an app enabled Center Stage on a device.
- [centerStageRectOfInterest](centerstagerectofinterest.md) — The effective region within the output pixel buffer to perform Center Stage framing.
- [centerStageControlMode](centerstagecontrolmode-swift.type.property.md) — A value that indicates the current mode of Center Stage control.
- [CenterStageControlMode](centerstagecontrolmode-swift.enum.md) — Constants that indicate the current Center Stage control mode.
