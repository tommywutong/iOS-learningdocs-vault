---
title: 'TN3125：深入代码签名：配置文件'
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/technotes/tn3125-inside-code-signing-provisioning-profiles
source_url: 'https://developer.apple.com/documentation/technotes/tn3125-inside-code-signing-provisioning-profiles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/technotes/tn3125-inside-code-signing-provisioning-profiles.json'
content_hash: 'sha256:9d7a83d81d2cadc6'
translated: true
---

> 导航：[技术](../technologies.md) · [技术笔记](../technotes.md)

# TN3125：深入代码签名：配置文件

<sub>文章</sub>

了解配置文件如何使第三方代码能够在 Apple 平台上运行。

## 概述

代码签名是所有 Apple 平台的基础技术。许多讨论代码签名的文档都侧重于解决特定问题。而《深入代码签名》技术笔记系列则有所不同：它揭开了代码签名的幕后，让你更好地理解这项技术的工作原理。阅读这些技术笔记，可以让你一开始就做出更好的代码签名选择，理解 Apple 的代码签名工具为何如此运作，为你调查遇到的任何代码签名问题提供参考，而且学习新知识本身就很有趣！

《深入代码签名》系列的其他技术笔记包括：

- [TN3126：深入代码签名：哈希值](tn3126-inside-code-signing-hashes.md)
- [TN3127：深入代码签名：需求](tn3127-inside-code-signing-requirements.md)
- [TN3161：深入代码签名：证书](tn3161-inside-code-signing-certificates.md)

> [!important] 重要
> 《深入代码签名》技术笔记讨论的代码签名细节不被视为 API。代码签名的结构过去已经多次更改，并且未来可能再次更改。请勿在你的产品中对这些信息进行硬编码。签署代码时，请使用 Xcode（所有平台）或 `codesign` 工具（仅限 macOS）。要获取信息或验证代码签名，请使用 `codesign` 工具或[代码签名服务](../security/code-signing-services.md) API。Apple 会更新这些设施，以适应代码签名结构在推出时的任何更改。

## 配置文件基础

除 macOS 外，Apple 平台不会运行任意的第三方代码。所有第三方代码的执行都必须获得 Apple 的授权。这种授权以配置文件（provisioning profile）的形式出现，它将以下五个条件联系在一起：

- 谁有资格签署代码？
- 他们可以签署哪些 App？
- 这些 App 可以在哪里运行？
- 这些 App 可以在何时运行？
- 这些 App 可以拥有哪些 entitlement？

> [!note] 注意
> 在本文档中，术语 _App_ 指打包在 bundle 结构中的主要可执行文件。这包括 App、App 扩展、轻 App（App Clip）、系统扩展和 XPC 服务。

你可以使用 Apple Developer 网站创建配置文件，可以直接通过网站，也可以间接通过 Xcode 或 [App Store Connect API](../appstoreconnectapi.md)。

当 Apple Developer 网站为你创建配置文件时，它会对其进行加密签名。当你在设备上运行 App 时，设备会检查此签名以确定配置文件是否有效，如果有效，则会检查 App 是否符合配置文件中的条件。

