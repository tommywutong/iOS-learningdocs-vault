---
title: exposurePointOfInterest
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/exposurepointofinterest
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposurepointofinterest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/exposurepointofinterest.json'
content_hash: 'sha256:45d9ff1935f2a6c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# exposurePointOfInterest

<sub>Instance Property</sub>

The point of interest for exposure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var exposurePointOfInterest: CGPoint { get set }
```

## Discussion

Setting a value for this property doesn’t initiate an exposure rebalancing operation. To set exposure using a point of interest, first set this property’s value, then set the [exposureMode](exposuremode-swift.property.md) property to [AVCaptureExposureModeAutoExpose](exposuremode-swift.enum/autoexpose.md) or [AVCaptureExposureModeContinuousAutoExposure](exposuremode-swift.enum/continuousautoexposure.md).

This property’s [CGPoint](../../corefoundation/cgpoint.md) value uses a coordinate system where `{0,0}` is the top-left of the picture area and `{1,1}` is the bottom-right. This coordinate system is always relative to a landscape device orientation with the home button on the right, regardless of the actual device orientation. You can convert between this coordinate system and view coordinates using [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md) methods.

Before changing the value of this property, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you’re done configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

## See Also

### Setting an exposure point of interest

- [exposurePointOfInterestSupported](isexposurepointofinterestsupported.md) — A Boolean value that indicates whether the device supports a point of interest for exposure.
