---
title: 通过编程方式捕获 Metal 工作负载
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/capturing-a-metal-workload-programmatically
source_url: 'https://developer.apple.com/documentation/xcode/capturing-a-metal-workload-programmatically'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/capturing-a-metal-workload-programmatically.json'
content_hash: 'sha256:032ceb52498a9cba'
translated: true
---

> 导航：[技术](<../technologies.md>) · [Xcode](../xcode.md) · [调试](debugging.md) · [Metal 调试器](metal-debugger.md)

# 通过编程方式捕获 Metal 工作负载

<sub>文章</sub>

通过调用 Metal 的帧捕获来分析你 App 的性能。

## 概述

使用 [MTLCaptureManager](../metal/mtlcapturemanager.md) 以编程方式捕获你发送给特定设备对象的命令信息。例如，你可以根据需要捕获特定帧或帧的一部分：通过实现触发捕获的自定义 UI，或在 App 运行时以编程方式触发捕获。

### 启用编程捕获

要在你的 App 中启用 Metal 捕获，请在 `Info.plist` 文件中添加键 `MetalCaptureEnabled`，并将其值设为 `YES`。在 Xcode 的属性列表编辑器中，该键显示为 `Metal Capture Enabled`。

或者在 macOS 14 及更高版本中，你可以在 Metal App 上设置环境变量：`MTL_CAPTURE_ENABLED=1`。

> [!tip] 提示
> 启用 Metal 捕获对你的 App 的 CPU 处理时间有微小但可测量的影响。你可能希望使用项目中的构建设置来设置此键的值，以便为某些构建版本启用它，但不要为最终的发布版本启用。

### 捕获设备或命令队列

创建一个 [MTLCaptureDescriptor](../metal/mtlcapturedescriptor.md) 对象，用于定义你想要记录哪些命令以及捕获完成后需要执行什么操作。要捕获特定 [MTLDevice](../metal/mtldevice.md) 或 [MTLCommandQueue](../metal/mtlcommandqueue.md) 的命令，请将捕获描述符的 [captureObject](../metal/mtlcapturedescriptor/captureobject.md) 属性设置为指向要跟踪的特定对象，并调用 [startCapture(with:)](<../metal/mtlcapturemanager/startcapture(with_).md>) 方法。要停止捕获命令，请调用 [stopCapture()](<../metal/mtlcapturemanager/stopcapture().md>) 方法。

```swift
func triggerProgrammaticCapture(device: MTLDevice) {
    let captureManager = MTLCaptureManager.shared()
    let captureDescriptor = MTLCaptureDescriptor()
    captureDescriptor.captureObject = self.device
    do {
        try captureManager.startCapture(with: captureDescriptor)
    } catch {
        fatalError("error when trying to capture: \(error)")
    }
}

func runMetalCommands(commandQueue: MTLCommandQueue) {
    let commandBuffer = commandQueue.makeCommandBuffer()!
    // 执行 Metal 工作。
    commandBuffer.commit()
    let captureManager = MTLCaptureManager.shared()
    captureManager.stopCapture()
}
```

捕获管理器仅捕获你在捕获开始后创建、并在捕获停止前提交的那些 [MTLCommandBuffer](../metal/mtlcommandbuffer.md) 对象中的命令。

> [!tip] 提示
> 以编程方式捕获帧时，你可以捕获跨越多帧的 Metal 命令。例如，在第 1 帧开始时调用 `startCapture`，在第 3 帧之后调用 `stopCapture`，则跟踪信息将包含系统在这三帧中提交的所有缓冲区的命令数据。

### 使用捕获范围捕获特定命令

要了解如何向你的 App 添加自定义范围，请参阅[创建并使用自定义捕获范围](creating-and-using-custom-capture-scopes.md)。要使用自定义范围捕获命令，请创建一个 [MTLCaptureScope](../metal/mtlcapturescope.md) 对象，并将捕获描述符的 [captureObject](../metal/mtlcapturedescriptor/captureobject.md) 属性设置为指向该范围。

