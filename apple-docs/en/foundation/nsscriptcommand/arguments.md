---
title: arguments
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommand/arguments
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommand/arguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommand/arguments.json'
content_hash: 'sha256:9bf183f813335715'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommand](../nsscriptcommand.md)

# arguments

<sub>Instance Property</sub>

Sets the arguments of the command to `args`.

<sub>Mac Catalyst, macOS</sub>

```swift
var arguments: [String : Any]? { get set }
```

## Discussion

Each argument in the dictionary is identified by the same name key used for the argument in the command’s class declaration in the script suite file.

## See Also

### Accessing arguments

- [evaluatedArguments](evaluatedarguments.md) — Returns a dictionary containing the arguments of the command, evaluated from object specifiers to objects if necessary. The keys in the dictionary are the argument names.
