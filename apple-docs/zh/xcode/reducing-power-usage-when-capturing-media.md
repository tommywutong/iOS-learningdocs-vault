---
title: 减少捕获媒体时的功耗
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/reducing-power-usage-when-capturing-media
source_url: 'https://developer.apple.com/documentation/xcode/reducing-power-usage-when-capturing-media'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/reducing-power-usage-when-capturing-media.json'
content_hash: 'sha256:38a061ec481f7e3a'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Performance and metrics](performance-and-metrics.md) · [Reducing your app’s battery use](reducing-your-app-s-battery-use.md)

# 减少捕获媒体时的功耗

<sub>文章</sub>

通过在不需要时停止会话以及选择合适的视频格式，优化设备摄像头的功耗。

## 概述

设备摄像头在使用时会消耗大量电量。为了将你的 App 使用设备摄像头的时间降到最低，只在 App 使用捕获数据期间运行 [AVCaptureSession](../avfoundation/avcapturesession.md)，并尽早调用 [stopRunning()](<../avfoundation/avcapturesession/stoprunning().md>)。例如，当你的 App 的相机视图被其他内容遮挡时，停止捕获会话，这样在没人能看到时设备就会停止捕获相机画面流。

由于捕获更高质量的图像会消耗更多电量，请将捕获设备的 [activeFormat](../avfoundation/avcapturedevice/activeformat.md) 设置为满足你的 App 功能需求的最低图像质量格式。确认你所使用格式的 [isVideoBinned](../avfoundation/avcapturedevice/format/isvideobinned.md) 属性为 `true`，因为像素合并（pixel binning）同样能提高能效。

## 另请参阅

### 图形与声音

- [提升 App 的渲染效率](improving-your-app-s-rendering-efficiency.md) — 通过最小化不必要的重绘并使用高效的更新策略来优化视图更新。
