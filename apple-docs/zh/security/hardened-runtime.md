---
title: 强化运行时
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/hardened-runtime
source_url: 'https://developer.apple.com/documentation/security/hardened-runtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/hardened-runtime.json'
content_hash: 'sha256:05a427443baff12a'
translated: true
---

> 导航：[技术](../technologies.md) · [安全性](../security.md)

# 强化运行时

为 macOS App 管理安全保护和资源访问。

## 概述

强化运行时（Hardened Runtime）与系统完整性保护（System Integrity Protection，SIP）共同保护软件的运行时完整性，防止某些类型的漏洞利用，例如代码注入、动态链接库（DLL）劫持和进程内存空间篡改。要为你的 App 启用强化运行时，请在 Xcode 中导航到目标的“签名与功能（Signing & Capabilities）”信息，点击 + 按钮。在出现的窗口中，选择“强化运行时（Hardened Runtime）”。

![显示在 Xcode 的“签名与功能（Signing & Capabilities）”标签页中点击何处以添加新功能的截屏。](../../../attachments/56cfc71df9e6bfd2a682fdd556780e09/media-3330446@2x.png)

强化运行时不会影响大多数 App 的操作，但确实会禁止某些不太常见的能力，例如即时编译（just-in-time，JIT）。如果你的 App 依赖于强化运行时限制的能力，可以添加一个 entitlement 来禁用某个单独的保护。你要通过启用 Xcode 中列出的某个运行时例外（runtime exception）或访问权限（access permission）来添加 entitlement。请确保仅使用你的 App 功能所绝对必需的 entitlement。

![显示 Xcode 中用于强化运行时例外的部分 entitlement 的截屏。](../../../attachments/e34650edf88337ff29b74fc8176cfc74/media-3330445@2x.png)

你只能对可执行文件添加 entitlement。共享库、框架和进程内插件会继承其宿主可执行文件的 entitlement。

由于在系统中享有特权地位，macOS 会拒绝加载使用了强化运行时例外 entitlement 的系统扩展。此通用规则有一个例外：macOS 允许在非 DEXT 系统扩展中使用[允许执行 JIT 编译代码 entitlement](../bundleresources/entitlements/com.apple.security.cs.allow-jit.md)。

这些布尔值 entitlement 的默认值为 false。当 Xcode 对你的代码进行签名时，仅当值为 true 时才会包含该 entitlement。如果你手动对代码进行签名，请遵循此约定以确保最大兼容性。如果值为 false，请不要包含该 entitlement。

> [!important] 重要
> 要上传 macOS App 进行公证，你必须启用强化运行时能力。有关公证的更多信息，请参阅[在分发前公证 macOS 软件](notarizing-macos-software-before-distribution.md)。

## 主题

### 运行时例外

- [允许执行 JIT 编译代码 entitlement](../bundleresources/entitlements/com.apple.security.cs.allow-jit.md) — 一个布尔值，指示 App 是否可以使用 `MAP_JIT` 标志创建可写且可执行的内存。
- [允许未签名可执行内存 entitlement](../bundleresources/entitlements/com.apple.security.cs.allow-unsigned-executable-memory.md) — 一个布尔值，指示 App 是否可以在不使用 `MAP_JIT` 标志施加限制的情况下创建可写且可执行的内存。
- [允许 DYLD 环境变量 entitlement](../bundleresources/entitlements/com.apple.security.cs.allow-dyld-environment-variables.md) — 一个布尔值，指示 App 是否会受到动态链接器环境变量的影响，你可以使用这些环境变量向 App 的进程注入代码。
- [禁用库验证 entitlement](../bundleresources/entitlements/com.apple.security.cs.disable-library-validation.md) — 一个布尔值，指示 App 是否可以在不要求代码签名的情况下加载任意插件或框架。
- [禁用可执行内存保护 entitlement](../bundleresources/entitlements/com.apple.security.cs.disable-executable-page-protection.md) — 一个布尔值，指示是否在启动 App 以及执行期间禁用所有代码签名保护。
- [调试工具 entitlement](../bundleresources/entitlements/com.apple.security.cs.debugger.md) — 一个布尔值，指示 App 是否是调试器，以及是否可以附加到其他进程或获取任务端口。

### 资源访问

- [音频输入 entitlement](../bundleresources/entitlements/com.apple.security.device.audio-input.md) — 一个布尔值，指示 App 是否可以使用内置麦克风录制音频，以及使用 Core Audio 访问音频输入。
- [相机 entitlement](../bundleresources/entitlements/com.apple.security.device.camera.md) — 一个布尔值，指示 App 是否可以与内置和外接相机交互，以及拍摄影片和静态图像。
- [位置 entitlement](../bundleresources/entitlements/com.apple.security.personal-information.location.md) — 一个布尔值，指示 App 是否可以访问来自“定位服务（Location Services）”的位置信息。
- [通讯录 entitlement](../bundleresources/entitlements/com.apple.security.personal-information.addressbook.md) — 一个布尔值，指示 App 是否可以读写用户通讯录中的联系人。
- [日历 entitlement](../bundleresources/entitlements/com.apple.security.personal-information.calendars.md) — 一个布尔值，指示 App 是否可以读写用户的日历。
- [照片图库 entitlement](../bundleresources/entitlements/com.apple.security.personal-information.photos-library.md) — 一个布尔值，指示 App 是否可以读写用户的“照片（Photos）”图库。
- [Apple 事件 entitlement](../bundleresources/entitlements/com.apple.security.automation.apple-events.md) — 一个布尔值，指示 App 是否可以提示用户允许向其他 App 发送 Apple 事件。
