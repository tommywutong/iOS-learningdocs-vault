---
title: videoGravity
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturevideopreviewlayer/videogravity
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideopreviewlayer/videogravity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideopreviewlayer/videogravity.json'
content_hash: 'sha256:cf769968a652dd5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureVideoPreviewLayer](../avcapturevideopreviewlayer.md)

# videoGravity

<sub>Instance Property</sub>

A value that indicates how the layer displays video content within its bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var videoGravity: AVLayerVideoGravity { get set }
```

## Discussion

Options are [AVLayerVideoGravityResizeAspect](../avlayervideogravity/resizeaspect.md), [AVLayerVideoGravityResizeAspectFill](../avlayervideogravity/resizeaspectfill.md), and [AVLayerVideoGravityResize](../avlayervideogravity/resize.md). The default is [AVLayerVideoGravityResizeAspect](../avlayervideogravity/resizeaspect.md).

This property is animatable.

## See Also

### Layer configuration

- [previewing](ispreviewing.md) — A Boolean value that indicates whether the layer is rendering video frames from its source.
