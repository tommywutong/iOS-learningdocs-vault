---
title: 用参数包泛化 API
session_id: 10168
collection: wwdc2023
year: 2023
duration: '18:24'
topics: [Developer Tools, Swift]
group: A · ObjC/Swift runtime 与语言实现
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2023/10168/'
content_hash: 'sha256:e0ab33e6f7fbe8e8'
translated: true
---

# 用参数包泛化 API

<sub>WWDC2023 · 18:24 · Developer Tools、Swift</sub>

Swift 参数包是扩展泛型代码可能性的强大工具，同时也能简化常见……

> [!note] 归档理由
> parameter packs（变参泛型），语言特性

## 章节

- [Introduction](/videos/play/wwdc2023/10168/?time=0)
- [What parameter packs solve](/videos/play/wwdc2023/10168/?time=52)
- [How to read parameter packs](/videos/play/wwdc2023/10168/?time=248)
- [Using parameter packs](/videos/play/wwdc2023/10168/?time=726)
- [Wrap up](/videos/play/wwdc2023/10168/?time=1042)

## 相关资源

- [Introduction](https://developer.apple.com/videos/play/wwdc2023/10168/?time=0)
- [What parameter packs solve](https://developer.apple.com/videos/play/wwdc2023/10168/?time=52)
- [How to read parameter packs](https://developer.apple.com/videos/play/wwdc2023/10168/?time=248)
- [Using parameter packs](https://developer.apple.com/videos/play/wwdc2023/10168/?time=726)
- [Wrap up](https://developer.apple.com/videos/play/wwdc2023/10168/?time=1042)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10168/4/C4DB8728-EFE7-49D9-B61E-3061B8F31EF5/downloads/wwdc2023-10168_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2023/10168/4/C4DB8728-EFE7-49D9-B61E-3061B8F31EF5/downloads/wwdc2023-10168_sd.mp4?dl=1)
- [What’s new in Swift](https://developer.apple.com/videos/play/wwdc2023/10164)
- [Design protocol interfaces in Swift](https://developer.apple.com/videos/play/wwdc2022/110353)
- [Embrace Swift generics](https://developer.apple.com/videos/play/wwdc2022/110352)
- [radians function](https://developer.apple.com/videos/play/wwdc2023/10168/?time=73)
- [Array type](https://developer.apple.com/videos/play/wwdc2023/10168/?time=86)
- [radians function and Array type with concrete expressions](https://developer.apple.com/videos/play/wwdc2023/10168/?time=108)
- [generic query](https://developer.apple.com/videos/play/wwdc2023/10168/?time=124)
- [variadic query](https://developer.apple.com/videos/play/wwdc2023/10168/?time=142)
- [generic query](https://developer.apple.com/videos/play/wwdc2023/10168/?time=196)
- [two query overloads](https://developer.apple.com/videos/play/wwdc2023/10168/?time=203)
- [three query overloads](https://developer.apple.com/videos/play/wwdc2023/10168/?time=208)
- [four query overloads with extra argument error](https://developer.apple.com/videos/play/wwdc2023/10168/?time=211)
- [for-in loop over requests](https://developer.apple.com/videos/play/wwdc2023/10168/?time=352)
- [four query overloads](https://developer.apple.com/videos/play/wwdc2023/10168/?time=521)
- [parameter pack query interface](https://developer.apple.com/videos/play/wwdc2023/10168/?time=577)
- [parameter pack query with single argument call](https://developer.apple.com/videos/play/wwdc2023/10168/?time=601)
- [parameter pack query with single and triple argument calls](https://developer.apple.com/videos/play/wwdc2023/10168/?time=608)
- [parameter pack query with triple argument call](https://developer.apple.com/videos/play/wwdc2023/10168/?time=615)
- [parameter pack query interface](https://developer.apple.com/videos/play/wwdc2023/10168/?time=656)
- [parameter pack query interface with conformance](https://developer.apple.com/videos/play/wwdc2023/10168/?time=663)
- [parameter pack query interface with where clause](https://developer.apple.com/videos/play/wwdc2023/10168/?time=677)
- [parameter pack query interface with minimum parameter count](https://developer.apple.com/videos/play/wwdc2023/10168/?time=704)
- [parameter pack query implementation](https://developer.apple.com/videos/play/wwdc2023/10168/?time=822)
- [parameter pack query implementation with different input and output types](https://developer.apple.com/videos/play/wwdc2023/10168/?time=964)
- [parameter pack query implementation with control flow break](https://developer.apple.com/videos/play/wwdc2023/10168/?time=1025)

## 逐字稿

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

♪ ♪ Sophia：大家好，欢迎观看"用参数包泛化 API"。我是 Sophia，我在 Swift 编译器团队工作。今天我将与你讨论 Swift 参数包，以及它们如何为泛型编程提供新的灵活性维度。

这是一场高级演讲，建立在现有泛型系统之上。如果你不熟悉这个主题，我鼓励你观看 WWDC22 的"拥抱 Swift 泛型"。今天，我将带你了解参数包能解决的问题类型、在库中遇到参数包时如何理解它们，最后深入探讨如何实现你自己的利用参数包的代码。在我跳入参数包之前，了解为什么它们存在很重要。所以我先谈一点泛型，然后是变参。你编写的代码从根本上由两类组成：值和类型。你可以通过编写接受不同值作为参数的函数来抽象值。例如 radians(from:) 函数，输入接受任何代表度数的 Double 值，输出返回代表弧度的新 Double 值。你可以通过编写接受不同类型作为参数的泛型代码来抽象类型。例如，标准库的 Array 类型被设计为可以容纳任何你希望填充的数据形式。它有 Element 类型参数，是给定 Array 实例将使用的具体类型的占位符。在这两种情况下，具体值或具体类型作为参数传递给抽象。大多数泛型代码抽象类型和值。为了探索这一点，我将编写一些向服务器发送查询的代码。

它的基本实现将接收某个 Payload 类型的 Request，然后把它作为查询传递给服务器，最后返回类型为 Payload 的服务器响应。函数有一个参数，但我想支持在同一调用中查询多个请求。为了支持可变数量的参数，我们有变参参数。变参参数允许函数灵活接受任意数量的单类型参数。但变参参数有限制。例如，你可能想把给定参数映射到与参数数量相同长度的元组。然而，用变参参数，无法声明基于参数长度的返回类型。变参参数也无法接受不同类型而不用类型擦除，因此无法保留每个参数的特定静态类型信息。泛型系统与变参参数所缺乏的是同时保留类型信息并改变参数数量的能力。今天，唯一能做到这一点的方式是重载，这迫使你选择支持的参数数量上限。我想，两个参数够吗？可能不够。支持最多三个参数更好。但如果我们想要四个呢？这种重载模式，以及其限制，普遍存在于概念上处理可变类型参数数量的 API 中。这种方法的缺点是冗余，但更重要的是，它迫使选择支持参数数量的任意上限。超出选择的限制将导致编译器报错多出参数。这是参数包解决的问题类型。如果你发现自己陷入这种重载模式，那是强烈信号你想要使用参数包。Swift 5.9 中，泛型系统获得对参数长度的一等抽象支持……

我将把 query 函数移入 Evaluator 结构体，并把类型参数包从 query 方法提升到 Evaluator 类型。Evaluator 结构体可以通过把请求包用括号包裹成元组值来存储。给定具体的 Payload 类型参数包，'item' 变量将是单个请求或每个请求的元组。接下来，我将把 Request 从结构体改为协议，带名为 Output 的关联类型。我还将给 Request 协议添加名为 Input 的关联类型。然后我更新 Request 中的 evaluate 方法，使其参数为协议的 Input 类型。这使方法的返回类型可以与参数类型不同。之后，我更新 Evaluator 要求所有 Payload 类型符合 Request，并相应地把 'item' 存储属性更新为仅类型 'each Payload'。然而此时，"Payload"作为 Evaluator 类型参数包的名称并不合适。Payload 不再是 Request 中包含的内容，而是符合整个 Request。因此我们把 Payload 改名为 Request，协议改名为 RequestProtocol。query 方法现在可以接受每个 Request 的 Input 类型的包，并返回每个 Request 的 Output 类型的列表。最后，query 方法的新参数 'input' 只需要传递给每个 item 的 evaluate 方法调用。现在我们能从服务器响应返回与查询中包含数据类型不同的类型。你可以知道方法的值参数包长度将与返回的值包长度匹配，因为它们的类型都基于 Evaluator 的类型包。存储属性 'item' 的参数长度也是如此。鉴于使用参数包是一种迭代形式，你可能想知道如果要……
