---
title: 使用 SwiftNIO 构建可续传上传服务器
framework: Foundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/building-a-resumable-upload-server-with-swiftnio
source_url: 'https://developer.apple.com/documentation/foundation/building-a-resumable-upload-server-with-swiftnio'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/building-a-resumable-upload-server-with-swiftnio.json'
content_hash: 'sha256:e53d65532e02a93a'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [URL 加载系统](url-loading-system.md)

# 使用 SwiftNIO 构建可续传上传服务器

<sub>示例代码</sub>

通过将可续传上传转换为常规上传，在 SwiftNIO 中支持 HTTP 可续传上传协议。

## 概述

> [!note] 注意
> 此示例代码项目与 WWDC23 第 10006 场 [构建可靠且可续传的文件传输](https://developer.apple.com/wwdc23/10006/)相关。

### 配置示例代码项目

运行示例代码项目之前：

1. 在现有 HTTP 服务器项目的 `Package.swift` 文件中，将 `.package(path: "/path/to/swift-nio-resumable-upload")` 添加为依赖项之一。
2. 在 SwiftNIO 引导代码中导入 `NIOResumableUpload`。
3. 创建上传上下文：`let uploadContext = HTTPResumableUploadContext(origin: "https://example.com")`。
4. 使用 `HTTPResumableUploadHandler` 包装 HTTP 服务器通道处理程序。

## 另请参阅

### 上传

- [将数据上传到网站](uploading-data-to-a-website.md) — 从你的 App 向服务器发布数据。
- [上传数据流](uploading-streams-of-data.md) — 向服务器发送数据流。
- [暂停和恢复上传](pausing-and-resuming-uploads.md) — 暂停并恢复上传而无需重新开始，即使连接中断也不例外。

## 下载

- [BuildingAResumableUploadServerWithSwiftNIO.zip](https://docs-assets.developer.apple.com/published/eecdd62f298f/BuildingAResumableUploadServerWithSwiftNIO.zip)
