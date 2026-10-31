---
title: 'TicTacFish：使用分布式 Actor 实现游戏'
framework: Distributed
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 16.0+, iPadOS 16.0+, Xcode 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/tictacfish_implementing_a_game_using_distributed_actors
source_url: 'https://developer.apple.com/documentation/swift/tictacfish_implementing_a_game_using_distributed_actors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/tictacfish_implementing_a_game_using_distributed_actors.json'
content_hash: 'sha256:0ff3af1d88522c7d'
translated: true
---

> 导航： [Technologies](../technologies.md) · [Swift](../swift.md)

# TicTacFish：使用分布式 Actor 实现游戏

<sub>示例代码</sub>

使用分布式 Actor 将你的 Swift 并发和基于 Actor 的 App 扩展到单个进程之外。

## 概述

> [!note] 注意
> 本示例代码项目关联 WWDC22 场次 [110356: 认识 Swift 中的分布式 Actor](../https_/developer.apple.com/wwdc22/110356.md)。

### 配置示例代码项目

由于这个示例 App 使用了 Swift 5.7 中引入的新的 Swift 语言特性，你需要至少以下版本的 iOS、macOS 和 Xcode 才能编辑和运行这些示例：

要运行 iOS App：

- iOS 16
- macOS 13
- Xcode 14

要在你的本地 Mac 上运行服务端应用程序：

- macOS 13
- Xcode 14

要在 Linux 服务器上运行服务端应用程序，使用以下环境编译并运行 `Server` 包：

- 任意受支持的 Linux 发行版
- Swift 5.7

你可以从同一个 Xcode 项目启动多个模拟器（例如一台 iPhone 13 和一台 iPhone 13 Pro），来试用这个示例 App 的点对点本地联网部分。

## 另请参阅

### 标准库

- [Int](int.md) — 一个有符号整数值类型。
- [Double](double.md) — 一个双精度浮点值类型。
- [String](string.md) — 一个 Unicode 字符串值，是字符的集合。
- [Array](array.md) — 一个有序的随机访问集合。
- [Dictionary](dictionary.md) — 一种元素为键值对的集合。
- [Swift 标准库](swift-standard-library.md) — 解决复杂问题并编写高性能、可读性强的代码。
- [更新 App 以使用 Swift 并发](updating_an_app_to_use_swift_concurrency.md) — 通过重构代码以利用 Swift 中的异步函数来提升 App 性能。

## 下载

- [TicTacFishImplementingAGameUsingDistributedActors.zip](https://docs-assets.developer.apple.com/published/b583f10d72/TicTacFishImplementingAGameUsingDistributedActors.zip)
