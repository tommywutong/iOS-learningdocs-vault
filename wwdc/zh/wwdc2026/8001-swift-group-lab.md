---
title: Swift 小组实验室
session_id: 8001
collection: wwdc2026
year: 2026
duration: '61:17'
topics: [Swift]
group: C · 并发、锁与线程
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2026/8001/'
content_hash: 'sha256:83792259f5faed83'
translated: true
---

# Swift 小组实验室

<sub>WWDC2026 · 61:17 · Swift</sub>

在线加入我们，与 Apple 工程师和设计师一起深入探究 WWDC26，提问、获取建议并跟随讨论……

> [!note] 归档理由
> Swift 实验室问答，含并发疑难（时效性一般）

## 章节

- [简介](/videos/play/wwdc2026/8001/?time=0)
- [在不复制的前提下，把不可 Sendable 数据的「所有权」从一个隔离域转移到另一个隔离域的最佳方式是什么——例如一个 actor 把大量数据交给另一个 actor？](/videos/play/wwdc2026/8001/?time=273)
- [对于使用 Swift 结构化并发，你们有哪些建议、最佳实践（以及陷阱）？](/videos/play/wwdc2026/8001/?time=365)
- [出于习惯给每个结构体都添加未使用/非必要的一致性（Sendable、Equatable、Hashable 等），会有额外的开销成本吗？底层会发生什么？](/videos/play/wwdc2026/8001/?time=716)
- [应用 @MainActor 会在整个遗留代码库中引发一连串大规模的 async 重构。在不牺牲 Swift 6 安全性的前提下，阻止这种「并发传染」的最干净的模式是什么？](/videos/play/wwdc2026/8001/?time=869)
- [为了高效率和出色的性能，最值得优先采用的现代 Swift 特性或官方资源有哪些？](/videos/play/wwdc2026/8001/?time=1039)
- [在完成一次完整的手动 Swift 6 严格并发迁移之后，我们是否应当删除那些在新的隔离模型下已显冗余的标注，还是把它们留作空操作？](/videos/play/wwdc2026/8001/?time=1188)
- [既然文档说 UserDefaults 是线程安全的，为什么它不是 Sendable 的？这是不是迈向某个目标的前置步骤？](/videos/play/wwdc2026/8001/?time=1388)
- [全面迁移到使用 'borrow/mutate' 而非 'get/set' 是不是好的实践？什么时候不建议这样做？](/videos/play/wwdc2026/8001/?time=1524)
- [面对 Mutex、InlineArray、Span、typed throws、不可复制类型这些新增特性，应用开发者如何分辨哪些是给自己的、哪些是给系统/嵌入式开发者的？又该如何跟进？](/videos/play/wwdc2026/8001/?time=1626)
- [我们的项目增量构建非常慢，Swift Emit Module 要花好几分钟，拆分成多个模块也没有帮助。类型推断/泛型等特性会影响这一点吗？我们该如何诊断？](/videos/play/wwdc2026/8001/?time=1917)
- [既然 Swift 6 并发已被广泛采用，如果今天重新设计，团队会有哪些不同的做法？](/videos/play/wwdc2026/8001/?time=2019)
- [最新版本中 Swift Package Manager 有哪些值得注意的改进，尤其是在大型多包项目的构建和依赖解析性能方面？](/videos/play/wwdc2026/8001/?time=2251)
- [有什么 Swift 特性是大多数开发者不知道其存在、但应当知道的？](/videos/play/wwdc2026/8001/?time=2360)
- [在语言演进方面，还差什么才能让元组最终有条件地遵循 Equatable、Hashable、Comparable 等协议？](/videos/play/wwdc2026/8001/?time=2895)
- [在 Swift 6 严格并发下，在后台 actor 上摄取高频传感器数据、并把更新流式推送到 MainActor 上的 @Observable 模型而不阻塞 UI，推荐的模式是什么？](/videos/play/wwdc2026/8001/?time=3005)
- [性能：为什么从方法返回的元组比结构体开销更大——还是说要视情况而定？](/videos/play/wwdc2026/8001/?time=3183)
- [你最喜欢 Swift 中的哪个生活质量／代码质量特性——不是那些显而易见的，而是让写 Swift 变得有趣的冷门好东西？](/videos/play/wwdc2026/8001/?time=3257)

## 相关资源

