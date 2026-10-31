---
title: 'setValue(_:forKeyPath:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setvalue(_:forkeypath:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setvalue(_:forkeypath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setvalue%28_%3Aforkeypath%3A%29.json'
content_hash: 'sha256:7bdacc7d392f0109'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setValue(_:forKeyPath:)

<sub>实例方法</sub>

将由给定键路径标识的属性的值设为给定值。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setValue(_ value: Any?, forKeyPath keyPath: String)
```

## 参数

- `value` — The value for the property identified by `keyPath`.

- `keyPath` — 形式为 relationship.property（带有一个或多个关系）的键路径：例如 “department.name” 或 “department.manager.lastName.”

## 讨论

此方法的默认实现使用 [- valueForKey:](<value(forkey_).md>) 获取每个关系的目标对象，并向最终对象发送 [- setValue:forKey:](<setvalue(__forkey_).md>) 消息。

### 特殊注意事项

使用此方法时，若目标对象未实现该值的访问器，则默认行为是该对象保留 `value`，而不是复制或赋值 `value`。

## 另请参阅

### 相关文档

- [- valueForKeyPath:](<value(forkeypath_).md>) — 返回由给定键路径标识的派生属性的值。

### 设置值

- [- setValuesForKeysWithDictionary:](<setvaluesforkeys(__).md>) — 使用给定字典中的值设置接收者的属性，并用其键标识这些属性。
- [- setNilValueForKey:](<setnilvalueforkey(__).md>) — 当 [- setValue:forKey:](<setvalue(__forkey_).md>) 收到标量值（例如 `int` 或 `float`）的 `nil` 值时调用。
- [- setValue:forKey:](<setvalue(__forkey_).md>) — 将接收者中由给定键指定的属性设为给定值。
- [- setValue:forUndefinedKey:](<setvalue(__forundefinedkey_).md>) — 当 [- setValue:forKey:](<setvalue(__forkey_).md>) 找不到给定键的属性时调用。
