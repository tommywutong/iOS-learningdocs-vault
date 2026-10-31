---
title: 将视频导出为其他格式
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/exporting-video-to-alternative-formats
source_url: 'https://developer.apple.com/documentation/avfoundation/exporting-video-to-alternative-formats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/exporting-video-to-alternative-formats.json'
content_hash: 'sha256:c1b22bea53a360f1'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [媒体读取与写入](media-reading-and-writing.md)

# 将视频导出为其他格式

<sub>文章</sub>

将现有的影片文件转换为不同的格式。

## 概述

要将现有的影片文件转换为使它与其他设备兼容的格式，你需要基于现有文件的内容生成一个新的影片文件。虽然你无法更改已保存视频的格式，但你可以按照本文概述的步骤创建一个所需格式的新文件。

> [!tip] 提示
> 如果你的 App 可以直接从视频捕捉中保存影片，那么按照[以其他格式录制影片](recording-movies-in-alternative-formats.md)中的步骤在捕捉时更改默认格式会更高效。

### 将新视频导出为所需格式

要将视频导出为其他格式，请从一个 [AVAsset](avasset.md) 影片文件开始，并执行以下步骤：

1. 从[导出预设](export-presets.md)列表中选择一个导出预设。
2. 从 [AVFileType](avfiletype.md) 预设列表中选择一个导出文件类型。
3. 验证 [AVAssetExportSession](avassetexportsession.md) 能否将影片从输入格式转换为你想要的输出格式。
4. 创建并配置一个 [AVAssetExportSession](avassetexportsession.md) 实例，然后用它执行导出。

下面的示例定义了一个方法，然后使用它来执行这些步骤：

```swift
func export(video: AVAsset,
            withPreset preset: String = AVAssetExportPresetHighestQuality,
            toFileType outputFileType: AVFileType = .mov,
            atURL outputURL: URL) async {
    
    // 检查预设与将视频导出为输出文件类型之间的兼容性。
    guard await AVAssetExportSession.compatibility(ofExportPreset: preset,
                                                   with: video,
                                                   outputFileType: outputFileType) else {
        print("The preset can't export the video to the output file type.")
        return
    }
    
    // 创建并配置导出会话。
    guard let exportSession = AVAssetExportSession(asset: video,
                                                   presetName: preset) else {
        print("Failed to create export session.")
        return
    }
    exportSession.outputFileType = outputFileType
    exportSession.outputURL = outputURL
    
    // 将视频转换为输出文件类型，并导出到输出 URL。
    await exportSession.export()
}

let video = // 你的来源 AVAsset 视频。 //
let outputURL = // 导出视频的目标 URL。 //

// 使用编码为 H.264 的预设将视频转换为 .mov 文件类型，
// 并异步执行导出。
Task {
    await export(video: video,
                 withPreset: AVAssetExportPresetHighestQuality,
                 toFileType: .mov,
                 atURL: outputURL)
}
```

## 另请参阅

### 媒体导出

- [AVAssetExportSession](avassetexportsession.md) — 一个使用导出预设以你指定的格式导出资源的对象。
