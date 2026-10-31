---
title: 'dictionaryWithValues(forKeys:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/dictionarywithvalues(forkeys:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/dictionarywithvalues(forkeys:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/dictionarywithvalues%28forkeys%3A%29.json'
content_hash: 'sha256:569eb9b99fe3f245'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# dictionaryWithValues(forKeys:)

<sub>实例方法</sub>

返回包含由给定数组中每个键标识的属性值的字典。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]
```

## 参数

- `keys` — 包含标识接收者属性的 `NSString` 对象的数组。

## 返回值

一个字典，其键为 `keys` 中的属性名称，对应值为相应的属性值。

## 讨论

默认实现对 `keys` 中的每个键调用 [- valueForKey:](<value(forkey_).md>)，并对返回的 `nil` 值在字典中替换为 `NSNull` 值。

## 另请参阅

### 相关文档

- [- setValuesForKeysWithDictionary:](<setvaluesforkeys(__).md>) — 使用给定字典中的值设置接收者的属性，并用其键标识这些属性。

### Getting Values

- [- valueForKey:](<value(forkey_).md>) — 返回由给定键标识的属性的值。
- [- valueForKeyPath:](<value(forkeypath_).md>) — 返回由给定键路径标识的派生属性的值。
- [- valueForUndefinedKey:](<value(forundefinedkey_).md>) — 当 [- valueForKey:](<value(forkey_).md>) 找不到与给定键对应的属性时调用。
- [- mutableArrayValueForKey:](<mutablearrayvalue(forkey_).md>) — 返回一个可变数组代理，为给定键指定的有序一对多关系提供读写访问。
- [- mutableArrayValueForKeyPath:](<mutablearrayvalue(forkeypath_).md>) — 返回一个可变数组，为给定键路径指定的有序一对多关系提供读写访问。
- [- mutableSetValueForKey:](<mutablesetvalue(forkey_).md>) — 返回一个可变集合代理，为给定键指定的无序一对多关系提供读写访问。
- [- mutableSetValueForKeyPath:](<mutablesetvalue(forkeypath_).md>) — 返回一个可变集合，为给定键路径指定的无序一对多关系提供读写访问。
- [- mutableOrderedSetValueForKey:](<mutableorderedsetvalue(forkey_).md>) — 返回一个可变有序集合，为给定键指定的唯一化有序一对多关系提供读写访问。
- [- mutableOrderedSetValueForKeyPath:](<mutableorderedsetvalue(forkeypath_).md>) — 返回一个可变有序集合，为给定键路径指定的唯一化有序一对多关系提供读写访问。
