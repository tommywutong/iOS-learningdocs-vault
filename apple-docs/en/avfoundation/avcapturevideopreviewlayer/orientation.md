---
title: orientation
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（6.0 起废弃）, iPadOS 4.0+（6.0 起废弃）, Mac Catalyst 14.0+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturevideopreviewlayer/orientation
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/orientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideopreviewlayer/orientation.json'
content_hash: 'sha256:11713cf3d701ead2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md)

# orientation

<sub>Instance Property</sub>

The layer’s orientation.

> [!warning] Deprecated
> Use [videoOrientation](../avcaptureconnection/videoorientation.md) ([AVCaptureConnection](../avcaptureconnection.md)) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) AVCaptureVideoOrientation orientation;
```

## Discussion

Changes in orientation are not supported on all hardware configurations. You should check the value of [supportsVideoOrientation](../avcaptureconnection/isvideoorientationsupported.md) (`AVCaptureConnection`) before attempting to change the orientation of the receiver. An exception is raised if this requirement is ignored.

## See Also

### Layer configuration

- [orientationSupported](orientationsupported.md) — Indicates whether the layer display supports changing the orientation. _(deprecated)_
- [mirrored](mirrored.md) — Indicates whether the layer display is mirrored. _(deprecated)_
- [mirroringSupported](mirroringsupported.md) — Indicates whether the layer display supports mirroring. _(deprecated)_
- [automaticallyAdjustsMirroring](automaticallyadjustsmirroring.md) — Indicates whether the layer display automatically adjusts mirroring. _(deprecated)_
