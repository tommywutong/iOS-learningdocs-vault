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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# coerceValue(_:forKey:)

<sub>Instance Method</sub>

Uses type info from the class description and `NSScriptCoercionHandler` to attempt to convert `value` for `key` to the proper type, if necessary.

<sub>Mac Catalyst, macOS</sub>

```swift
func coerceValue(_ value: Any?, forKey key: String) -> Any?
```

## Discussion

The method `coerceValueFor<Key>:` is used if it exists.
