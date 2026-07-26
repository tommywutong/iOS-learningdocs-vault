---
title: outputBufferDescription
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablevideocomposition/outputbufferdescription
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/outputbufferdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocomposition/outputbufferdescription.json'
content_hash: 'sha256:16de560346183de4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoComposition](../avmutablevideocomposition.md)

# outputBufferDescription

<sub>Instance Property</sub>

The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of CMTagCollectionRef objects that describes the output buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) NSArray * outputBufferDescription;
```

## Discussion

If the video composition will output tagged buffers, the details of those buffers should be specified with CMTags. Specifically, the StereoView (eyes) and ProjectionKind must be specified. The behavior is undefined if the output tagged buffers do not match the outputBufferDescription. The default is nil, which means monoscopic output. Note that an empty array is not valid. An exception will be thrown if the objects in the array are not of type CMTagCollectionRef. Note that tagged buffers are only supported for custom compositors.

## See Also

### Configuring video composition properties

- [frameDuration](frameduration.md) — A time interval for which the video composition should render composed video frames. _(deprecated)_
- [renderSize](rendersize.md) — The size at which the video composition should render. _(deprecated)_
- [renderScale](renderscale.md) — The scale at which the video composition should render. _(deprecated)_
- [animationTool](animationtool.md) — A video composition tool to use with Core Animation in offline rendering. _(deprecated)_
