---
title: 在结构体与类之间选择
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/choosing-between-structures-and-classes
source_url: 'https://developer.apple.com/documentation/swift/choosing-between-structures-and-classes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/choosing-between-structures-and-classes.json'
content_hash: 'sha256:ca25f096091a6aef'
translated: true
---

> 导航： [技术](../technologies.md) · [Swift](../swift.md)

# 在结构体与类之间选择

<sub>文章</sub>

决定如何存储数据和为行为建模。

## 概述

结构体和类都是在 App 中存储数据和为行为建模的良好选择，但两者的相似性可能让人难以抉择该用哪一个。

请参考以下建议，在为 App 添加新的数据类型时，帮助你判断应该选用哪种方案。

- 默认使用结构体。
- 当你需要 Objective-C 互操作性时使用类。
- 当你需要控制所建模数据的标识时使用类。
- 将结构体与协议结合使用，通过共享实现来采用行为。

### 默认使用结构体

使用结构体来表示常见类型的数据。Swift 中的结构体包含了许多在其他语言里只有类才具备的特性：它们可以包含存储属性、计算属性和方法。而且，Swift 结构体可以采用协议，通过默认实现获得行为。Swift 标准库和 Foundation 对你经常使用的类型（比如数字、字符串、数组和字典）都使用结构体。

使用结构体能让你更容易在无需考虑 App 整体状态的情况下，对代码的某一部分进行推理。因为结构体是值类型——这一点与类不同——对结构体的局部更改，除非你有意将这些更改作为 App 流程的一部分传达出去，否则对 App 的其余部分是不可见的。因此，你可以查看一段代码，并更有把握地认为：该段代码中对实例的更改都是显式做出的，而不是被某个只有间接关联的函数调用悄悄改动的。

### 当你需要 Objective-C 互操作性时使用类

如果你使用的某个 Objective-C API 需要处理你的数据，或者你需要将你的数据模型纳入某个 Objective-C 框架中已定义的现有类层级结构，你可能需要使用类和类继承来为数据建模。例如，许多 Objective-C 框架公开的类都是设计给你去子类化的。

### 当你需要控制标识时使用类

Swift 中的类自带一种内置的标识概念，因为它们是引用类型。这意味着，当两个不同的类实例的每个存储属性都取值相同时，恒等运算符（`===`）仍然认为它们是不同的。这也意味着，当你在 App 中共享一个类实例时，你对该实例所做的更改，对持有该实例引用的每一部分代码都是可见的。当你需要实例具备这种标识时，请使用类。常见的使用场景包括文件句柄、网络连接，以及像 [CBCentralManager](../corebluetooth/cbcentralmanager.md) 这样的共享硬件中介对象。

举例来说，如果你有一个表示本地数据库连接的类型，管理该数据库访问的代码就需要完全控制该数据库在 App 中呈现出的状态。这种情况下适合使用类，但要注意限制 App 中哪些部分可以访问这个共享的数据库对象。

> [!important] 重要
> 谨慎对待标识。在 App 中大面积共享类实例会让逻辑错误更容易发生。你可能无法预料到更改一个被大量共享的实例会带来什么后果，因此要正确编写这样的代码需要付出更多工夫。

### 当你不控制标识时使用结构体

当你要建模的数据包含的是某个你并不控制其标识的实体的信息时，使用结构体。

例如，在一个查询远程数据库的 App 中，某个实例的标识可能完全由外部实体拥有，并通过一个标识符来传达。如果 App 模型的一致性存储在服务器上，你就可以把记录建模为带标识符的结构体。在下面的示例中，`jsonResponse` 包含了一个从服务器编码而来的 `PenPalRecord` 实例：

```swift
struct PenPalRecord {
    let myID: Int
    var myNickname: String
    var recommendedPenPalID: Int
}

var myRecord = try JSONDecoder().decode(PenPalRecord.self, from: jsonResponse)
```

对 `PenPalRecord` 这类模型类型进行局部更改是有用的。例如，一个 App 可能会根据用户反馈推荐多个不同的笔友。因为 `PenPalRecord` 结构体并不控制底层数据库记录的标识，所以对本地 `PenPalRecord` 实例所做的更改不会有意外更改数据库中数值的风险。

如果 App 的另一部分更改了 `myNickname` 并向服务器提交了变更请求，那么最近被拒绝的笔友推荐就不会被这次变更误纳入。因为 `myID` 属性被声明为常量，它在本地无法更改。因此，对数据库的请求就不会意外更改错误的记录。

### 使用结构体和协议为继承建模并共享行为

结构体和类都支持某种形式的继承。结构体和协议只能采用协议；它们不能从类继承。不过，你用类继承能构建出的那种继承层级结构，同样也可以用协议继承和结构体来建模。

如果你从零开始构建继承关系，请优先选用协议继承。协议允许类、结构体和枚举参与继承，而类继承只能与其他类兼容。当你决定如何为数据建模时，可以先尝试用协议继承构建数据类型的层级结构，然后再让你的结构体采用这些协议。

## 另请参阅

### 数据建模

- [采用通用协议](adopting-common-protocols.md) — 通过确保自定义类型符合 Swift 协议，让它们更易于使用。
