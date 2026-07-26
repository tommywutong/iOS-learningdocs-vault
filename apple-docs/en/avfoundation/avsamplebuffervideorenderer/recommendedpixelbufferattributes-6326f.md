---
title: recommendedPixelBufferAttributes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebuffervideorenderer/recommendedpixelbufferattributes-6326f
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/recommendedpixelbufferattributes-6326f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/recommendedpixelbufferattributes-6326f.json'
content_hash: 'sha256:c42932c345959988'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferVideoRenderer](../avsamplebuffervideorenderer.md)

# recommendedPixelBufferAttributes

<sub>Instance Property</sub>

Recommended pixel buffer attributes for optimal performance when using CMSampleBuffers containing CVPixelBuffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly, nonnull) NSDictionary<NSString *,id> * recommendedPixelBufferAttributes;
```

## Discussion

The returned dictionary does not contain all of the attributes needed for creating pixel buffers. Use `CVPixelBufferCreateResolvedAttributesDictionary()` to reconcile these attributes with the pixel buffer creation attributes.

## See Also

### Accessing the pixel buffer

- [- copyDisplayedPixelBuffer](<displayedpixelbuffer().md>)
