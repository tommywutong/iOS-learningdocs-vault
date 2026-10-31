---
title: 保护用户的隐私
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/protecting-the-user-s-privacy
source_url: 'https://developer.apple.com/documentation/uikit/protecting-the-user-s-privacy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/protecting-the-user-s-privacy.json'
content_hash: 'sha256:da358bf405617e4d'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md)

# 保护用户的隐私

保护个人数据，并尊重用户关于数据使用方式的偏好。

## 概述

为用户隐私做设计很重要。大多数 Apple 设备都包含用户不想暴露给 App 或外部实体的个人数据。如果你的 App 不当访问或使用数据，用户可能会停止使用你的 App，甚至将其从设备上删除。

只有在依据适用法律获得用户知情同意的情况下，才能访问用户或设备数据。此外，要采取适当步骤保护用户和设备数据，并对你如何使用这些数据保持透明。

### 审查政府和行业来源的指导方针

请查阅这些文档：

- [Mobile Privacy Disclosures: Building Trust Through Transparency](https://www.ftc.gov/sites/default/files/documents/reports/mobile-privacy-disclosures-building-trust-through-transparency-federal-trade-commission-staff-report/130201mobileprivacyreport.pdf)。联邦贸易委员会关于移动隐私的报告。
- [Opinion 02/2013 on Apps on Smart Devices](https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2013/wp202_en.pdf)。欧盟数据保护专员关于移动 App 数据保护的意见。
- [Privacy on the Go: Recommendations for the Mobile Ecosystem](https://oag.ca.gov/sites/all/files/agweb/pdfs/privacy/privacy_on_the_go.pdf)。加州总检察长关于移动隐私的建议。
- Smartphone Privacy Initiative (2012)，参见 [English](http://www.soumu.go.jp/main_sosiki/joho_tsusin/eng/presentation/pdf/Initiative.pdf) 或 [Japanese](http://www.soumu.go.jp/main_content/000171225.pdf)；以及 Smartphone Privacy Initiative II (2013)，参见 [English](http://www.soumu.go.jp/main_sosiki/joho_tsusin/eng/presentation/pdf/Summary_II.pdf) 或 [Japanese](http://www.soumu.go.jp/main_content/000247654.pdf)。日本总务省的智能手机隐私倡议。

### 仅在 App 需要数据时请求访问

在你的 App 需要数据时，再请求访问位置、联系人、照片等敏感的用户或设备数据。在你的 App 的[信息属性列表](../bundleresources/information-property-list.md)中提供一段用途说明字符串（purpose string，有时也称使用说明字符串），以便系统向用户展示，说明你的 App 为何需要访问权限。在用户未授予所请求数据的访问权限时，提供合理的回退行为。更多细节，参见[请求访问受保护的资源](requesting-access-to-protected-resources.md)。

### 对数据的使用方式保持透明

例如，当你把 App 提交到 App Store 时，作为 App Store Connect 元数据的一部分，为你的隐私政策或声明指定一个 URL。你也可以在 App 描述中概括该政策或声明。

### 让用户控制数据并保护你收集的数据

尊重用户的偏好，并采取合理步骤保护你在 App 中收集的数据：

- 提供设置，让用户能够禁用对敏感信息的访问。对于位置、联系人和健康数据等受保护的系统资源，操作系统会通过「设置」App 的隐私菜单自动完成这一点。把这种行为扩展到你从这些来源缓存或直接收集的任何数据上。例如，如果你的用户构建了包含个人信息的社交媒体资料，请为他们提供删除这些数据的方式（包括你在服务器上的任何副本）。
- 在 iOS 中存储文件时，使用适用于你的 App 的最强数据保护级别，详见[加密你的 App 的文件](encrypting-your-app-s-files.md)。通过网络发送用户或设备数据时，使用 App 传输安全，详见 [NSAppTransportSecurity](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/plist/info/NSAppTransportSecurity)。
- 如果你的 App 使用 [ASIdentifierManager](../adsupport/asidentifiermanager.md) 类，请尊重其 [isAdvertisingTrackingEnabled](../adsupport/asidentifiermanager/isadvertisingtrackingenabled.md) 属性的值。如果用户将该属性设为 false，那么仅将 [ASIdentifierManager](../adsupport/asidentifiermanager.md) 类用于受限的广告用途，例如频次上限、归因、转化事件、估算独立用户数量、广告欺诈检测和调试。更多信息，参见 [AdSupport](../adsupport.md) 框架。
- 如果你必须持久地标识用户，请使用 [UIDevice](uidevice.md) 类的 [identifierForVendor](uidevice/identifierforvendor.md) 属性，或 [ASIdentifierManager](../adsupport/asidentifiermanager.md) 类的 [advertisingIdentifier](../adsupport/asidentifiermanager/advertisingidentifier.md) 属性。

### 使用所需的最低数据量

请求并使用完成给定任务所需的最低限度的用户或设备数据。不要因不必要的或非显而易见的原因访问或收集数据，也不要因为你认为以后可能有用而这样做。

如果你的 App 支持音频输入，请仅在你实际计划开始录制的时刻，把音频会话配置为录制模式。如果你不打算立即录制，不要在启动时把音频会话配置为录制模式。当 App 把音频会话配置为录制模式时，系统会提醒用户，并让用户选择为你 App 禁用录制。

## 主题

### 支持隐私

- [请求访问受保护的资源](requesting-access-to-protected-resources.md) — 提供一段用途说明字符串，向用户解释你为何需要访问其设备上受保护的资源。
- [加密你的 App 的文件](encrypting-your-app-s-files.md) — 通过在磁盘上加密来保护 iOS 中的用户数据。

## 另请参阅

### 基础

- [Adopting Liquid Glass](../technologyoverviews/adopting-liquid-glass.md) — 了解如何将新材质带到你的 App 中。
- [UIKit updates](../updates/uikit.md) — 了解 UIKit 的重要更改。
- [关于使用 UIKit 进行 App 开发](about-app-development-with-uikit.md) — 了解 UIKit 和 Xcode 为你的 iOS 和 tvOS App 提供的基本支持。
