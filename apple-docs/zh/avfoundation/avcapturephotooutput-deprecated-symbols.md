---
title: 已废弃符号
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput-deprecated-symbols.json'
content_hash: 'sha256:3fcdeb77b8d12d5f'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [照片拍摄](photo-capture.md) · [AVCapturePhotoOutput](avcapturephotooutput.md)

# 已废弃符号

<sub>API 集合</sub>

查阅不再支持的符号及其替代方案。

## 主题

### 获取格式化输出

- [+ JPEGPhotoDataRepresentationForJPEGSampleBuffer:previewPhotoSampleBuffer:](<avcapturephotooutput/jpegphotodatarepresentation(forjpegsamplebuffer_previewphotosamplebuffer_).md>) — 返回与指定样本缓冲区中所拍摄照片对应的 JPEG 格式数据。 _(已废弃)_
- [+ DNGPhotoDataRepresentationForRawSampleBuffer:previewPhotoSampleBuffer:](<avcapturephotooutput/dngphotodatarepresentation(forrawsamplebuffer_previewphotosamplebuffer_).md>) — 返回与指定样本缓冲区中所拍摄的 RAW 照片对应的数字负片（DNG）格式数据。 _(已废弃)_

### 配置双摄像头拍摄

- [dualCameraFusionSupported](avcapturephotooutput/isdualcamerafusionsupported.md) — 一个布尔值，指示捕获输出当前是否支持在双摄像头设备上自动融合图像数据。 _(已废弃)_
- [dualCameraDualPhotoDeliverySupported](avcapturephotooutput/isdualcameradualphotodeliverysupported.md) — 一个布尔值，指示捕获输出当前是否支持在双摄像头设备上用两个相机同时拍摄照片。 _(已废弃)_
- [dualCameraDualPhotoDeliveryEnabled](avcapturephotooutput/isdualcameradualphotodeliveryenabled.md) — 一个布尔值，指定是否为在双摄像头设备上用两个相机同时拍摄照片而配置捕获管线。 _(已废弃)_

### 配置高分辨率静态拍摄

- [highResolutionCaptureEnabled](avcapturephotooutput/ishighresolutioncaptureenabled.md) — 一个布尔值，指定是否为高分辨率静态图像拍摄而配置捕获管线。 _(已废弃)_

### 监控可见场景

- [isStillImageStabilizationScene](avcapturephotooutput/isstillimagestabilizationscene.md) — 一个布尔值，指示相机当前预览的场景是否需要图像防抖动。 _(已废弃)_

### 确定可用设置

- [stillImageStabilizationSupported](avcapturephotooutput/isstillimagestabilizationsupported.md) — 一个布尔值，指示捕获输出当前是否支持静态图像拍摄的自动防抖动。 _(已废弃)_
