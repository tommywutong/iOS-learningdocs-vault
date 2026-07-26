---
title: activeDepthDataFormat
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/activedepthdataformat
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/activedepthdataformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/activedepthdataformat.json'
content_hash: 'sha256:daed47e4cd0f4945'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# activeDepthDataFormat

<sub>Instance Property</sub>

The currently active depth data format of the capture device.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var activeDepthDataFormat: AVCaptureDevice.Format? { get set }
```

## Discussion

You must obtain exclusive access to the device by calling [- lockForConfiguration:](<lockforconfiguration().md>) before setting this property value.

You can set this property only to formats present in the active format’s [supportedDepthDataFormats](format/supporteddepthdataformats.md) array. Attempting to set an unsupported format throws an exception.

You can’t set the frame rate of depth data directly. Instead, the system synchronizes the depth data frame rate to the device’s [activeVideoMinFrameDuration](activevideominframeduration.md) and [activeVideoMaxFrameDuration](activevideomaxframeduration.md) values. It may match the device’s current frame rate, or lower, if the system can’t produce depth data fast enough for the active video frame rate.

Delivery of depth data to a [AVCaptureDepthDataOutput](../avcapturedepthdataoutput.md) may increase the system load, resulting in a reduced video frame rate for thermal sustainability.

On devices where depth data isn’t supported, this property value is `nil`.

This property is key-value observable.

## See Also

### Configuring capture formats

- [formats](formats.md) — The capture formats a device supports.
- [activeFormat](activeformat.md) — The capture format in use by the device.
- [Format](format.md) — A class that defines media formats and capture settings that capture devices support.
