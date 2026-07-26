---
title: 加密你的 App 的文件
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/encrypting-your-app-s-files
source_url: 'https://developer.apple.com/documentation/uikit/encrypting-your-app-s-files'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/encrypting-your-app-s-files.json'
content_hash: 'sha256:1ac83b41580306e2'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Protecting the User’s Privacy](protecting-the-user-s-privacy.md)

# 加密你的 App 的文件

<sub>文章</sub>

通过在磁盘上加密数据来保护 iOS 中用户的数据。

## 概述

数据保护是 iOS 的一项功能，你可以用它来保护 App 的文件安全，防止未经授权的访问。当用户为设备设置了有效的密码后，数据保护会自动启用。你照常读写文件，但系统会在后台对你的内容进行加密和解密。加密和解密过程是自动的，并由硬件加速。

你可以为 App 的每个文件指定想要应用的数据保护级别。共有四种级别可供选择，每种级别都决定了你何时可以访问该文件。如果你在创建文件时没有指定保护级别，iOS 会自动应用默认保护级别。

- **无保护。** 该文件始终可访问。
- **首次用户认证后完全保护。**（默认）在用户首次解锁设备之前，该文件不可访问。设备首次解锁后，该文件将保持可访问状态，直到设备关机或重启。
- **打开时完全保护。** 只有当设备处于解锁状态时，你才能打开现有文件。如果你已经打开了某个文件，即使用户之后锁定了设备，你也可以继续访问该文件。你也可以在设备锁定或解锁时创建新文件并访问它们。
- **完全保护。** 该文件仅在设备解锁时才可访问。

要一步创建并加密一个新文件，请用文件内容构造一个数据对象，并调用 [write(to:options:)](<../foundation/data/write(to_options_).md>) 方法。调用该方法时，指定你想应用于该文件的数据保护选项。以下代码展示了一个示例，说明如何将 [Data](../foundation/data.md) 实例的内容写入文件，并使用完全保护级别对其进行加密。

```swift
do {
   try data.write(to: fileURL, options: .completeFileProtection)
}
catch {
   // Handle errors.
}
```

要更改现有文件的数据保护级别，请使用 [NSURL](../foundation/nsurl.md) 的 [setResourceValue(_:forKey:)](<../foundation/nsurl/setresourcevalue(__forkey_).md>) 方法。调用此方法时，将新的数据保护选项赋值给 [fileProtectionKey](../foundation/urlresourcekey/fileprotectionkey.md) 资源键。以下代码展示了一个将此键添加到现有文件的示例。

```swift
do {
   try (fileURL as NSURL).setResourceValue( 
                  URLFileProtection.complete,
                  forKey: .fileProtectionKey)
}
catch {
   // Handle errors.
}
```

### 管理你对已加密文件的访问

根据文件的保护级别，当用户之后锁定设备时，读取或写入其内容的尝试可能会失败。为确保你的 App 能够访问文件，请执行以下操作：

- 为你的需求选择正确的数据保护级别。
- 使用 App 委托的 [- applicationProtectedDataWillBecomeUnavailable:](<uiapplicationdelegate/applicationprotecteddatawillbecomeunavailable(__).md>) 和 [- applicationProtectedDataDidBecomeAvailable:](<uiapplicationdelegate/applicationprotecteddatadidbecomeavailable(__).md>) 方法，以 [completeFileProtection](../foundation/nsdata/writingoptions/completefileprotection.md) 级别关闭并重新打开文件。

将完全保护级别分配给 App 仅在前台运行时才访问的文件。如果你的 App 支持后台功能，比如处理位置更新，请为可能在后台访问的文件分配不同的保护级别。例如，一款健身 App 可能会对其用于在后台记录位置事件的文件使用「打开时完全保护」级别。

包含用户个人信息的文件，或由用户直接创建的文件，始终值得使用最强的保护级别。将完全保护级别分配给用户数据文件，并使用 App 委托方法管理对这些文件的访问。App 委托方法可以让你在文件对 App 变得不可访问之前有时间关闭它们。

## 另请参阅

### 支持隐私

- [请求访问受保护的资源](requesting-access-to-protected-resources.md) — 提供一个用途字符串，向用户说明你为什么需要访问其设备上受保护的资源。
