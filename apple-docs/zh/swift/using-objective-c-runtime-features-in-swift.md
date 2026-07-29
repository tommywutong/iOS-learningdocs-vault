---
title: 在 Swift 中使用 Objective-C 运行时特性
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/using-objective-c-runtime-features-in-swift
source_url: 'https://developer.apple.com/documentation/swift/using-objective-c-runtime-features-in-swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/using-objective-c-runtime-features-in-swift.json'
content_hash: 'sha256:d5ca27731c9bae98'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md)

# 在 Swift 中使用 Objective-C 运行时特性

<sub>文章</sub>

使用选择器（selector）和键路径（key path）来与动态的 Objective-C API 交互。

## 概述

某些 Objective-C API——比如目标-动作（target-action）——接受方法名或属性名作为参数，然后使用这些名称来动态调用或访问方法或属性。在 Swift 中，你可以使用 `#selector` 和 `#keyPath` 表达式，将这些方法或属性名分别表示为选择器或键路径。

### 使用选择器来安排对 Objective-C 方法的调用

在 Objective-C 中，选择器是一种引用 Objective-C 方法名称的类型。在 Swift 中，Objective-C 选择器由 [Selector](../objectivec/selector.md) 结构体表示，你可以使用 `#selector` 表达式来创建它们。

在 Swift 中，你可以通过将方法名放到 `#selector` 表达式中来为 Objective-C 方法创建选择器：`#selector(MyViewController.tappedButton(_:))`。要为属性的 Objective-C getter 或 setter 方法构造选择器，可以使用 `getter:` 或 `setter:` 标签来加在属性名前，例如 `#selector(getter: MyViewController.myButton)`。下面的例子展示了一个选择器如何作为目标-动作模式的一部分来使用，以响应 [touchUpInside](../uikit/uicontrol/event/touchupinside.md) 事件调用某个方法。

```swift
import UIKit
class MyViewController: UIViewController {
    let myButton = UIButton(frame: CGRect(x: 0, y: 0, width: 100, height: 50))

    override init(nibName nibNameOrNil: NSNib.Name?, bundle nibBundleOrNil: Bundle?) {
        super.init(nibName: nibNameOrNil, bundle: nibBundleOrNil)
        let action = #selector(MyViewController.tappedButton)
        myButton.addTarget(self, action: action, forControlEvents: .touchUpInside)
    }

    @objc func tappedButton(_ sender: UIButton?) {
        print("tapped button")
    }

    required init?(coder: NSCoder) {
        super.init(coder: coder)
    }
}
```

如果你需要消除重载函数之间的歧义，可以使用带括号的表达式配合 `as` 操作符，使 `#selector` 表达式无歧义地指向某个特定的重载。

### 使用键路径动态访问 Objective-C 属性

在 Objective-C 中，键（key）是一个字符串，用于标识对象的某个特定属性。键路径（key path）是一个由点号分隔的键构成的字符串，用于指定需要遍历的一系列对象属性。键和键路径经常用于键值编码（KVC），这是一种通过字符串标识符间接访问对象属性（attribute）和关系的机制。

> [!important] 重要
> Objective-C 键路径与 Swift 中的键路径表达式不同但相关联。关于键路径表达式的信息，请参阅 [The Swift Programming Language](https://docs.swift.org/swift-book/) 中的 [Key-Path Expression](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/expressions#Key-Path-Expression)。

你可以使用 `#keyPath` 字符串表达式来创建经过编译器检查的键和键路径，这些键和键路径可以被 KVC 方法使用，例如 [value(forKey:)](<../objectivec/nsobject-swift.class/value(forkey_).md>) 和 [value(forKeyPath:)](<../objectivec/nsobject-swift.class/value(forkeypath_).md>)。`#keyPath` 字符串表达式接受链式的方法或属性引用。它也支持通过链中的可选值（optional value）进行链式访问，例如 `#keyPath(Person.bestFriend.name)`。使用 `#keyPath` 字符串表达式创建的键路径，不会将所引用的属性或方法的类型信息传递给接受键路径的 API。

下面的例子定义了一个 `Person` 类，创建了它的两个实例，并使用多个 `#keyPath` 字符串表达式来访问其属性以及这些属性的属性：

```swift
class Person: NSObject {
    @objc var name: String
    @objc var friends: [Person] = []
    @objc var bestFriend: Person? = nil

    init(name: String) {
        self.name = name
    }
}

let gabrielle = Person(name: "Gabrielle")
let jim = Person(name: "Jim")
let yuanyuan = Person(name: "Yuanyuan")
gabrielle.friends = [jim, yuanyuan]
gabrielle.bestFriend = yuanyuan

#keyPath(Person.name)
// "name"
gabrielle.value(forKey: #keyPath(Person.name))
// "Gabrielle"
#keyPath(Person.bestFriend.name)
// "bestFriend.name"
gabrielle.value(forKeyPath: #keyPath(Person.bestFriend.name))
// "Yuanyuan"
#keyPath(Person.friends.name)
// "friends.name"
gabrielle.value(forKeyPath: #keyPath(Person.friends.name))
// ["Yuanyuan", "Jim"]
```

## 另请参阅

### 与 Objective-C 和 C 的语言互操作性

- [Objective-C 与 C 代码定制](objective-c-and-c-code-customization.md) — 应用宏到你的 Objective-C API，以定制它们如何被导入到 Swift 中。
- [将 Objective-C 代码迁移到 Swift](migrating-your-objective-c-code-to-swift.md) — 学习迁移代码的推荐步骤。
- [Cocoa 设计模式](cocoa-design-patterns.md) — 在你的 Swift App 中采纳 Cocoa 设计模式并与之互操作。
- [在 Swift 中处理动态类型的方法和对象](handling-dynamically-typed-methods-and-objects-in-swift.md) — 将 Objective-C `id` 类型的实例转换为特定的 Swift 类型。
- [导入的 C 与 Objective-C API](imported-c-and-objective-c-apis.md) — 使用原生 Swift 语法与 C 和 Objective-C 中的类型和函数进行互操作。
- [异步调用 Objective-C API](calling-objective-c-apis-asynchronously.md) — 了解接受完成处理程序（completion handler）的函数和方法如何被转换为 Swift 异步函数。
