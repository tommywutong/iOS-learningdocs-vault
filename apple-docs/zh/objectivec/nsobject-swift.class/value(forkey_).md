---
title: 'value(forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/value(forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/value%28forkey%3A%29.json'
content_hash: 'sha256:695aa07ef4581163'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# value(forKey:)

<sub>实例方法</sub>

返回由给定键标识的属性的值。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value(forKey key: String) -> Any?
```

## 参数

- `key` — 接收者某个属性的名称。

## 返回值

The value for the property identified by `key`.

## 讨论

`valueForKey:` 用于查找要返回的正确值的搜索模式在 [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i) 的 [Accessor Search Patterns](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/SearchImplementation.html#//apple_ref/doc/uid/20000955) 中有描述。

## 另请参阅

### 相关文档

- [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)

### Getting Values

- [- valueForKeyPath:](<value(forkeypath_).md>) — 返回由给定键路径标识的派生属性的值。
- [- dictionaryWithValuesForKeys:](<dictionarywithvalues(forkeys_).md>) — 返回一个字典，包含给定数组中每个键所标识的属性值。
- [- valueForUndefinedKey:](<value(forundefinedkey_).md>) — 当 [- valueForKey:](<value(forkey_).md>) 找不到与给定键对应的属性时调用。
- [- mutableArrayValueForKey:](<mutablearrayvalue(forkey_).md>) — 返回一个可变数组代理，提供对由给定键指定的有序一对多关系的读写访问。
- [- mutableArrayValueForKeyPath:](<mutablearrayvalue(forkeypath_).md>) — 返回一个可变数组，为给定键路径指定的有序一对多关系提供读写访问。
- [- mutableSetValueForKey:](<mutablesetvalue(forkey_).md>) — 返回一个可变集合代理，为给定键指定的无序一对多关系提供读写访问。
- [- mutableSetValueForKeyPath:](<mutablesetvalue(forkeypath_).md>) — 返回一个可变集合，为给定键路径指定的无序一对多关系提供读写访问。
- [- mutableOrderedSetValueForKey:](<mutableorderedsetvalue(forkey_).md>) — 返回一个可变有序集合，为给定键指定的唯一化有序一对多关系提供读写访问。
- [- mutableOrderedSetValueForKeyPath:](<mutableorderedsetvalue(forkeypath_).md>) — 返回一个可变有序集合，为给定键路径指定的唯一化有序一对多关系提供读写访问。
