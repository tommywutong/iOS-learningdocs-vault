---
title: 在 iCloud 中同步 App 偏好设置
framework: Foundation
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 13.5+, iPadOS 13.5+, Mac Catalyst 13.5+, macOS 10.13+, Xcode 11.6+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/synchronizing-app-preferences-with-icloud
source_url: 'https://developer.apple.com/documentation/foundation/synchronizing-app-preferences-with-icloud'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/synchronizing-app-preferences-with-icloud.json'
content_hash: 'sha256:3aba78bf189e1450'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [iCloud](icloud.md)

# 在 iCloud 中同步 App 偏好设置

<sub>示例代码</sub>

将 App 偏好设置存储在 iCloud 中，并在用户已连接设备上运行的 App 实例之间共享它们。

## 概述

本示例演示如何使用 [NSUbiquitousKeyValueStore](nsubiquitouskeyvaluestore.md) 类将偏好、配置和 App 状态数据存储在 iCloud 键值存储中。随后，你可以与连接到用户 iCloud 账户的每台设备上运行的所有 App 实例共享这些数据。

在本示例中，用户选择一种背景颜色。随后，使用同一 iCloud 账户登录的其他设备上运行的 App 实例会收到通知并匹配该颜色。

> [!note] Note
> 使用 [NSUbiquitousKeyValueStore](nsubiquitouskeyvaluestore.md) 时，你的总空间上限为 1 MB。不要用它存储大量数据。

键值存储不能替代 [UserDefaults](userdefaults.md) 或其他用于保存相同数据的本地技术。键值存储的用途是在同一用户不同设备上运行的 App 实例之间同步键值数据。如果某台设备上未启用 iCloud 或 iCloud 不可用，App 仍会在 [UserDefaults](userdefaults.md) 中保留数据的本地副本。

## 配置示例代码项目

要配置你的 Xcode 项目，首先需要把 macOS 和 iOS 两个 target 的 Bundle Identifiers 更改为你自己的。接下来，要使用 iCloud 和 [NSUbiquitousKeyValueStore](nsubiquitouskeyvaluestore.md)，你需要为两个 target 设置 iCloud 键值存储 ID。本示例已经为两个 target 设置好了 iCloud 功能，并已创建 `PrefsInCloud.entitlements` 文件。你需要在那些 entitlement 文件中填入你自己的键值存储 ID 来完成配置。

对于每个 target（iOS 和 macOS）：

1. 在 Xcode 项目中，打开 target 的 `PrefsInCloud.entitlements` 文件。
2. 在该文件中，找到 `com.apple.developer.ubiquity-kvstore-identifier` entitlement，并将 `$(CFBundleIdenfier)` 替换为你的键值存储 ID（即 `$(TeamIdentifierPrefix)<your key-value_store ID>`）。例如，如果你的键值存储 ID 是「com.mycompany.myKeyValueStoreID」，则应如下所示：`$(TeamIdentifierPrefix)com.mycompany.myKeyValueStoreID`。两个 target 的键值存储 ID 部分必须相同，这一点很重要。

除了配置项目外，你还需要配置项目运行的设备。

要配置 iOS 和 macOS 设备，请确认 iCloud 云盘已开启。然后在两台设备上登录同一个 iCloud 账户。

构建并运行 App 以将其安装到两台设备上，然后执行以下操作：

- iOS：轻点右上角的操作按钮来选择想要的背景颜色。
- macOS：从窗口的弹出菜单中选择想要的背景颜色。

所选颜色代表一个值（编号 0 到 3），该值会上传到 iCloud。登录同一 iCloud 账户的其他设备上运行的 App 实例会收到通知，以匹配该特定背景颜色。

> [!important] Important
> 键值存储旨在存储不常更改的数据。在测试设备时，如果某台设备上的 App 频繁更改键值存储，系统可能会推迟某些更改的同步，以尽量减少与服务器往返的次数。App 更改得越频繁，更改被推迟、不会立即出现在其他设备上的可能性就越大。

## 注册以响应键值存储更改

示例使用 [NotificationCenter](notificationcenter.md) 注册为通知 [NSUbiquitousKeyValueStoreDidChangeExternallyNotification](nsubiquitouskeyvaluestore/didchangeexternallynotification.md) 的观察者。下面的示例将 App 安装为观察者，以响应键值存储的更改：

```swift
NotificationCenter.default.addObserver(self,
    selector: #selector(ubiquitousKeyValueStoreDidChange(_:)),
    name: NSUbiquitousKeyValueStore.didChangeExternallyNotification,
    object: NSUbiquitousKeyValueStore.default)
```

在调用 `addObserver` 之后立即调用 `synchronize()`，以获取自上次启动以来的键值存储更改。操作系统控制键和值何时上传到 iCloud。调用 `synchronize()` 只是将它们存入本地缓存，并通知 iCloud 有等待上传的新数据。

## 响应键值存储更改

示例使用 [NotificationCenter](notificationcenter.md) 注册为通知 [NSUbiquitousKeyValueStoreDidChangeExternallyNotification](nsubiquitouskeyvaluestore/didchangeexternallynotification.md) 的观察者，以检测 iCloud 中的值变化。

示例实现了函数 `ubiquitousKeyValueStoreDidChange` 来监听键值通知更改。当云中的键值存储被外部更改时会调用此函数。它用新的键值颜色替换旧的颜色。此外，此函数还会更新 [UserDefaults](userdefaults.md) 的键值。

本示例通过使用通知的 `userInfo` 中的 [NSUbiquitousKeyValueStoreChangeReasonKey](nsubiquitouskeyvaluestorechangereasonkey.md) 来检查更改原因。

```swift
guard let userInfo = notification.userInfo else { return }

// 获取通知的原因（初始下载、外部更改或超出配额更改）。
guard let reasonForChange = userInfo[NSUbiquitousKeyValueStoreChangeReasonKey] as? Int else { return }
```

键值通知更改的原因是以下之一：

- [NSUbiquitousKeyValueStoreServerChange](nsubiquitouskeyvaluestoreserverchange.md)：值被来自其他用户／设备的外部来源更改。
- [NSUbiquitousKeyValueStoreInitialSyncChange](nsubiquitouskeyvaluestoreinitialsyncchange.md)：设备首次连接到 iCloud 账户时、以及用户切换其主 iCloud 账户时，会发生初始下载。
- [NSUbiquitousKeyValueStoreQuotaViolationChange](nsubiquitouskeyvaluestorequotaviolationchange.md)：App 的键值存储已超出其在 iCloud 服务器上的空间配额。
- [NSUbiquitousKeyValueStoreAccountChange](nsubiquitouskeyvaluestoreaccountchange.md)：用户更改了主 iCloud 账户。

要获取已更改的键值，请使用通知的 `userInfo` 中的 [NSUbiquitousKeyValueStoreChangedKeysKey](nsubiquitouskeyvaluestorechangedkeyskey.md) 键。

```swift
guard let keys =
          userInfo[NSUbiquitousKeyValueStoreChangedKeysKey] as? [String] else { return }
```

```swift
let possibleColorIndexFromiCloud =
          NSUbiquitousKeyValueStore.default.longLong(forKey: gBackgroundColorKey)
```

## 另请参阅

### App 偏好设置

- [NSUbiquitousKeyValueStore](nsubiquitouskeyvaluestore.md) — 一个基于 iCloud 的键值对容器，可在用户设备上运行的 App 实例之间共享。

## 下载

- [SynchronizingAppPreferencesWithICloud.zip](https://docs-assets.developer.apple.com/published/fbdec1516d89/SynchronizingAppPreferencesWithICloud.zip)
