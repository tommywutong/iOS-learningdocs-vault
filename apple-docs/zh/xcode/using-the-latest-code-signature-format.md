---
title: 使用最新的代码签名格式
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/using-the-latest-code-signature-format
source_url: 'https://developer.apple.com/documentation/xcode/using-the-latest-code-signature-format'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/using-the-latest-code-signature-format.json'
content_hash: 'sha256:619b5749b669cb70'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Distribution](distribution.md)

# 使用最新的代码签名格式

<sub>文章</sub>

更新旧版 App 代码签名，让你的 App 能够在当前操作系统版本上运行。

## 概述

分发 App 之前，你需要为其应用代码签名。签名可证明你是 App 的创建者，并让系统能够检测 App 签名后发生的意外或恶意修改。作为一项安全措施，iOS 会拒绝启动缺少签名或签名无效的 App。

从 iOS 15、iPadOS 15、tvOS 15 和 watchOS 8 开始，系统会检查一种更安全的新签名格式。该格式使用可辨别编码规则（Distinguished Encoding Rules，DER）将 entitlement 嵌入 App 签名。使用先前签名格式签名的 App 将无法启动。

### 确定 App 是否需要新签名

对 DER 嵌入式 entitlement 的这项更改不会影响大多数 App。对于通过 App Store 或 TestFlight 分发的 App，App Store Connect 会先验证你的签名，然后使用 Apple 身份重新签署 App，之后再让 App 可供下载。通过这些渠道提供的 App 已经使用新签名格式。

对于通过其他方式分发的 App（例如 Ad Hoc 或通过 [Apple Developer Enterprise Program](https://developer.apple.com/programs/enterprise) 分发），Xcode 和 `codesign` 实用工具多年来一直会创建使用新格式的签名。如果你在运行 macOS 10.14 至 macOS 11 的 Mac 上签署 App，App 已使用新签名格式，但签名可能不包含必需的 DER entitlement。macOS 11 及更高版本默认会使用包含 DER entitlement 的新签名格式签署 App bundle。

要检查名为 `MyApp.app` 的 App 是否使用新签名，可以使用 [codesign](x-man-page://1/codesign) 实用工具：

```other
% codesign -dv /path/to/MyApp.app
```

在输出中查找类似 `CodeDirectory v=20500` 的字符串。如果 `v` 的值小于 `20400`，则需要重新签署 App。

如果代码目录值为 20400 或更高，但 App 无法安装到 iOS 15、iPadOS 15、tvOS 15 或 watchOS 8，请确认系统已将 DER entitlement 添加到 App 签名。还要确认所有嵌套代码均已正确签名，例如 App 扩展、框架或捆绑的 watchOS App。

要检查 App 是否包含 DER entitlement，请在签名中查找 Page size 下方的哈希列表。如果 `-5` 包含值，而 `-7` 包含零值或不存在，则需要重新签署 App，以包含新的 DER entitlement。

有效签名：

```other
Page size=4096
     -7=f4c7c0ae394247097dca9b19333001200747691e1d9e25ec0cf0f35a8ade21f3
     -6=0000000000000000000000000000000000000000000000000000000000000000
     -5=7379374fd375633558fd972e33809c06e61f9f8191f67c71875899b0dc290945
     -4=0000000000000000000000000000000000000000000000000000000000000000
     -3=53cc3cc9830555e6d7bc864522fdf160b61ccc0d2fda9331368d333dfaa4fe24
```

无效签名：

```other
Page size=4096
     -5=7c741a970873bb7f6a05c1ad5b9425f4b5b1ac86645b2cb8c842a57f51818eb5
     -4=0000000000000000000000000000000000000000000000000000000000000000
     -3=f7ddc8d932def2f393dfc1719252e61b1561afeed76d32044ae0cd793e380bc6
     -2=904f563968898c7569794e19bcd9304d46ca5c0b9f09c792081bdb8ec9c04c92
```

### 确定 App 是否需要新的预置描述文件

从 iOS 15、iPadOS 15、tvOS 15 和 watchOS 8 开始，如果 App 具有你在 `com.apple.developer` 命名空间之外构建、且预置描述文件默认不包含的 entitlement（包括 `application-identifier` 或 `get-task-allow`），则可能需要 DER 编码版本的预置描述文件。从 Xcode 13 开始，预置描述文件默认使用 DER 编码签发。如果 App 能够成功安装但无法启动，则需要使用新的预置描述文件重新签署 App。有关 DER 编码预置描述文件的更多信息，请参阅[预置描述文件更新](https://developer.apple.com/help/account/manage-profiles/provisioning-profile-updates)。

### 重新签署 App

如果 App 没有使用新签名格式，或签名中缺少 DER entitlement，则需要在运行 macOS 11 或更高版本的 Mac 上重新签署 App，这些版本默认包含 DER 编码。

如果无法使用 macOS 11 或更高版本重新签署 App，可以在 macOS 10.14 及更高版本中通过命令行重新签署。为此，请使用以下命令，通过钥匙串中名为“Your Codesign Identity”的签名身份，使用 DER entitlement 重新签署 `MyApp.app` App bundle：

```other
% codesign -s "Your Codesign Identity" -f --preserve-metadata --generate-entitlement-der /path/to/MyApp.app
```

有关使用 codesign 实用工具的更多信息，请通过“终端”查看其 [man 页面](x-man-page://1/codesign)。

> [!important] 重要
> 仅在更新代码签名以包含 DER entitlement 的最后手段下，才通过命令行重新签署 App。iOS、iPadOS、tvOS、visionOS 和 watchOS 不支持通过命令行重新签署 App。建议你在条件允许后尽快使用 macOS 11 或更高版本签署 App。

如果 App 包含嵌套代码，例如 App 扩展、框架或捆绑的 watchOS App，请从嵌套最深的可执行文件开始，分别签署各个项目，然后最后签署主 App。签署框架时不要包含 entitlement 或描述文件，否则会产生无效的代码签名。

有关 App 分发的一般信息，请参阅[分发 App 以进行 Beta 测试和发布](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases)。

## 另请参阅

### 代码签名

- [为 macOS 创建分发签名代码](creating-distribution-signed-code-for-the-mac.md) — 使用 Xcode 或命令行工具签署 Mac 代码以供分发。
- [分发前对 macOS 软件进行公证](../security/notarizing-macos-software-before-distribution.md) — 将 macOS 软件提交给 Apple 进行公证，进一步增强用户信心。
- [使用受限 entitlement 签署守护进程](signing-a-daemon-with-a-restricted-entitlement.md) — 将守护进程封装在类似 App 的结构中，以使用预置描述文件授权的 entitlement。
- [将代码签名身份与开发者账户同步](sharing-your-teams-signing-certificates.md) — 确保你和其他团队成员能够在 Xcode 中签署组织的代码和安装器包。
- [TN3125：代码签名内幕：预置描述文件](../technotes/tn3125-inside-code-signing-provisioning-profiles.md) — 了解预置描述文件如何让第三方代码能够在 Apple 平台上运行。
