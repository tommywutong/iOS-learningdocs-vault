---
title: 'value(withName:inPropertyWithKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/value(withname:inpropertywithkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(withname:inpropertywithkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/value%28withname%3Ainpropertywithkey%3A%29.json'
content_hash: 'sha256:088603662cf31b42'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# value(withName:inPropertyWithKey:)

<sub>实例方法</sub>

从由传入键指定的集合中检索命名对象。

<sub>Mac Catalyst, macOS</sub>

```swift
func value(withName name: String, inPropertyWithKey key: String) -> Any?
```

## 讨论

如果存在方法 `valueIn<Key>WithName:`，则使用它。否则引发 `NSUndefinedKeyException`。

## 另请参阅

### 按名称、键或 ID 访问

- [- insertValue:inPropertyWithKey:](<insertvalue(__inpropertywithkey_).md>) — 在由传入键指定的集合中插入对象。
- [- valueWithUniqueID:inPropertyWithKey:](<value(withuniqueid_inpropertywithkey_).md>) — 从由传入键指定的集合中按 ID 检索对象。
