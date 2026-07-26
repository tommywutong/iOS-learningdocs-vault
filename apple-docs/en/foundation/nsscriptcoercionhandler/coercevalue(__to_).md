---
title: 'coerceValue(_:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptcoercionhandler/coercevalue(_:to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcoercionhandler/coercevalue(_:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcoercionhandler/coercevalue%28_%3Ato%3A%29.json'
content_hash: 'sha256:fbe6200dee922263'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCoercionHandler](../nsscriptcoercionhandler.md)

# coerceValue(_:to:)

<sub>Instance Method</sub>

Returns an object of a given class representing a given value.

<sub>Mac Catalyst, macOS</sub>

```swift
func coerceValue(_ value: Any, to toClass: AnyClass) -> Any?
```

## Parameters

- `value` — The value to coerce.

- `toClass` — The class with which to represent `value`.

## Return Value

An object of the class `toClass` representing the value specified by `value`. Returns `nil` if an error occurs.

## See Also

### Working with handlers

- [- registerCoercer:selector:toConvertFromClass:toClass:](<registercoercer(__selector_toconvertfrom_to_).md>) — Registers a given object (typically a class) to handle coercions (conversions) from one given class to another.
