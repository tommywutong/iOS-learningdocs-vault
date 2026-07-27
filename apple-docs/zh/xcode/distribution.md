---
title: 分发
framework: xcode
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/distribution
source_url: 'https://developer.apple.com/documentation/xcode/distribution'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/distribution.json'
content_hash: 'sha256:205fca24ad519702'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md)

# 分发

准备你的 App，并将其与你的团队、beta 测试者和用户共享。

## 主题

### 基础

- [Preparing your app for distribution](preparing-your-app-for-distribution.md) — 在分发你的 App 之前，配置信息属性列表并添加图标。
- [Changing the bundle identifier](changing-the-bundle-identifier.md) — 修改你的 App 的 bundle 标识符，并在其出现的任何位置更新它。

### 分发与发布

- [Distributing your app for beta testing and releases](distributing-your-app-for-beta-testing-and-releases.md) — 将你的 App 发布给 beta 测试者和用户。
- [Distributing your app to registered devices](distributing-your-app-to-registered-devices.md) — 在你的开发者账户中注册设备，并将你的 App 部署到这些设备上进行测试。
- [Packaging Mac software for distribution](packaging-mac-software-for-distribution.md) — 构建一个 zip 归档、磁盘映像或安装程序包，以分发你的 Mac 软件。

### 代码签名

- [Creating distribution-signed code for macOS](creating-distribution-signed-code-for-the-mac.md) — 使用 Xcode 或命令行工具为 Mac 代码进行分发签名。
- [Using the latest code signature format](using-the-latest-code-signature-format.md) — 更新旧版 App 代码签名，以便你的 App 能在当前的操作系统版本上运行。
- [Notarizing macOS software before distribution](../security/notarizing-macos-software-before-distribution.md) — 通过将你的 macOS 软件提交给 Apple 进行公证，让用户对你的软件更加放心。
- [Signing a daemon with a restricted entitlement](signing-a-daemon-with-a-restricted-entitlement.md) — 将守护进程包装成类似 App 的结构，以使用由描述文件授权的 entitlement。
- [Synchronizing code signing identities with your developer account](sharing-your-teams-signing-certificates.md) — 确保你和其他团队成员能够在 Xcode 中为你所在组织的代码和安装程序包签名。
- [TN3125: Inside Code Signing: Provisioning Profiles](../technotes/tn3125-inside-code-signing-provisioning-profiles.md) — 了解描述文件如何使第三方代码能够在 Apple 平台上运行。

### 测试

- [Testing a release build](testing-a-release-build.md) — 在模拟的用户环境中运行你的 App，以发现和识别部署错误。
- [Testing a beta OS](testing-a-beta-os.md) — 通过测试 beta 操作系统（OS）版本来管理你的 App 中的意外差异。

### 反馈

- [Viewing and responding to feedback from beta testers](viewing-and-responding-to-feedback.md) — 使用 Feedback 管理器跟进 beta 测试者的反馈。

## 另请参阅

### 分发与持续集成

- [Xcode Cloud](xcode-cloud.md) — 使用 Xcode Cloud 自动构建、测试和分发你的 App，以验证更改并创建高质量的 App。
