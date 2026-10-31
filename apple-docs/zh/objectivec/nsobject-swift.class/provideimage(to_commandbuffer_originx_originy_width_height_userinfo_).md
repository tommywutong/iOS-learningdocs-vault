---
title: 'provideImage(to:commandBuffer:originx:originy:width:height:userInfo:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/provideimage(to:commandbuffer:originx:originy:width:height:userinfo:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/provideimage(to:commandbuffer:originx:originy:width:height:userinfo:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/provideimage%28to%3Acommandbuffer%3Aoriginx%3Aoriginy%3Awidth%3Aheight%3Auserinfo%3A%29.json'
content_hash: 'sha256:05bd14ca280dba48'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# `provideImage(to:commandBuffer:originx:originy:width:height:userInfo:)`

<sub>实例方法</sub>

图像提供程序对象可以实现的可选方法。
使用此方法，提供程序对象可以使用 Metal API 提供像素
数据到 MTLTexture 中，以便在渲染图像对象时使用。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func provideImage(to texture: any MTLTexture, commandBuffer: any MTLCommandBuffer, originx: Int, originy: Int, width: Int, height: Int, userInfo info: Any?)
```

## 参数

- `texture` — 提供程序应将请求子矩形的像素复制到其中的 `<id>MTLTexture`。

- `commandBuffer` — 提供程序应用于编码复制的 `<id>MTLCommandBuffer`。

- `originx` — 请求子矩形相对于图像左上角的 x 原点。

- `originy` — 请求子矩形相对于图像左上角的 y 原点。

- `width` — The width of the requested sub-rect.

- `height` — The height of the requested sub-rect.

- `info` — 调用以下内容时指定的 `kCIImageProviderTileSize` 选项的值：*`/CIImage/imageWithImageProvider:size::format:colorSpace:options:`` * ``/CIImage/initWithImageProvider:size::format:colorSpace:options:``

## 讨论

实现应为图像的请求子矩形 `x,y,width,height` 提供像素。该子矩形在图像的本地坐标空间中定义，原点相对于图像的左上角。

填充 `MTLTexture` 的工作应在指定的 `commandBuffer` 上编码。
若实现使用自己的 commandBuffer，则应在返回前调用 `waitUntilCompleted`。若纹理是表面支持的，则只需在返回前调用 `waitUntilScheduled`。

默认情况下，无论当前渲染需要哪个子矩形，都会调用此方法以请求完整图像。在这种情况下，请求的 `x,y,width,height` 将为 `0,0,imageWidth,imageHeight`

若在创建 `CIImage` 时指定了 `kCIImageProviderTileSize` 选项，则对于当前渲染所需的每个图块，可能会调用此方法一次。
