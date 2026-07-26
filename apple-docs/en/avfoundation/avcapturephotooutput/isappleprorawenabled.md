---
title: isAppleProRAWEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.3+, iPadOS 14.3+, Mac Catalyst 14.3+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/isappleprorawenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isappleprorawenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/isappleprorawenabled.json'
content_hash: 'sha256:dfa45ee6acd86671'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isAppleProRAWEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether you’ve configured the photo output to deliver Apple ProRAW formats.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isAppleProRAWEnabled: Bool { get set }
```

## Discussion

If [appleProRAWSupported](isappleprorawsupported.md) returns [true](../../swift/true.md), you can enable Apple ProRAW capture by setting this property to [true](../../swift/true.md). Compared to photos taken in Bayer RAW format, the system demosaics and partially processes Apple ProRAW photos. They’re still scene-referred, however, and allow capturing RAW photos in modes that don’t have a traditional Bayer RAW format available, such as modes that rely on fusing multiple captures.

Apple ProRAW formats aren’t supported on all platforms and devices. You can determine the pixel formats the system supports by querying the [availableRawPhotoPixelFormatTypes](availablerawphotopixelformattypes-9t9k5.md) property. Use the [+ isBayerRAWPixelFormat:](<isbayerrawpixelformat(__).md>) or [+ isAppleProRAWPixelFormat:](<isappleprorawpixelformat(__).md>) method to determine whether the pixel format is Bayer RAW or Apple ProRAW, respectively.

This property is key-value observable.

> [!tip] Tip
> Set this property to [true](../../swift/true.md) before calling [- startRunning](<../avcapturesession/startrunning().md>) on the capture session. Enabling this property later requires a lengthy reconfiguration of the capture pipeline.

## See Also

### Configuring ProRAW support

- [appleProRAWSupported](isappleprorawsupported.md) — A Boolean value that indicates whether the current device and configuration supports Apple ProRAW pixel formats.
