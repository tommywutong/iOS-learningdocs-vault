---
title: 'AVMultiCamPiP：从多个相机捕捉'
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, Xcode 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmulticampip-capturing-from-multiple-cameras
source_url: 'https://developer.apple.com/documentation/avfoundation/avmulticampip-capturing-from-multiple-cameras'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmulticampip-capturing-from-multiple-cameras.json'
content_hash: 'sha256:638b7bb45c2da892'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [捕捉设置](capture-setup.md)

# AVMultiCamPiP：从多个相机捕捉

<sub>示例代码</sub>

使用多相机捕捉会话，将前后相机的输出同时录制到单个电影文件中。

## 概述

> [!note] 注意
> 本示例代码项目关联 WWDC 2019 场次 [225: Advances in Camera Capture & Portrait Segmentation](https://developer.apple.com/videos/play/wwdc19/225/)。

### 配置示例代码项目

你必须 在以下设备之一上运行本示例代码：

- 搭载 A12 或更新处理器的 iPhone
- 搭载 A12X 或更新处理器的 iPad Pro

## 另请参阅

### 捕捉会话

- [设置捕捉会话](setting-up-a-capture-session.md) — 在捕捉照片或视频之前配置输入设备、输出媒体、预览视图和基本设置。
- [在 iPad 上多任务处理时访问相机](../avkit/accessing-the-camera-while-multitasking-on-ipad.md) — 在分屏浏览、侧拉、画中画和舞台管理模式下操作相机。
- [AVCam：构建相机 App](avcam-building-a-camera-app.md) — 使用 iPhone 和 iPad 的前后置相机拍摄照片和录制视频。
- [构建启动迅速的响应式相机 App](build-a-responsive-camera-app-that-launches-quickly.md) — 为你的 iOS 和 iPadOS App 构建快速的相机启动体验。
- [捕捉电影效果视频](capturing-cinematic-video.md) — 捕捉具有可调景深和焦点的视频。
- [在 iOS App 中支持舞台居中前置相机](supporting-center-stage-front-camera-in-your-ios-app.md) — 在 iPhone 前置相机上为照片和视频启用舞台居中。
- [AVCamBarcode：检测条形码和人脸](avcambarcode-detecting-barcodes-and-faces.md) — 使用相机识别机器可读代码或人脸。
- [AVCaptureSession](avcapturesession.md) — 一个配置捕捉行为并协调从输入设备到捕捉输出数据流的对象。
- [AVCaptureMultiCamSession](avcapturemulticamsession.md) — 一种捕捉会话，支持从同一媒体类型的多个输入同时捕捉。
- [AVCaptureInput](avcaptureinput.md) — 为捕捉会话提供输入数据的对象的抽象超类。
- [AVCaptureOutput](avcaptureoutput.md) — 为捕捉会话提供媒体输出目的地的对象的抽象超类。
- [AVCaptureConnection](avcaptureconnection.md) — 一个表示从捕捉输入到捕捉输出之间连接的对象。

## 下载

- [AVMultiCamPiPCapturingFromMultipleCameras.zip](https://docs-assets.developer.apple.com/published/cc1a2216fde0/AVMultiCamPiPCapturingFromMultipleCameras.zip)
