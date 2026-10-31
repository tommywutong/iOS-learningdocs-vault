---
title: 'setValue(_:forUndefinedKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setvalue(_:forundefinedkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setvalue(_:forundefinedkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setvalue%28_%3Aforundefinedkey%3A%29.json'
content_hash: 'sha256:5ce401c0c34f0c57'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setValue(_:forUndefinedKey:)

<sub>实例方法</sub>

当 [- setValue:forKey:](<setvalue(__forkey_).md>) 找不到给定键的属性时调用。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue(_ value: Any?, forUndefinedKey key: String)
```

## 参数

- `value` — 由 `key` 标识的键的值。

- `key` — 不等于接收者任何属性名称的字符串。

## 讨论

子类可以重写此方法以其他方式处理该请求。默认实现会引发 `NSUndefinedKeyException`。

## 另请参阅

### 相关文档

- [- valueForUndefinedKey:](<value(forundefinedkey_).md>) — 当 [- valueForKey:](<value(forkey_).md>) 找不到与给定键对应的属性时调用。

### 设置值

- [- setValue:forKeyPath:](<setvalue(__forkeypath_).md>) — 将由给定键路径标识的属性的值设为给定值。
- [- setValuesForKeysWithDictionary:](<setvaluesforkeys(__).md>) — 使用给定字典中的值设置接收者的属性，并用其键标识这些属性。
- [- setNilValueForKey:](<setnilvalueforkey(__).md>) — 当 [- setValue:forKey:](<setvalue(__forkey_).md>) 收到标量值（例如 `int` 或 `float`）的 `nil` 值时调用。
- [- setValue:forKey:](<setvalue(__forkey_).md>) — 将接收者中由给定键指定的属性设为给定值。
