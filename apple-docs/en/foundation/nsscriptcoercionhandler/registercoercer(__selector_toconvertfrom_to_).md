---
title: 'registerCoercer(_:selector:toConvertFrom:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptcoercionhandler/registercoercer(_:selector:toconvertfrom:to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcoercionhandler/registercoercer(_:selector:toconvertfrom:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcoercionhandler/registercoercer%28_%3Aselector%3Atoconvertfrom%3Ato%3A%29.json'
content_hash: 'sha256:1c80f517f7254771'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCoercionHandler](../nsscriptcoercionhandler.md)

# registerCoercer(_:selector:toConvertFrom:to:)

<sub>Instance Method</sub>

Registers a given object (typically a class) to handle coercions (conversions) from one given class to another.

<sub>Mac Catalyst, macOS</sub>

```swift
func registerCoercer(_ coercer: Any, selector: Selector, toConvertFrom fromClass: AnyClass, to toClass: AnyClass)
```

## Parameters

- `coercer` — The object that performs the coercion. `coercer` should typically be a class object.

- `selector` — A selector that specifies the method to perform the coercion. `selector` should typically be a factory method, and must take two arguments. The first is the value to be converted. The second is the class to convert it to.

- `fromClass` — The class for which instances are coerced.

- `toClass` — The class to which instances of `fromClass` are coerced.

## See Also

### Working with handlers

- [- coerceValue:toClass:](<coercevalue(__to_).md>) — Returns an object of a given class representing a given value.
