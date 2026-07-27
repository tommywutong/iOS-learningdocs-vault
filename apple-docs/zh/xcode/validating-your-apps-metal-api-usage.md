---
title: 验证 App 的 Metal API 使用情况
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/validating-your-apps-metal-api-usage
source_url: 'https://developer.apple.com/documentation/xcode/validating-your-apps-metal-api-usage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/validating-your-apps-metal-api-usage.json'
content_hash: 'sha256:1cd9f291b6b9ebc3'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Metal developer workflows](metal-developer-workflows.md)

# 验证 App 的 Metal API 使用情况

<sub>文章</sub>

使用 API Validation 捕获 Metal App 中的运行时问题。

## 概述

API Validation 层会检查错误调用 Metal API 的代码，包括创建资源、编码 Metal 命令和执行其他常见任务时的错误。你可以使用 Xcode 中的运行时诊断选项或环境变量启用 API Validation。

> [!important] 重要
> API Validation 层会对 CPU 性能产生轻微但可测量的影响。

### 在 Xcode 中启用 API Validation

按照以下步骤，使用方案设置中的运行时诊断选项启用 API Validation：

1. 在 Xcode 工具栏中，从 Scheme 菜单选取 Edit Scheme。也可以选取 Product \> Scheme \> Edit Scheme。![Xcode 屏幕截图，显示 Scheme 菜单，其中 Edit Scheme 菜单项处于高亮状态。](../../../attachments/6276e85b8ecf3632dbf5391a2175b1f6/gputools-runtime-edit-scheme@2x.png)
2. 在方案操作面板中，选择 Run。
3. 在操作设置标签页中，点按 Diagnostics。
4. 选择 API Validation 将其启用，然后点按 Close。![Xcode 方案编辑器的屏幕截图，其中 API Validation 选项已启用并处于高亮状态。](../../../attachments/5d075c197535b591db100b25d2afbf1f/gputools-runtime-api-validation@2x.png)

现在，每次运行方案时，Xcode 都会启用 API Validation。

你还可以使用 Diagnostics 标签页启用其他 API Validation 行为：

- Include load and store actions：启用此选项可帮助调试不正确的载入和存储操作。它会动态地将 [MTLLoadAction.dontCare](../metal/mtlloadaction/dontcare.md) 改为以品红色执行的 [MTLLoadAction.clear](../metal/mtlloadaction/clear.md)，并向每个使用 [MTLStoreAction.dontCare](../metal/mtlstoreaction/dontcare.md) 存储操作的渲染目标写入红白交替的棋盘格图案。使用此选项调试不正确的载入和存储操作模式，或对“无所谓”行为的错误假设。
- Log non-fatal actions：额外记录不会阻止 App 执行的不正确或次优 Metal 使用情况。使用此选项进一步检查 Metal App。

> [!note] 注意
> 你也可以通过环境变量控制这些选项。

### 使用环境变量启用 API Validation

你还可以在 Metal App 上设置以下环境变量来启用 API Validation：

- **MTL_DEBUG_LAYER=1** — 启用所有 API Validation 测试。
- **MTL_DEBUG_LAYER_ERROR_MODE** — 设置调试层发生错误时的行为。可用值为 `assert`（默认值）、`ignore` 和 `nslog`。`assert` 会让调试层记录错误，然后在错误处触发断言。`ignore` 会让调试层忽略错误，这可能导致未定义行为。`nslog` 会让调试层使用 [NSLog](../foundation/nslog.md) 记录错误，这也可能导致未定义行为。
- **MTL_DEBUG_LAYER_VALIDATE_LOAD_ACTIONS=1** — 使用品红色将所有 [MTLLoadAction.dontCare](../metal/mtlloadaction/dontcare.md) 转换为 [MTLLoadAction.clear](../metal/mtlloadaction/clear.md)，可用于定位和调试不正确的载入操作模式，或对 [MTLLoadAction.dontCare](../metal/mtlloadaction/dontcare.md) 行为的错误假设。
- **MTL_DEBUG_LAYER_VALIDATE_STORE_ACTIONS=1** — 向每个使用 [MTLStoreAction.dontCare](../metal/mtlstoreaction/dontcare.md) 存储操作的渲染目标写入红白交替的棋盘格图案，可用于调试不正确的存储操作模式，或对 [MTLStoreAction.dontCare](../metal/mtlstoreaction/dontcare.md) 行为的错误假设。
- **MTL_DEBUG_LAYER_VALIDATE_UNRETAINED_RESOURCES** — 此选项接受用于启用模式的位字段。默认值为 0x1。位字段值如下：- **0x1** — 启用此标志会让命令缓冲区标记所有绑定到它、但系统内部未保留的对象。如果系统在命令缓冲区完成前释放了已标记对象，Metal Validation 就会引发错误。
- **0x2** — 启用此标志会让命令缓冲区标记它在内部保留的对象。通常不需要此标志，因为命令缓冲区本身尚未完成时，系统无法释放对象。
- **0x4** — 启用此标志会让系统在提交命令缓冲区之前就将已释放的标记对象视为错误。这样能更快地报告错误（例如在释放操作的调用栈中），比提交时报告更便于调试。
- **MTL_DEBUG_LAYER_WARNING_MODE** — 设置调试层发生警告时的行为。可用值为 `assert`、`ignore`（默认值）、`nslog` 和 `oslog`。`assert` 会让调试层记录警告，然后在警告处触发断言。`ignore` 会让调试层忽略警告。`nslog` 会让调试层使用 [NSLog](../foundation/nslog.md) 记录警告。`oslog` 会让调试层使用 [os_log](../os/os_log.md) 记录警告。

如需完整设置列表，请在“终端”中运行 `man MetalValidation`。

> [!note] 注意
> API Validation 只检查 [MTLCommandBuffer](../metal/mtlcommandbuffer.md) 实例中未保留的资源引用，不检查 [MTL4CommandBuffer](../metal/mtl4commandbuffer.md) 中的引用。

## 另请参阅

### 运行时诊断

- [在运行时检查实时资源](inspecting-live-resources-at-runtime.md) — 调试 Metal App 时，通过查看纹理和缓冲区的内容来验证资源。
- [验证 App 的 Metal 着色器使用情况](validating-your-apps-metal-shader-usage.md) — 使用 Shader Validation 捕获常见的着色器运行时问题。
- [监控 Metal App 的图形性能](monitoring-your-metal-apps-graphics-performance.md) — 在 App 运行时，使用 Metal Performance HUD 捕获性能问题。
- [自定义 Metal Performance HUD](customizing-metal-performance-hud.md) — 修改 Metal 平视显示器的外观，以监控图形性能。
- [了解 Metal Performance HUD 指标](understanding-metal-performance-hud-metrics.md) — 了解平视显示器报告的各项指标所表示的含义。
- [使用 Metal Performance HUD 获取性能洞察](gaining-performance-insights-with-metal-performance-hud.md) — 在 App 运行时，使用 Metal 平视显示器捕获潜在的性能问题。
- [使用 Metal Performance HUD 生成性能报告](generating-performance-reports-with-metal-performance-hud.md) — 使用平视显示器记录 App 的性能。
