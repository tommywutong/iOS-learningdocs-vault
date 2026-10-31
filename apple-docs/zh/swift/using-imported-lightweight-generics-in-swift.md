---
title: 在 Swift 中使用导入的轻量泛型
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/using-imported-lightweight-generics-in-swift
source_url: 'https://developer.apple.com/documentation/swift/using-imported-lightweight-generics-in-swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/using-imported-lightweight-generics-in-swift.json'
content_hash: 'sha256:0d8d23e998b726a7'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [导入的 C 与 Objective-C API](imported-c-and-objective-c-apis.md)

# 在 Swift 中使用导入的轻量泛型

<sub>文章</sub>

了解导入的 Objective-C 轻量泛型类型声明的限制。

## 概述

使用轻量泛型参数化的 Objective-C 类型声明被 Swift 导入时会保留其内容类型的信息。例如，给定以下 Objective-C 属性声明：

```occ
@property NSArray<NSDate *> *dates;
@property NSCache<NSObject *, id<NSDiscardableContent>> *cachedData;
@property NSDictionary <NSString *, NSArray<NSLocale *> *> *supportedLocales;
```

导入这些声明后，它们对应的 Swift 版本如下：

```swift
var dates: [Date]
var cachedData: NSCache<NSObject, NSDiscardableContent>
var supportedLocales: [String: [Locale]]
```

用 Objective-C 编写的参数化类被导入到 Swift 时，是一个具有相同数量类型参数的泛型类。Swift 导入的所有 Objective-C 泛型类型参数都带有一个类型约束，要求该类型必须是类（`T: AnyObject`）。

如果 Objective-C 的泛型参数化指定了类或协议限定，导入的 Swift 声明就带有一个约束，要求该类型必须是指定类的子类或符合指定的协议。对于未特化的 Objective-C 类型，Swift 会为导入的类类型约束推断泛型参数化。例如，考虑以下 Objective-C 类和分类声明：

```occ
@interface List<T: id<NSCopying>> : NSObject
- (List<T> *)listByAppendingItemsInList:(List<T> *)otherList;
@end

@interface ListContainer : NSObject
- (List<NSValue *> *)listOfValues;
@end

@interface ListContainer (ObjectList)
- (List *)listOfObjects;
@end
```

当你把这些声明导入 Swift 时，`List` 类型的 `NSCopying` 协议限定和 `listOfValues` 方法的 `NSValue` 类限定都会被保留。此外，未加限定的 `listOfObjects` 方法使用从 `List` 类型推断出的 `NSCopying` 泛型约束。

```swift
class List<T: NSCopying> : NSObject {
    func listByAppendingItemsInList(otherList: List<T>) -> List<T>
}

class ListContainer : NSObject {
    func listOfValues() -> List<NSValue>
}

extension ListContainer {
    func listOfObjects() -> List<NSCopying>
}
```

## 另请参阅

### Objective-C API

- [在 Swift 中使用导入的带协议限定的类](using-imported-protocol-qualified-classes-in-swift.md) — 了解导入的带协议限定的 Objective-C 类和元类是如何表示的。
