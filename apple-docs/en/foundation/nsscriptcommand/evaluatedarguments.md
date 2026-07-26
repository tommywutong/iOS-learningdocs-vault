---
title: evaluatedArguments
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommand/evaluatedarguments
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommand/evaluatedarguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommand/evaluatedarguments.json'
content_hash: 'sha256:43bc49d0ca4c0511'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommand](../nsscriptcommand.md)

# evaluatedArguments

<sub>Instance Property</sub>

Returns a dictionary containing the arguments of the command, evaluated from object specifiers to objects if necessary. The keys in the dictionary are the argument names.

<sub>Mac Catalyst, macOS</sub>

```swift
var evaluatedArguments: [String : Any]? { get }
```

## Discussion

Arguments initially can be either a normal object or an object specifier such as `word 5` (represented as an instance of an `NSScriptObjectSpecifier` subclass). If arguments are object specifiers, the receiver evaluates them before using the referenced objects. Returns `nil` if the command is not well formed. Also returns `nil` if an object specifier does not evaluate to an object or if there is no type defined for the argument in the command description.

## See Also

### Related Documentation

- [wellFormed](iswellformed.md) — Returns a Boolean value indicating whether the receiver is well formed according to its command description.

### Accessing arguments

- [arguments](arguments.md) — Sets the arguments of the command to `args`.
