---
title: Metal 调试类型
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/metal-debugging-types
source_url: 'https://developer.apple.com/documentation/metal/metal-debugging-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/metal-debugging-types.json'
content_hash: 'sha256:988009837763d9b8'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Metal](../metal.md)

# Metal 调试类型

<sub>API 集合</sub>

创建捕获管理器和捕获范围，并在 GPU 设备运行命令缓冲区后检查其日志。

## 主题

### 帧捕获

- [MTLCaptureDescriptor](mtlcapturedescriptor.md) — Metal 捕获会话的配置。
- [MTLCaptureManager](mtlcapturemanager.md) — 你用来在 App 中捕获 Metal 命令数据的一个实例。
- [MTLCaptureDestination](mtlcapturedestination.md) — 已捕获命令数据的目的地种类。
- [MTLCaptureScope](mtlcapturescope.md) — 一种可以通过编程方式定制 GPU 帧捕获的类型。

### 捕获错误

- [MTLCaptureError](mtlcaptureerror.md) — 捕获会话返回的错误。
- [MTLCaptureErrorDomain](mtlcaptureerrordomain.md) — 捕获错误的错误域。

### Shader 日志

- [MTLFunctionLog](mtlfunctionlog.md) — Metal 设备运行命令缓冲区时生成的一条日志。
- [MTLLogContainer](mtllogcontainer-swift.struct.md) — Metal 设备运行命令缓冲区时创建的已记录消息集合。

## 另请参阅

### 开发者工具

- [Supporting Simulator in a Metal app](supporting-simulator-in-a-metal-app.md) — 在你的 Metal App 中配置替代渲染路径，让你的 App 能够在 Simulator 中运行。
- [Capturing Metal commands programmatically](capturing-metal-commands-programmatically.md) — 从你的 App 中调用 Metal 帧捕获，然后将生成的 GPU 追踪信息保存到文件或在 Xcode 中查看。
- [Logging shader debug messages](logging-shader-debug-messages.md) — 使用 shader 日志记录打印 shader 生成的调试消息。
- [Developing Metal apps that run in Simulator](developing-metal-apps-that-run-in-simulator.md) — 在 Simulator 中原型设计并测试你的 Metal App。
- [Improving your game's graphics performance and settings](improving-your-games-graphics-performance-and-settings.md) — 使用强大的 Metal 开发工具套件修复性能小故障，并为 Apple 平台上的流畅体验开发默认设置。
- [Metal debugger](../xcode/metal-debugger.md) — 使用 GPU 追踪信息调试并分析你的 Metal 工作负载。
- [Metal developer workflows](../xcode/metal-developer-workflows.md) — 定位并修复与你 App 对 Metal API 和 GPU 函数的使用相关的问题。
- [GPU counters and counter sample buffers](gpu-counters-and-counter-sample-buffers.md) — 通过对 GPU 设备的一个或多个计数器进行采样，从中获取运行时数据。
