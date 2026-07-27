---
title: 执行你自己的色调映射
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/performing-your-own-tone-mapping
source_url: 'https://developer.apple.com/documentation/metal/performing-your-own-tone-mapping'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/performing-your-own-tone-mapping.json'
content_hash: 'sha256:d55222c80fd08483'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [HDR content](hdr-content.md)

# 执行你自己的色调映射

<sub>文章</sub>

应用你自己的色调映射，以获得你想要的确切效果。

## 概述

要执行你自己的 EDR 色调映射，请创建一个 Metal 图层，为它设置一个扩展线性色彩空间，并将其 [wantsExtendedDynamicRangeContent](../quartzcore/cametallayer/wantsextendeddynamicrangecontent.md) 属性设置为 [true](../swift/true.md)。例如，下面的代码创建了一个 Metal 图层，其扩展色彩空间会把像素值线性映射到亮度值：

```objective-c
CAMetalLayer *metalLayer = [CAMetalLayer new];
metalLayer.wantsExtendedDynamicRangeContent = YES;
metalLayer.pixelFormat = MTLPixelFormatRGBA16Float;
const CFStringRef name = kCGColorSpaceExtendedLinearSRGB;
CGColorSpaceRef colorspace = CGColorSpaceCreateWithName(name);
metalLayer.colorspace = colorspace;
CGColorSpaceRelease(colorspace);
```

### 了解 EDR 像素值

在支持 EDR 的 Mac 上，像素的 `1.0` 值对应标准动态范围（SDR）的最高亮度级别，但这个亮度级别不一定对应显示器的最高亮度。如果显示器能够产生更高的亮度级别，那么可能会有额外的范围（余量）可用。余量的大小可能因实际显示器特性而异：

- 如果界面亮度级别为 `100` 尼特，而面板的最高亮度可达 `400` 尼特，那么启用 EDR 后，最高可以让数值达到 `4.0` 的内容以 `400` 尼特显示。
- 在同一面板上，如果用户将界面亮度级别调整为 `200` 尼特，那么 1.0 的值会以 `200` 尼特显示，`2.0` 的值则以 `400` 尼特显示。

### 将你的内容映射到可用范围

可显示数值的实际上限可能会随时间发生变化。要确定当前上限，请读取 [NSScreen](../appkit/nsscreen.md) 对象的 [maximumExtendedDynamicRangeColorComponentValue](../appkit/nsscreen/maximumextendeddynamicrangecolorcomponentvalue.md) 属性。请注意，即使在支持 EDR 的显示器上，如果显示器被设置为可能的最高亮度，当前的最大值也可能是 1.0。

下面的代码在处理一帧的过程中读取了 [maximumExtendedDynamicRangeColorComponentValue](../appkit/nsscreen/maximumextendeddynamicrangecolorcomponentvalue.md) 属性。在渲染这一帧时，把所有数值映射到 `0` 与当前最大值之间。如果你指定了超出该值的数值，系统会将其钳制为不超过当前最大值。

```objective-c
id<MTLDrawable> drawable = metalLayer.nextDrawable;
NSScreen *screen = view.window.screen;
float maxEDR = screen.maximumExtendedDynamicRangeColorComponentValue;
// <encode Metal commands to process the frame.
```

注册 [didChangeScreenParametersNotification](../appkit/nsapplication/didchangescreenparametersnotification.md) 通知，以便在某个显示器的当前最大值发生变化时收到通知。另外请注意，用户可能会把内容移动到另一个显示器上。

如果你的内容超出了显示器当前的能力范围，请决定你想如何将其呈现给用户。例如，你可以把内容色调映射到可用范围内（每次渲染一帧时都对内容进行适配），也可以通知用户部分内容超出了显示器的能力范围。当用户调高亮度时，他们通常期望中间调随之提升，而高光部分会被压缩，以适配显示器的范围。

## 另请参阅

### 高动态范围内容

- [使用 Metal 处理 HDR 图像](processing-hdr-images-with-metal.md) — 使用 Apple GPU 上的最新特性实现一条后处理管线。
- [在 Metal 图层中显示 HDR 内容](displaying-hdr-content-in-a-metal-layer.md) — 将你的高动态范围（HDR）内容呈现到兼容的 Mac 显示器上。
- [确定对 EDR 值的支持情况](determining-support-for-edr-values.md) — 检查某个显示器是否支持 EDR。
- [使用色彩空间显示 HDR 内容](using-color-spaces-to-display-hdr-content.md) — 在你不需要编辑或处理像素数据时，使用色彩空间。
- [对视频内容使用系统色调映射](using-system-tone-mapping-on-video-content.md) — 使用 EDR 元数据，为某个图层应用默认的系统色调映射。
- [在参考显示器上实现色调映射](implementing-tone-mapping-on-reference-displays.md) — 检测参考显示器，并让你的内容保持在显示器硬件的能力范围之内。
