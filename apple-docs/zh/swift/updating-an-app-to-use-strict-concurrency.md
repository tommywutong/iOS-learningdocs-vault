---
title: 更新 App 以使用严格并发
framework: Swift
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, watchOS 8.0+, Xcode 16.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/updating-an-app-to-use-strict-concurrency
source_url: 'https://developer.apple.com/documentation/swift/updating-an-app-to-use-strict-concurrency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/updating-an-app-to-use-strict-concurrency.json'
content_hash: 'sha256:db0ca2ebeea718ce'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md) · [Concurrency](concurrency.md)

# 更新 App 以使用严格并发

<sub>示例代码</sub>

使用此代码跟随指南，迁移你的代码，以充分利用 Swift 6 语言模式（Swift 6 language mode）提供的完整并发保护。

## 概述

> [!note] 注意
> 此示例代码项目与 WWDC24 会议 10169：[Migrate your app to Swift 6](https://developer.apple.com/wwdc24/10169) 相关联。它基于 WWDC21 中一个类似的会议，展示了如何在 App 中采用 Swift 并发：[Swift concurrency: Update a sample app](https://developer.apple.com/videos/play/wwdc2021/10194/)。

此示例提供了 App 的两个独立版本：

- 原始版本使用了 Swift 并发特性，但包含了一些问题，这些问题可以通过启用 Swift 完整并发检查（Swift Complete Concurrency Checking）检测到，并且需要在启用 Swift 6 语言模式（Swift 6 language mode）之前解决。
- 更新后的版本解决了这些问题，并已启用 Swift 6。它还添加了新功能，可以在用户记录饮用咖啡时记录用户的位置。

观看会议以逐步了解此过程，然后比较两个项目以查看差异。

### 配置示例代码项目

要将复杂功能添加到活动表盘，首先构建并在模拟器中运行示例代码项目，然后按照以下步骤操作：

1. 点按数码旋钮以退出 App 并返回表盘。
2. 使用触控板，用力按压表盘以进入编辑模式，然后点按“自定（Customize）”。
3. 向左轻扫，直到配置屏幕高亮显示复杂功能。选择要修改的复杂功能。
4. 滚动到示例 App 的复杂功能，然后再次点按数码旋钮以保存你的更改。
5. 点按新添加的复杂功能以进入 App。

有关设置表盘的更多信息，请参阅[在 Apple Watch 上更换表盘](https://support.apple.com/en-us/HT205536)。

配置并运行 App 后，你可以测试后台更新。确保复杂功能出现在活动表盘上。然后构建并在模拟器中运行 App，并按照以下步骤操作：

1. 使用 App 的主视图添加一个或多个饮品。
2. 点按数码旋钮将 App 发送到后台。
3. 打开“设置”，向下滚动到“健康”\>“健康数据”\>“营养”\>“咖啡因”，以查看你添加到 App 中的所有饮品。
4. 点按“删除咖啡因数据”以清除 HealthKit 中的所有咖啡因样本。
5. 导航回表盘。
6. 复杂功能将在 15 分钟内更新；但是，更新可能会根据系统的当前状态而延迟。

### 在 Swift 中采用严格并发检查

要查看原始项目中高亮显示的问题，请按照以下步骤操作：

1. 在 Xcode 中，导航到项目设置。
2. 对于每个目标，将“构建设置（Build Settings）”下方的“严格并发检查（Strict Concurrency Checking）”更改为“完整（Complete）”。
3. 每个目标都会生成必须解决的警告。
4. 解决警告后，将“构建设置（Build Settings）”中的“Swift 语言版本（Swift Language Version）”更改为“Swift 6”。

比较原始项目和更新后的项目，以了解它如何解决并发问题。

## 另请参阅

### 基础

- [代码演练：使用 Swift 并发提升 App 体验](code-along-elevating-an-app-with-swift-concurrency.md) — 与 WWDC 演示者一起进行代码演练，使用 Swift 并发提升 SwiftUI App。
- [更新 App 以使用 Swift 并发](updating_an_app_to_use_swift_concurrency.md) — 通过重构代码以利用 Swift 中的异步函数来提升 App 性能。

## 下载

- [UpdatingAnAppToUseStrictConcurrency.zip](https://docs-assets.developer.apple.com/published/4dd408a8fcf3/UpdatingAnAppToUseStrictConcurrency.zip)
