---
title: Message-ID 与 iOS 和 macOS 上的 Mail.app 深度链接
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/message-id/'
original_language: en
published: 2019-11-04
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:362828033113a4b8'
translated: true
---

> 原文：[Message-ID and Mail.app Deep Linking on iOS and macOS](https://nshipster.com/message-id/)　·　NSHipster (Mattt)

# [Message-ID 与 iOS 和 macOS 上的 Mail.app 深度链接](https://nshipster.com/message-id/)

作者：[Mattt](https://nshipster.com/authors/mattt/)　　2019 年 11 月 4 日

[上周](https://nshipster.com/device-identifiers/)，我们讨论了设备标识符，并简要探讨了 App 如何使用[设备指纹（device fingerprinting）](https://nshipster.com/device-identifiers/#fingerprinting-in-todays-ios)来绕过 Apple 提供的 API，在用户不知情且未同意的情况下对其进行追踪。作为回应，一些读者联系我们，解释了为何他们使用设备指纹来桥接 Safari 和原生 App 的做法是合理的。

在 WWDC 2018 上，Apple [宣布](https://developer.apple.com/videos/play/wwdc2017/702/)自 iOS 11 起，App 将无法再访问共享的 Cookie 存储。此前，如果用户在 iOS 上的 Safari 中登录了一个网站，然后安装了原生 App，该 App 可以从 `SFSafariViewController` 中获取会话 Cookie，从而自动让用户登录。这一变更旨在作为一项对策，阻止广告商和其他第三方对用户进行追踪，但代价是牺牲了当时使用的一些用户引导流程。

虽然 [iCloud 钥匙串（iCloud Keychain）](https://support.apple.com/en-us/HT204085)、[共享网络凭据（Shared Web Credentials）](https://developer.apple.com/documentation/security/shared_web_credentials)、[密码自动填充（Password Autofill）](https://developer.apple.com/documentation/security/password_autofill)、[通用链接（Universal Links）](https://developer.apple.com/documentation/uikit/inter-process_communication/allowing_apps_and_websites_to_link_to_your_content)以及[通过 Apple 登录（Sign in with Apple）](https://developer.apple.com/documentation/signinwithapplejs/)已大大降低了创建帐户和进行身份验证的摩擦，但仍有一些使用场景未被这些新功能完全覆盖。

在本周的文章中，我们将尝试回答这样一个使用场景，具体是：**如何在 iOS 上通过电子邮件实现无缝的“无密码”身份验证。**

---

## Apple 平台上的邮件与日历集成

在 macOS 和 iOS 上查看电子邮件时，邮件（Mail）会为[检测到的日期和时间](https://nshipster.com/nsdatadetector/)添加下划线。你可以与它们交互来创建新的日历事件。如果你在日历（Calendar）中打开这样的事件，会在其扩展详情中看到一个“在邮件中显示”链接。点击此链接会带你回到原始的电子邮件。

这一功能可以追溯到 iPhone 的发布；同年它在 [Mac OS X 版本（Leopard）](https://daringfireball.net/2007/12/message_urls_leopard_mail)中被包含，标志着移动端功能登陆桌面端的先河。

如果你把这个“神奇”的 URL 复制到剪贴板并在文本编辑器中查看，你会看到类似这样的内容：

```
"message:%3C1572873882024.NSHIPSTER%40mail.example.com%3E"
```

资深的 iOS 开发者会立即认出这是使用了[自定义 URL 方案](https://developer.apple.com/documentation/uikit/inter-process_communication/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app)。其中精通网络的人可以对其进行百分比解码，并认出它类似于电子邮件地址，但并非如此。

_那么，如果它不是电子邮件地址，我们在这里看到的又是什么？_ 这是一个不同的电子邮件字段，称为 Message-ID。

## Message-ID

[RFC 5322 §3.6.4](https://tools.ietf.org/html/rfc5322#section-3.6.4) 规定，每封电子邮件应该有一个“Message-ID:”字段，包含一个唯一的消息标识符。此标识符的语法本质上是一个用尖括号（`<>`）括起来的电子邮件地址。

虽然该规范对于什么构成一个好的 Message-ID 没有规范性指导，但有一份 1998 年的 [IETF 文档草案](https://tools.ietf.org/html/draft-ietf-usefor-message-id-01)至今仍相当适用。

让我们看看如何在 Swift 中做到这一点：

### 生成一个随机的 Message ID

前述文档中描述的第一种技术涉及生成一个带有 64 位随机数（nonce）的随机 Message ID，并在前面附加一个时间戳以进一步减少冲突的可能性。我们可以使用 Swift 5 内置的随机数生成器 API 和 [`String(_:radix:uppercase:)` 初始化方法](https://developer.apple.com/documentation/swift/string/2997127-init)来相当轻松地做到这一点：

```
import Foundation

let timestamp = String(Int(Date().timeIntervalSince1970 * 1000))
let nonce = String(UInt64.random(in: 0..<UInt64.max), radix: 36, uppercase: true)
let domain = "mail.example.com"

let MessageID = "<\(timestamp).\(nonce)@\(domain)>"
//"<[email protected]>"
```

然后我们可以将生成的 Message-ID 与关联的记录一起保存，以便日后链接到它。然而，在许多情况下，一个更简单的替代方案是使 Message ID 成为确定性的，可以从其现有状态计算得出。

### 生成一个确定性的 Message ID

考虑一个遵循 [`Identifiable` 协议](https://nshipster.com/identifiable/)且其关联的 `ID` 类型是 [UUID](https://nshipster.com/uuid-udid-unique-identifier/) 的记录结构。你可以像这样生成一个 Message ID：

```
import Foundation

func messageID<Value>(for value: Value, domain: String) -> String
    where Value: Identifiable, Value.ID == UUID
{
    return "<\(value.id.uuidString)@\(domain)>"
}
```

## 移动端深度链接

iOS 和 macOS 上的自带邮件客户端会尝试打开带有自定义 `message:` 方案的 URL，方法是启动到前台并尝试打开具有编码后 Message-ID 字段的邮件。

### 使用 Message ID 生成邮件深度链接

有了 Message-ID，最后一项任务是创建一个深度链接，用它可以打开邮件应用并定位到关联的邮件。这里唯一的技巧是对 URL 中的 Message ID 进行[百分比编码](https://en.wikipedia.org/wiki/Percent-encoding)。你可以使用 [`addingPercentEncoding(withAllowedCharacters:)` 方法](https://nshipster.com/character-set/) 来做到这一点，但我们更倾向于将这一切委托给 [`URLComponents`](https://nshipster.com/nsurl/)——这还有一个额外的好处，即无需[格式字符串](https://nshipster.com/expressiblebystringinterpolation/)即可完整构建 URL。

```
import Foundation

var components = URLComponents()
components.scheme = "message"
components.host = MessageID
components.string!
// "message://%3C1572873882024.NSHIPSTER%40mail.example.com%3E"
```

### 打开邮件深度链接

如果你在 iOS 上打开一个 `message:` URL，并且链接的邮件在你的某个帐户的收件箱中可以被快速访问，邮件（Mail）将立即启动并打开该邮件。如果未找到该邮件，App 将启动并在后台异步加载邮件，一旦可用便将其打开。

例如，[Flight School](https://flight.school/) 在其无密码身份验证系统中使用了此方法。要访问你购买的电子书，你需要输入购买时使用的电子邮件地址。提交表单后，iOS 上的用户会看到一个深度链接，用于打开邮件（Mail）应用，定位到包含“魔法登录链接”✨ 的电子邮件。

其他系统可能会使用 Message-ID，通过通用链接来简化其原生 App 或网站的无密码身份验证，或者将其作为双因素身份验证（2FA）策略的一部分（因为[SMS 已不再被视为安全可靠的方式](https://pages.nist.gov/800-63-3/sp800-63b.html#ooba)）。

---

与 Apple 平台上许多保持为第一方 App 专属领域的私有集成不同，“在邮件中显示”的秘密武器是我们所有人都可以使用的。虽然未记录在案，但由于其深度的系统集成和基于基础 Web 标准，该功能不太可能在短期内被移除。

在这个时代，从[浏览器厂商](https://amp.dev)和[社交媒体公司](https://facebook.com)到[政府](https://en.wikipedia.org/wiki/Internet_censorship)——甚至有时 Apple 本身——都试图拆解开放的 Web 并控制我们能看到和做什么，得知电子邮件在[近 50 年](http://openmap.bbn.com/~tomlinso/ray/mistakes.html)后，仍坚定不移地保持互联网的自由和去中心化，这令人感到欣慰。
