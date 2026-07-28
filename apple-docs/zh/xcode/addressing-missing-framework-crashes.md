---
title: 处理缺失框架崩溃
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/addressing-missing-framework-crashes
source_url: 'https://developer.apple.com/documentation/xcode/addressing-missing-framework-crashes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/addressing-missing-framework-crashes.json'
content_hash: 'sha256:e1dbb25151dc7995'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [通过崩溃报告和设备日志诊断问题](diagnosing-issues-using-crash-reports-and-device-logs.md) · [识别常见崩溃的原因](identifying-the-cause-of-common-crashes.md)

# 处理缺失框架崩溃

<sub>文章</sub>

从崩溃报告中识别缺失的框架，并调整 App 的构建以正确包含该框架。

## 概述

如果你将 App 的功能模块化为多个框架，App 必须在构建时链接这些框架，并在构建过程中将框架的副本嵌入到 App 包（app bundle）中。如果 App 链接了某个框架但未嵌入它，App 会在启动时崩溃，因为动态链接器（dynamic linker）无法找到缺失的框架。

### 识别缺失的框架

动态链接器 `dyld` 会在崩溃报告的“终止描述”（Termination Description）中输出关于它无法定位的框架的详细信息：

```other
Exception Type: EXC_CRASH (SIGABRT)
Exception Codes: 0x0000000000000000, 0x0000000000000000
Exception Note: EXC_CORPSE_NOTIFY
Termination Description: DYLD, 
    dependent dylib '@rpath/MyFramework.framework/MyFramework' not found for '<path>/MyCoolApp.app/MyCoolApp',
    tried but didn't find: 
    '/usr/lib/swift/MyFramework.framework/MyFramework' 
    '<path>/MyCoolApp.app/Frameworks/MyFramework.framework/MyFramework' 
    '@rpath/MyFramework.framework/MyFramework' 
    '/System/Library/Frameworks/MyFramework.framework/MyFramework'
```

具体消息取决于操作系统及其版本。以下是另一个示例：

```other
Exception Type: EXC_CRASH (SIGABRT)
Exception Codes: 0x0000000000000000, 0x0000000000000000
Exception Note: EXC_CORPSE_NOTIFY
Termination Description: DYLD, Library not loaded: @rpath/MyFramework.framework/MyFramework 
    | Referenced from: <path>/MyCoolApp.app/MyCoolApp 
    | Reason: image not found
```

> [!note] 注意
> 为便于阅读，此示例中加入了额外的换行。在这些示例的原始崩溃报告文件中，`dyld` 信息位于较少的几行内。

### 检查框架的配置

确保框架已正确嵌入到 App 包中——请参阅[在 App 中嵌入框架](https://developer.apple.com/library/archive/technotes/tn2435/_index.html#//apple_ref/doc/uid/DTS40017543)。

如果你无法复现崩溃，请归档 App，将其导出用于 Development 分发，并应用 App 精简（app thinning），如[为 Beta 测试和发布分发 App](distributing-your-app-for-beta-testing-and-releases.md)所述。测试通过 App 精简产生的不同变体，以查看框架是否仅在应用 App 精简后缺失。如果这样能复现崩溃，请执行以下操作：

- 验证框架的“架构”（Architectures，`ARCHS`）构建设置是否为默认值。
- 验证框架的“有效架构”（Valid Architectures，`VALID_ARCHS`）构建设置是否为默认值。
- 验证框架 `Info.plist` 文件中的 [UIRequiredDeviceCapabilities](../bundleresources/information-property-list/uirequireddevicecapabilities.md) 键是否正确指定该框架支持的 CPU 架构。

> [!note] 注意
> 如果缺失的框架来自第三方框架供应商，或使用了第三方开发工具将其集成到你的 App 中，请联系供应商以获取解决此问题的帮助。

## 另请参阅

### 相关文档

- [分析崩溃报告](analyzing-a-crash-report.md) — 识别崩溃报告中有助于诊断问题的线索。
