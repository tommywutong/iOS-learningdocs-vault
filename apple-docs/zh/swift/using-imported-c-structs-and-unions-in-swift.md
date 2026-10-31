---
title: 在 Swift 中使用导入的 C 结构体与联合体
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/using-imported-c-structs-and-unions-in-swift
source_url: 'https://developer.apple.com/documentation/swift/using-imported-c-structs-and-unions-in-swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/using-imported-c-structs-and-unions-in-swift.json'
content_hash: 'sha256:5b4043684d1b023f'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [导入的 C 与 Objective-C API](imported-c-and-objective-c-apis.md)

# 在 Swift 中使用导入的 C 结构体与联合体

<sub>文章</sub>

了解 Swift 如何表示导入的 C 结构体与联合体，包括带位域（bitfield）和未命名字段的类型。

## 概述

Swift 会把 C 头文件中声明的任何 C 结构体都导入为 Swift 结构体。导入后的 Swift 结构体会为 C 结构体的每个字段提供一个存储属性，并提供一个初始化方法，其参数与这些存储属性一一对应。

### 带默认值的结构体

如果所有导入的成员都有默认值，Swift 还会提供一个不接受任何实参的默认初始化方法。例如，给定以下 C 结构体：

```occ
struct Color {
    float r, g, b;
};
typedef struct Color Color;
```

导入 `Color` 结构体后，对应的 Swift 版本等价于以下代码：

```swift
public struct Color {
    var r: Float
    var g: Float
    var b: Float

    init()
    init(r: Float, g: Float, b: Float)
}
```

### 联合体

Swift 会把 C 联合体导入为 Swift 结构体。虽然 Swift 不支持以原生方式声明联合体，但作为 Swift 结构体导入的 C 联合体仍然表现得像 C 联合体。例如，考虑一个名为 `SchroedingersCat` 的 C 联合体，它有 `isAlive` 和 `isDead` 两个字段：

```occ
union SchroedingersCat {
    bool isAlive;
    bool isDead;
};
```

在 Swift 中，它会被导入成这样：

```swift
struct SchroedingersCat {
    var isAlive: Bool { get set }
    var isDead: Bool { get set }

    init(isAlive: Bool)
    init(isDead: Bool)

    init()
}
```

由于 C 中的联合体让所有字段共用同一个基础内存地址，由 Swift 导入的联合体中所有计算属性都使用同一块底层内存。因此，更改导入结构体实例上某个属性的值，会同时更改该结构体定义的所有其他属性的值。

在下面的示例中，更改 `SchroedingersCat` 结构体实例上 `isAlive` 计算属性的值，也会更改该实例 `isDead` 计算属性的值：

```swift
var mittens = SchroedingersCat(isAlive: false)

print(mittens.isAlive, mittens.isDead)
// 输出 "false false"

mittens.isAlive = true
print(mittens.isDead)
// 输出 "true"
```

### 位域

Swift 会把声明在结构体中的位域（bit field，例如 Foundation 的 `NSDecimal` 类型中的那些）导入为计算属性。访问与位域对应的计算属性时，Swift 会自动在兼容的 Swift 类型之间对该值进行双向转换。

### 未命名的结构体与联合体字段

C 的 `struct` 和 `union` 类型可以定义没有名字的字段，或类型本身未命名的字段。未命名字段由一个嵌套的、带有命名字段的 `struct` 或 `union` 类型构成。

例如，考虑一个名为 `Cake` 的 C 结构体：它在一个未命名的联合体类型中嵌套了 `layers` 和 `height` 两个字段，还有一个属于未命名 struct 类型的字段 `toppings`：

```occ
struct Cake {
    union {
        int layers;
        double height;
    };

    struct {
        bool icing;
        bool sprinkles;
    } toppings;
};
```

导入 `Cake` 结构体之后，你可以使用默认初始化方法创建实例，并按如下方式使用它：

```swift
var simpleCake = Cake()
simpleCake.layers = 5
print(simpleCake.toppings.icing)
// 输出 "false"
```

导入的 `Cake` 结构体及其嵌套类型会带有一个逐成员初始化方法（memberwise initializer），你可以用它为各个字段提供自定义值来初始化该结构体：

```swift
let cake = Cake(
    .init(layers: 2),
    toppings: .init(icing: true, sprinkles: false)
)

print("The cake has \(cake.layers) layers.")
// 输出 "The cake has 2 layers."
print("Does it have sprinkles?", cake.toppings.sprinkles ? "Yes." : "No.")
// 输出 "Does it have sprinkles? No."
```

由于 `Cake` 结构体的第一个字段没有名字，其初始化方法的第一个参数没有实参标签。又由于 `Cake` 结构体拥有类型未命名的字段，你需要使用 `.init` 初始化方法（得益于 Swift 的类型推断才可用）为结构体的每个未命名字段设置初始值。

## 另请参阅

### C API

- [在 Swift 中使用导入的 C 函数](using-imported-c-functions-in-swift.md) —— 了解如何调用在 C 头文件中声明的导入函数。
- [在 Swift 中使用导入的 C 宏](using-imported-c-macros-in-swift.md) —— 将导入的 C 定义的宏用作常量。
