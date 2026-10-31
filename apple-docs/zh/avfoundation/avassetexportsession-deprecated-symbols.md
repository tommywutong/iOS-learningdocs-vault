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
doc_path: /documentation/avfoundation/avassetexportsession-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession-deprecated-symbols.json'
content_hash: 'sha256:c7da3e492f320290'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [媒体读写](media-reading-and-writing.md) · [AVAssetExportSession](avassetexportsession.md)

# 已废弃符号

<sub>API 集合</sub>

查阅不再支持的符号及其替代方案。

## 主题

### 访问导出预设

- [+ exportPresetsCompatibleWithAsset:](<avassetexportsession/exportpresets(compatiblewith_).md>) — 返回与该媒体资源兼容的导出预设。 _(已废弃)_

### 配置输出

- [outputURL](avassetexportsession/outputurl.md) — 媒体资源导出会话写入其输出的 URL。 _(已废弃)_
- [outputFileType](avassetexportsession/outputfiletype.md) — 媒体资源导出会话写入的输出的文件类型。 _(已废弃)_

### 导出媒体

- [- exportAsynchronouslyWithCompletionHandler:](<avassetexportsession/exportasynchronously(completionhandler_).md>) — 开始异步执行导出会话。 _(已废弃)_
- [- cancelExport](<avassetexportsession/cancelexport().md>) — 取消导出会话的执行。 _(已废弃)_

### 监控导出进度

- [status](avassetexportsession/status-swift.property.md) — 导出会话的状态。 _(已废弃)_
- [progress](avassetexportsession/progress.md) — 一个指示导出进度的值。 _(已废弃)_
- [error](avassetexportsession/error.md) — 一个可选的错误对象。 _(已废弃)_

### 估算文件长度和时长

- [estimatedOutputFileLength](avassetexportsession/estimatedoutputfilelength.md) — 导出文件的预计长度（以字节为单位）。 _(已废弃)_

### 估算时长

- [maxDuration](avassetexportsession/maxduration.md) — 提供导出媒体的最大时长的估计值。 _(已废弃)_
