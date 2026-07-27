---
title: App 扩展支持
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/app-extension-support
source_url: 'https://developer.apple.com/documentation/foundation/app-extension-support'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/app-extension-support.json'
content_hash: 'sha256:a63fe0bbe79ffd88'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md)

# App 扩展支持

<sub>API 集合</sub>

管理 App 扩展与其宿主 App 之间的交互。

## 主题

### 扩展支持

- [NSExtensionRequestHandling](nsextensionrequesthandling.md) — App 扩展用来响应宿主 App 请求的接口。
- [NSExtensionContext](nsextensioncontext.md) — 调用 App 扩展的宿主 App 上下文。

### 共享扩展

- [在 App 的共享扩展中支持建议](supporting-suggestions-in-your-app-s-share-extension.md) — 让你的信息 App 可用于共享表单建议，并使用 SiriKit intent 填充 App 的共享扩展。

### 附件

- [NSItemProvider](nsitemprovider.md) — 在拖放或复制粘贴活动期间，或从宿主 App 向 App 扩展传递数据或文件的项目提供器。
- [NSExtensionItem](nsextensionitem.md) — 表示扩展要处理的项目各个方面的一组不可变值。
- [使用操作扩展为访达添加功能](../appkit/add-functionality-to-finder-with-action-extensions.md) — 实现操作扩展，以便快速访问 App 的常用功能。

### 与宿主 App 交互

- [NSUserActivity](nsuseractivity.md) — App 在某一时刻状态的表示。
- [NSUserActivityDelegate](nsuseractivitydelegate.md) — 用户活动实例通过此接口向其委托（delegate）通知更新。

## 另请参阅

### App 支持

- [任务管理](task-management.md) — 管理 App 的工作，以及它与接力和快捷指令等系统服务的交互方式。
- [资源](resources.md) — 访问与 App 捆绑的资源和其他数据。
- [通知](notifications.md) — 用于广播信息和订阅广播的设计模式。
- [错误与异常](errors-and-exceptions.md) — 响应与 API 交互时出现的问题，并对 App 进行微调以改善调试体验。
- [脚本支持](scripting-support.md) — 允许用户通过 AppleScript 和其他自动化技术控制你的 App，或从 App 内运行脚本。