- [简介](https://developer.apple.com/videos/play/wwdc2026/8001/?time=0)
- [在不复制的前提下，把不可 Sendable 数据的「所有权」从一个隔离域转移到另一个隔离域的最佳方式是什么——例如一个 actor 把大量数据交给另一个 actor？](https://developer.apple.com/videos/play/wwdc2026/8001/?time=273)
- [对于使用 Swift 结构化并发，你们有哪些建议、最佳实践（以及陷阱）？](https://developer.apple.com/videos/play/wwdc2026/8001/?time=365)
- [出于习惯给每个结构体都添加未使用/非必要的一致性（Sendable、Equatable、Hashable 等），会有额外的开销成本吗？底层会发生什么？](https://developer.apple.com/videos/play/wwdc2026/8001/?time=716)
- [应用 @MainActor 会在整个遗留代码库中引发一连串大规模的 async 重构。在不牺牲 Swift 6 安全性的前提下，阻止这种「并发传染」的最干净的模式是什么？](https://developer.apple.com/videos/play/wwdc2026/8001/?time=869)
- [为了高效率和出色的性能，最值得优先采用的现代 Swift 特性或官方资源有哪些？](https://developer.apple.com/videos/play/wwdc2026/8001/?time=1039)
- [在完成一次完整的手动 Swift 6 严格并发迁移之后，我们是否应当删除那些在新的隔离模型下已显冗余的标注，还是把它们留作空操作？](https://developer.apple.com/videos/play/wwdc2026/8001/?time=1188)
- [既然文档说 UserDefaults 是线程安全的，为什么它不是 Sendable 的？这是不是迈向某个目标的前置步骤？](https://developer.apple.com/videos/play/wwdc2026/8001/?time=1388)
- [全面迁移到使用 'borrow/mutate' 而非 'get/set' 是不是好的实践？什么时候不建议这样做？](https://developer.apple.com/videos/play/wwdc2026/8001/?time=1524)
- [面对 Mutex、InlineArray、Span、typed throws、不可复制类型这些新增特性，应用开发者如何分辨哪些是给自己的、哪些是给系统/嵌入式开发者的？又该如何跟进？](https://developer.apple.com/videos/play/wwdc2026/8001/?time=1626)
- [我们的项目增量构建非常慢，Swift Emit Module 要花好几分钟，拆分成多个模块也没有帮助。类型推断/泛型等特性会影响这一点吗？我们该如何诊断？](https://developer.apple.com/videos/play/wwdc2026/8001/?time=1917)
- [既然 Swift 6 并发已被广泛采用，如果今天重新设计，团队会有哪些不同的做法？](https://developer.apple.com/videos/play/wwdc2026/8001/?time=2019)
- [最新版本中 Swift Package Manager 有哪些值得注意的改进，尤其是在大型多包项目的构建和依赖解析性能方面？](https://developer.apple.com/videos/play/wwdc2026/8001/?time=2251)
- [有什么 Swift 特性是大多数开发者不知道其存在、但应当知道的？](https://developer.apple.com/videos/play/wwdc2026/8001/?time=2360)
- [在语言演进方面，还差什么才能让元组最终有条件地遵循 Equatable、Hashable、Comparable 等协议？](https://developer.apple.com/videos/play/wwdc2026/8001/?time=2895)
- [在 Swift 6 严格并发下，在后台 actor 上摄取高频传感器数据、并把更新流式推送到 MainActor 上的 @Observable 模型而不阻塞 UI，推荐的模式是什么？](https://developer.apple.com/videos/play/wwdc2026/8001/?time=3005)
- [性能：为什么从方法返回的元组比结构体开销更大——还是说要视情况而定？](https://developer.apple.com/videos/play/wwdc2026/8001/?time=3183)
- [你最喜欢 Swift 中的哪个生活质量／代码质量特性——不是那些显而易见的，而是让写 Swift 变得有趣的冷门好东西？](https://developer.apple.com/videos/play/wwdc2026/8001/?time=3257)
- [高清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2026/8001/1/6ee7f28d-d198-4690-af7e-ac35f4173c3c/downloads/wwdc2026-8001_hd.mp4?dl=1)
- [标清视频](https://devstreaming-cdn.apple.com/videos/wwdc/2026/8001/1/6ee7f28d-d198-4690-af7e-ac35f4173c3c/downloads/wwdc2026-8001_sd.mp4?dl=1)

> [!warning] 本场没有可用的逐字稿。
