---
title: flashMode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturedevice/flashmode-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/flashmode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/flashmode-swift.property.json'
content_hash: 'sha256:575d56914f1e9d01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# flashMode

<sub>Instance Property</sub>

The device’s current flash mode.

> [!warning] Deprecated
> Use [flashMode](../avcapturephotosettings/flashmode.md) on [AVCapturePhotoSettings](../avcapturephotosettings.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var flashMode: AVCaptureDevice.FlashMode { get set }
```

## Discussion

Before changing the value of this property, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

## See Also

### Configuring flash settings

- [hasFlash](hasflash.md) — A Boolean value that indicates whether the capture device has a flash.
- [flashAvailable](isflashavailable.md) — A Boolean value that indicates whether the flash is currently available for use.
- [flashActive](isflashactive.md) — A Boolean value that indicates whether the flash is currently active. _(deprecated)_
- [- isFlashModeSupported:](<isflashmodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the given flash mode. _(deprecated)_
- [FlashMode](flashmode-swift.enum.md) — Constants that specify the flash modes of a capture device.
