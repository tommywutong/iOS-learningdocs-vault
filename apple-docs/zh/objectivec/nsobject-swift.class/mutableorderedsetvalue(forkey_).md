---
title: 'mutableOrderedSetValue(forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/mutableorderedsetvalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/mutableorderedsetvalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/mutableorderedsetvalue%28forkey%3A%29.json'
content_hash: 'sha256:21bf030831be4908'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# mutableOrderedSetValue(forKey:)

<sub>实例方法</sub>

返回一个可变有序集，提供对由给定键指定的唯一化有序一对多关系的读写访问。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet
```

## 参数

- `key` — 唯一化有序一对多关系的名称。

## 返回值

提供对由 `key` 指定的唯一化一对多关系的读写访问的可变有序集。

## 讨论

添加到可变集代理的对象会与接收者建立关系，从可变集移除的对象会解除关系。默认实现识别与 [- valueForKey:](<value(forkey_).md>) 相同的简单访问器方法和集访问器方法，并遵循相同的直接实例变量访问策略，但始终返回可变集合代理对象，而不是 [- valueForKey:](<value(forkey_).md>) 会返回的不可变集合。

`mutableOrderedSetValueForKey:` 使用的搜索模式在 [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i) 的 [Accessor Search Patterns](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/SearchImplementation.html#//apple_ref/doc/uid/20000955) 中有描述。

## 另请参阅

### Getting Values

- [- valueForKey:](<value(forkey_).md>) — 返回由给定键标识的属性的值。
- [- valueForKeyPath:](<value(forkeypath_).md>) — 返回由给定键路径标识的派生属性的值。
- [- dictionaryWithValuesForKeys:](<dictionarywithvalues(forkeys_).md>) — 返回一个字典，包含给定数组中每个键所标识的属性值。
- [- valueForUndefinedKey:](<value(forundefinedkey_).md>) — 当 [- valueForKey:](<value(forkey_).md>) 找不到与给定键对应的属性时调用。
- [- mutableArrayValueForKey:](<mutablearrayvalue(forkey_).md>) — 返回一个可变数组代理，为给定键指定的有序一对多关系提供读写访问。
- [- mutableArrayValueForKeyPath:](<mutablearrayvalue(forkeypath_).md>) — 返回一个可变数组，为给定键路径指定的有序一对多关系提供读写访问。
- [- mutableSetValueForKey:](<mutablesetvalue(forkey_).md>) — 返回一个可变集合代理，为给定键指定的无序一对多关系提供读写访问。
- [- mutableSetValueForKeyPath:](<mutablesetvalue(forkeypath_).md>) — 返回一个可变集合，为给定键路径指定的无序一对多关系提供读写访问。
- [- mutableOrderedSetValueForKeyPath:](<mutableorderedsetvalue(forkeypath_).md>) — 返回一个可变有序集合，为给定键路径指定的唯一化有序一对多关系提供读写访问。
