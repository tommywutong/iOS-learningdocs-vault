---
title: 以其他格式录制影片
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/recording-movies-in-alternative-formats
source_url: 'https://developer.apple.com/documentation/avfoundation/recording-movies-in-alternative-formats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/recording-movies-in-alternative-formats.json'
content_hash: 'sha256:780750e9f518a07e'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [音频与视频捕捉](audio-and-video-capture.md)

# 以其他格式录制影片

<sub>文章</sub>

更改捕捉影片文件的默认格式。

## 概述

你使用 [AVCaptureMovieFileOutput](avcapturemoviefileoutput.md) 来捕捉 QuickTime 影片文件，在大多数 iPhone 和 iPad 机型上，框架默认选择 HEVC 格式。不过，如果你知道自己需要不同的格式，可以提前更改默认格式。

如果你的 App 通过系统共享表单分享捕捉到的视频，系统会自动将视频转换为与目标设备兼容的格式。但是，如果你的 App 是为系统共享表单之外的应用场景在内部保存或分享捕捉到的视频，则需要使用与所有目标设备兼容的视频捕捉格式。本文介绍如何动态更改捕捉格式，使你的 App 捕捉到的视频一开始就是所需的格式。

### 更改默认捕捉格式

你可以在捕捉时通过在捕捉影片文件的输出设置中指定格式来更改默认格式。每个捕捉设备都有一个设置字典，你可以调整它来控制输出影片文件的属性。例如，要以 H.264/MPEG-4 AVC 捕捉视频，请将输出设置键 [AVVideoCodecKey](avvideocodeckey.md) 设置为 [AVVideoCodecTypeH264](avvideocodectype/h264.md)，如下例所示：

**Swift**

```swift
import AVFoundation

let movieFileOutput = // 你的 AVCaptureMovieFileOutput。 //

if movieFileOutput.availableVideoCodecTypes.contains(.h264),
    let connection = movieFileOutput.connection(with: .video) {
    // 使用 H.264 编解码器对视频进行编码。
    movieFileOutput.setOutputSettings([AVVideoCodecKey: AVVideoCodecType.h264], for: connection)
}
```

**Objective-C**

```objc
#import <AVFoundation/AVFoundation.h>

AVCaptureMovieFileOutput *movieFileOutput = // 你的 AVCaptureMovieFileOutput。 //;
    
if ([movieFileOutput.availableVideoCodecTypes containsObject:AVVideoCodecTypeH264]) {
    AVCaptureConnection* connection = [movieFileOutput connectionWithMediaType:AVMediaTypeVideo];
    // 使用 H.264 编解码器对视频进行编码。
    [movieFileOutput setOutputSettings:@{AVVideoCodecKey: AVVideoCodecTypeH264} forConnection:connection];
}
```

有关支持的捕捉编解码器列表，请参阅 [AVVideoCodecType](avvideocodectype.md)。

### 转换之前捕捉的影片文件

除了使用不同的默认格式保存或分享捕捉到的视频外，你还可以通过基于现有文件的内容生成新的影片文件来转换现有的影片文件内容。具体做法请参阅[将视频导出为其他格式](exporting-video-to-alternative-formats.md)。

## 另请参阅

### 相关文档

- [AVVideoCodecTypeH264](avvideocodectype/h264.md) — H.264 视频编解码器。
- [AVVideoCodecTypeHEVC](avvideocodectype/hevc.md) — HEVC 视频编解码器。
- [AVVideoCodecTypeJPEG](avvideocodectype/jpeg.md) — JPEG 视频编解码器。
- [AVVideoCodecTypeAppleProRes422](avvideocodectype/prores422.md) — Apple ProRes 422 视频编解码器。
- [AVVideoCodecTypeAppleProRes4444](avvideocodectype/prores4444.md) — Apple ProRes 4444 视频编解码器。

### 文件捕捉

- [AVCaptureMovieFileOutput](avcapturemoviefileoutput.md) — 一种将视频和音频录制到 QuickTime 影片文件的捕捉输出。
- [AVCaptureAudioFileOutput](avcaptureaudiofileoutput.md) — 一种录制音频并将录制的音频保存到文件的捕捉输出。
- [AVCaptureFileOutput](avcapturefileoutput.md) — 可将捕捉到的数据录制到文件的捕捉输出的抽象超类。
- [AVCaptureFileOutputDelegate](avcapturefileoutputdelegate.md) — 用于监控或控制媒体文件捕捉输出的方法。
- [AVCaptureFileOutputRecordingDelegate](avcapturefileoutputrecordingdelegate.md) — 用于响应将捕捉的媒体录制到文件时发生的事件的方法。
