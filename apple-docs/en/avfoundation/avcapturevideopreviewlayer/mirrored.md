---
title: mirrored
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（6.0 起废弃）, iPadOS 4.0+（6.0 起废弃）, Mac Catalyst 14.0+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturevideopreviewlayer/mirrored
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/mirrored'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideopreviewlayer/mirrored.json'
content_hash: 'sha256:937a15c69cf05c11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md)

# mirrored

<sub>Instance Property</sub>

Indicates whether the layer display is mirrored.

> [!warning] Deprecated
> Use [videoMirrored](../avcaptureconnection/isvideomirrored.md) ([AVCaptureConnection](../avcaptureconnection.md)) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, getter=isMirrored) BOOL mirrored;
```

## Discussion

To change the value of this property, the value of [automaticallyAdjustsMirroring](automaticallyadjustsmirroring.md) must be [false](../../swift/false.md).

Mirroring is not supported on all hardware configurations. You should check the value of [supportsVideoMirroring](../avcaptureconnection/isvideomirroringsupported.md) (`AVCaptureConnection`) before attempting to change this value.

## See Also

### Layer configuration

- [orientation](orientation.md) — The layer’s orientation. _(deprecated)_
- [orientationSupported](orientationsupported.md) — Indicates whether the layer display supports changing the orientation. _(deprecated)_
- [mirroringSupported](mirroringsupported.md) — Indicates whether the layer display supports mirroring. _(deprecated)_
- [automaticallyAdjustsMirroring](automaticallyadjustsmirroring.md) — Indicates whether the layer display automatically adjusts mirroring. _(deprecated)_
