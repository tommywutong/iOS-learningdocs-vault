---
title: 'setValue(_:forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setvalue(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setvalue(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setvalue%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:7bbd6f39dff261a9'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setValue(_:forKey:)

<sub>实例方法</sub>

将接收者中由给定键指定的属性设置为给定值。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue(_ value: Any?, forKey key: String)
```

## 参数

- `value` — 由 `key` 标识的属性的值。

- `key` — 接收者某个属性的名称。

## 讨论

若 `key` 标识一对一关系，则将 `value` 指定的对象与接收者关联，并解除先前关联的对象（如有）。给定集合对象和标识一对多关系的 `key`，则将集合中包含的对象与接收者关联，并解除先前关联的对象（如有）。

`setValue:forKey:` 使用的搜索模式在 [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i) 的 [Accessor Search Patterns](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/SearchImplementation.html#//apple_ref/doc/uid/20000955) 中有说明。

在引用计数环境中，若直接访问实例变量，则会保留 `value`。

## 另请参阅

### 设置值

- [- setValue:forKeyPath:](<setvalue(__forkeypath_).md>) — 将由给定键路径标识的属性的值设为给定值。
- [- setValuesForKeysWithDictionary:](<setvaluesforkeys(__).md>) — 使用给定字典中的值设置接收者的属性，并用其键标识这些属性。
- [- setNilValueForKey:](<setnilvalueforkey(__).md>) — 当 [- setValue:forKey:](<setvalue(__forkey_).md>) 收到标量值（例如 `int` 或 `float`）的 `nil` 值时调用。
- [- setValue:forUndefinedKey:](<setvalue(__forundefinedkey_).md>) — 当 [- setValue:forKey:](<setvalue(__forkey_).md>) 找不到给定键的属性时调用。
