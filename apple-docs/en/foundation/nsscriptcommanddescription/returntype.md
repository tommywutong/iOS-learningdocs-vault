---
title: returnType
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommanddescription/returntype
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/returntype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommanddescription/returntype.json'
content_hash: 'sha256:2255a9b4e278de94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommandDescription](../nsscriptcommanddescription.md)

# returnType

<sub>Instance Property</sub>

Returns the return type of the command.

<sub>Mac Catalyst, macOS</sub>

```swift
var returnType: String? { get }
```

## Return Value

The receiver’s command return type; for example, `"NSNumber"` or `"NSDictionary"`).

## See Also

### Getting Command Return-Type Information

- [appleEventCodeForReturnType](appleeventcodeforreturntype.md) — Returns the Apple event code that identifies the command’s return type.
