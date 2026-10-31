---
title: 'insertValue(_:inPropertyWithKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/insertvalue(_:inpropertywithkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/insertvalue(_:inpropertywithkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/insertvalue%28_%3Ainpropertywithkey%3A%29.json'
content_hash: 'sha256:c5c0bf70461c4a84'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# insertValue(_:inPropertyWithKey:)

<sub>实例方法</sub>

在由传入键指定的集合中插入对象。

<sub>Mac Catalyst, macOS</sub>

```swift
func insertValue(_ value: Any, inPropertyWithKey key: String)
```

## 讨论

如果存在方法 `insertIn<Key>:`，则使用它。否则引发 `NSUndefinedKeyException`。这是 Cocoa 脚本支持的一部分，用于将新创建的对象插入容器中。

## 另请参阅

### 按名称、键或 ID 访问

- [- valueWithName:inPropertyWithKey:](<value(withname_inpropertywithkey_).md>) — 从由传入键指定的集合中检索命名对象。
- [- valueWithUniqueID:inPropertyWithKey:](<value(withuniqueid_inpropertywithkey_).md>) — 从由传入键指定的集合中按 ID 检索对象。
