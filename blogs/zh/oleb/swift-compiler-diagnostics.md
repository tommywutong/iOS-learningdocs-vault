---
title: Swift 编译器诊断
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2015/08/swift-compiler-diagnostics/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e9e5f482638d4fc4'
translated: true
---

> 原文：[Swift Compiler Diagnostics](https://oleb.net/blog/2015/08/swift-compiler-diagnostics/)　·　Ole Begemann

# Swift 编译器诊断

在最近几个 Xcode 7 beta 版本的发布说明中，我最喜欢的一条就是下面这条相当含糊的说明：

> 类型检查器诊断在精度和特异性上持续改进。

无用的错误消息会严重打击生产力，尤其是当你面对一门仍在演变的语言和一个仍有不少粗糙边缘的编译器时。而 Swift 编译器在这方面显然还有很大的改进空间。很高兴看到 Swift 团队意识到了这个问题，并正在积极努力提供更好的诊断。

# 示例

下面是我最近注意到的一个具体改进实例。考虑这段简单代码，我想通过对一个数字范围进行映射来构造一个字符串数组：

```
let xs = 1...10.map(String.init)
```

这段代码无法编译。你能发现问题吗？如果能，那不错。如果不能，让我们看看编译器能不能帮我们。

## Beta 3

在 Xcode 7 beta 3 中，它会显示以下错误消息：

```
Could not find an overload for 'init' that accepts the supplied arguments
```

我不知道你怎么样，但对我来说，这句话暗示 `String.init` 部分有问题。我之前遇到过把初始化方法作为函数值引用[并不总是按预期工作](https://twitter.com/nnnnnnnn/status/616696761889861632)的情况，所以我可能会尝试使用内联闭包（inline closure）：

```
let xs = 1...10.map { String($0) }
```

而 beta 3 会回复这条错误消息：

```
Cannot invoke 'map' with an argument list of type '((_) -> _)'
```

真的，我完全不知道你想告诉我什么。

## Beta 5

让我们在 Xcode 7 beta 5 中试试同样的代码：

[![Swift 编译器在 Xcode 中显示一条错误消息](https://oleb.net/media/swift-compiler-error-message.png)](https://oleb.net/media/swift-compiler-error-message.png)

<sub>有了正确的错误消息，修复就很简单了。</sub>

```
let xs = 1...10.map(String.init)
// error: value of type 'Int' has no member 'map'
```

啊，现在我们有点进展了。显然，编译器试图在 `Int` 上调用 `map`，这解释了为什么代码不工作。它还高亮了 `10` 来指示问题的位置。有了这个信息，很容易就能看出我的错误：我错误地认为范围运算符 `...` 的优先级高于函数调用。修复方法是在范围周围加上括号：

```
let xs = (1...10).map(String.init)
// => ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
```

---

如果你立刻发现了我的错误，你可能会觉得这是一个微不足道的例子。也许吧，但如果一条改进的错误消息能为你节省几分钟的挫败感（更重要的是，帮助你不打断工作流），我认为这是一大胜利。谢谢，Swift 团队！

# Bug 报告有时有效

我于 2015 年 7 月 17 日提交了一个包含这个具体例子的功能请求，不到三周它就得到了修复。虽然我不知道我的 bug 报告是否在其中起了作用（我没有收到回复），但我确实知道 Swift 团队需要我们的反馈来了解我们在哪些地方对编译器感到困惑。所以下次你遇到一条你觉得有误导性或令人困惑的错误消息时，请提交一个 bug。这通常[只需要几分钟](http://www.quickradar.com/)。
