---
title: 音频与视频捕捉
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/audio-and-video-capture
source_url: 'https://developer.apple.com/documentation/avfoundation/audio-and-video-capture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/audio-and-video-capture.json'
content_hash: 'sha256:651c6645091338df'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md)

# 音频与视频捕捉

<sub>API 集合</sub>

将音频和视频直接捕捉到媒体文件，或捕捉媒体流以直接访问媒体样本缓冲区。

## 主题

### 文件捕捉

- [以其他格式录制影片](recording-movies-in-alternative-formats.md) — 更改捕捉影片文件的默认格式。
- [AVCaptureMovieFileOutput](avcapturemoviefileoutput.md) — 一种将视频和音频录制到 QuickTime 影片文件的捕捉输出。
- [AVCaptureAudioFileOutput](avcaptureaudiofileoutput.md) — 一种录制音频并将录制的音频保存到文件的捕捉输出。
- [AVCaptureFileOutput](avcapturefileoutput.md) — 可将捕捉到的数据录制到文件的捕捉输出的抽象超类。
- [AVCaptureFileOutputDelegate](avcapturefileoutputdelegate.md) — 用于监控或控制媒体文件捕捉输出的方法。
- [AVCaptureFileOutputRecordingDelegate](avcapturefileoutputrecordingdelegate.md) — 用于响应将捕捉的媒体录制到文件时发生的事件的方法。

### 流捕捉

- [在 iOS App 中捕捉空间音频](capturing-spatial-audio-in-your-ios-app.md) — 通过支持空间音频捕捉来增强 App 的录音能力。
- [AVCaptureVideoDataOutput](avcapturevideodataoutput.md) — 一种录制视频并提供视频帧访问以进行处理的捕捉输出。
- [AVCaptureAudioDataOutput](avcaptureaudiodataoutput.md) — 一种录制音频并在录制时提供音频样本缓冲区访问的捕捉输出。
- [AVCaptureSpatialAudioMetadataSampleGenerator](avcapturespatialaudiometadatasamplegenerator.md) — 用于生成空间音频定时元数据样本的接口。

### Mac 屏幕捕捉

- [AVCaptureScreenInput](avcapturescreeninput.md) — 一种用于在 macOS 中录制屏幕的捕捉输入。

### 直播视频输出

- [AVCaptureBroadcastVideoOutput](avcapturebroadcastvideooutput.md) — [AVCaptureBroadcastVideoOutput](avcapturebroadcastvideooutput.md) 是 [AVCaptureOutput](avcaptureoutput.md) 的子类，通过设备的 DisplayPort 硬件接口（USB-C DP Alt 模式）交付广播级质量的视频和辅助数据。_(beta)_
- [AVCaptureBroadcastVideoOutputDelegate](avcapturebroadcastvideooutputdelegate.md) — 用于接收广播视频输出事件和数据的协议。_(beta)_

## 另请参阅

### 捕捉

- [捕捉设置](capture-setup.md) — 为媒体捕捉配置内置相机和麦克风，以及外部捕捉设备。
- [照片捕捉](photo-capture.md) — 捕捉高质量静态图像、实况照片以及配套的照片数据。
- [附加数据捕捉](additional-data-capture.md) — 捕捉深度和元数据等附加数据，并同步来自多个输出的捕捉。
