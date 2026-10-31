---
title: 'setValuesForKeys(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setvaluesforkeys(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setvaluesforkeys(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setvaluesforkeys%28_%3A%29.json'
content_hash: 'sha256:88b3f2b4ab0780d7'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setValuesForKeys(_:)

<sub>实例方法</sub>

使用给定字典中的值设置接收者的属性，并用其键标识这些属性。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValuesForKeys(_ keyedValues: [String : Any])
```

## 参数

- `keyedValues` — 其键标识接收者中属性的字典。接收者中属性的值会被设置为字典中的对应值。

## 讨论

默认实现会对每个键值对调用 [- setValue:forKey:](<setvalue(__forkey_).md>)，并将 `keyedValues` 中的 `NSNull` 值替换为 `nil`。

## 另请参阅

### 相关文档

- [- dictionaryWithValuesForKeys:](<dictionarywithvalues(forkeys_).md>) — 返回一个字典，包含给定数组中每个键所标识的属性值。

### 设置值

- [- setValue:forKeyPath:](<setvalue(__forkeypath_).md>) — 将由给定键路径标识的属性的值设为给定值。
- [- setNilValueForKey:](<setnilvalueforkey(__).md>) — 当 [- setValue:forKey:](<setvalue(__forkey_).md>) 收到标量值（例如 `int` 或 `float`）的 `nil` 值时调用。
- [- setValue:forKey:](<setvalue(__forkey_).md>) — 将接收者中由给定键指定的属性设为给定值。
- [- setValue:forUndefinedKey:](<setvalue(__forundefinedkey_).md>) — 当 [- setValue:forKey:](<setvalue(__forkey_).md>) 找不到给定键的属性时调用。
