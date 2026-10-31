---
title: 'setNilValueForKey(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setnilvalueforkey(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setnilvalueforkey(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setnilvalueforkey%28_%3A%29.json'
content_hash: 'sha256:3f40a434bded5a40'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setNilValueForKey(_:)

<sub>实例方法</sub>

当 [- setValue:forKey:](<setvalue(__forkey_).md>) 收到标量值（例如 `int` 或 `float`）的 `nil` 值时调用。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setNilValueForKey(_ key: String)
```

## 参数

- `key` — 接收者某个属性的名称。

## 讨论

子类可以重写此方法以其他方式处理该请求，例如用 `0` 或哨兵值替代 `nil` 并再次调用 [- setValue:forKey:](<setvalue(__forkey_).md>)，或直接设置变量。默认实现会引发 `NSInvalidArgumentException`。

## 另请参阅

### 设置值

- [- setValue:forKeyPath:](<setvalue(__forkeypath_).md>) — 将由给定键路径标识的属性的值设为给定值。
- [- setValuesForKeysWithDictionary:](<setvaluesforkeys(__).md>) — 使用给定字典中的值设置接收者的属性，并用其键标识这些属性。
- [- setValue:forKey:](<setvalue(__forkey_).md>) — 将接收者中由给定键指定的属性设为给定值。
- [- setValue:forUndefinedKey:](<setvalue(__forundefinedkey_).md>) — 当 [- setValue:forKey:](<setvalue(__forkey_).md>) 找不到给定键的属性时调用。
