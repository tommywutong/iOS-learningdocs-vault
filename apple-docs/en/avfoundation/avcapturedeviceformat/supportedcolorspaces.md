---
title: supportedColorSpaces
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeviceformat/supportedcolorspaces
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/supportedcolorspaces'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeviceformat/supportedcolorspaces.json'
content_hash: 'sha256:3ddffd8ae48a3ac4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [Format](../avcapturedevice/format.md)

# supportedColorSpaces

<sub>Instance Property</sub>

The list of color spaces the format supports for image and video capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * supportedColorSpaces;
```

## Discussion

The [NSNumber](../../foundation/nsnumber.md) objects in this array contain [AVCaptureColorSpace](../avcapturecolorspace.md) values. The ordering of the array is such that spaces with a narrower color gamut appear before those with wider color gamuts.

All devices and formats support capture in the sRGB color space. Some devices and formats can also capture in the P3 color space, which includes a much wider gamut of colors than the sRGB color space. (Content captured in the P3 color space is viewable on all devices. Devices without wide-color displays render P3 content as accurately as possible in the sRGB color gamut). By default, a capture session automatically enables wide-gamut capture for supported devices and capture workflows (for details, see the [AVCaptureSession](../avcapturesession.md) property [automaticallyConfiguresCaptureDeviceForWideColor](../avcapturesession/automaticallyconfigurescapturedeviceforwidecolor.md)).

## See Also

### Determining color support

- [globalToneMappingSupported](../avcapturedevice/format/isglobaltonemappingsupported.md) — A Boolean value that indicates whether the format supports global tone mapping.
