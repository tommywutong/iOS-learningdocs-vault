---
title: 在参考显示器上实现色调映射
framework: Metal
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/implementing-tone-mapping-on-reference-displays
source_url: 'https://developer.apple.com/documentation/metal/implementing-tone-mapping-on-reference-displays'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/implementing-tone-mapping-on-reference-displays.json'
content_hash: 'sha256:3fe2b519d9e70dc5'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md) · [HDR content](hdr-content.md)

# 在参考显示器上实现色调映射

<sub>文章</sub>

检测参考显示器，并将你的内容保持在显示硬件能力范围之内。

## 概述

参考显示器经过校准，可以在指定范围内产生精确的亮度和颜色值，你可以在受控环境中使用它来创建经过优化的视频内容。在处理任何数据之前，务必先确认你是否正在使用参考显示器，这样你就可以避免系统色调映射，并将像素值限制在该显示器能够精确呈现的范围内。

要确定你是否正在使用参考显示器，读取屏幕的 [maximumReferenceExtendedDynamicRangeColorComponentValue](../appkit/nsscreen/maximumreferenceextendeddynamicrangecolorcomponentvalue.md) 属性。如果该显示器是参考显示器，该属性的值将是一个非零值，表示该显示器在不经过限幅或色调映射的情况下能够重现的最大可能像素值。这个值可能小于 [maximumExtendedDynamicRangeColorComponentValue](../appkit/nsscreen/maximumextendeddynamicrangecolorcomponentvalue.md)。

为确保参考显示器能够精确呈现你的内容，请在线性色彩空间中执行你自己的色调映射，并将像素值保持在 `0.0` 与参考最大值之间。更多信息参见 [Performing your own tone mapping](performing-your-own-tone-mapping.md)。

## 另请参阅

### 高动态范围内容

- [Processing HDR images with Metal](processing-hdr-images-with-metal.md) — 使用 Apple GPU 的最新特性实现一个后处理管线。
- [Displaying HDR content in a Metal layer](displaying-hdr-content-in-a-metal-layer.md) — 将你的高动态范围（HDR）内容呈现到兼容的 Mac 显示器上。
- [Determining support for EDR values](determining-support-for-edr-values.md) — 检查某个显示器是否支持 EDR。
- [Using color spaces to display HDR content](using-color-spaces-to-display-hdr-content.md) — 当你不需要编辑或处理像素数据时，使用色彩空间。
- [Using system tone mapping on video content](using-system-tone-mapping-on-video-content.md) — 使用 EDR 元数据将系统默认色调映射应用于某个层。
- [Performing your own tone mapping](performing-your-own-tone-mapping.md) — 应用你自己的色调映射以获得你想要的确切效果。
