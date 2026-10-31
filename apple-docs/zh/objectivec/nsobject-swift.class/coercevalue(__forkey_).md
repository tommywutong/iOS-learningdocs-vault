---
title: 'coerceValue(_:forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/coercevalue(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/coercevalue(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/coercevalue%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:d314b37b2517ca1d'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# coerceValue(_:forKey:)

<sub>实例方法</sub>

使用类描述和 `NSScriptCoercionHandler` 中的类型信息，在必要时尝试将 `key` 的 `value` 转换为适当类型。

<sub>Mac Catalyst, macOS</sub>

```swift
func coerceValue(_ value: Any?, forKey key: String) -> Any?
```

## 讨论

如果存在方法 `coerceValueFor<Key>:`，则使用该方法。
