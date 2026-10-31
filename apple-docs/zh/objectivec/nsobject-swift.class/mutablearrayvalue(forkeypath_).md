---
title: 'mutableArrayValue(forKeyPath:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/mutablearrayvalue(forkeypath:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/mutablearrayvalue(forkeypath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/mutablearrayvalue%28forkeypath%3A%29.json'
content_hash: 'sha256:60edbe7ac8734ddc'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# mutableArrayValue(forKeyPath:)

<sub>实例方法</sub>

返回一个可变数组，提供对由给定键路径指定的有序一对多关系的读写访问。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray
```

## 参数

- `keyPath` — 相对于接收者、指向有序一对多关系的键路径。

## 返回值

提供对由 `keyPath` 指定的有序一对多关系的读写访问的可变数组。

## 讨论

See [- mutableArrayValueForKey:](<mutablearrayvalue(forkey_).md>) for additional details.

## 另请参阅

### Getting Values

- [- valueForKey:](<value(forkey_).md>) — 返回由给定键标识的属性的值。
- [- valueForKeyPath:](<value(forkeypath_).md>) — 返回由给定键路径标识的派生属性的值。
- [- dictionaryWithValuesForKeys:](<dictionarywithvalues(forkeys_).md>) — 返回一个字典，包含给定数组中每个键所标识的属性值。
- [- valueForUndefinedKey:](<value(forundefinedkey_).md>) — 当 [- valueForKey:](<value(forkey_).md>) 找不到与给定键对应的属性时调用。
- [- mutableArrayValueForKey:](<mutablearrayvalue(forkey_).md>) — 返回一个可变数组代理，为给定键指定的有序一对多关系提供读写访问。
- [- mutableSetValueForKey:](<mutablesetvalue(forkey_).md>) — 返回一个可变集合代理，为给定键指定的无序一对多关系提供读写访问。
- [- mutableSetValueForKeyPath:](<mutablesetvalue(forkeypath_).md>) — 返回一个可变集合，为给定键路径指定的无序一对多关系提供读写访问。
- [- mutableOrderedSetValueForKey:](<mutableorderedsetvalue(forkey_).md>) — 返回一个可变有序集合，为给定键指定的唯一化有序一对多关系提供读写访问。
- [- mutableOrderedSetValueForKeyPath:](<mutableorderedsetvalue(forkeypath_).md>) — 返回一个可变有序集合，为给定键路径指定的唯一化有序一对多关系提供读写访问。
