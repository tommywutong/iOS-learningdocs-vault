---
title: mirroringSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（6.0 起废弃）, iPadOS 4.0+（6.0 起废弃）, Mac Catalyst 14.0+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturevideopreviewlayer/mirroringsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/mirroringsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideopreviewlayer/mirroringsupported.json'
content_hash: 'sha256:b987529753264d9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md)

# mirroringSupported

<sub>Instance Property</sub>

Indicates whether the layer display supports mirroring.

> [!warning] Deprecated
> Use [supportsVideoMirroring](../avcaptureconnection/isvideomirroringsupported.md) ([AVCaptureConnection](../avcaptureconnection.md)) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly, getter=isMirroringSupported) BOOL mirroringSupported;
```

## See Also

### Layer configuration

- [orientation](orientation.md) — The layer’s orientation. _(deprecated)_
- [orientationSupported](orientationsupported.md) — Indicates whether the layer display supports changing the orientation. _(deprecated)_
- [mirrored](mirrored.md) — Indicates whether the layer display is mirrored. _(deprecated)_
- [automaticallyAdjustsMirroring](automaticallyadjustsmirroring.md) — Indicates whether the layer display automatically adjusts mirroring. _(deprecated)_
