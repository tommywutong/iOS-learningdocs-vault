---
title: 'AVCamBarcode：检测条形码和人脸'
framework: AVFoundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, Xcode 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcambarcode-detecting-barcodes-and-faces
source_url: 'https://developer.apple.com/documentation/avfoundation/avcambarcode-detecting-barcodes-and-faces'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcambarcode-detecting-barcodes-and-faces.json'
content_hash: 'sha256:f67254dbb5ab1d85'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [捕获设置](capture-setup.md)

# AVCamBarcode：检测条形码和人脸

<sub>示例代码</sub>

使用相机识别机器可读代码或人脸。

## 概述

> [!note] 注意
> 本示例代码项目关联 WWDC21 场次 [10047: What's New in Camera Capture](https://developer.apple.com/videos/play/wwdc21/10047/)。

## 另请参阅

### 捕获会话

- [设置捕获会话](setting-up-a-capture-session.md) — 在拍摄照片或视频之前配置输入设备、输出媒体、预览视图和基本设置。
- [在 iPad 上多任务处理时访问相机](../avkit/accessing-the-camera-while-multitasking-on-ipad.md) — 在分屏浏览、侧拉、画中画和台前调度模式下操作相机。
- [AVCam：构建相机 App](avcam-building-a-camera-app.md) — 使用 iPhone 和 iPad 的前后摄像头拍摄照片和录制视频。
- [构建快速启动的响应式相机 App](build-a-responsive-camera-app-that-launches-quickly.md) — 为你的 iOS 和 iPadOS App 构建快速的相机启动体验。
- [拍摄电影效果视频](capturing-cinematic-video.md) — 拍摄具有可调景深和焦点的视频。
- [在你的 iOS App 中支持 Center Stage 前置摄像头](supporting-center-stage-front-camera-in-your-ios-app.md) — 在 iPhone 前置摄像头拍摄的照片和视频中启用人物居中功能。
- [AVMultiCamPiP：从多个相机捕获](avmulticampip-capturing-from-multiple-cameras.md) — 使用多相机捕获会话将前后摄像头的输出同时录制到一个影片文件中。
- [AVCaptureSession](avcapturesession.md) — 一个配置捕获行为并协调数据从输入设备流向捕获输出的对象。
- [AVCaptureMultiCamSession](avcapturemulticamsession.md) — 一种支持从相同媒体类型的多个输入同时捕获的捕获会话。
- [AVCaptureInput](avcaptureinput.md) — 向捕获会话提供输入数据的对象的抽象超类。
- [AVCaptureOutput](avcaptureoutput.md) — 为捕获会话提供媒体输出目的地的对象的抽象超类。
- [AVCaptureConnection](avcaptureconnection.md) — 一个表示从捕获输入到捕获输出的连接的对象。

## 下载

- [AVCamBarcodeDetectingBarcodesAndFaces.zip](https://docs-assets.developer.apple.com/published/306f40997d58/AVCamBarcodeDetectingBarcodesAndFaces.zip)
