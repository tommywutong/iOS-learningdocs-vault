---
title: hasFlash
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/hasflash
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/hasflash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/hasflash.json'
content_hash: 'sha256:a0feb44b6001aa50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# hasFlash

<sub>Instance Property</sub>

A Boolean value that indicates whether the capture device has a flash.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var hasFlash: Bool { get }
```

## Discussion

This property is key-value observable.

## See Also

### Configuring flash settings

- [flashAvailable](isflashavailable.md) — A Boolean value that indicates whether the flash is currently available for use.
- [flashActive](isflashactive.md) — A Boolean value that indicates whether the flash is currently active. _(deprecated)_
- [flashMode](flashmode-swift.property.md) — The device’s current flash mode. _(deprecated)_
- [- isFlashModeSupported:](<isflashmodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the given flash mode. _(deprecated)_
- [FlashMode](flashmode-swift.enum.md) — Constants that specify the flash modes of a capture device.
