---
title: focusPointOfInterest
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/focuspointofinterest
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/focuspointofinterest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/focuspointofinterest.json'
content_hash: 'sha256:307d912b82b8d3af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# focusPointOfInterest

<sub>Instance Property</sub>

The point of interest for focusing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var focusPointOfInterest: CGPoint { get set }
```

## Discussion

Setting a value for this property doesn’t initiate a focusing operation. To focus the camera on a point of interest, first set this property’s value, then set the [focusMode](focusmode-swift.property.md) property to [AVCaptureFocusModeAutoFocus](focusmode-swift.enum/autofocus.md) or [AVCaptureFocusModeContinuousAutoFocus](focusmode-swift.enum/continuousautofocus.md).

This property’s [CGPoint](../../corefoundation/cgpoint.md) value uses a coordinate system where `{0,0}` is the top-left of the picture area and `{1,1}` is the bottom-right. This coordinate system is always relative to a landscape device orientation with the home button on the right, regardless of the actual device orientation. You can convert between this coordinate system and view coordinates using [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md) methods.

Before changing the value of this property, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

## See Also

### Setting a focus point of interest

- [focusPointOfInterestSupported](isfocuspointofinterestsupported.md) — A Boolean value that indicates whether the device supports a point of interest for focus.
