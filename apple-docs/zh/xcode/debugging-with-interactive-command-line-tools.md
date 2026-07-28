---
title: 使用交互式命令行工具进行调试
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/debugging-with-interactive-command-line-tools
source_url: 'https://developer.apple.com/documentation/xcode/debugging-with-interactive-command-line-tools'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/debugging-with-interactive-command-line-tools.json'
content_hash: 'sha256:ecf66a31d1cd1599'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [Metal 调试器](metal-debugger.md)

# 使用交互式命令行工具进行调试

<sub>文章</sub>

无需离开终端即可调查 GPU 跟踪中的渲染问题。

## 概述

当绘制调用产生不正确的输出（例如阴影缺失、表面呈黑色、出现闪烁伪影等）时，你需要在数百个 API 调用之间导览、检查管线状态并检查资源，以找出根本原因。`gpudebug` 命令让你可以从命令行进行交互式调查，或将调查纳入脚本化工作流。

本文将引导你完成一次完整的调试会话，从打开跟踪到确定视觉伪影的来源。若要查看完整的命令参考，请运行 `man gpudebug`。

## 打开跟踪

使用跟踪文件的路径启动 `gpudebug`。你会获得会话编号和交互式提示符：

```shell
% gpudebug -t /path/to/Scene.gputrace
Session 412 created.
gpudebug — GPU Debugger (v1.0)
Trace:    /path/to/Scene.gputrace
Device:   Apple M4 Max
Summary:  3 command buffers, 18 encoders, 412 draw calls
Replayer ready.
gpudebug> 
```

`REPL` 会立即就绪，但重放器会在后台加载。重放器连接期间，你可以使用 `list` 和 `go` 命令在跟踪结构中导览；需要实时重放的命令（例如 `info pipeline` 和 `fetch`）会阻塞，直到重放器就绪。有关重放器的更多信息，请参阅[重放 GPU 跟踪文件](replaying-a-gpu-trace-file.md)。

## 找到有问题的 pass

直接在树中导览。根节点有四个子节点：`commands`、`performance`、`api_calls` 和 `resources`。从命令缓冲区开始：

```shell
gpudebug> go commands/cb1/re0
Name     Label                                Summary                                 Actions
───────  ───────────────────────────────────  ──────────────────────────────────────  ───────────
color0   "CAMetalLayer Display Drawable (3)"  @tex18                                  info, fetch
color1   "Albedo + Shadow GBuffer"            @tex12 1536x1536 RGBA8Unorm_sRGB        info, fetch
depth    "MTKView Depth Stencil"              @tex15 1536x1536 Depth32Float_Stencil8  info, fetch
grp0     "Draw G-Buffer"                      8 draws                                          go
grp1     "Draw Directional Light"             1 draw                                           go
grp2     "Draw Light Mask"                    1 draw                                           go
grp3     "Draw Point Lights"                  1 draw                                           go
(7 items)
```

进入出现伪影的 G-Buffer pass：

```shell
gpudebug> go grp0/draw6
Name         Label                                Summary                                 Actions
───────────  ───────────────────────────────────  ──────────────────────────────────────  ───────────
pipeline     "G-buffer Creation"                  @rps0                                          info
vertex       "gbuffer_vertex"                     3 buffers                                        go
fragment     "gbuffer_fragment"                   1 buffer, 4 textures                             go
color0       "CAMetalLayer Display Drawable (3)"  @tex18                                  info, fetch
depth        "MTKView Depth Stencil"              @tex15 1536x1536 Depth32Float_Stencil8  info, fetch
indexBuffer  "MDL_OBJ-Indices"                    @buf4                                   info, fetch
(6 items)

Links:
  :a   /api_calls/api45
```

## 检查管线

当绘制产生不正确的输出时，首先检查其管线状态。在管线节点上运行 `info` 命令，以打印入口点、颜色附件格式和顶点布局：

```shell
gpudebug commands/cb1/re0/grp0/draw6> info pipeline
label:  G-buffer Creation
name:   rps0

-- Entry Points --
vertex:    gbuffer_vertex (lib0 "MTLLibrary 1")
fragment:  gbuffer_fragment (lib0 "MTLLibrary 1")

-- Color Attachments --
  color0:  BGRA8Unorm_sRGB  (opaque)
  color1:  RGBA8Unorm_sRGB  (opaque)

-- Vertex Layout --
  buffer 0 (stride=12, perVertex):
    attr0   Float3  @0
  buffer 1 (stride=32, perVertex):
    attr1   Float2  @0
    attr2   Half4   @8
    attr3   Half4   @16
    attr4   Half4   @24
```

绘制调用还会显示编码器状态（剔除模式、绕序、深度模板状态），因此你无需导览到其他位置，就能查看绘制时的完整渲染配置：

