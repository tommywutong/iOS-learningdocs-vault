---
title: 配置强化运行时
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/configuring-the-hardened-runtime
source_url: 'https://developer.apple.com/documentation/xcode/configuring-the-hardened-runtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/configuring-the-hardened-runtime.json'
content_hash: 'sha256:7adf3366537d7199'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [能力](capabilities.md)

# 配置强化运行时

<sub>文章</sub>

通过限制对敏感资源的访问并防范常见漏洞利用，保护你的 macOS App 的运行时完整性。

## 概述

_强化运行时（Hardened Runtime）_ 是一组由系统强制实施的限制，它会停用某些功能（例如加载第三方框架），并禁止访问受限资源（例如设备的内置摄像头），以防止某些类型的漏洞利用危害你的 macOS App 的运行时完整性。如果你的 App 依赖强化运行时所限制的功能，可以向 App 的 entitlement 文件添加相应 entitlement，以移除该项特定保护。Xcode 的 Hardened Runtime 能力提供了一种管理这些 entitlement 的简便方式。

在选择你的 App 所需的运行时例外和受限资源访问权限之前，请按照[为 App 添加能力](adding-capabilities-to-your-app.md)中的[添加能力](adding-capabilities-to-your-app.md#Add-a-capability)一节所述步骤，为 macOS App 的 target 添加 Hardened Runtime 能力。如果使用模板创建新的 macOS App，Xcode 会自动为 App 添加 Hardened Runtime 能力。

![Xcode 的 Capabilities 资源库截图，其中 Hardened Runtime 能力处于选中状态。](../../../attachments/1f958077627be4b499f7ec9fbc2f2d9e/hardened-runtime@2x.png)

> [!important] 重要
> Apple 只对启用了 Hardened Runtime 能力的 macOS App 进行公证。有关更多信息，请参阅[在分发前公证 macOS 软件](../security/notarizing-macos-software-before-distribution.md)。

### 指定 App 的运行时例外

你的 App 要执行依赖一个或多个运行时例外的功能，必须先按以下步骤添加这些例外所需的 entitlement：

1. 在 Xcode 的 Project 导览器中选择你的项目。
2. 在 Targets 列表中选择 App 的 target。
3. 在项目编辑器中点按 Signing & Capabilities 标签页。
4. 找到 Hardened Runtime 能力的 Runtime Exceptions 部分。
5. 勾选相应复选框，以选择一个或多个运行时例外。

![](../../../attachments/c145206f3f710dfbdfb8a90d131eaf71/runtime-exceptions@2x.png)

<sub>Hardened Runtime 能力中可用运行时例外的截图，其中 Allow Execution of JIT-compiled Code 例外处于启用状态。</sub>

Xcode 会自动更新 App 的 entitlement 文件，加入与所选运行时例外相对应的 entitlement，并将这些 entitlement 的值设为 `true`。

下表介绍了 Hardened Runtime 支持的运行时例外：

| 名称 | 功能 |
|---|---|
| Allow Execution of JIT-compiled Code | 使用 `MAP_JIT` 标志创建可写且可执行的内存。有关更多信息，请参阅[允许执行 JIT 编译代码的 entitlement](../bundleresources/entitlements/com.apple.security.cs.allow-jit.md)。 |
| Allow Unsigned Executable Memory | 创建可写且可执行的内存，而不受 `MAP_JIT` 标志所施加的限制。适用于旧式 App。有关更多信息，请参阅[允许未签名可执行内存的 entitlement](../bundleresources/entitlements/com.apple.security.cs.allow-unsigned-executable-memory.md)。 |
| Allow DYLD Environment Variables | 使用动态链接变量修改 App 的运行时行为。有关更多信息，请参阅[允许 DYLD 环境变量的 entitlement](../bundleresources/entitlements/com.apple.security.cs.allow-dyld-environment-variables.md)。 |
| Disable Library Validation | 加载由第三方开发者编写的框架和插件。有关更多信息，请参阅[停用库验证的 entitlement](../bundleresources/entitlements/com.apple.security.cs.disable-library-validation.md)。 |
| Disable Executable Memory Protection | 停用代码签名（code signing）所提供的保护。有关更多信息，请参阅[停用可执行内存保护的 entitlement](../bundleresources/entitlements/com.apple.security.cs.disable-executable-page-protection.md)。 |
| Debugging Tool | 通过向系统表明你的 App 是调试器，附加到其他进程或获取任务端口。有关更多信息，请参阅[调试工具 entitlement](../bundleresources/entitlements/com.apple.security.cs.debugger.md)。 |

> [!warning] 警告
> 某些运行时例外（例如 Disable Executable Memory Protection）会移除 App 的核心安全屏障。使用运行时例外时务必谨慎，并选择能够启用所需功能的最小 entitlement 集合。

### 指定 App 所需的资源访问权限

如果你的 App 会访问受限或敏感资源（例如用户的照片图库或通讯录），必须按以下步骤加入用于访问这些资源的 entitlement：

1. 在 Xcode 的 Project 导览器中选择你的项目。
2. 在 Targets 列表中选择 App 的 target。
3. 在项目编辑器中点按 Signing & Capabilities 标签页。
4. 找到 Hardened Runtime 能力的 Resource Access 部分。
5. 勾选相应复选框，以选择一个或多个资源的访问权限。

![](../../../attachments/439b2e6bbb7e1397166eb71ca5c3947a/resource-access@2x.png)

<sub>Hardened Runtime 能力中可用资源访问选项的截图，其中 Audio Input 选项处于启用状态。</sub>

选择所需的资源访问权限后，Xcode 会更新 App 的 entitlement 文件，加入相应的 entitlement，并将这些 entitlement 的值设为 `true`。

> [!important] 重要
> 即使 App 包含必要的 entitlement，在访问摄像头等受限资源前仍必须征得用户的明确许可。具体要求请参阅各资源对应的框架文档。

下表介绍了 Hardened Runtime 支持的资源访问 entitlement：

| 名称 | 功能 |
|---|---|
| Audio Input | 使用内置麦克风录制音频，并通过 Core Audio API 访问音频输入。有关更多信息，请参阅[音频输入 entitlement](../bundleresources/entitlements/com.apple.security.device.audio-input.md)。 |
| Camera | 使用内置和外接摄像头拍摄图像和影片。有关更多信息，请参阅[摄像头 entitlement](../bundleresources/entitlements/com.apple.security.device.camera.md)。 |
| Location | 使用定位服务确定用户的位置。有关更多信息，请参阅[定位 entitlement](../bundleresources/entitlements/com.apple.security.personal-information.location.md)。 |
| Contacts | 启用对用户通讯录数据库的读写访问。有关更多信息，请参阅[通讯录 entitlement](../bundleresources/entitlements/com.apple.security.personal-information.addressbook.md)。 |
| Calendar | 启用对用户日历的读写访问。有关更多信息，请参阅[日历 entitlement](../bundleresources/entitlements/com.apple.security.personal-information.calendars.md)。 |
| Photos Library | 启用对用户照片图库的读写访问。有关更多信息，请参阅[照片图库 entitlement](../bundleresources/entitlements/com.apple.security.personal-information.photos-library.md)。 |
| Apple Events | 向其他 App 和进程发送 Apple Events。有关更多信息，请参阅[Apple Events entitlement](../bundleresources/entitlements/com.apple.security.automation.apple-events.md)。 |

## 另请参阅

### 安全性

- [配置家庭控制](configuring-family-controls.md) — 添加 Family Controls entitlement，为你的 App 及其 Screen Time API App 扩展启用家长控制功能。
- [配置 macOS App 沙盒](configuring-the-macos-app-sandbox.md) — 通过限制对文件系统、网络连接等的访问，保护系统资源和用户数据免受受损 App 的侵害。
- [配置钥匙串共享](configuring-keychain-sharing.md) — 在属于同一开发者的多个 App 之间共享钥匙串项目。
- [使用 macOS 上的容器保护本地 App 数据](protecting-local-app-data-using-containers.md) — 保护你的 App 的本地存储数据，使其免遭未经授权的访问和修改。
- [在现有 macOS App 中访问 App Group 容器](accessing-app-group-containers.md) — 确保你的 App 具备 App Group 容器 entitlement，并且 macOS 能够对其进行授权。