> [!note] 注意
> 与 Apple 的其他平台不同，macOS 不需要配置文件来运行第三方代码。但是，配置文件在 macOS 上仍然相关，如 [macOS 上的 Entitlement](tn3125-inside-code-signing-provisioning-profiles.md#Entitlements-on-macOS) 中所述。

配置文件有一个值得关注的特殊情况：当你将 App 提交到 App Store 时，App Store 会在分发过程中重新签署该 App。在此之前，它会检查 App 是否已正确签署和配置。该检查意味着每个单独的设备无需执行进一步的安全检查，因此最终发布的 App 不包含配置文件。然而，这个第三方代码仍然是通过配置文件授权的，尽管是在 App Store 分发过程中。

## 解包配置文件

配置文件是一个包裹在加密消息语法（Cryptographic Message Syntax，CMS）签名中的属性列表（property list）。要查看原始的属性列表，请使用 `security` 工具移除 CMS 包装：

```shell
% security cms -D -i Profile_Explainer_iOS_Dev.mobileprovision -o Profile_Explainer_iOS_Dev-payload.plist
% cat Profile_Explainer_iOS_Dev-payload.plist 
…
<dict>
  … lots of properties …
</dict>
</plist>
```

有关 CMS 的更多详细信息，请参阅 [RFC 5652](https://tools.ietf.org/html/rfc5652)。

> [!important] 重要
> 配置文件的确切格式并未文档化，并且可能随时更改。请将此处展示的技术用于理解和调试目的。避免基于这些细节构建产品；如果你确实构建了此类产品，请准备好随着 Apple 开发进程的演进更新它。

为了说明这一点，传统的基于属性列表的配置文件视图在现代系统上不再是权威来源。相反，每个配置文件都包含一个 `DER-Encoded-Profile` 属性，该属性保存了配置文件的二进制形式，这才是新的权威来源。有关此转换的更多信息，请参阅[未来是 DER](tn3125-inside-code-signing-provisioning-profiles.md#The-future-is-DER)。

尽管如此，属性列表更易于阅读，因此本技术笔记的大部分内容都将重点放在它上面。

有关这些示例中所用工具的更多信息，请阅读它们的 man 手册。如果你不熟悉该过程，请参阅[阅读 UNIX 手册页面](../os/reading-unix-manual-pages.md)。

## 谁

每个配置文件都有一个 `DeveloperCertificates` 属性，其中包含可以签署该配置文件所涵盖代码的每位开发者的证书。例如：

```shell
% plutil -extract DeveloperCertificates xml1 -o - Profile_Explainer_iOS_Dev-payload.plist
…
<array>
  <data>
  MIIFxDCCBKygAwIBAgIQfv+ckbvr2KtCgVI1ZPkPcjANBgkqhkiG9w0BAQsFADB1MUQw
  …
  PX0ovWucPvYp/HUcOnlbchPf/H63K8Jm5siTJlKsgGYEMX5wCJkh/+mlX1oAOH6CtOLy
  kA==
  </data>
  … perhaps more …
</array>
</plist>
```

要提取特定证书，请将其索引添加到键路径：

```shell
% plutil -extract DeveloperCertificates.0 raw -o - Profile_Explainer_iOS_Dev-payload.plist | base64 -D > cert0.cer
% certtool d cert0.cer 
Serial Number      : 7E FF 9C 91 BB EB D8 AB 42 81 52 35 64 F9 0F 72 
Issuer Name        :
   Common Name     : Apple Worldwide Developer Relations Certification Authority
   …
Subject Name       :
   …
   Common Name     : Apple Development: …
   …
Not Before         : 09:15:23 Apr 21, 2021
Not After          : 09:15:22 Apr 21, 2022
…
```

要了解更多关于代码签名证书的信息，请阅读 [TN3161：深入代码签名：证书](tn3161-inside-code-signing-certificates.md)。

## 什么

大多数配置文件适用于单个 App ID，该 ID 编码在 `Entitlements` \> `application-identifier` 属性中：

```shell
% plutil -extract Entitlements.application-identifier raw -o - Profile_Explainer_iOS_Dev-payload.plist
SKMME9E2Y8.com.example.apple-samplecode.ProfileExplainer
```

> [!note] 注意
> 在 macOS 上，标准的 App ID entitlement 是 `com.apple.application-identifier`。Mac Catalyst App 同时使用 `com.apple.application-identifier` 和 `application-identifier`。

此属性持有一个 App ID，由 App ID 前缀和 bundle ID 组成。在此示例中，`SKMME9E2Y8` 是 App ID 前缀，`com.example.apple-samplecode.ProfileExplainer` 是 bundle ID。

配置文件可能引用通配符 App ID：

```shell
% security cms -D -i Profile_Explainer_Wild_iOS_Dev.mobileprovision -o Profile_Explainer_Wild_iOS_Dev-payload.plist          
% plutil -extract Entitlements.application-identifier raw -o - Profile_Explainer_Wild_iOS_Dev-payload.plist
SKMME9E2Y8.com.example.apple-samplecode.*
```

此配置文件适用于 App ID 以 `SKMME9E2Y8.com.example.apple-samplecode.` 开头的任何 App。

## 哪里

大多数配置文件适用于特定的设备列表。这编码在 `ProvisionedDevices` 属性中：

```shell
% plutil -extract ProvisionedDevices xml1 -o - Profile_Explainer_iOS_Dev-payload.plist 
…
<array>
    <string>00008030-001544522E60802E</string>
    … perhaps more …
</array>
</plist>
```

App Store 分发配置文件没有 `ProvisionedDevices` 属性，因为你无法在本地运行带有 App Store 分发签名的 App。

Developer ID 和 In-House（企业）分发配置文件具有 `ProvisionsAllDevices` 属性，表明它们适用于所有设备。有关 Mac 上 Developer ID 配置文件的更多详细信息，请参阅 [macOS 上的 Entitlement](tn3125-inside-code-signing-provisioning-profiles.md#Entitlements-on-macOS)。

## 何时

每个配置文件都有一个 `ExpirationDate` 属性，用于限制配置文件保持有效的时间。例如：

```shell
% plutil -extract ExpirationDate raw -o - Profile_Explainer_iOS_Dev-payload.plist    
2022-07-23T14:30:34Z
```

此有效期因配置文件类型而异，但通常不超过一年。例外情况是 Developer ID 配置文件，其过期日期非常遥远。

## 如何

每个配置文件都有一个 `Entitlements` 属性，用于授权 App 使用特定的 entitlement。例如：

```shell
% plutil -extract Entitlements xml1 -o - Profile_Explainer_iOS_Dev-payload.plist
…
<dict>
  <key>application-identifier</key>
  <string>SKMME9E2Y8.com.example.apple-samplecode.ProfileExplainer</string>
  <key>com.apple.developer.team-identifier</key>
  <string>SKMME9E2Y8</string>
  <key>get-task-allow</key>
  <true/>
  <key>keychain-access-groups</key>
  <array>
    <string>SKMME9E2Y8.*</string>
    <string>com.apple.token</string>
  </array>
</dict>
</plist>
```

配置文件中的 entitlement 充当允许列表（allowlist）。这不同于 App 声明的 entitlement。要实际声明一个 entitlement，需要将该 entitlement 包含在 App 的代码签名中。

App 声明的每个 entitlement 都必须存在于配置文件的允许列表中，但反之则不然。允许列表包含 App 未声明的 entitlement 是没问题的。

> [!note] 注意
> macOS App 可以声明某些 entitlement，而无需配置文件授权。有关更多信息，请参阅 [macOS 上的 Entitlement](tn3125-inside-code-signing-provisioning-profiles.md#Entitlements-on-macOS)。

允许列表中的某些 entitlement 使用通配符语法。在上面的示例中，`SKMME9E2Y8.*` 表示 App 可以声明任何以 `SKMME9E2Y8.` 为前缀的钥匙串访问组。通配符在 App 的代码签名中没有意义。

要转储 App 声明的 entitlement，请使用带有 `--entitlements` 参数的 `codesign`：

```shell
% codesign --display --entitlements - --xml ProfileExplainer.app | plutil -convert xml1 -o - -
…
<dict>
  <key>application-identifier</key>
  <string>SKMME9E2Y8.com.example.apple-samplecode.ProfileExplainer</string>
  <key>com.apple.developer.team-identifier</key>
  <string>SKMME9E2Y8</string>
  <key>get-task-allow</key>
  <true/>
  <key>keychain-access-groups</key>
  <array>
    <string>SKMME9E2Y8.com.example.apple-samplecode.ProfileExplainer</string>
    <string>SKMME9E2Y8.com.example.apple-samplecode.shared</string>
  </array>
</dict>
</plist>
```

> [!note] 注意
> 默认情况下，`--entitlements` 转储的是 DER 编码的 entitlement 的人类可读表示。上面的示例使用 `--xml` 强制输出 XML。它将输出通过 `plutil` 进行美化打印。要了解有关配置文件中 DER 的更多信息，请参阅[未来是 DER](tn3125-inside-code-signing-provisioning-profiles.md#The-future-is-DER)。

此 App 声明的每个 entitlement 都得到了其配置文件的授权，因此 iOS 允许该 App 运行。请注意，`keychain-access-groups` 的值 `SKMME9E2Y8.com.example.apple-samplecode.ProfileExplainer` 以 `SKMME9E2Y8.` 开头，因此被通配符所允许。

## macOS 上的 Entitlement

macOS App 可以声明某些 entitlement，而无需通过配置文件授权。这些_不受限制的 entitlement_ 包括：

- `com.apple.security.get-task-allow`
- `com.apple.security.application-groups`
- 那些用于启用和配置 [App Sandbox](../security/app-sandbox.md) 的 entitlement
- 那些用于配置 [Hardened Runtime](../security/hardened-runtime.md) 的 entitlement

> [!note] 注意
> 在其他 Apple 平台上，与 `com.apple.security.get-task-allow` 等效的是 `get-task-allow`，并且与这些平台上的所有 entitlement 一样，必须由配置文件授权。此外，App Groups 在 macOS 和其他平台上的工作方式不同。有关详细信息，请参阅 [App Groups Entitlement](../bundleresources/entitlements/com.apple.security.application-groups.md)。

相比之下，_受限的 entitlement_ 必须由配置文件授权。这是 macOS 上一个重要的安全特性。例如，`keychain-access-groups` entitlement 必须由配置文件授权，这意味着其他开发者无法冒充你的 App 来窃取其钥匙串项目。

不使用任何受限 entitlement 的 Mac App 不需要配置文件。即使该 App 在 App Store 上分发也是如此。此规则的唯一例外是 TestFlight，它始终需要配置文件。

macOS 同时支持 App Store 和 Developer ID 分发的配置文件。Developer ID 配置文件不支持某些 entitlement。有关详细信息，请参阅 [Developer Account Help](https://help.apple.com/developer-account/) 中的 [Supported capabilities (macOS)](https://help.apple.com/developer-account/#/devadf555df9)。有关 Developer ID 签名的一般信息，请参阅 [Signing Mac Software with Developer ID](https://developer.apple.com/developer-id/)

## 配置文件位置

在 iOS 开发的早期，通常会（在“设置” App 中）将配置文件整体安装到设备上。这仍然可行，但当前的最佳实践是将配置文件嵌入到 App 本身中：

- macOS 期望在 `MyApp.app/Contents/embedded.provisionprofile` 找到配置文件。
- 其他 Apple 平台期望在 `MyApp.app/embedded.mobileprovision` 找到配置文件。

请注意，macOS 对配置文件使用了不同的文件扩展名。

你从 App Store 下载的 App 不包含嵌入式配置文件，因为 App Store 在其分发过程中会检查 App 是否已正确签署和配置。

一些 macOS 产品，如 daemon 和命令行工具，作为独立的可执行文件分发。独立的可执行文件不能声明受限的 entitlement，因为无法嵌入授权该声明的配置文件。如果你的独立可执行文件需要这样做，请将其包装在类似 App 的结构中。有关示例，请参阅[使用受限 entitlement 签署 daemon](../xcode/signing-a-daemon-with-a-restricted-entitlement.md)。

## 未来是 DER

现代系统不再将配置文件的属性列表视为权威来源。相反，它们使用存储在配置文件 `DER-Encoded-Profile` 属性中的配置文件二进制形式：

```shell
% plutil -extract DER-Encoded-Profile raw -o - Profile_Explainer_iOS_Dev-payload.plist
MIINQQYJKoZIhvcNAQcCoIINMjCCDS4CAQExDzANBglghkgBZQMEAgEFADCCAvwGCSqG…
```

配置文件的这种形式被编码为 DER，这是一种在加密文件格式中常见的 ASN.1 二进制编码。要提取它，首先将属性提取到一个文件中：

```shell
% plutil -extract DER-Encoded-Profile raw Profile_Explainer_iOS_Dev-payload.plist | base64 -D > Profile_Explainer_iOS_Dev.der 
```

这是配置文件的一个全新副本，所以再次解开 CMS 包装：

```shell
% security cms -D -i Profile_Explainer_iOS_Dev.der -o Profile_Explainer_iOS_Dev-payload.der 
```

最后，转储 DER 编码的负载本身：

```shell
% openssl asn1parse -in Profile_Explainer_iOS_Dev-payload.der -inform der -i | cut -c 30- 
SET               
 …
 SEQUENCE          
  UTF8STRING        :ExpirationDate
  UTCTIME           :220723143034Z
 …
 SEQUENCE          
  UTF8STRING        :ProvisionedDevices
  SEQUENCE          
   UTF8STRING        :00008030-001544522E60802E
 SEQUENCE          
  UTF8STRING        :DeveloperCertificates
  SEQUENCE          
   OCTET STRING      [HEX DUMP]:1A6836292903FEFEB3A1303507436AD808BEDE7100E360F8F632579AC7EACA96
 SEQUENCE          
  UTF8STRING        :Entitlements
  appl [ 16 ]       
   INTEGER           :01
   cont [ 16 ]       
    SEQUENCE          
     UTF8STRING        :application-identifier
     UTF8STRING        :SKMME9E2Y8.com.example.apple-samplecode.ProfileExplainer
    SEQUENCE          
     UTF8STRING        :com.apple.developer.team-identifier
     UTF8STRING        :SKMME9E2Y8
    SEQUENCE          
     UTF8STRING        :get-task-allow
     BOOLEAN           :255
    SEQUENCE          
     UTF8STRING        :keychain-access-groups
     SEQUENCE          
      UTF8STRING        :SKMME9E2Y8.*
      UTF8STRING        :com.apple.token
```

此输出包含与属性列表大致相同的信息，只是以 DER 形式编码。

一个例外是 `DeveloperCertificates` 属性。它不包含每个证书的完整副本，而是包含证书的 SHA-256 校验和。假设之前从属性列表中提取的证书名为 `cert0.cer`，运行 `shasum` 来确认该校验和：

```shell
% shasum -a 256 cert0.cer
1a6836292903fefeb3a1303507436ad808bede7100e360f8f632579ac7eaca96 …
```

从 iOS 15、iPadOS 15、tvOS 15 和 watchOS 8 开始，需要使用这种 DER 编码的配置文件。有关此更改的更多信息，请参阅[使用最新的代码签名格式](../xcode/using-the-latest-code-signature-format.md)。

## 修订历史

- **2024-02-06** 添加了指向 [TN3126：深入代码签名：哈希值](tn3126-inside-code-signing-hashes.md) 的链接。进行了其他小幅编辑修改。
- **2022-05-24** 进行了小幅编辑修改。
- **2022-05-03** 以 TN3125 重新发布。添加了[未来是 DER](tn3125-inside-code-signing-provisioning-profiles.md#The-future-is-DER) 部分。更新了示例以使用 `plutil`。同时进行了重要的编辑修改。
- **2021-07-26** 首次以“配置文件到底是什么？”为题在 Apple Developer Forums 上发布。

## 另请参阅

### 最新

- [TN3213：从 Multipeer Connectivity 迁移到 Network framework](tn3213-moving-from-multipeer-connectivity-to-network-framework.md) — 了解如何将你的 Multipeer Connectivity App 迁移到 Network framework。
- [TN3210：为 iPhone 镜像优化你的 App](tn3210-optimizing-your-app-for-iphone-mirroring.md) — 测试你的 App 并改善与 iPhone 镜像的兼容性。
- [TN3211：解决 SwiftUI 中 State 和 ContentBuilder 的源代码不兼容问题](tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder.md) — 针对在 Xcode 27 中构建的 SwiftUI 的两项基础性更改，更新现有代码。
- [TN3212：为 Sidecar 触控支持采用手势识别器](tn3212-adopting-gesture-recognizers-for-sidecar-touch-support.md) — 使用手势识别器处理 Sidecar 触控输入，并更新你的 macOS 27 事件处理代码。
- [TN3208：准备好 App 的启动屏幕以满足 App Store 要求](tn3208-preparing-your-apps-launch-screen-to-meet-app-store-requirements.md) — 了解自 iOS 27 和 iPadOS 27 起，App Store 提交的启动屏幕要求。
- [TN3205：通过 Thunderbolt 使用 RDMA 实现低延迟通信](tn3205-low-latency-communication-with-rdma-over-thunderbolt.md) — 了解如何使用 RDMA over Thunderbolt 在 Mac 计算机集群之间实现低延迟通信。
- [TN3206：更新 Apple Pay 证书](tn3206-updating-apple-pay-certificates.md) — 了解如何创建、管理和轮换 Apple Pay 证书以维持不间断的支付处理。
- [TN3179：了解局域网隐私](tn3179-understanding-local-network-privacy.md) — 了解局域网隐私如何影响你的软件。
- [TN3190：USB 音频设备设计注意事项](tn3190-usb-audio-device-design-considerations.md) — 了解设计符合 USB Audio Device Class 规范的设备的最佳技术。
- [TN3194：处理“通过 Apple 登录”的账户删除和令牌吊销](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md) — 了解管理“通过 Apple 登录”用户会话和响应账户删除请求的最佳技术。
- [TN3193：管理设备端基础模型的上下文窗口](tn3193-managing-the-on-device-foundation-model-s-context-window.md) — 了解如何预算 Apple 设备端基础模型的上下文窗口限制，并在达到限制时处理错误。
- [TN3115：蓝牙状态恢复 App 重新启动规则](tn3115-bluetooth-state-restoration-app-relaunch-rules.md) — 了解蓝牙状态恢复重新启动 iOS App 的条件。
- [TN3192：将 iPad App 从已废弃的 UIRequiresFullScreen key 迁移](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md) — 在更新你的 App 以移除已废弃的全屏兼容模式的同时，支持 iPad 多任务处理和动态调整大小。
- [TN3151：选择正确的网络 API](tn3151-choosing-the-right-networking-api.md) — 了解哪种网络 API 最适合你。
- [TN3111：iOS Wi-Fi API 概览](tn3111-ios-wifi-api-overview.md) — 探索 iOS 上可用的各种 Wi-Fi API 及其预期使用场景。