> [!important] 重要
> 将 `outputURL` 的文件扩展名设置为 `.gputrace`，以确保你稍后可以在 Metal 调试器中重放该文件。有关重放 GPU 跟踪文件的更多信息，请参阅[重放 GPU 跟踪文件](replaying-a-gpu-trace-file.md)。

```swift
func setupProgrammaticCaptureScope(device: MTLDevice) {
    myCaptureScope = MTLCaptureManager.shared().makeCaptureScope(device: device)
    myCaptureScope?.label = "My Capture Scope"
}

func triggerProgrammaticCaptureScope() {
    guard let captureScope = myCaptureScope else { return }
    let captureManager = MTLCaptureManager.shared()
    let captureDescriptor = MTLCaptureDescriptor()
    captureDescriptor.captureObject = captureScope
    do {
        try captureManager.startCapture(with: captureDescriptor)
    } catch {
        fatalError("error when trying to capture: \(error)")
    }
}
```

要定义范围捕获的边界，请在要捕获的命令之前和之后分别调用 [MTLCaptureScope](../metal/mtlcapturescope.md) 对象的 [begin()](<../metal/mtlcapturescope/begin().md>) 和 [end()](<../metal/mtlcapturescope/end().md>) 方法。当你的 App 到达捕获范围对应的 `end()` 方法时，Xcode 会自动停止捕获。

```swift
func runMetalCommands(commandQueue: MTLCommandQueue) {
    myCaptureScope?.begin()
    let commandBuffer = commandQueue.makeCommandBuffer()!
    // 执行 Metal 工作。
    commandBuffer.commit()
    myCaptureScope?.end()
}
```

> [!important] 重要
> 捕获范围仅捕获你在范围开始后创建、并在范围结束前提交的那些 [MTLCommandBuffer](../metal/mtlcommandbuffer.md) 对象中的命令。

### 将捕获保存到电脑

如果你想稍后分析捕获的内容，可以跳过启动 Metal 调试器，直接将 GPU 命令信息保存到 GPU 跟踪文件中。在尝试记录跟踪文件之前，先调用捕获管理器的 [supportsDestination(_:)](<../metal/mtlcapturemanager/supportsdestination(__).md>) 方法，以确保该功能可用。

```swift
let captureManager = MTLCaptureManager.shared()

guard captureManager.supportsDestination(.gpuTraceDocument) else {
    print("Capturing to a GPU trace file isn't supported.")
    return
}
```

然后，将捕获描述符的 destination 属性设置为 `MTLCaptureDestination.gpuTraceDocument`，并指定文件的目标路径。

```swift
let captureDescriptor = MTLCaptureDescriptor()
captureDescriptor.captureObject = self.device
captureDescriptor.destination = .gpuTraceDocument
captureDescriptor.outputURL = self.traceURL
...
```

有关重放 GPU 跟踪文件的更多信息，请参阅[重放 GPU 跟踪文件](replaying-a-gpu-trace-file.md)。

## 另请参阅

### 基础

- [在 Xcode 中捕获 Metal 工作负载](capturing-a-metal-workload-in-xcode.md) — 通过配置项目以使用 Metal 调试器来分析你 App 的性能。
- [重放 GPU 跟踪文件](replaying-a-gpu-trace-file.md) — 使用 Metal 调试器中的 GPU 跟踪文件调试和分析你 App 的性能。
- [调查视觉伪影](investigating-visual-artifacts.md) — 使用 Metal 调试器发现、诊断并修复你 App 中的视觉伪影。
- [优化 GPU 性能](optimizing-gpu-performance.md) — 使用 Metal 调试器查找并解决性能瓶颈。
- [使用交互式命令行工具进行调试](debugging-with-interactive-command-line-tools.md) — 无需离开终端即可调查 GPU 跟踪中的渲染问题。
- [使用 AI 代理调查 GPU 问题](investigating-gpu-issues-with-ai-agents.md) — 通过将大型 GPU 跟踪交给 AI 代理进行自主调查，找到问题的根本原因。
