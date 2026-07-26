---
title: orientationSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（6.0 起废弃）, iPadOS 4.0+（6.0 起废弃）, Mac Catalyst 14.0+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturevideopreviewlayer/orientationsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/orientationsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideopreviewlayer/orientationsupported.json'
content_hash: 'sha256:b78ae92163f5afeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md)

# orientationSupported

<sub>Instance Property</sub>

Indicates whether the layer display supports changing the orientation.

> [!warning] Deprecated
> Use [supportsVideoOrientation](../avcaptureconnection/isvideoorientationsupported.md) ([AVCaptureConnection](../avcaptureconnection.md)) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly, getter=isOrientationSupported) BOOL orientationSupported;
```

## See Also

### Layer configuration

- [orientation](orientation.md) — The layer’s orientation. _(deprecated)_
- [mirrored](mirrored.md) — Indicates whether the layer display is mirrored. _(deprecated)_
- [mirroringSupported](mirroringsupported.md) — Indicates whether the layer display supports mirroring. _(deprecated)_
- [automaticallyAdjustsMirroring](automaticallyadjustsmirroring.md) — Indicates whether the layer display automatically adjusts mirroring. _(deprecated)_
