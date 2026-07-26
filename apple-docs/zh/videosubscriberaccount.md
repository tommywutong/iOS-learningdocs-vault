---
title: Video Subscriber Account
framework: Video Subscriber Account
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/videosubscriberaccount
source_url: 'https://developer.apple.com/documentation/videosubscriberaccount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/videosubscriberaccount.json'
content_hash: 'sha256:78dd63de866c4a5c'
translated: true
---

> 导航：[Technologies](technologies.md)

# Video Subscriber Account

<sub>框架</sub>

支持 TV 提供商与 Apple TV app 的功能。

## 概述

`VideoSubscriberAccount` 提供 API，帮助你创建需要与 TV 提供商的认证服务进行安全通信的 app。该框架还会向 Apple TV app 提供某人是否拥有订阅及其订阅详情的信息。

## 主题

### Essentials

- [Video Subscriber Account updates](updates/videosubscriberaccount.md) — 了解 Video Subscriber Account 中的重要变更。

### TV provider authentication

- [VSAccountManager](videosubscriberaccount/vsaccountmanager.md) — 协调你的 app 与 TV 提供商认证服务之间认证请求的对象。

### TV app integration

- [VSAppleSubscription](videosubscriberaccount/vsapplesubscription-swift.struct.md) — 一位 Apple 流媒体服务客户及其订阅。
- [VSSubscriptionRegistrationCenter](videosubscriberaccount/vssubscriptionregistrationcenter.md) — 存储系统提供给 Apple TV app 的订阅信息的对象。
- [VSAccountApplicationProvider](videosubscriberaccount/vsaccountapplicationprovider.md) — 用于在你的 app 中显示特定于 app 的提供商的对象。

### User account management

- [Signing people in to their media accounts automatically](videosubscriberaccount/signing-people-in-to-media-apps-automatically.md) — 通过在个人的 Apple Account 上管理登录令牌，为媒体流 app 实现单点登录。
- [VSUserAccountManager](videosubscriberaccount/vsuseraccountmanager.md) — 协调你的 app 用户账户操作的对象。
- [VSUserAccount](videosubscriberaccount/vsuseraccount-swift.struct.md) — 表示用户账户的对象。

### Errors

- [VSErrorDomain](videosubscriberaccount/vserrordomain.md) — 该框架中所有错误的域。
- [VSErrorInfoKeySAMLResponse](videosubscriberaccount/vserrorinfokeysamlresponse.md) — 订阅提供商的 SAML 错误响应。
- [VSErrorInfoKeySAMLResponseStatus](videosubscriberaccount/vserrorinfokeysamlresponsestatus.md) — 订阅提供商的 SAML 错误响应状态码。
- [VSErrorInfoKeyAccountProviderResponse](videosubscriberaccount/vserrorinfokeyaccountproviderresponse.md) — 账户提供商的错误响应对象。
- [VSErrorInfoKeyUnsupportedProviderIdentifier](videosubscriberaccount/vserrorinfokeyunsupportedprovideridentifier.md) — 不受支持的订阅提供商的标识符。
- [VSError](videosubscriberaccount/vserror.md) — 该框架错误域中的错误信息。
- [Code](videosubscriberaccount/vserror/code.md) — 该框架错误域中的错误代码。

### Deprecated

- [VSSubscription](videosubscriberaccount/vssubscription.md) — 描述订阅者对内容的访问权限的对象。_(已废弃)_
