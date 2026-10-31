---
title: toManyRelationshipKeys
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/tomanyrelationshipkeys
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/tomanyrelationshipkeys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/tomanyrelationshipkeys.json'
content_hash: 'sha256:0c25c1667b6bfcaf'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# toManyRelationshipKeys

<sub>实例属性</sub>

包含接收者一对多关系属性键的数组。

<sub>Mac Catalyst, macOS</sub>

```swift
var toManyRelationshipKeys: [String] { get }
```

## 另请参阅

### 使用类描述

- [attributeKeys](attributekeys.md) — 包含接收者类的实例所包含的不可变值名称的 `NSString` 对象数组。
- [classDescription](classdescription.md) — 包含接收者类的属性和关系信息的对象。
- [- inverseForRelationshipKey:](<inverse(forrelationshipkey_).md>) — 对于定义从接收者类到另一类的关系名称的给定键，返回从另一类到接收者类的关系名称。
- [toOneRelationshipKeys](toonerelationshipkeys.md) — 接收者一对一关系属性的键（如果有）。
