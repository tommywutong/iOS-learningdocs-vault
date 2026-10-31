---
title: 'inverse(forRelationshipKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/inverse(forrelationshipkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/inverse(forrelationshipkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/inverse%28forrelationshipkey%3A%29.json'
content_hash: 'sha256:7c27f189e95acd27'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# inverse(forRelationshipKey:)

<sub>实例方法</sub>

对于定义从接收者的类到另一个类的关系名称的给定键，返回从另一个类到接收者的类的关系名称。

<sub>Mac Catalyst, macOS</sub>

```swift
func inverse(forRelationshipKey relationshipKey: String) -> String?
```

## 参数

- `relationshipKey` — 从接收者的类到另一个类的关系的名称。

## 返回值

作为接收者名为 `relationshipKey` 的关系的逆关系的关系名称。

## 讨论

`NSObject` 的 `inverseForRelationshipKey:` 实现仅调用 `[[self classDescription] inverseForRelationshipKey:relationshipKey]`。因此，要使用默认实现，你必须实现并注册合适的类描述——请参阅 [NSClassDescription](../../foundation/nsclassdescription.md)。

例如，假设 Employee 类有一个名为 `department` 的关系到 Department 类，并且 Department 有一个名为 `employees` 的关系到 Employee。语句：

```objc
employee inverseForRelationshipKey:@"department"];
```

returns the string `employees`.

## 另请参阅

### 使用类描述

- [attributeKeys](attributekeys.md) — 包含接收者类的实例所包含的不可变值名称的 `NSString` 对象数组。
- [classDescription](classdescription.md) — 包含接收者类的属性和关系信息的对象。
- [toManyRelationshipKeys](tomanyrelationshipkeys.md) — 包含接收者一对多关系属性键的数组。
- [toOneRelationshipKeys](toonerelationshipkeys.md) — 接收者一对一关系属性的键（如果有）。
