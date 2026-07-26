---
title: 'provideImageData(_:bytesPerRow:origin:_:size:_:userInfo:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/provideimagedata(_:bytesperrow:origin:_:size:_:userinfo:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/provideimagedata(_:bytesperrow:origin:_:size:_:userinfo:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/provideimagedata%28_%3Abytesperrow%3Aorigin%3A_%3Asize%3A_%3Auserinfo%3A%29.json'
content_hash: 'sha256:425331de5d91cedd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# provideImageData(_:bytesPerRow:origin:_:size:_:userInfo:)

<sub>Instance Method</sub>

Supplies data to a `CIImage` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin originx: Int, _ originy: Int, size width: Int, _ height: Int, userInfo info: Any?)
```

## Parameters

- `data` — A pointer to image data. Note that `data[0]` refers to the first byte of the requested subimage, not the larger image buffer.

- `rowbytes` — The number of bytes per row.

- `width` — The width of the image data.

- `height` — The height of the image data.

- `info` — User supplied data, which is optional.

## Discussion

You can supply the image provider to these methods of the `CIImage` class:

- [imageWithImageProvider:size::format:colorSpace:options:](../../coreimage/ciimage/imagewithimageprovider_size__format_colorspace_options_.md) to create a CIImage object from image data
- [init(imageProvider:size:_:format:colorSpace:options:)](<../../coreimage/ciimage/init(imageprovider_size___format_colorspace_options_).md>) to initialize an existing CIImage with data

You initialize the given bitmap with the subregion specified by the arguments `x`, `y`, `width`, and `height`. The subregion uses the local coordinate space of the image, with the origin at the upper-left corner of the image. If you change the virtual memory mapping of the buffer specified by the `data` argument (such as by using `vm_copy` to modify it), the behavior is undefined.

That this callback always requests the full image data regardless of what is actually visible. All of the image is loaded or none of it is. The exception is when you create a tiled image by specifying the `kCIImageProviderTileSize` option. In this case, only the needed tiles are requested.

## See Also

### Related Documentation

- [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)
