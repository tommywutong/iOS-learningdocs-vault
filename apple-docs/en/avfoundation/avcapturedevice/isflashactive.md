---
title: isFlashActive
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（10.0 起废弃）, iPadOS 5.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturedevice/isflashactive
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isflashactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isflashactive.json'
content_hash: 'sha256:d1223f713f231fef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isFlashActive

<sub>Instance Property</sub>

A Boolean value that indicates whether the flash is currently active.

> [!warning] Deprecated
> Use [isFlashScene](../avcapturephotooutput/isflashscene.md) on [AVCapturePhotoOutput](../avcapturephotooutput.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isFlashActive: Bool { get }
```

## Discussion

When the flash is active, it flashes when capturing a photo.

This property is key-value observable.

## See Also

### Configuring flash settings

- [hasFlash](hasflash.md) — A Boolean value that indicates whether the capture device has a flash.
- [flashAvailable](isflashavailable.md) — A Boolean value that indicates whether the flash is currently available for use.
- [flashMode](flashmode-swift.property.md) — The device’s current flash mode. _(deprecated)_
- [- isFlashModeSupported:](<isflashmodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the given flash mode. _(deprecated)_
- [FlashMode](flashmode-swift.enum.md) — Constants that specify the flash modes of a capture device.
