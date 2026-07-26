---
title: 'isFlashModeSupported(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avcapturedevice/isflashmodesupported(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isflashmodesupported(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isflashmodesupported%28_%3A%29.json'
content_hash: 'sha256:075c4adb020687ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isFlashModeSupported(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the device supports the given flash mode.

> [!warning] Deprecated
> Use [supportedFlashModes](../avcapturephotooutput/supportedflashmodes-1n6nm.md) on [AVCapturePhotoOutput](../avcapturephotooutput.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func isFlashModeSupported(_ flashMode: AVCaptureDevice.FlashMode) -> Bool
```

## Parameters

- `flashMode` — A flash mode to test if the device supports.

## Return Value

[true](../../swift/true.md) if the device supports the flash mode; otherwise, [false](../../swift/false.md).

## See Also

### Configuring flash settings

- [hasFlash](hasflash.md) — A Boolean value that indicates whether the capture device has a flash.
- [flashAvailable](isflashavailable.md) — A Boolean value that indicates whether the flash is currently available for use.
- [flashActive](isflashactive.md) — A Boolean value that indicates whether the flash is currently active. _(deprecated)_
- [flashMode](flashmode-swift.property.md) — The device’s current flash mode. _(deprecated)_
- [FlashMode](flashmode-swift.enum.md) — Constants that specify the flash modes of a capture device.
