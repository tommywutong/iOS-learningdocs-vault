---
title: automaticallyAdjustsMirroring
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（6.0 起废弃）, iPadOS 4.0+（6.0 起废弃）, Mac Catalyst 14.0+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturevideopreviewlayer/automaticallyadjustsmirroring
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/automaticallyadjustsmirroring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideopreviewlayer/automaticallyadjustsmirroring.json'
content_hash: 'sha256:26fcabbe27d41c2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md)

# automaticallyAdjustsMirroring

<sub>Instance Property</sub>

Indicates whether the layer display automatically adjusts mirroring.

> [!warning] Deprecated
> Use [automaticallyAdjustsVideoMirroring](../avcaptureconnection/automaticallyadjustsvideomirroring.md) ([AVCaptureConnection](../avcaptureconnection.md)) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) BOOL automaticallyAdjustsMirroring;
```

## Discussion

For some session configurations, preview will be mirrored by default.

When the value of this property is [true](../../swift/true.md), the value of [mirrored](mirrored.md) may change depending on the configuration of the session, for example after switching to a different capture device input.

## See Also

### Layer configuration

- [orientation](orientation.md) — The layer’s orientation. _(deprecated)_
- [orientationSupported](orientationsupported.md) — Indicates whether the layer display supports changing the orientation. _(deprecated)_
- [mirrored](mirrored.md) — Indicates whether the layer display is mirrored. _(deprecated)_
- [mirroringSupported](mirroringsupported.md) — Indicates whether the layer display supports mirroring. _(deprecated)_
