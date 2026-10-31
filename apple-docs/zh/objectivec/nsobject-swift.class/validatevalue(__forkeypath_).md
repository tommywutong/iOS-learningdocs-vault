---
title: 'validateValue(_:forKeyPath:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/validatevalue(_:forkeypath:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/validatevalue(_:forkeypath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/validatevalue%28_%3Aforkeypath%3A%29.json'
content_hash: 'sha256:dba4241934236cb9'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# validateValue(_:forKeyPath:)

<sub>实例方法</sub>

指示由给定指针指定的值相对于接收者、对于给定键路径是否无效。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws
```

## 参数

- `ioValue` — 指向由 `inKeyPath` 标识的属性的新值的指针。此方法可以修改或替换该值以使其有效。

- `inKeyPath` — 接收者某个属性的名称。键路径必须指定属性或一对一关系。键路径的形式为 `relationship``.``property`（含一个或多个关系）；例如 `department.name` 或 `department.manager.lastName`。

## 讨论

在 Swift 中，若值无效，此方法会抛出错误。在 Objective-C 中，它返回布尔值。

此方法的默认实现使用 [- valueForKey:](<value(forkey_).md>) 获取每个关系的目标对象，并返回为该属性调用 [- validateValue:forKey:error:](<validatevalue(__forkey_).md>) 方法的结果。

## 另请参阅

### 验证

- [- validateValue:forKey:error:](<validatevalue(__forkey_).md>) — 指示由给定指针指定的值对于由给定键标识的属性是否有效，或能否变为有效。
