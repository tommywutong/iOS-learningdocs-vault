---
title: 'insertValue(_:at:inPropertyWithKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/insertvalue(_:at:inpropertywithkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/insertvalue(_:at:inpropertywithkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/insertvalue%28_%3Aat%3Ainpropertywithkey%3A%29.json'
content_hash: 'sha256:6acca38cae15d5eb'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# insertValue(_:at:inPropertyWithKey:)

<sub>实例方法</sub>

在由传入键指定的集合中的指定索引处插入对象。

<sub>Mac Catalyst, macOS</sub>

```swift
func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)
```

## 讨论

若存在方法 `insertIn<Key>:atIndex:` 则会调用它。若未找到对应的符合脚本 KVC 的方法（`insertIn<Key>:atIndex:`），此方法会调用 `mutableArrayValueForKey:` 并变更结果。

> [!note] 注意
> 在 OS X 10.4 版之前，此方法不会调用 `-mutableArrayValueForKey:`。

## 另请参阅

### 索引访问

- [- removeValueAtIndex:fromPropertyWithKey:](<removevalue(at_frompropertywithkey_).md>) — 从由传入键指定的集合中移除指定索引处的对象。
- [- replaceValueAtIndex:inPropertyWithKey:withValue:](<replacevalue(at_inpropertywithkey_withvalue_).md>) — 替换由传入键指定的集合中指定索引处的对象。
- [- valueAtIndex:inPropertyWithKey:](<value(at_inpropertywithkey_).md>) — 从由传入键指定的集合中检索索引对象。
