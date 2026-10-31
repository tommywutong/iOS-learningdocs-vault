---
title: 'replaceValue(at:inPropertyWithKey:withValue:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/replacevalue(at:inpropertywithkey:withvalue:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/replacevalue(at:inpropertywithkey:withvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/replacevalue%28at%3Ainpropertywithkey%3Awithvalue%3A%29.json'
content_hash: 'sha256:b5ff9aa9438a9c48'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# replaceValue(at:inPropertyWithKey:withValue:)

<sub>实例方法</sub>

替换由传入键指定的集合中指定索引处的对象。

<sub>Mac Catalyst, macOS</sub>

```swift
func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)
```

## 讨论

若存在方法 `replaceIn<Key>:atIndex:` 则会调用它。若未找到对应的符合脚本 KVC 的方法（`-replaceIn<Key>atIndex:`），此方法会调用 `-mutableArrayValueForKey:` 并变更结果。

> [!note] 注意
> 在 OS X 10.4 版之前，此方法不会调用 `-mutableArrayValueForKey:`。

## 另请参阅

### 索引访问

- [- insertValue:atIndex:inPropertyWithKey:](<insertvalue(__at_inpropertywithkey_).md>) — 在由传入键指定的集合中的指定索引处插入对象。
- [- removeValueAtIndex:fromPropertyWithKey:](<removevalue(at_frompropertywithkey_).md>) — 从由传入键指定的集合中移除指定索引处的对象。
- [- valueAtIndex:inPropertyWithKey:](<value(at_inpropertywithkey_).md>) — 从由传入键指定的集合中检索索引对象。
