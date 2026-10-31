---
title: 'value(withUniqueID:inPropertyWithKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/value(withuniqueid:inpropertywithkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(withuniqueid:inpropertywithkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/value%28withuniqueid%3Ainpropertywithkey%3A%29.json'
content_hash: 'sha256:fce36c1196ca4599'
translated: true
---
> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# value(withUniqueID:inPropertyWithKey:)

<sub>实例方法</sub>

从由传入键指定的集合中按 ID 检索对象。

<sub>Mac Catalyst, macOS</sub>

```swift
func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?
```

## 讨论

如果存在方法 `valueIn<Key>WithUniqueID:`，则调用它。否则引发 `NSUndefinedKeyException`。所构造方法中 `uniqueID` 的声明类型必须为 `id`、`NSNumber *`、`NSString *`，或可由 `NSNumber` 封装的标量类型之一。

## 另请参阅

### 按名称、键或 ID 访问

- [- insertValue:inPropertyWithKey:](<insertvalue(__inpropertywithkey_).md>) — 在由传入键指定的集合中插入对象。
- [- valueWithName:inPropertyWithKey:](<value(withname_inpropertywithkey_).md>) — 从由传入键指定的集合中检索命名对象。
