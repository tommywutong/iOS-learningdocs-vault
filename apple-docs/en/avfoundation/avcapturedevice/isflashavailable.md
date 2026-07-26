---
title: isFlashAvailable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isflashavailable
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isflashavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isflashavailable.json'
content_hash: 'sha256:0c88f4a8ce029995'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isFlashAvailable

<sub>Instance Property</sub>

A Boolean value that indicates whether the flash is currently available for use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isFlashAvailable: Bool { get }
```

## Discussion

The flash may become unavailable if, for example, the device overheats and needs to cool off.

This property is key-value observable.

## See Also

### Configuring flash settings

- [hasFlash](hasflash.md) — A Boolean value that indicates whether the capture device has a flash.
- [flashActive](isflashactive.md) — A Boolean value that indicates whether the flash is currently active. _(deprecated)_
- [flashMode](flashmode-swift.property.md) — The device’s current flash mode. _(deprecated)_
- [- isFlashModeSupported:](<isflashmodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the given flash mode. _(deprecated)_
- [FlashMode](flashmode-swift.enum.md) — Constants that specify the flash modes of a capture device.
