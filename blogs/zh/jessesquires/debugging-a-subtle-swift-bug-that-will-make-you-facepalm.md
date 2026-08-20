---
title: 调试一个让人想捂脸的隐晦 Swift bug
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2018/11/07/debugging-subtle-swift-bug-facepalm/'
original_language: en
published: 2018-11-07
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:341b92f22194ed73'
translated: true
---

> 原文：[Debugging a subtle Swift bug that will make you facepalm](https://www.jessesquires.com/blog/2018/11/07/debugging-subtle-swift-bug-facepalm/)　·　Jesse Squires

前几天我给工作中一个开放 pull request 调试 UI 测试的崩溃。这个 bug 极其隐晦，很难发现。我花了很长时间盯着变更代码，试图理解哪里出了问题。让我们看看你能不能找到错误。

以下是问题行：

```
func toDictionary() -> [String: Any] {
    var dict: [String: Any] = [:]

    // 设置其他键和值的代码…

    dict[JSONKeys.dateClosed] = self.dateClosed?.toMongoDate

    return dict
}
```

这里的细节不重要。这是一些遗留的 JSON 序列化（serialization）代码，在 `Codable`（[SE-0166](https://github.com/apple/swift-evolution/blob/master/proposals/0166-swift-archival-serialization.md) 和 [SE-0167](https://github.com/apple/swift-evolution/blob/master/proposals/0167-swift-encoders.md)）推出之前就有了。这个函数将对象序列化为 JSON 字典，`self.dateClosed` 是 `Date` 类型，而 `JSONKeys.dateClosed` 是一个 `String` 常量。

但 bug 在哪里？我们来看看 `toMongoDate` 的定义（也是遗留代码）。

```
extension Date {
    func toMongoDate() -> [String: Any] {
        // 返回期望的 mongo 日期格式
    }
}
```

看起来没问题，对吗？一切都能编译通过。把一个 `[String: Any]` 字典作为另一个 `[String: Any]` 字典的值也不会有问题。`Any` 可以是_任何_类型。但问题恰好就出在这里。

我们再看看那一行：`self.dateClosed?.toMongoDate`。这返回的是_函数_ `toMongoDate` 本身。也就是说，其引用类型为 `() -> [String: Any]`——**而不是**调用函数后的_结果_。我忘了加括号 `()`。那一行应该是 `self.dateClosed?.toMongoDate()`。然而，这样也能工作，编译器也不会报错，因为函数是一等类型（first-class type），把函数作为 `[String: Any]` 字典的值是合法的。这显然是采用 [`Codable`](https://developer.apple.com/documentation/swift/codable) 的一个理由，它本可以避免这个错误。

更糟的是：同样的错误在我们的代码库中至少还在另一个场景出现过。实在太容易被忽略了。

实在是让人捂脸。

![Swift 函数引用搞笑图](https://www.jessesquires.com/img/blog/swift-function-ref.jpg)
