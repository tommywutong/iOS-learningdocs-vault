---
title: AVSpatialVideoConfiguration
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avspatialvideoconfiguration-c.class
source_url: 'https://developer.apple.com/documentation/avfoundation/avspatialvideoconfiguration-c.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avspatialvideoconfiguration-c.class.json'
content_hash: 'sha256:12af9c38b4d12e82'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSpatialVideoConfiguration

<sub>Class</sub>

An AVSpatialVideoConfiguration specifies spatial video properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface AVSpatialVideoConfiguration : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Creating a configuration

- [init](avspatialvideoconfiguration-c.class/init.md)
- [initWithFormatDescription:](avspatialvideoconfiguration-c.class/initwithformatdescription_.md) — Initializes an AVSpatialVideoConfiguration with a format description.

### Modifying the configuration

- [cameraCalibrationDataLensCollection](avspatialvideoconfiguration-c.class/cameracalibrationdatalenscollection.md) — Specifies intrinsic and extrinsic parameters for single or multiple lenses.
- [cameraSystemBaseline](avspatialvideoconfiguration-c.class/camerasystembaseline.md) — Specifies the distance between centers of the lenses of the camera system that created the video.
- [disparityAdjustment](avspatialvideoconfiguration-c.class/disparityadjustment.md) — Specifies a relative shift of the left and right images, which changes the zero parallax plane.
- [horizontalFieldOfView](avspatialvideoconfiguration-c.class/horizontalfieldofview.md) — Specifies horizontal field of view in thousandths of a degree. Can be nil if the value is unknown.

## See Also

### Inspecting the video composition

- [renderSize](avvideocomposition/rendersize.md) — The size at which the video composition should render.
- [renderScale](avvideocomposition/renderscale.md) — The scale at which the video composition should render.
- [frameDuration](avvideocomposition/frameduration.md) — A time interval for which the video composition should render composed video frames.
- [animationTool](avvideocomposition/animationtool.md) — A video composition tool to use with Core Animation in offline rendering.
- [colorPrimaries](avvideocomposition/colorprimaries.md) — The color primaries used for video composition.
- [colorTransferFunction](avvideocomposition/colortransferfunction.md) — The transfer function used for video composition.
- [colorYCbCrMatrix](avvideocomposition/colorycbcrmatrix.md) — The YCbCr matrix used for video composition.
- [customVideoCompositorClass](avvideocomposition/customvideocompositorclass.md) — A custom compositor class to use.
- [outputBufferDescription](avvideocomposition/outputbufferdescription-3wsar.md) — The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of CMTagCollectionRef objects that describes the output buffers.
- [spatialVideoConfigurations](avvideocomposition/spatialvideoconfigurations-2ipps.md) — Indicates the spatial configurations that are available to associate with the output of the video composition.
