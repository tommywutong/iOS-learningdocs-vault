---
title: 采用常用协议
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/adopting-common-protocols
source_url: 'https://developer.apple.com/documentation/swift/adopting-common-protocols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/adopting-common-protocols.json'
content_hash: 'sha256:3582fb4666a91414'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md)

# 采用常用协议

<sub>文章</sub>

通过确保你的自定义类型符合 Swift 协议，让它们更易于使用。

## 概述

在程序中使用自定义类型为数据建模时，你经常需要检查两个值是相同还是不同，或者某个特定的值是否包含在一列值之中。这种能力，以及把值存储到集合（set）中或把它们用作字典（dictionary）键的能力，都由两个相关的标准库协议 [Equatable](equatable.md) 和 [Hashable](hashable.md) 管理。

- 你可以使用等于（`==`）和不等于（`!=`）运算符来比较_可判等（equatable）_类型的实例。
- _可哈希（hashable）_类型的实例可以在数学上把它的值归约为单个整数，集合和字典在内部使用该整数，让查找始终保持快速。

许多标准库类型既可判等也可哈希，包括字符串、整数、浮点值、布尔值，以及由可判等且可哈希的类型组成的集合。下面示例中的 `==` 比较和 `contains(_:)` 方法调用，都依赖于字符串和整数可判等这一事实：

```swift
if username == "Arturo" {
    print("Hi, Arturo!")
}

let favoriteNumbers = [4, 7, 8, 9]
if favoriteNumbers.contains(todaysDate.day) {
    print("It's a good day today!")
}
```

符合 `Equatable` 和 `Hashable` 协议非常简单直接，并且能让你在 Swift 中更方便地使用自己的类型。让你的所有自定义模型类型都符合这两个协议是个好做法。

### 自动符合 Equatable 和 Hashable

只需在与类型原始声明相同的文件中声明这些协议一致性，就能让许多自定义类型可判等、可哈希。在声明类型时，把 `Equatable` 和 `Hashable` 添加到所采用的协议列表中，编译器就会自动补全这两个协议的要求：

```swift
/// x-y 坐标系中的一个位置。
struct Position: Equatable, Hashable {
    var x: Int
    var y: Int

    init(_ x: Int, _ y: Int) {
        self.x = x
        self.y = y
    }
}
```

有了 `Equatable` 一致性，你就可以对 `Position` 类型的任意两个实例使用等于运算符（`==`）或不等于运算符（`!=`）。

```swift
let availablePositions = [Position(0, 0), Position(0, 1), Position(1, 0)]
let gemPosition = Position(1, 0)

for position in availablePositions {
    if gemPosition == position {
        print("Gem found at (\(position.x), \(position.y))!")
    } else {
        print("No gem at (\(position.x), \(position.y))")
    }
}
// (0, 0) 处没有宝石
// (0, 1) 处没有宝石
// 在 (1, 0) 处找到了宝石！

```

`Hashable` 一致性意味着你可以把位置存储到集合中，并快速检查你之前是否到过某个位置，如下例所示：

```swift
var visitedPositions: Set = [Position(0, 0), Position(1, 0)]
let currentPosition = Position(1, 3)

if visitedPositions.contains(currentPosition) {
    print("Already visited (\(currentPosition.x), \(currentPosition.y))")
} else {
    print("First time at (\(currentPosition.x), \(currentPosition.y))")
    visitedPositions.insert(currentPosition)
}
// 第一次到 (1, 3)

```

除了简化代码之外，这种自动一致性还能减少错误，因为你添加到自定义类型中的任何新属性都会在哈希和相等性测试时被自动纳入。当一个类型是满足以下条件的结构体或枚举时，它就有资格自动符合 `Equatable` 和 `Hashable`：

- 对于结构体，其_全部_存储属性都必须符合 `Equatable` 和 `Hashable`。
- 对于枚举，其_全部_关联值都必须符合 `Equatable` 和 `Hashable`。（没有关联值的枚举即使不声明采用，也符合 `Equatable` 和 `Hashable`。）

### 手动符合 Equatable 和 Hashable

在以下情况下，你需要为某个类型手动实现 `Equatable` 和 `Hashable` 一致性：

- 该类型不满足上一节列出的条件。
- 你想自定义该类型的一致性。
- 你想扩展在另一个文件或模块中声明的类型，使其符合协议。

```swift
class Player {
    var name: String
    var position: Position

    init(name: String, position: Position) {
        self.name = name
        self.position = position
    }
}
```

`Player` 类型是一个类，因此它没有资格自动合成 `Equatable` 或 `Hashable` 的要求。要让这个类符合 `Equatable` 协议，请在一个扩展中声明一致性，并实现静态的 `==` 运算符方法。在 `==` 方法的实现中，对每个有影响的属性进行相等比较：

```swift
extension Player: Equatable {
    static func ==(lhs: Player, rhs: Player) -> Bool {
        return lhs.name == rhs.name && lhs.position == rhs.position
    }
}
```

要让 `Player` 符合 `Hashable` 协议，请在另一个扩展中声明一致性，并实现 `hash(into:)` 方法。在 `hash(into:)` 方法中，对提供的哈希器调用 `combine(_:)` 方法，传入每个有影响的属性：

```swift
extension Player: Hashable {
    func hash(into hasher: inout Hasher) {
        hasher.combine(name)
        hasher.combine(position)
    }
}
```

#### 对可判等和可哈希使用所有有影响的属性

在实现 `==` 方法和 `hash(into:)` 方法时，要使用所有会影响自定义类型两个实例是否被视为相等的属性。在上面的实现中，`Player` 类型在两个方法中都使用了 `name` 和 `position`。

如果你的类型包含不影响两个实例是否被视为相等的属性，请在 `==` 方法的比较中和 `hash(into:)` 的哈希计算中排除这些属性。例如，某个类型可能会缓存一个开销很大的计算值，这样它只需要计算一次。如果你比较该类型的两个实例，这个计算值是否已被缓存不应影响它们的相等性，因此应把缓存的值排除在比较和哈希之外。

> [!important] 重要
> 在你的 `==` 和 `hash(into:)` 两个方法中，始终使用相同的属性。在这两个方法中使用不同的属性组，可能会在你把自定义类型用于集合和字典时导致意外的行为或性能。

### 自定义 NSObject 子类的行为

`NSObject` 的子类继承了对 `Equatable` 和 `Hashable` 协议的一致性，其相等性基于实例同一性。如果你需要自定义这一行为，请重写 [isEqual(_:)](<../objectivec/nsobjectprotocol/isequal(__).md>) 方法和 [hash](../objectivec/nsobjectprotocol/hash.md) 属性，而不是 `==` 运算符方法和 `hashValue` 属性。

```swift
extension MyNSObjectSubclass {
    override func isEqual(_ object: Any?) -> Bool {
        guard let other = object as? MyNSObjectSubclass
            else { return false }
        return self.firstProperty == other.firstProperty 
            && self.secondProperty == other.secondProperty
    }

    override var hash: Int {
        var hasher = Hasher()
        hasher.combine(firstProperty)
        hasher.combine(secondProperty)
        return hasher.finalize()
    }
}
```

如上一节所述，被视为相等的两个实例必须具有相同的哈希值。如果你重写了这两个声明之一，就必须同时重写另一个，以维持这一保证。

## 另请参阅

### 数据建模

- [在结构体与类之间选择](choosing-between-structures-and-classes.md) — 决定如何存储数据以及如何为行为建模。