```shell
gpudebug commands/cb1/re0/grp0/draw6> info
-[MTLRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:]
  primitiveType:      Triangle
  indexCount:         61266
  indexType:          UInt32
  indexBuffer:        @buf4 "MDL_OBJ-Indices"
  indexBufferOffset:  0

-- Encoder State --
Cull mode             Back
Front facing winding  Clockwise
Stencil front ref     128
Stencil back ref      128
Depth stencil state   @dss0 "G-buffer Creation (2)"
```

## 获取附件以查看输出

若要查看一次绘制实际渲染了什么，请将其颜色附件获取为 PNG 文件：

```shell
gpudebug commands/cb1/re0/grp0/draw6> fetch color0
Fetched .../commands_cb1_re0_grp0_draw6_color0.png (1.8 MiB)
```

若要验证这次绘制是否是问题来源，请后退一步并获取上一次绘制的颜色附件。如果上一次绘制正确渲染，说明问题出在这次绘制的设置中，例如其管线状态、附件或着色器输入：

```shell
gpudebug commands/cb1/re0/grp0/draw6> prev
gpudebug commands/cb1/re0/grp0/draw5> fetch color0
```

## 检查着色器绑定

如果管线状态和附件看起来正确，下一个可疑对象就是着色器接收到的数据。进入 `vertex` 或 `fragment` 节点，列出绑定的缓冲区和纹理：

```shell
gpudebug commands/cb1/re0/grp0/draw6> go vertex
Name    Label                 Summary          Actions
──────  ────────────────────  ───────────────  ───────────
buf[0]  "MTLBuffer 8"         @buf7 252 KiB    info, fetch
buf[1]  "MTLBuffer 9"         @buf8 673 KiB    info, fetch
buf[2]  "LightPositions (2)"  @buf2 640 bytes  info, fetch
(3 items)
```

## 浏览 API 调用

`api_calls` 子树以扁平的时间顺序列表提供每个 Metal API 调用，并内嵌显示实参值：

```shell
gpudebug> go api_calls
Name   Result  API Call                                                         Actions
─────  ──────  ───────────────────────────────────────────────────────────────  ────────
api0           [MTLLayer nextDrawable]                                              info
api1           [@cq0 commandBuffer]                                                 info
api2           [MTLCommandBuffer setLabel:"Shadow commands"]                        info
api3           [MTLCommandBuffer renderCommandEncoderWithDescriptor:<descriptor>]   info
api4           [MTLRenderCommandEncoder setLabel:"Shadow Map Pass"]                 info
api5           [MTLRenderCommandEncoder setRenderPipelineState:@rps4]               info
(showing 5 of 116 — use list N-M or list --all for more)
```

绘制、调度和 blit 调用具有双向链接。从 API 调用使用 `go :d` 可跳转到其绘制节点，从绘制使用 `go :a` 可找到对应的 API 调用。

## 设备选择与会话

默认情况下，`gpudebug` 会在本地 GPU 上重放。若要以远程设备为目标：

```shell
% gpudebug --list-devices
ID     Name       Model       OS
─────  ─────────  ──────────  ──────────
local  my-mac     Mac15,9     macOS 26.2
0      my-iphone  iPhone17,4  iOS 27.0

% gpudebug -t trace.gputrace -d 0
```

> [!important] 重要
> 发现远程设备需要 Xcode 正在运行。Xcode 会提供 `gpudebug` 所连接的设备浏览器服务。

断开连接后会话仍然保留。使用 `exit` 命令分离，然后使用 `gpudebug -s <id>` 重新连接。完成后，使用 `exit --terminate` 结束会话。

## 另请参阅

### 基础

- [在 Xcode 中捕捉 Metal 工作负载](capturing-a-metal-workload-in-xcode.md) — 通过配置项目使用 Metal 调试器，分析 App 的性能。
- [以编程方式捕捉 Metal 工作负载](capturing-a-metal-workload-programmatically.md) — 通过调用 Metal 的帧捕捉功能，分析 App 的性能。
- [重放 GPU 跟踪文件](replaying-a-gpu-trace-file.md) — 使用 Metal 调试器中的 GPU 跟踪文件调试并分析 App 性能。
- [调查视觉伪影](investigating-visual-artifacts.md) — 使用 Metal 调试器发现、诊断并修复 App 中的视觉伪影。
- [优化 GPU 性能](optimizing-gpu-performance.md) — 使用 Metal 调试器查找并解决性能瓶颈。
- [使用 AI agent 调查 GPU 问题](investigating-gpu-issues-with-ai-agents.md) — 将大型 GPU 跟踪交给 AI agent 自主调查，以找出问题的根本原因。
