---
title: 提升 App 的渲染效率
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/improving-your-app-s-rendering-efficiency
source_url: 'https://developer.apple.com/documentation/xcode/improving-your-app-s-rendering-efficiency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/improving-your-app-s-rendering-efficiency.json'
content_hash: 'sha256:06e44120d331aa45'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [性能与指标](performance-and-metrics.md) · [减少 App 的电池消耗](reducing-your-app-s-battery-use.md)

# 提升 App 的渲染效率

<sub>文章</sub>

尽量减少不必要的重绘并使用高效的更新策略，以优化视图更新。

## 概述

不必要地重绘视图或执行复杂更新，会增加 CPU 和 GPU 的耗电量。此外，低效的视图更新还可能导致 App 出现挂起（hang）和卡顿（hitch），降低用户使用 App 时的体验。有关更多信息，请参阅[理解用户界面的响应能力](understanding-user-interface-responsiveness.md)。

### 提升 SwiftUI 性能

使用 SwiftUI instrument 对 App 进行性能分析，以识别 App 中耗时较长的视图 body 更新和频繁的视图更新，并重新组织视图以避免这些情况。有关更多信息，请参阅[理解并提升 SwiftUI 性能](understanding-and-improving-swiftui-performance.md)。

### 限制动画的帧率和持续时间

使用动画传达 App 中的变化和更新，并在更新完成时暂停或停止动画。有关更多信息，请参阅《人机界面指南》中的 [Foundations \> Motion](https://developer.apple.com/design/human-interface-guidelines/motion)。

在需要精确控制动画行为的情况下，请使用 [Core Animation](../quartzcore.md) 向系统提供动画首选帧率的提示，并控制动画持续时间。帧率越高，系统耗电越多。有关更多信息，请参阅[优化 iPhone 和 iPad App 以支持 ProMotion 显示屏](../quartzcore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays.md)。

### 高效更新视图

Xcode 运行 App 时，选择 Debug \> View Debugging \> Rendering \> Flash Updated Regions，以识别 App 何时更新屏幕区域。App 显示区域发生闪烁表示屏幕更新；如果闪烁区域在视觉上没有明显变化，则说明存在不必要的屏幕使用，还可能存在为准备该更新而进行的不必要计算。

需要更新视图时，请计算需要更新的最小区域，并将其传给 [setNeedsDisplay(_:)](<../uikit/uiview/setneedsdisplay(__).md>)（UIKit）或 [setNeedsDisplay(_:)](<../appkit/nsview/setneedsdisplay(__).md>)（AppKit），使系统只更新发生变化的区域。避免采用更新一个图层时需要系统重绘其他重叠图层的视图布局。

请特别注意位于 [Liquid Glass](../technologyoverviews/liquid-glass.md) 效果下方视图中的更新区域，因为 App 更新 Liquid Glass 效果周围的屏幕区域时，系统需要执行额外计算来更新 Liquid Glass 外观。

### 尽量减少复杂效果

采用 [Liquid Glass](../technologyoverviews/liquid-glass.md) 时，请使用 [GlassEffectContainer](../swiftui/glasseffectcontainer.md) 合并多个视图中的 Liquid Glass 效果。有关更多信息，请参阅[将 Liquid Glass 应用于自定义视图](../swiftui/applying-liquid-glass-to-custom-views.md)。

将空间上相距较远的视图分组时请务必谨慎，因为这可能导致不必要的更新。例如，将分别位于屏幕顶部和底部的两个按钮分组，意味着屏幕中间的任何变化都会使系统同时更新这两个按钮。使用上文[高效更新视图](improving-your-app-s-rendering-efficiency.md#Update-views-efficiently)中介绍的 Flash Updated Regions 工具，评估由 [GlassEffectContainer](../swiftui/glasseffectcontainer.md) 范围造成的屏幕更新。

相比 [UIVisualEffectView](../uikit/uivisualeffectview.md) 等复杂效果，应优先使用纯色等简单背景。

### 使用推荐的 API 播放媒体

尽可能使用 [AVPlayer](../avfoundation/avplayer.md) 播放媒体资源，因为它经过优化，能够高效渲染音频和视频。如果需要使用更底层的 API，请测量 App 的耗电量，并选择既能支持 App 功能又最高效的方式。例如，使用 [AVSampleBufferDisplayLayer](../avfoundation/avsamplebufferdisplaylayer.md) 播放视频的耗电量通常低于 [CAMetalLayer](../quartzcore/cametallayer.md)。

使用 [VTDecompressionSession](../videotoolbox/vtdecompressionsession-api-collection.md) 解码要在 [AVSampleBufferDisplayLayer](../avfoundation/avsamplebufferdisplaylayer.md) 中显示的视频帧时，请将 [kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey](../corevideo/kcvpixelbufferiosurfacecoreanimationcompatibilitykey.md) 作为图像缓冲区特性（attribute）传给 [VTDecompressionSessionCreate(allocator:formatDescription:decoderSpecification:imageBufferAttributes:decompressionSessionOut:)](<../videotoolbox/vtdecompressionsessioncreate(allocator_formatdescription_decoderspecification_imagebufferattributes_decompressionsessionout_).md>)，使 Video Toolbox 选择最高效的像素格式：

```swift
_ = VTDecompressionSessionCreate(allocator: nil,
                                 formatDescription: formatDescription,
                                 decoderSpecification: nil,
                                 imageBufferAttributes: [kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey],
                                 decompressionSessionOut: &decompressionSession)
```

### 降低 App 的平均像素亮度

较亮的像素比较暗的像素耗电更多，因此 App 中视图的平均像素亮度越低，系统为显示屏供电所消耗的能量就越少。在 App 中支持深色模式（Dark Mode），并在用户启用此设置时降低显示屏的整体亮度。有关更多信息，请参阅[在界面中支持深色模式](../uikit/supporting-dark-mode-in-your-interface.md)。

使用 Power Profiler 测量 App 中视图的平均像素亮度。有关更多信息，请参阅[使用 Power Profiler 测量 App 的耗电量](measuring-your-app-s-power-use-with-power-profiler.md)。使用 [MXUnitAveragePixelLuminance](../metrickit/mxunitaveragepixelluminance.md) 收集像素亮度指标。

## 另请参阅

### 图形与声音

- [减少捕获媒体时的耗电量](reducing-power-usage-when-capturing-media.md) — 在不需要时停止会话并选择合适的视频格式，以优化设备摄像头的耗电量。
