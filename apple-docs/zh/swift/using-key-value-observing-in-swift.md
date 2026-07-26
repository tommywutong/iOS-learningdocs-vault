---
title: 在 Swift 中使用键值观察
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/using-key-value-observing-in-swift
source_url: 'https://developer.apple.com/documentation/swift/using-key-value-observing-in-swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/using-key-value-observing-in-swift.json'
content_hash: 'sha256:c2c8575fdd68fb5c'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Swift](../swift.md) · [Cocoa Design Patterns](cocoa-design-patterns.md)

# 在 Swift 中使用键值观察

<sub>文章</sub>

在其他对象的属性发生变化时通知相关对象。

## 概述

键值观察（Key-Value Observing，KVO）是一种 Cocoa 编程模式，用于在某个对象的属性发生变化时通知其他对象。它对于在你的 App 中逻辑上分离的部分之间（例如模型与视图之间）传递变化信息很有用。你只能对继承自 [NSObject](../objectivec/nsobject-swift.class.md) 的类使用键值观察。

### 为属性标注键值观察

给你想通过键值观察来监听的属性同时标注 `@objc` 特性和 `dynamic` 修饰符。下面的例子定义了 `MyObjectToObserve` 类，其中的 `myDate` 属性可以被观察：

```swift
class MyObjectToObserve: NSObject {
    @objc dynamic var myDate = NSDate(timeIntervalSince1970: 0) // 1970
    func updateDate() {
        myDate = myDate.addingTimeInterval(Double(2 << 30)) // Adds about 68 years.
    }
}
```

### 定义观察者

观察者类的实例负责管理某一个或多个属性变化的相关信息。创建观察者时，你需要调用 `observe(_:options:changeHandler:)` 方法并传入一个指向你想观察的属性的键路径，以此开始观察。

在下面的例子中，`\.objectToObserve.myDate` 这个键路径指向了 `MyObjectToObserve` 的 `myDate` 属性：

```swift
class MyObserver: NSObject {
    @objc var objectToObserve: MyObjectToObserve
    var observation: NSKeyValueObservation?

    init(object: MyObjectToObserve) {
        objectToObserve = object
        super.init()

        observation = observe(
            \.objectToObserve.myDate,
            options: [.old, .new]
        ) { object, change in
            print("myDate changed from: \(change.oldValue!), updated to: \(change.newValue!)")
        }
    }
}
```

你可以用 [NSKeyValueObservedChange](../foundation/nskeyvalueobservedchange.md) 实例的 `oldValue` 和 `newValue` 属性，查看你所观察的属性发生了什么变化。

如果你不需要知道属性具体是_如何_变化的，可以省略 `options` 参数。省略 `options` 参数会导致系统不再存储新旧属性值，从而使 `oldValue` 和 `newValue` 属性变为 `nil`。

### 将观察者与要观察的属性关联起来

你可以通过把要观察的对象传给观察者的初始化方法，把它和它的观察者关联起来：

```swift
let observed = MyObjectToObserve()
let observer = MyObserver(object: observed)
```

### 响应属性变化

设置好使用键值观察的对象（比如上面的 `observed`）会通知其观察者属性发生了变化。下面的例子通过调用 `updateDate` 方法来改变 `myDate` 属性。这次方法调用会自动触发观察者的变化处理程序：

```swift
observed.updateDate() // Triggers the observer's change handler.
// Prints "myDate changed from: 1970-01-01 00:00:00 +0000, updated to: 2038-01-19 03:14:08 +0000"
```

上面的例子通过打印日期的新值和旧值来响应属性变化。

## 另请参阅

### Common Patterns

- [Using Delegates to Customize Object Behavior](using-delegates-to-customize-object-behavior.md) — 代表委托方（delegator）响应事件。
- [Managing a Shared Resource Using a Singleton](managing-a-shared-resource-using-a-singleton.md) — 使用单个共享的类实例，提供对共享资源的访问。
- [About Imported Cocoa Error Parameters](about-imported-cocoa-error-parameters.md) — 了解 Cocoa 错误参数是如何被转换为 Swift 抛出方法的。
- [Handling Cocoa Errors in Swift](handling-cocoa-errors-in-swift.md) — 抛出并捕获使用 Cocoa 错误类型的错误。
