---
title: isCameraCalibrationDataDeliverySupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/iscameracalibrationdatadeliverysupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/iscameracalibrationdatadeliverysupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/iscameracalibrationdatadeliverysupported.json'
content_hash: 'sha256:8db829f6dd7db78d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isCameraCalibrationDataDeliverySupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the photo output currently supports the delivery of camera calibration data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isCameraCalibrationDataDeliverySupported: Bool { get }
```

## Discussion

A photo output can deliver camera calibration data only when it’s [virtualDeviceConstituentPhotoDeliveryEnabled](isvirtualdeviceconstituentphotodeliveryenabled.md) property is `true` and its [contentAwareDistortionCorrectionEnabled](iscontentawaredistortioncorrectionenabled.md) property is `false`. Additionally, the source capture device’s [geometricDistortionCorrectionEnabled](../avcapturedevice/isgeometricdistortioncorrectionenabled.md) property must be `false`.

This property is key-value observable.
