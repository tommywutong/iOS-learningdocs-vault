---
title: isWellFormed
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommand/iswellformed
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommand/iswellformed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommand/iswellformed.json'
content_hash: 'sha256:9b6e033d7cd65e42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommand](../nsscriptcommand.md)

# isWellFormed

<sub>Instance Property</sub>

Returns a Boolean value indicating whether the receiver is well formed according to its command description.

<sub>Mac Catalyst, macOS</sub>

```swift
var isWellFormed: Bool { get }
```

## Discussion

The method ensures that there is a description of the command and that the number of arguments and the types of non-specifier arguments conform to the command description.

## See Also

### Getting command information

- [commandDescription](commanddescription.md) — Returns the command description for the command.
