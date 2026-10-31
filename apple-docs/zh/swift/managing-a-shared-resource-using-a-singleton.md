---
title: 使用单例管理共享资源
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/managing-a-shared-resource-using-a-singleton
source_url: 'https://developer.apple.com/documentation/swift/managing-a-shared-resource-using-a-singleton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/managing-a-shared-resource-using-a-singleton.json'
content_hash: 'sha256:a1db7f7cb452eb4c'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Cocoa Design Patterns](cocoa-design-patterns.md)

# 使用单例管理共享资源

<sub>文章</sub>

使用单个共享的类实例来提供对共享资源的访问。

## 概述

你可以使用单例（singleton）来提供类的全局可访问的共享实例。你可以创建自己的单例，为 App 内共享的资源或服务提供一个统一的访问点，例如用于播放音效的音频通道，或用于发起 HTTP 请求的网络管理器。

### 创建单例

使用静态类型属性来创建简单的单例，该属性保证只进行一次惰性初始化，即使多个线程同时访问也是如此：

```swift
class Singleton {
    static let shared = Singleton()
}
```

如果需要在初始化之外执行额外的设置，可以将闭包调用的结果赋给全局常量：

```swift
class Singleton {
    static let shared: Singleton = {
        let instance = Singleton()
        // 设置代码
        return instance
    }()
}
```

## 另请参阅

### 常见模式

- [在 Swift 中使用键值观察](using-key-value-observing-in-swift.md) — 在其他对象的属性发生更改时通知对象。
- [使用委托自定义对象行为](using-delegates-to-customize-object-behavior.md) — 代表委托方响应事件。
- [关于导入的 Cocoa 错误参数](about-imported-cocoa-error-parameters.md) — 了解 Cocoa 错误参数是如何转换为 Swift 抛出方法的。
- [在 Swift 中处理 Cocoa 错误](handling-cocoa-errors-in-swift.md) — 抛出并捕获使用 Cocoa 错误类型的错误。
