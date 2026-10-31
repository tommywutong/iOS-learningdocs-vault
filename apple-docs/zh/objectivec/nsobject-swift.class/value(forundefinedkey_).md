---
title: 'value(forUndefinedKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/value(forundefinedkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(forundefinedkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/value%28forundefinedkey%3A%29.json'
content_hash: 'sha256:7231abe968f2362b'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# value(forUndefinedKey:)

<sub>实例方法</sub>

当 [- valueForKey:](<value(forkey_).md>) 找不到与给定键对应的属性时调用。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value(forUndefinedKey key: String) -> Any?
```

## 参数

- `key` — 不等于接收者任何属性名称的字符串。

## 讨论

子类可以重写此方法以为未定义的键返回替代值。默认实现会引发 `NSUndefinedKeyException`。

## 另请参阅

### 相关文档

- [- setValue:forUndefinedKey:](<setvalue(__forundefinedkey_).md>) — 当 [- setValue:forKey:](<setvalue(__forkey_).md>) 找不到给定键的属性时调用。

### Getting Values

- [- valueForKey:](<value(forkey_).md>) — 返回由给定键标识的属性的值。
- [- valueForKeyPath:](<value(forkeypath_).md>) — 返回由给定键路径标识的派生属性的值。
- [- dictionaryWithValuesForKeys:](<dictionarywithvalues(forkeys_).md>) — 返回一个字典，包含给定数组中每个键所标识的属性值。
- [- mutableArrayValueForKey:](<mutablearrayvalue(forkey_).md>) — 返回一个可变数组代理，提供对由给定键指定的有序一对多关系的读写访问。
- [- mutableArrayValueForKeyPath:](<mutablearrayvalue(forkeypath_).md>) — 返回一个可变数组，为给定键路径指定的有序一对多关系提供读写访问。
- [- mutableSetValueForKey:](<mutablesetvalue(forkey_).md>) — 返回一个可变集合代理，为给定键指定的无序一对多关系提供读写访问。
- [- mutableSetValueForKeyPath:](<mutablesetvalue(forkeypath_).md>) — 返回一个可变集合，为给定键路径指定的无序一对多关系提供读写访问。
- [- mutableOrderedSetValueForKey:](<mutableorderedsetvalue(forkey_).md>) — 返回一个可变有序集合，为给定键指定的唯一化有序一对多关系提供读写访问。
- [- mutableOrderedSetValueForKeyPath:](<mutableorderedsetvalue(forkeypath_).md>) — 返回一个可变有序集合，为给定键路径指定的唯一化有序一对多关系提供读写访问。
