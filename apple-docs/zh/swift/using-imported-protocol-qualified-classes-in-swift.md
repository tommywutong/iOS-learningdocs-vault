---
title: 在 Swift 中使用导入的协议限定类
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/using-imported-protocol-qualified-classes-in-swift
source_url: 'https://developer.apple.com/documentation/swift/using-imported-protocol-qualified-classes-in-swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/using-imported-protocol-qualified-classes-in-swift.json'
content_hash: 'sha256:f5f4308e250d48a9'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [导入的 C 与 Objective-C API](imported-c-and-objective-c-apis.md)

# 在 Swift 中使用导入的协议限定类

<sub>文章</sub>

了解导入的 Objective-C 协议限定类及元类是如何表示的。

## 概述

由一个或多个协议限定的 Objective-C 类，例如下例中的类，会被 Swift 导入为协议组合类型。下面的 Objective-C 属性引用了一个视图控制器，它同时还充当数据源和委托：

```occ
@property UIViewController<UITableViewDataSource, UITableViewDelegate> * myController;
```

导入之后，对应的 Swift 接口如下：

```swift
var myController: UIViewController & UITableViewDataSource & UITableViewDelegate
```

Objective-C 的协议限定元类会被 Swift 导入为协议元类型（protocol metatype），即表示协议自身类型的类型。例如，给定以下对指定类执行操作的 Objective-C 方法：

```occ
- (void)doSomethingForClass:(Class<NSCoding>)codingClass;
```

导入之后，对应的 Swift 接口如下：

```swift
func doSomething(for codingClass: NSCoding.Type)
```

## 另请参阅

### Objective-C API

- [在 Swift 中使用导入的轻量泛型](using-imported-lightweight-generics-in-swift.md) —— 了解导入的 Objective-C 轻量泛型类型声明的限制。
