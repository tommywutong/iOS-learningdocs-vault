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
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# provideImageData(_:bytesPerRow:origin:_:size:_:userInfo:)

<sub>实例方法</sub>

Supplies data to a `CIImage` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin originx: Int, _ originy: Int, size width: Int, _ height: Int, userInfo info: Any?)
```

## 参数

- `data` — 指向图像数据的指针。请注意，`data[0]` 指的是请求子图像的第一个字节，而不是更大的图像缓冲区。

- `rowbytes` — The number of bytes per row.

- `width` — The width of the image data.

- `height` — The height of the image data.

- `info` — User supplied data, which is optional.

## 讨论

你可以将图像提供程序提供给 `CIImage` 类的这些方法：

- [imageWithImageProvider:size::format:colorSpace:options:](../../coreimage/ciimage/imagewithimageprovider_size__format_colorspace_options_.md) 以从图像数据创建 CIImage 对象
- [init(imageProvider:size:_:format:colorSpace:options:)](<../../coreimage/ciimage/init(imageprovider_size___format_colorspace_options_).md>) 以用数据初始化现有 CIImage

你使用参数 `x`、`y`、`width` 和 `height` 指定的子区域初始化给定位图。该子区域使用图像的本地坐标空间，原点位于图像的左上角。若你更改由 `data` 参数指定的缓冲区的虚拟内存映射（例如通过使用 `vm_copy` 修改它），则行为未定义。

此回调始终请求完整图像数据，无论实际可见内容是什么。加载全部图像或完全不加载。例外是当你通过指定 `kCIImageProviderTileSize` 选项创建平铺图像时。在这种情况下，仅请求所需的图块。

## 另请参阅

### 相关文档

- [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)
