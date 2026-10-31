---
title: 'value(at:inPropertyWithKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/value(at:inpropertywithkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(at:inpropertywithkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/value%28at%3Ainpropertywithkey%3A%29.json'
content_hash: 'sha256:e2592098597b7218'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# value(at:inPropertyWithKey:)

<sub>实例方法</sub>

从由传入键指定的集合中检索索引对象。

<sub>Mac Catalyst, macOS</sub>

```swift
func value(at index: Int, inPropertyWithKey key: String) -> Any?
```

## 讨论

如果 `index` 为 0，这也适用于单值键。如果存在方法 `valueIn<Key>AtIndex:`，则使用它。

## 另请参阅

### 索引访问

- [- insertValue:atIndex:inPropertyWithKey:](<insertvalue(__at_inpropertywithkey_).md>) — 在传入键指定的集合中，将某个对象插入到指定索引处。
- [- removeValueAtIndex:fromPropertyWithKey:](<removevalue(at_frompropertywithkey_).md>) — 从传入键指定的集合中，移除指定索引处的对象。
- [- replaceValueAtIndex:inPropertyWithKey:withValue:](<replacevalue(at_inpropertywithkey_withvalue_).md>) — 替换传入键指定的集合中指定索引处的对象。
